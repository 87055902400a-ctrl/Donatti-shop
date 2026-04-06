import os
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.main_kb import sections_kb, products_kb, product_card_kb
from data.catalog_loader import get_sections, get_section, get_product, search_products, format_price
from utils.database import get_section_reviews
from utils.i18n import t, get_user_lang, all_variants, translate_product_name

IMAGES_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "section_images")

def get_section_photo(section_id: str):
    safe = section_id.replace(" ", "_").replace("Á", "A").replace("Ó", "O")
    path = os.path.join(IMAGES_DIR, f"{safe}.jpeg")
    if os.path.exists(path):
        return FSInputFile(path)
    return None

router = Router()

class SearchState(StatesGroup):
    waiting_query = State()

SECTION_ICONS = {
    "SPECIALE":       "✨",
    "THEION":         "⚗️",
    "COLORE":         "🎨",
    "CREAM BLOND":    "💛",
    "BAOBÁ":          "🌿",
    "BAOBÁ REDUCE":   "🌿",
    "DNAVANZE":       "🧬",
    "BIODETOX":       "🍃",
    "MIO RICCI":      "🌀",
    "NATURALE":       "🌸",
    "LUXURY":         "👑",
    "PREMIUM VIOLET": "💜",
    "EXTRA":          "⭐",
}

SECTION_REVIEWS = {
    "SPECIALE": (
        "⭐⭐⭐⭐⭐ *Нилуфар М., мастер-колорист:*\n"
        "«Маска Nutri — просто спасение для волос клиенток после окрашивания. "
        "Держу в запасе всегда. Результат виден уже после первого применения.»\n\n"
        "⭐⭐⭐⭐ *Гульбахор, Ташкент:*\n"
        "«Раньше брала Salerm Keratin Shot — тоже неплохо питает. "
        "Но Speciale мягче и не утяжеляет. Перешла и не жалею 🙂»"
    ),
    "THEION": (
        "⭐⭐⭐⭐⭐ *Дилноза К., владелец салона:*\n"
        "«THEION закупаем для всех процедур восстановления. "
        "Клиентки замечают разницу — волосы становятся эластичными, не ломаются.»\n\n"
        "⭐⭐⭐⭐ *Гульбахор, Ташкент:*\n"
        "«Честно, я сомневалась — у подруги хороший результат от Salerm. "
        "Попробовала THEION и волосы реально стали крепче. Беру второй раз.»"
    ),
    "COLORE": (
        "⭐⭐⭐⭐⭐ *Малика Р., колорист:*\n"
        "«После окрашивания рекомендую клиенткам именно эту линейку. "
        "Цвет держится дольше, блеск сохраняется 4–5 недель.»\n\n"
        "⭐⭐⭐ *Гульбахор, Ташкент:*\n"
        "«Хороший шампунь, но Salerm Color Care мне нравился больше по запаху. "
        "Зато здесь цена приятнее и результат не хуже.»"
    ),
    "CREAM BLOND": (
        "⭐⭐⭐⭐⭐ *Зарина Т., блондинка со стажем:*\n"
        "«Наконец-то нашла уход который не пересушивает! "
        "После осветления волосы были как солома — теперь мягкие и живые.»\n\n"
        "⭐⭐⭐⭐⭐ *Гульбахор, Ташкент:*\n"
        "«Обожаю! Желтизна уходит, волосы блестят. "
        "Подруга советовала Salerm Blond, но Cream Blond мне зашёл больше 💛»"
    ),
    "BAOBÁ REDUCE": (
        "⭐⭐⭐⭐⭐ *Феруза А., мастер по выпрямлению:*\n"
        "«Делаю кератин этой системой уже год. Клиентки довольны — "
        "результат держится 3–4 месяца, без резкого запаха.»\n\n"
        "⭐⭐⭐⭐ *Гульбахор, Ташкент:*\n"
        "«До этого делала кератин другой маркой. BAOBÁ держится дольше "
        "и волосы после не такие «пластиковые». Рекомендую!»"
    ),
    "DNAVANZE": (
        "⭐⭐⭐⭐⭐ *Камола Ш., мастер:*\n"
        "«Аналог Olaplex, но доступнее. Добавляю в каждое окрашивание — "
        "волосы клиенток стали значительно крепче.»\n\n"
        "⭐⭐⭐⭐ *Гульбахор, Ташкент:*\n"
        "«После осветления волосы жуть что были. Мастер посоветовала DNAVANZE. "
        "Через месяц — небо и земля! Хотя Salerm тоже восстанавливает, но дороже.»"
    ),
    "BIODETOX": (
        "⭐⭐⭐⭐⭐ *Насиба М., трихолог:*\n"
        "«Рекомендую всем клиенткам с жирной кожей головы. "
        "Активированный уголь реально очищает — перхоть и зуд проходят.»\n\n"
        "⭐⭐⭐ *Гульбахор, Ташкент:*\n"
        "«Пробовала Salerm для детокса — результат похожий. "
        "У BIODETOX приятнее консистенция и меньше расход. Беру теперь его.»"
    ),
    "MIO RICCI": (
        "⭐⭐⭐⭐⭐ *Шахло Н., кудрявая красотка:*\n"
        "«Наконец кудри живут своей жизнью — упругие, без пушистости. "
        "Совместима с Curly Girl, без сульфатов — всё как надо!»\n\n"
        "⭐⭐⭐⭐ *Гульбахор, Ташкент:*\n"
        "«Моя дочка кудрявая, долго искала подходящий уход. "
        "MIO RICCI отлично держит форму. Salerm тоже есть для кудрей, но дороже.»"
    ),
    "NATURALE": (
        "⭐⭐⭐⭐⭐ *Барно Т., чувствительная кожа:*\n"
        "«Единственная линейка которая не вызывает раздражение. "
        "Monoi и ojon — волосы мягкие и пахнут потрясающе!»\n\n"
        "⭐⭐⭐⭐ *Гульбахор, Ташкент:*\n"
        "«Мне дерматолог посоветовал мягкий уход. NATURALE подошёл отлично. "
        "Честно, ожидала большего от Salerm Organic — а здесь результат лучше.»"
    ),
    "LUXURY": (
        "⭐⭐⭐⭐⭐ *Моhinur А., VIP-клиент:*\n"
        "«Беру для себя лично. Золото и икра — звучит как маркетинг, "
        "но волосы реально блестят и выглядят дорого.»\n\n"
        "⭐⭐⭐⭐⭐ *Гульбахор, Ташкент:*\n"
        "«Подарили на день рождения. Думала — просто красивая упаковка. "
        "Нет! Волосы шелковые, муж заметил сразу 😄 Salerm такого не даёт.»"
    ),
    "PREMIUM VIOLET": (
        "⭐⭐⭐⭐⭐ *Лола С., блондинка:*\n"
        "«Раньше желтизна появлялась через неделю после окрашивания. "
        "Теперь использую PREMIUM VIOLET и цвет остаётся холодным 3–4 недели.»\n\n"
        "⭐⭐⭐ *Гульбахор, Ташкент:*\n"
        "«Salerm Silver мне нравился — держала его долго. "
        "Попробовала PREMIUM VIOLET — нейтрализация лучше, не даёт лиловость. "
        "Перехожу постепенно 😊»"
    ),
    "EXTRA": (
        "⭐⭐⭐⭐⭐ *Дилфуза Р., мастер с 10-летним стажем:*\n"
        "«Профессиональные расходники — всегда в наличии в моём кабинете. "
        "Качество стабильное, поставки регулярные.»\n\n"
        "⭐⭐⭐⭐ *Гульбахор, Ташкент:*\n"
        "«Брала пробники на выставке. Качество хорошее. "
        "Salerm тоже профессиональная линейка, но у Donatti шире ассортимент.»"
    ),
}

