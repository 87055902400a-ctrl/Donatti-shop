"""
🕵️ ВОЛОСЯНОЙ ДЕТЕКТИВ — мини-игра в Telegram боте DONATTI
Пользователь получает «дело», задаёт вопросы кнопками и раскрывает причину проблемы.
"""

import random
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.i18n import all_variants

router = Router()

class DetectiveState(StatesGroup):
    playing = State()

# ── База дел ──────────────────────────────────────────────────────
CASES = [
    {
        "id": "case_1",
        "title": "Дело №1: «Таинственные хлопья»",
        "story": (
            "📋 *ДОСЬЕ КЛИЕНТКИ*\n"
            "Имя: Малика, 28 лет, менеджер\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Малика пришла в панике. На плечах её тёмного пиджака — "
            "белые хлопья. Голова чешется особенно к вечеру. "
            "Говорит: «Я мою голову каждый день, но становится только хуже!»\n\n"
            "🕵️ *Задайте вопросы чтобы раскрыть дело:*"
        ),
        "questions": [
            {
                "q": "Хлопья жирные и крупные или сухие и мелкие?",
                "a": "Крупные, жирноватые, прилипают к волосам у корней."
            },
            {
                "q": "Была ли смена шампуня или косметики недавно?",
                "a": "Нет, пользуется одним шампунем уже два года."
            },
            {
                "q": "Есть ли покраснение или воспаление кожи головы?",
                "a": "Да, небольшое покраснение в теменной зоне."
            },
            {
                "q": "Как питается и много ли стресса на работе?",
                "a": "Много стресса, питается нерегулярно, часто фастфуд."
            },
            {
                "q": "Используете ли укладочные средства каждый день?",
                "a": "Да — лак и мусс ежедневно, смывает не всегда тщательно."
            },
        ],
        "answer_section": "BIODETOX",
        "answer_icon": "🍃",
        "verdict": (
            "🔍 *ВЕРДИКТ ДЕТЕКТИВА*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Причина: *жирная себорея* — нарушение микробиома кожи головы "
            "из-за стресса и накопления остатков укладочных средств.\n\n"
            "Ежедневное мытьё только усиливает выработку себума — "
            "кожа «пересыхает» и компенсирует это жиром.\n\n"
            "💊 *Назначение:* **BIODETOX** — активированный уголь глубоко "
            "очищает кожу головы и восстанавливает баланс. "
            "Рекомендовать 2 раза в неделю, не ежедневно."
        ),
        "wrong_verdict": (
            "🤔 Близко, но не совсем! Жирные хлопья + покраснение + "
            "накопление стайлинга указывают на *жирную себорею*. "
            "Правильный ответ: **BIODETOX** — детокс кожи головы."
        ),
    },
    {
        "id": "case_2",
        "title": "Дело №2: «Призрак блонда»",
        "story": (
            "📋 *ДОСЬЕ КЛИЕНТКИ*\n"
            "Имя: Зарина, 32 года, фотограф\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Зарина рыдает в кресле. Три недели назад она осветлилась "
            "до платинового блонда — мечта! Но сегодня волосы жёлтые как солома, "
            "сухие, трескаются на кончиках. «Я всё делала правильно!» — кричит она.\n\n"
            "🕵️ *Задайте вопросы чтобы раскрыть дело:*"
        ),
        "questions": [
            {
                "q": "Какой шампунь использует после осветления?",
                "a": "Обычный шампунь для всех типов волос, ничего специального."
            },
            {
                "q": "Как часто моет голову и использует ли горячую воду?",
                "a": "Каждый день, очень горячей водой — «люблю когда прям кипяток»."
            },
            {
                "q": "Делала ли восстанавливающие процедуры после осветления?",
                "a": "Нет, мастер ничего не сказал, она и не знала."
            },
            {
                "q": "Есть ли ломкость или обрыв волос?",
                "a": "Да, на расчёске много коротких обломанных волосков."
            },
            {
                "q": "Использует ли термоинструменты после осветления?",
                "a": "Плойка каждый день, без термозащиты."
            },
        ],
        "answer_section": "DNAVANZE",
        "answer_icon": "🧬",
        "verdict": (
            "🔍 *ВЕРДИКТ ДЕТЕКТИВА*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Причина: *разрушение дисульфидных связей волоса* после осветления. "
            "Обычный шампунь + горячая вода + плойка без защиты — "
            "тройной удар по ослабленной структуре.\n\n"
            "Желтизна — это окисление остаточного пигмента от высокой температуры.\n\n"
            "💊 *Назначение:* **DNAVANZE** — Mimetecnol Technology восстанавливает "
            "разорванные связи изнутри. Плюс **CREAM BLOND** нейтрализует желтизну."
        ),
        "wrong_verdict": (
            "🤔 Не угадали! Ломкость + желтизна + плойка после осветления = "
            "разрушение структуры волоса. Правильный ответ: **DNAVANZE** + **CREAM BLOND**."
        ),
    },
    {
        "id": "case_3",
        "title": "Дело №3: «Непослушные локоны»",
        "story": (
            "📋 *ДОСЬЕ КЛИЕНТКИ*\n"
            "Имя: Шахло, 25 лет, учительница\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Шахло врывается с криком: «Мои кудри исчезли!». "
            "У неё природные локоны, но последние месяцы волосы просто "
            "пушатся огромным облаком, завиток не держится, "
            "кончики сухие и торчат в разные стороны.\n\n"
            "🕵️ *Задайте вопросы чтобы раскрыть дело:*"
        ),
        "questions": [
            {
                "q": "Какой шампунь использует для кудрявых волос?",
                "a": "Обычный с сульфатами — «беру что подешевле в супермаркете»."
            },
            {
                "q": "Как расчёсывает волосы — сухие или влажные?",
                "a": "Расчёсывает сухими, жёсткой щёткой, каждое утро."
            },
            {
                "q": "Наносит ли несмываемый уход или крем для локонов?",
                "a": "Никогда ничего не слышала о несмываемом уходе."
            },
            {
                "q": "Изменился ли рацион или была ли смена воды?",
                "a": "Переехала в новый район — вода очень жёсткая, известковая."
            },
            {
                "q": "Как сушит волосы после мытья?",
                "a": "Полотенцем — трёт сильно, потом феном с горячим воздухом."
            },
        ],
        "answer_section": "MIO RICCI",
        "answer_icon": "🌀",
        "verdict": (
            "🔍 *ВЕРДИКТ ДЕТЕКТИВА*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Причина: *неправильный уход за кудрявыми волосами*. "
            "Сульфатный шампунь высушивает локоны, расчёска разрушает завиток, "
            "жёсткая вода оставляет налёт, полотенце создаёт фризz.\n\n"
            "Кудрявые волосы — особый тип, требует специального протокола.\n\n"
            "💊 *Назначение:* **MIO RICCI** — без сульфатов и силиконов, "
            "совместима с Curly Girl методом. Расчёсывать только влажными пальцами."
        ),
        "wrong_verdict": (
            "🤔 Почти! Пушистость + потеря завитка + сульфаты = "
            "кудрявые волосы без правильного ухода. Правильный ответ: **MIO RICCI**."
        ),
    },
    {
        "id": "case_4",
        "title": "Дело №4: «Тайна выпадения»",
        "story": (
            "📋 *ДОСЬЕ КЛИЕНТКИ*\n"
            "Имя: Гульнора, 35 лет, предприниматель\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Гульнора приходит тихо, без слёз — но видно что она в отчаянии. "
            "На расчёске каждое утро — огромный пучок волос. "
            "«Я боюсь мыть голову, — шепчет она, — там столько выпадает.»\n\n"
            "🕵️ *Задайте вопросы чтобы раскрыть дело:*"
        ),
        "questions": [
            {
                "q": "Когда началось выпадение — было ли что-то стрессовое за 2-3 месяца до?",
                "a": "Да! Три месяца назад очень тяжёлый развод и переезд."
            },
            {
                "q": "Выпадение равномерное или очагами в определённых местах?",
                "a": "Равномерно по всей голове, больше на висках."
            },
            {
                "q": "Сдавала ли анализы — ферритин, ТТГ, витамин D?",
                "a": "Нет, давно не была у врача."
            },
            {
                "q": "Как питается — достаточно ли белка и железа?",
                "a": "Почти не ест мясо, часто пропускает завтраки."
            },
            {
                "q": "Принимает ли какие-то лекарства или была ли болезнь?",
                "a": "Полгода назад переболела ковидом, довольно тяжело."
            },
        ],
        "answer_section": "SPECIALE",
        "answer_icon": "✨",
        "verdict": (
            "🔍 *ВЕРДИКТ ДЕТЕКТИВА*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Причина: *телогеновое выпадение* — классическая реакция организма "
            "на стресс и перенесённую болезнь. Волосы «уходят в сон» через "
            "2-3 месяца после триггера.\n\n"
            "⚠️ Важно: внешний уход — поддержка, но нужно лечить изнутри. "
            "Анализы обязательны!\n\n"
            "💊 *Назначение:* **SPECIALE Nutri** — питание и укрепление "
            "волосяных фолликулов. Плюс консультация трихолога."
        ),
        "wrong_verdict": (
            "🤔 Не совсем! Стресс + болезнь + равномерное выпадение = "
            "телогеновое выпадение. Внешне поможет **SPECIALE**, "
            "но главное — разобраться с причиной изнутри."
        ),
    },
    {
        "id": "case_5",
        "title": "Дело №5: «Цвет-призрак»",
        "story": (
            "📋 *ДОСЬЕ КЛИЕНТКИ*\n"
            "Имя: Камила, 29 лет, дизайнер\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Камила красит волосы каждые 4 недели — цвет вымывается катастрофически быстро. "
            "Тратит огромные деньги у колориста, а через 10 дней — "
            "уже бледная невзрачная масса. «Я думала у меня плохой мастер, "
            "но сменила трёх — результат тот же!»\n\n"
            "🕵️ *Задайте вопросы чтобы раскрыть дело:*"
        ),
        "questions": [
            {
                "q": "Каким шампунем моет окрашенные волосы?",
                "a": "Обычным антиперхотным — «ну там же нет перхоти, просто привычка»."
            },
            {
                "q": "Как часто моет голову и какой температуры вода?",
                "a": "Раз в день, очень горячей водой — «холодная раздражает»."
            },
            {
                "q": "Выходит ли на солнце без защиты для волос?",
                "a": "Работает у окна весь день, летом на море без шапки."
            },
            {
                "q": "Использует ли кондиционер или маску для окрашенных?",
                "a": "Иногда берёт что-то случайное, без системы."
            },
            {
                "q": "Делает ли глубокое очищение волос перед окрашиванием?",
                "a": "Нет, мастер красит сразу — без подготовки."
            },
        ],
        "answer_section": "COLORE",
        "answer_icon": "🎨",
        "verdict": (
            "🔍 *ВЕРДИКТ ДЕТЕКТИВА*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Причина: *вымывание пигмента* из-за агрессивного шампуня, "
            "горячей воды и УФ-излучения. Антиперхотные шампуни особенно "
            "агрессивны для красителя.\n\n"
            "Горячая вода открывает чешуйку волоса и пигмент «вытекает» с каждым мытьём.\n\n"
            "💊 *Назначение:* **COLORE** — специальная линейка для защиты "
            "цвета, закрывает чешуйку и предотвращает вымывание пигмента."
        ),
        "wrong_verdict": (
            "🤔 Близко! Быстрое вымывание цвета + горячая вода + агрессивный шампунь = "
            "нужна защита пигмента. Правильный ответ: **COLORE**."
        ),
    },
]

