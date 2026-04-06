from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from utils.consultant import respond_ai, trim_history
from utils.i18n import t, get_user_lang, all_variants

router = Router()

class ConsultantState(StatesGroup):
    chatting = State()

QUICK_TOPICS = [
    ("💧 Выпадение волос",     "Расскажи о причинах выпадения волос и какие продукты Donatti помогут"),
    ("❄️ Перхоть",             "Как избавиться от перхоти? Какие продукты Donatti подойдут?"),
    ("💦 Жирные волосы",       "Что делать с жирными волосами и жирной кожей головы?"),
    ("🌵 Сухие и ломкие",      "Мои волосы сухие и ломкие. Что посоветуешь из Donatti?"),
    ("🌀 Кудрявые волосы",     "Как ухаживать за кудрявыми волосами? Расскажи о линейке Mio Ricci"),
    ("✂️ Секущиеся кончики",   "Как бороться с секущимися кончиками?"),
    ("👱 Желтизна блонд",      "Как убрать желтизну с осветлённых волос? Cream Blond или Premium Violet?"),
    ("⚗️ После осветления",    "Как восстановить волосы после осветления? Расскажи о DNAvanze"),
    ("💎 Кератин",             "Расскажи о кератиновом выпрямлении Baobá — как это работает?"),
    ("🎨 Окрашенные волосы",   "Как ухаживать за окрашенными волосами? Линейка Colore"),
    ("🌿 Детокс",              "Что такое детокс кожи головы? Расскажи о Biodetox"),
    ("🧬 Структура волоса",    "Объясни строение волоса и почему он повреждается"),
    ("⚖️ pH баланс",           "Что такое pH баланс волос и почему он важен?"),
    ("♨️ Термозащита",         "Как защитить волосы от высоких температур?"),
    ("🤱 После родов",         "Выпадение волос после родов — что делать?"),
]


def consultant_menu_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    rows = []
    for i in range(0, len(QUICK_TOPICS), 2):
        row = [InlineKeyboardButton(text=QUICK_TOPICS[i][0], callback_data=f"ask:{i}")]
        if i + 1 < len(QUICK_TOPICS):
            row.append(InlineKeyboardButton(text=QUICK_TOPICS[i+1][0], callback_data=f"ask:{i+1}"))
        rows.append(row)
    rows.append([InlineKeyboardButton(text=t("btn_free_question", lang), callback_data="consultant:free")])
    rows.append([InlineKeyboardButton(text=t("btn_clear_history",  lang), callback_data="consultant:clear")])
    rows.append([InlineKeyboardButton(text=t("btn_main_menu",      lang), callback_data="menu:main")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


SECTION_ICONS = {
    "BAOBÁ":           "🌿",
    "SPECIALE":        "✨",
    "COLORE":          "🎨",
    "CREAM BLOND":     "💛",
    "THEION":          "⚗️",
    "DNAVANZE":        "🧬",
    "BIODETOX":        "🍃",
    "MIO RICCI":       "🌀",
    "NATURALE":        "🌸",
    "LUXURY":          "👑",
    "PREMIUM VIOLET":  "💜",
    "EXTRA":           "⭐",
}

def detect_sections(text: str) -> list[str]:
    found = []
    text_upper = text.upper()
    for section in SECTION_ICONS:
        if section in text_upper or section.replace("Á", "A") in text_upper:
            found.append(section)
    return found


def back_to_consultant_kb(answer: str = "", lang: str = "ru") -> InlineKeyboardMarkup:
    rows = []
    sections = detect_sections(answer)
    for section in sections[:3]:
        icon = SECTION_ICONS.get(section, "•")
        rows.append([InlineKeyboardButton(
            text=t("view_in_catalog", lang).format(s=f"{icon} {section}"),
            callback_data=f"section:{section}"
        )])

    if not sections:
        rows.append([InlineKeyboardButton(text=t("btn_open_catalog", lang), callback_data="catalog:sections")])

    rows.append([
        InlineKeyboardButton(text=t("btn_more_question", lang), callback_data="consultant:free"),
        InlineKeyboardButton(text=t("btn_topics",        lang), callback_data="consultant:menu"),
    ])
    rows.append([InlineKeyboardButton(text=t("btn_cart", lang), callback_data="cart:view")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def chat_kb(lang: str = "ru") -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=t("chat_btn_question", lang)), KeyboardButton(text=t("chat_btn_topics", lang))],
            [KeyboardButton(text=t("btn_catalog",       lang)), KeyboardButton(text=t("btn_cart",        lang))],
            [KeyboardButton(text=t("chat_btn_back",     lang))],
        ],
        resize_keyboard=True
    )