# ── Открыть каталог ───────────────────────────────────────────────
@router.message(F.text.in_(all_variants("btn_catalog")))
async def open_catalog(message: Message):
    lang = await get_user_lang(message.from_user.id)
    sections = get_sections()
    total = sum(s["product_count"] for s in sections)
    await message.answer(
        t("catalog_title", lang).format(total=total, count=len(sections)),
        parse_mode="Markdown",
        reply_markup=sections_kb(sections, lang)
    )

@router.callback_query(F.data == "catalog:sections")
async def cb_catalog_sections(call: CallbackQuery):
    lang = await get_user_lang(call.from_user.id)
    sections = get_sections()
    total = sum(s["product_count"] for s in sections)
    text = t("catalog_title", lang).format(total=total, count=len(sections))
    kb = sections_kb(sections, lang)
    if call.message.photo:
        await call.message.delete()
        await call.bot.send_message(chat_id=call.message.chat.id, text=text,
                                    parse_mode="Markdown", reply_markup=kb)
        await call.answer()
        return
    await call.message.edit_text(
        text,
        parse_mode="Markdown",
        reply_markup=sections_kb(sections, lang)
    )

# ── Список товаров линейки ────────────────────────────────────────
@router.callback_query(F.data.startswith("section:"))
async def cb_section(call: CallbackQuery):
    section_id = call.data.split(":", 1)[1]
    section = get_section(section_id)
    if not section:
        await call.answer("Линейка не найдена", show_alert=True)
        return

    lang = await get_user_lang(call.from_user.id)
    icon = SECTION_ICONS.get(section_id, "•")
    desc = section["description"].split(" - ")
    desc_ru = desc[1] if len(desc) > 1 else section["description"]

    # Диапазон цен
    prices = [p["price_sum"] for p in section["products"] if p.get("price_sum")]
    price_range = ""
    if prices:
        mn = f"{min(prices):,}".replace(",", " ")
        mx = f"{max(prices):,}".replace(",", " ")
        price_range = f"\n💰 Цены: от *{mn}* до *{mx}* сум"

    # Отзывы — сначала живые из DB, потом hardcoded
    live_reviews = await get_section_reviews(section_id, limit=3)
    review_block = ""
    if live_reviews:
        lines = [f"\n\n💬 *{t('reviews_title', lang).format(section=section_id)}*"]
        for r in live_reviews:
            stars = "⭐" * r["rating"]
            lines.append(f"{stars} *{r['full_name']}*\n_{r['text']}_")
        review_block = "\n".join(lines)
    elif SECTION_REVIEWS.get(section_id):
        review_block = f"\n\n💬 *Отзывы покупателей:*\n{SECTION_REVIEWS[section_id]}"

    text = (
        f"{icon} *{section['id']}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"_{desc_ru}_\n"
        f"{price_range}\n"
        f"📦 Позиций: *{section['product_count']}*\n"
        f"🇧🇷 Donatti Professional · Made in Brazil"
        f"{review_block}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"Выберите товар 👇"
    )
    photo = get_section_photo(section_id)
    kb = products_kb(section["products"], section_id, lang=lang)
    if photo:
        await call.message.delete()
        await call.bot.send_photo(
            chat_id=call.message.chat.id,
            photo=photo,
            caption=text,
            parse_mode="Markdown",
            reply_markup=kb
        )
    else:
        await call.message.edit_text(text, parse_mode="Markdown", reply_markup=kb)
    await call.answer()

