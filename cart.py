import json
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.main_kb import cart_kb, delivery_kb, main_menu_kb
from data.catalog_loader import get_product, format_price
from utils.database import cart_add, cart_remove, cart_clear, cart_get, save_order
from utils.i18n import t, get_user_lang, all_variants
from config import DISCOUNT_TIERS, MANAGER_CHAT_ID

router = Router()

class OrderForm(StatesGroup):
    name     = State()
    company  = State()
    city     = State()
    phone    = State()
    delivery = State()

def calc_discount(total_items: int) -> float:
    for threshold, pct in DISCOUNT_TIERS:
        if total_items >= threshold:
            return pct
    return 0.0

async def build_cart_text(user_id: int, lang: str = "ru") -> tuple[str, int, int]:
    rows = await cart_get(user_id)
    if not rows:
        return t("cart_empty", lang), 0, 0

    lines = [t("cart_title", lang)]
    total = 0
    total_qty = 0
    for row in rows:
        product, section = get_product(row["product_num"])
        if not product:
            continue
        qty = row["quantity"]
        subtotal = product["price_sum"] * qty
        total += subtotal
        total_qty += qty
        lines.append(
            f"• *{t('art_short', lang)}{product['number']}* {product['name']}\n"
            f"  {qty} {t('pcs_short', lang)} × {format_price(product['price_sum'])} = *{format_price(subtotal)}*"
        )

    discount = calc_discount(total_qty)
    discount_sum = int(total * discount)
    final = total - discount_sum

    lines.append(t("cart_qty", lang).format(n=total_qty))
    if discount > 0:
        lines.append(t("cart_discount", lang).format(pct=int(discount*100), sum=format_price(discount_sum)))
    lines.append(t("cart_total", lang).format(sum=format_price(final)))
    return "\n".join(lines), final, total_qty


# ── Добавить в корзину ────────────────────────────────────────────
@router.callback_query(F.data.startswith("cart_add:"))
async def cb_cart_add(call: CallbackQuery):
    lang = await get_user_lang(call.from_user.id)
    product_num = int(call.data.split(":")[1])
    product, _ = get_product(product_num)
    if not product:
        await call.answer(t("product_not_found", lang), show_alert=True)
        return
    await cart_add(call.from_user.id, product_num)
    await call.answer(t("item_added", lang).format(num=product_num))

# ── Просмотр корзины ──────────────────────────────────────────────
@router.message(F.text.in_(all_variants("btn_cart")))
async def open_cart_msg(message: Message):
    lang = await get_user_lang(message.from_user.id)
    text, total, qty = await build_cart_text(message.from_user.id, lang)
    if qty == 0:
        await message.answer(text)
        return
    await message.answer(text, parse_mode="Markdown", reply_markup=cart_kb(lang))

@router.callback_query(F.data == "cart:view")
async def cb_cart_view(call: CallbackQuery):
    lang = await get_user_lang(call.from_user.id)
    text, total, qty = await build_cart_text(call.from_user.id, lang)
    if qty == 0:
        await call.message.edit_text(text)
        return
    await call.message.edit_text(text, parse_mode="Markdown", reply_markup=cart_kb(lang))

# ── Очистить корзину ──────────────────────────────────────────────
@router.callback_query(F.data == "cart:clear")
async def cb_cart_clear(call: CallbackQuery):
    lang = await get_user_lang(call.from_user.id)
    await cart_clear(call.from_user.id)
    await call.message.edit_text(t("cart_cleared", lang))

# ── Оформление заявки — шаги ──────────────────────────────────────
@router.callback_query(F.data == "order:start")
async def cb_order_start(call: CallbackQuery, state: FSMContext):
    lang = await get_user_lang(call.from_user.id)
    rows = await cart_get(call.from_user.id)
    if not rows:
        await call.answer(t("cart_empty_order", lang), show_alert=True)
        return
    await call.message.edit_text(t("order_ask_name", lang), parse_mode="Markdown")
    await state.update_data(lang=lang)
    await state.set_state(OrderForm.name)