SECTION_OPTIONS = ["BIODETOX", "DNAVANZE", "MIO RICCI", "SPECIALE",
                   "COLORE", "CREAM BLOND", "THEION", "NATURALE",
                   "PREMIUM VIOLET", "LUXURY"]

MAX_QUESTIONS = 3

def case_kb(case_id: str, asked: list, stage: str) -> InlineKeyboardMarkup:
    """Клавиатура для текущего дела."""
    case = next((c for c in CASES if c["id"] == case_id), None)
    if not case:
        return InlineKeyboardMarkup(inline_keyboard=[])

    rows = []
    if stage == "questions":
        available = [q for q in case["questions"] if q["q"] not in asked]
        for q in available[:4]:
            rows.append([InlineKeyboardButton(
                text=f"❓ {q['q'][:50]}",
                callback_data=f"det_q:{case_id}:{case['questions'].index(q)}"
            )])
        rows.append([InlineKeyboardButton(
            text="🎯 Поставить диагноз!",
            callback_data=f"det_guess:{case_id}"
        )])

    elif stage == "guess":
        # Перемешиваем варианты, правильный среди них
        options = [case["answer_section"]]
        others = [s for s in SECTION_OPTIONS if s != case["answer_section"]]
        options += random.sample(others, min(3, len(others)))
        random.shuffle(options)
        for opt in options:
            rows.append([InlineKeyboardButton(
                text=f"💊 {opt}",
                callback_data=f"det_answer:{case_id}:{opt}"
            )])

    return InlineKeyboardMarkup(inline_keyboard=rows)

