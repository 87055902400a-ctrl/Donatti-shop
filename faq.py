from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.main_kb import faq_kb, main_menu_kb
from utils.i18n import t, get_user_lang, all_variants

router = Router()

FAQ = {
    "delivery": (
        "🚚 *Доставка*\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🏙 *По Ташкенту*\n"
        "• Бесплатно при заказе от 500 000 сум\n"
        "• Платная доставка — при меньшей сумме\n\n"
        "🗺 *По Узбекистану*\n"
        "• Транспортные компании: Yandex Delivery, Express24 и др.\n\n"
        "🚗 *Самовывоз* — бесплатно\n"
        "_(адрес предоставит менеджер)_\n\n"
        "⏱ Срок обработки заказа: *1–2 рабочих дня*"
    ),
    "payment": (
        "💳 *Оплата*\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "✅ Наличные при получении\n"
        "✅ Перевод на карту\n"
        "✅ По счёту для юридических лиц\n"
        "🔜 Онлайн: Payme / Click _(скоро)_"
    ),
    "cert": (
        "📋 *Оригинальность и сертификаты*\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🇪🇺 Сертификат *EU CPNP* (Европейский союз)\n"
        "🇧🇷 Производство: Бразилия\n"
        "📦 Прямые поставки от производителя\n"
        "🧪 Дерматологическое тестирование\n"
        "🚫 Без SLS и парабенов _(в линейках Home Care)_\n\n"
        "*100% оригинальная продукция — гарантия MALINI BEAUTY GROUP*"
    ),
    "return": (
        "↩️ *Возврат товара*\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "• Возврат в течение *7 дней* при сохранении товарного вида\n"
        "• Упаковка должна быть *не вскрытой*\n"
        "• При обнаружении брака — *замена без ограничений*\n\n"
        "По вопросам возврата обратитесь к менеджеру 👇"
    ),
    "min_order": (
        "📦 *Минимальный заказ и скидки*\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "💼 Розница: от *500 000 сум*\n"
        "🏭 Оптовый партнёр: от *2 000 000 сум*\n\n"
        "🎁 *Оптовые скидки:*\n"
        "├ 10–49 позиций → скидка *5%*\n"
        "├ 50–99 позиций → скидка *10%*\n"
        "└ 100+ позиций  → скидка *15%*\n\n"
        "_Скидка применяется автоматически при оформлении заказа_"
    ),
}

@router.message(F.text.in_(all_variants("btn_faq")))
async def open_faq(message: Message):
    lang = await get_user_lang(message.from_user.id)
    await message.answer(
        t("faq_title", lang),
        parse_mode="Markdown",
        reply_markup=faq_kb(lang)
    )

@router.callback_query(F.data.startswith("faq:"))
async def cb_faq(call: CallbackQuery):
    lang = await get_user_lang(call.from_user.id)
    key = call.data.split(":")[1]
    if key == "back":
        await call.message.edit_text(
            t("faq_title", lang),
            parse_mode="Markdown",
            reply_markup=faq_kb(lang)
        )
        return

    text = FAQ.get(key)
    if not text:
        await call.answer(t("faq_unavail", lang))
        return

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("faq_back",    lang), callback_data="faq:back")],
        [InlineKeyboardButton(text=t("faq_catalog", lang), callback_data="catalog:sections")],
        [InlineKeyboardButton(text=t("faq_contact", lang), callback_data="contact:manager")],
    ])
    await call.message.edit_text(text, parse_mode="Markdown", reply_markup=kb)


@router.message(F.text.in_(all_variants("btn_manager")))
async def contact_manager(message: Message):
    lang = await get_user_lang(message.from_user.id)
    await message.answer(t("manager_text", lang), parse_mode="Markdown")

@router.callback_query(F.data == "contact:manager")
async def cb_contact_manager(call: CallbackQuery):
    lang = await get_user_lang(call.from_user.id)
    await call.message.answer(t("manager_text", lang), parse_mode="Markdown")
    await call.answer()

@router.message(F.text.in_(all_variants("btn_profile")))
async def my_profile(message: Message):
    lang = await get_user_lang(message.from_user.id)
    from utils.database import get_user
    user = await get_user(message.from_user.id)
    type_labels = {
        "salon":     t("type_salon",     lang),
        "master":    t("type_master",    lang),
        "school":    t("type_school",    lang),
        "wholesale": t("type_wholesale", lang),
    }
    lang_names = {
        "ru": t("lang_name_ru", lang),
        "uz": t("lang_name_uz", lang),
        "pt": t("lang_name_pt", lang),
    }
    if not user or not user["client_type"]:
        await message.answer(t("profile_empty", lang), parse_mode="Markdown")
        return
    user_lang = user.get("lang", "ru")
    await message.answer(
        t("profile_text", lang).format(
            type=type_labels.get(user["client_type"], user["client_type"]),
            city=user["city"] or "—",
            phone=user["phone"] or "—",
            lang=lang_names.get(user_lang, user_lang),
        ),
        parse_mode="Markdown"
    )

@router.callback_query(F.data == "menu:main")
async def cb_main_menu(call: CallbackQuery):
    lang = await get_user_lang(call.from_user.id)
    await call.message.delete()
    await call.message.answer(t("main_menu_lbl", lang), reply_markup=main_menu_kb(lang))