@router.message(OrderForm.name)
async def order_name(message: Message, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data.get("lang", "ru")
    await state.update_data(name=message.text.strip())
    await message.answer(t("order_ask_company", lang), parse_mode="Markdown")
    await state.set_state(OrderForm.company)

@router.message(OrderForm.company)
async def order_company(message: Message, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data.get("lang", "ru")
    await state.update_data(company=message.text.strip())
    await message.answer(t("order_ask_city", lang))
    await state.set_state(OrderForm.city)

@router.message(OrderForm.city)
async def order_city(message: Message, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data.get("lang", "ru")
    await state.update_data(city=message.text.strip())
    await message.answer(t("order_ask_phone", lang), parse_mode="Markdown")
    await state.set_state(OrderForm.phone)

@router.message(OrderForm.phone)
async def order_phone(message: Message, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data.get("lang", "ru")
    await state.update_data(phone=message.text.strip())
    await message.answer(t("order_ask_delivery", lang), reply_markup=delivery_kb(lang))
    await state.set_state(OrderForm.delivery)

@router.callback_query(OrderForm.delivery, F.data.startswith("delivery:"))
async def order_delivery(call: CallbackQuery, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data.get("lang", "ru")
    delivery_map = {
        "pickup":    t("delivery_pickup",    lang),
        "tashkent":  t("delivery_tashkent",  lang),
        "transport": t("delivery_transport", lang),
    }
    delivery_key = call.data.split(":")[1]
    delivery_str = delivery_map.get(delivery_key, delivery_key)
    await state.update_data(delivery=delivery_str)

    data = await state.get_data()
    rows = await cart_get(call.from_user.id)

    items = []
    total = 0
    total_qty = 0
    cart_lines = []
    for row in rows:
        product, section = get_product(row["product_num"])
        if not product:
            continue
        qty = row["quantity"]
        subtotal = product["price_sum"] * qty
        total += subtotal
        total_qty += qty
        items.append({"num": product["number"], "name": product["name"],
                      "qty": qty, "price": product["price_sum"]})
        cart_lines.append(f"• Арт.{product['number']} {product['name']} × {qty} шт.")

    discount = calc_discount(total_qty)
    discount_sum = int(total * discount)
    final = total - discount_sum

    from utils.sheets import log_order_to_sheets
    order_id = await save_order(
        user_id=call.from_user.id,
        items_json=json.dumps(items, ensure_ascii=False),
        total_sum=final,
        name=data["name"],
        company=data["company"],
        city=data["city"],
        phone=data["phone"],
        delivery=delivery_str
    )

    await log_order_to_sheets(
        order_id=order_id, user_id=call.from_user.id,
        name=data["name"], company=data["company"],
        city=data["city"], phone=data["phone"],
        delivery=delivery_str,
        items_json=json.dumps(items, ensure_ascii=False),
        total_sum=final
    )

    await call.message.edit_text(
        t("order_confirmed", lang).format(id=order_id, phone=data["phone"], total=format_price(final)),
        parse_mode="Markdown"
    )

    # Manager notification (always Russian for manager)
    if MANAGER_CHAT_ID:
        manager_text = (
            f"🔔 *НОВАЯ ЗАЯВКА №{order_id}*\n\n"
            f"👤 {data['name']}\n"
            f"🏢 {data['company']}\n"
            f"📍 {data['city']}\n"
            f"📱 {data['phone']}\n"
            f"🚚 {delivery_str}\n\n"
            f"*Состав заказа:*\n" + "\n".join(cart_lines) + "\n\n"
            f"📦 Позиций: {total_qty} шт.\n"
        )
        if discount > 0:
            manager_text += f"💚 Скидка {int(discount*100)}%: −{format_price(discount_sum)}\n"
        manager_text += f"💰 *Итого: {format_price(final)}*"
        await call.bot.send_message(MANAGER_CHAT_ID, manager_text, parse_mode="Markdown")

    await cart_clear(call.from_user.id)
    await state.clear()
    await call.message.answer(t("main_menu_lbl", lang), reply_markup=main_menu_kb(lang))


# ── Заказ из Telegram Mini App (webapp.html) ──────────────────────
@router.message(F.web_app_data)
async def on_webapp_order(message: Message):
    lang = await get_user_lang(message.from_user.id)
    try:
        data = json.loads(message.web_app_data.data)
    except (json.JSONDecodeError, AttributeError):
        await message.answer(t("webapp_error", lang))
        return

    order_type = data.get("type", "order")

    if order_type == "order":
        items = data.get("items", [])
        total = data.get("total", 0)
        discount = data.get("discount", 0)
        name = data.get("name", "—")
        phone = data.get("phone", "—")
        delivery = data.get("delivery", "—")

        if not items:
            await message.answer(t("webapp_cart_empty", lang))
            return

        cart_lines = []
        items_for_db = []
        for item in items:
            line = f"• Арт.{item.get('number', '?')} {item.get('name', '?')} × {item.get('qty', 1)} шт."
            cart_lines.append(line)
            items_for_db.append({
                "num":   item.get("number"),
                "name":  item.get("name"),
                "qty":   item.get("qty", 1),
                "price": item.get("price", 0),
            })

        total_qty = sum(i.get("qty", 1) for i in items)

        from utils.sheets import log_order_to_sheets
        order_id = await save_order(
            user_id=message.from_user.id,
            items_json=json.dumps(items_for_db, ensure_ascii=False),
            total_sum=total,
            name=name,
            company="—",
            city="—",
            phone=phone,
            delivery=delivery,
        )

        await log_order_to_sheets(
            order_id=order_id,
            user_id=message.from_user.id,
            name=name,
            company="Mini App",
            city="—",
            phone=phone,
            delivery=delivery,
            items_json=json.dumps(items_for_db, ensure_ascii=False),
            total_sum=total,
        )

        await message.answer(
            t("order_confirmed", lang).format(id=order_id, phone=phone, total=format_price(total)),
            parse_mode="Markdown",
            reply_markup=main_menu_kb(lang),
        )

        if MANAGER_CHAT_ID:
            discount_line = f"💚 Скидка: −{format_price(discount)}\n" if discount > 0 else ""
            manager_text = (
                f"🔔 *НОВАЯ ЗАЯВКА №{order_id}* _(Mini App)_\n\n"
                f"👤 {name}\n"
                f"📱 {phone}\n"
                f"🚚 {delivery}\n\n"
                f"*Состав заказа:*\n" + "\n".join(cart_lines) + "\n\n"
                f"📦 Позиций: {total_qty} шт.\n"
                f"{discount_line}"
                f"💰 *Итого: {format_price(total)}*"
            )
            await message.bot.send_message(MANAGER_CHAT_ID, manager_text, parse_mode="Markdown")