def score_emoji(questions_used: int) -> str:
    if questions_used == 0: return "🏆 ГЕНИЙ!"
    if questions_used == 1: return "⭐⭐⭐ Отлично!"
    if questions_used == 2: return "⭐⭐ Хорошо!"
    return "⭐ Неплохо!"

def next_case_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🕵️ Следующее дело!", callback_data="detective:start")],
        [InlineKeyboardButton(text="📦 Открыть каталог", callback_data="catalog:sections")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="menu:main")],
    ])

# ── Хэндлеры ─────────────────────────────────────────────────────

@router.message(F.text.in_(all_variants("btn_detective")))
async def start_detective(message: Message, state: FSMContext):
    await _send_new_case(message.answer, state)

@router.callback_query(F.data == "detective:start")
async def cb_start_detective(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await _send_new_case(call.message.answer, state)

async def _send_new_case(send_fn, state: FSMContext):
    case = random.choice(CASES)
    await state.set_state(DetectiveState.playing)
    await state.update_data(
        case_id=case["id"],
        asked=[],
        questions_used=0,
    )
    await send_fn(
        f"🕵️ *ВОЛОСЯНОЙ ДЕТЕКТИВ*\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"*{case['title']}*\n\n"
        f"{case['story']}\n\n"
        f"_У вас есть {MAX_QUESTIONS} вопроса. Чем меньше зададите — тем выше оценка!_",
        parse_mode="Markdown",
        reply_markup=case_kb(case["id"], [], "questions")
    )

@router.callback_query(F.data.startswith("det_q:"))
async def cb_detective_question(call: CallbackQuery, state: FSMContext):
    _, case_id, q_idx_str = call.data.split(":")
    q_idx = int(q_idx_str)

    data = await state.get_data()
    if data.get("case_id") != case_id:
        await call.answer("Это старое дело!", show_alert=True)
        return

    case = next((c for c in CASES if c["id"] == case_id), None)
    if not case:
        return

    question = case["questions"][q_idx]
    asked = data.get("asked", [])
    questions_used = data.get("questions_used", 0)

    if question["q"] in asked:
        await call.answer("Вы уже задавали этот вопрос!", show_alert=True)
        return

    asked.append(question["q"])
    questions_used += 1
    await state.update_data(asked=asked, questions_used=questions_used)

    remaining = MAX_QUESTIONS - questions_used
    text = (
        f"🔎 *Вопрос:* _{question['q']}_\n\n"
        f"💬 *Ответ:* {question['a']}\n\n"
        f"{'⚠️ Последний вопрос! Пора ставить диагноз.' if remaining == 0 else f'Осталось вопросов: {remaining}'}"
    )

    if remaining <= 0:
        await call.message.edit_text(
            text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
                InlineKeyboardButton(text="🎯 Поставить диагноз!", callback_data=f"det_guess:{case_id}")
            ]])
        )
    else:
        await call.message.edit_text(
            text,
            parse_mode="Markdown",
            reply_markup=case_kb(case_id, asked, "questions")
        )