# ── Открыть консультанта ──────────────────────────────────────────
@router.message(F.text.in_(all_variants("btn_consultant")))
async def open_consultant(message: Message, state: FSMContext):
    lang = await get_user_lang(message.from_user.id)
    await state.clear()
    await message.answer(
        t("consultant_welcome", lang),
        parse_mode="Markdown",
        reply_markup=consultant_menu_kb(lang)
    )


# ── Быстрые темы ─────────────────────────────────────────────────
@router.callback_query(F.data.startswith("ask:"))
async def cb_quick_topic(call: CallbackQuery, state: FSMContext):
    lang = await get_user_lang(call.from_user.id)
    idx = int(call.data.split(":")[1])
    if idx >= len(QUICK_TOPICS):
        await call.answer()
        return

    question = QUICK_TOPICS[idx][1]
    await call.message.edit_reply_markup(reply_markup=None)

    thinking = await call.message.answer(t("consultant_thinking", lang), parse_mode="Markdown")

    data = await state.get_data()
    history = data.get("history", [])
    answer = await respond_ai(question, history)

    history.append({"role": "user",      "content": question})
    history.append({"role": "assistant", "content": answer})
    await state.update_data(history=trim_history(history))
    await state.set_state(ConsultantState.chatting)

    await thinking.delete()
    await call.message.answer(answer, reply_markup=back_to_consultant_kb(answer, lang))


# ── Свободный вопрос ─────────────────────────────────────────────
@router.callback_query(F.data == "consultant:free")
async def cb_free_question(call: CallbackQuery, state: FSMContext):
    lang = await get_user_lang(call.from_user.id)
    await call.message.edit_text(t("consultant_ask", lang))
    await state.set_state(ConsultantState.chatting)


@router.message(ConsultantState.chatting)
async def on_free_question(message: Message, state: FSMContext):
    if not message.text:
        return
    lang = await get_user_lang(message.from_user.id)

    thinking = await message.answer(t("consultant_thinking", lang), parse_mode="Markdown")

    data = await state.get_data()
    history = data.get("history", [])
    answer = await respond_ai(message.text, history)

    history.append({"role": "user",      "content": message.text})
    history.append({"role": "assistant", "content": answer})
    await state.update_data(history=trim_history(history))

    await thinking.delete()
    await message.answer(answer, reply_markup=back_to_consultant_kb(answer, lang))


# ── Кнопки возврата ──────────────────────────────────────────────
@router.callback_query(F.data == "consultant:menu")
async def cb_consultant_menu(call: CallbackQuery, state: FSMContext):
    lang = await get_user_lang(call.from_user.id)
    await call.message.edit_text(
        t("consultant_topic_menu", lang),
        parse_mode="Markdown",
        reply_markup=consultant_menu_kb(lang)
    )


@router.callback_query(F.data == "consultant:clear")
async def cb_clear_history(call: CallbackQuery, state: FSMContext):
    lang = await get_user_lang(call.from_user.id)
    await state.update_data(history=[])
    await call.answer(t("history_cleared", lang), show_alert=False)
    await call.message.edit_text(
        t("consultant_cleared", lang),
        parse_mode="Markdown",
        reply_markup=consultant_menu_kb(lang)
    )


@router.message(F.text.in_(all_variants("chat_btn_question") | all_variants("chat_btn_topics")))
async def kb_shortcuts(message: Message, state: FSMContext):
    lang = await get_user_lang(message.from_user.id)
    if message.text in all_variants("chat_btn_topics"):
        await message.answer(
            t("consultant_topic_menu", lang),
            parse_mode="Markdown",
            reply_markup=consultant_menu_kb(lang)
        )
    else:
        await message.answer(t("consultant_ask", lang))
        await state.set_state(ConsultantState.chatting)


@router.message(F.text.in_(all_variants("chat_btn_back")))
async def back_to_main(message: Message, state: FSMContext):
    from keyboards.main_kb import main_menu_kb
    lang = await get_user_lang(message.from_user.id)
    await state.clear()
    await message.answer(t("main_menu_lbl", lang), reply_markup=main_menu_kb(lang))