@router.callback_query(F.data.startswith("section_page:"))
async def cb_section_page(call: CallbackQuery):
    _, section_id, page_str = call.data.split(":")
    page = int(page_str)
    section = get_section(section_id)
    if not section:
        await call.answer()
        return
    await call.message.edit_reply_markup(
        reply_markup=products_kb(section["products"], section_id, page)
    )

# ── Карточка товара ───────────────────────────────────────────────
@router.callback_query(F.data.startswith("product:"))
async def cb_product(call: CallbackQuery):
    product_num = int(call.data.split(":")[1])
    product, section = get_product(product_num)
    if not product:
        await call.answer("Товар не найден", show_alert=True)
        return

    lang = await get_user_lang(call.from_user.id)
    icon = SECTION_ICONS.get(section["id"], "•")
    price_str = format_price(product["price_sum"])
    eur_str = f"{product['price_eur']:.2f} €"
    usd_str = f"≈ ${product['price_sum'] / 12700:.1f}"
    name = translate_product_name(product['name'], lang)

    text = (
        f"🏷 *Арт. {product['number']}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"*{name}*\n\n"
        f"{icon} Линейка: *{section['id']}*\n\n"
        f"💰 *{price_str}*\n"
        f"{eur_str}  ·  {usd_str}\n\n"
        f"🇧🇷 Donatti Professional — Made in Brazil\n"
        f"✅ EU CPNP · 100% оригинал"
    )
    kb = product_card_kb(product_num, section["id"])
    photo = get_section_photo(section["id"])
    await call.message.delete()
    if photo:
        await call.bot.send_photo(
            chat_id=call.message.chat.id,
            photo=photo,
            caption=text,
            parse_mode="Markdown",
            reply_markup=kb
        )
    else:
        await call.bot.send_message(
            chat_id=call.message.chat.id,
            text=text,
            parse_mode="Markdown",
            reply_markup=kb
        )

# ── Поиск ─────────────────────────────────────────────────────────
@router.callback_query(F.data == "catalog:search")
async def cb_search_start(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(
        "🔍 *Поиск по каталогу*\n\n"
        "Введите название товара или линейки:\n"
        "_(например: шампунь, баобаб, кератин)_",
        parse_mode="Markdown"
    )
    await state.set_state(SearchState.waiting_query)

@router.message(SearchState.waiting_query)
async def on_search_query(message: Message, state: FSMContext):
    await state.clear()
    lang = await get_user_lang(message.from_user.id)
    results = search_products(message.text.strip())

    if not results:
        await message.answer(
            f"😔 По запросу *\"{message.text}\"* ничего не найдено\.\n\n"
            "Попробуйте другой запрос или выберите линейку из каталога\.",
            parse_mode="MarkdownV2",
            reply_markup=sections_kb(get_sections())
        )
        return

    rows = []
    for p, sec in results[:15]:
        icon = SECTION_ICONS.get(sec["id"], "•")
        rows.append([InlineKeyboardButton(
            text=f"{icon} Арт.{p['number']} — {translate_product_name(p['name'], lang)[:38]}",
            callback_data=f"product:{p['number']}"
        )])
    rows.append([InlineKeyboardButton(text="⬅️ К линейкам", callback_data="catalog:sections")])

    await message.answer(
        f"🔍 Найдено *{len(results)}* позиций по запросу *\"{message.text}\"*:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=rows)
    )

@router.callback_query(F.data == "noop")
async def cb_noop(call: CallbackQuery):
    await call.answer()