@router.callback_query(F.data.startswith("det_guess:"))
async def cb_detective_guess(call: CallbackQuery, state: FSMContext):
    case_id = call.data.split(":")[1]
    data = await state.get_data()
    questions_used = data.get("questions_used", 0)

    await call.message.edit_text(
        f"🎯 *Время ставить диагноз!*\n\n"
        f"Вы задали {questions_used} из {MAX_QUESTIONS} вопросов.\n\n"
        f"Какая линейка Donatti решит проблему клиентки?",
        parse_mode="Markdown",
        reply_markup=case_kb(case_id, [], "guess")
    )

@router.callback_query(F.data.startswith("det_answer:"))
async def cb_detective_answer(call: CallbackQuery, state: FSMContext):
    _, case_id, answer = call.data.split(":")
    data = await state.get_data()
    questions_used = data.get("questions_used", 0)

    case = next((c for c in CASES if c["id"] == case_id), None)
    if not case:
        return

    correct = answer == case["answer_section"]
    score = score_emoji(questions_used)

    if correct:
        result_text = (
            f"✅ *ВЕРНО! Дело раскрыто!*\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{case['verdict']}\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n"
            f"📊 *Ваша оценка:* {score}\n"
            f"Использовано вопросов: {questions_used}/{MAX_QUESTIONS}"
        )
    else:
        result_text = (
            f"❌ *Не угадали...*\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{case['wrong_verdict']}\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n"
            f"Правильный ответ: {case['answer_icon']} *{case['answer_section']}*\n\n"
            f"_Попробуйте следующее дело — там получится!_"
        )

    await state.clear()
    await call.message.edit_text(
        result_text,
        parse_mode="Markdown",
        reply_markup=next_case_kb()
    )

@router.callback_query(F.data == "menu:main")
async def cb_menu_main(call: CallbackQuery, state: FSMContext):
    from keyboards.main_kb import main_menu_kb
    await state.clear()
    await call.message.answer("Главное меню:", reply_markup=main_menu_kb())
