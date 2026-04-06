"""
DONATTI Bot — i18n (Russian / Uzbek / Portuguese)
Usage: from utils.i18n import t, get_user_lang
"""
from __future__ import annotations

TEXTS: dict[str, dict[str, str]] = {

    # ── Language selection ─────────────────────────────────────────
    "choose_lang": {
        "ru": "🌐 Выберите язык / Tilni tanlang / Escolha o idioma:",
    },
    "lang_set_ru": {
        "ru": "✅ Язык установлен: *Русский*",
        "uz": "✅ Til o'rnatildi: *Ruscha*",
        "pt": "✅ Idioma definido: *Russo*",
    },
    "lang_set_uz": {
        "ru": "✅ Язык установлен: *Ўзбекча*",
        "uz": "✅ Til o'rnatildi: *O'zbekcha*",
        "pt": "✅ Idioma definido: *Uzbeque*",
    },
    "lang_set_pt": {
        "ru": "✅ Язык установлен: *Português*",
        "uz": "✅ Til o'rnatildi: *Portugalcha*",
        "pt": "✅ Idioma definido: *Português*",
    },

    # ── Onboarding ─────────────────────────────────────────────────
    "welcome_new": {
        "ru": (
            "👑 *MALINI BEAUTY GROUP*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Добро пожаловать\\! Мы — официальный дистрибьютор *Donatti Professional* в Узбекистане\\.\n\n"
            "🇧🇷 Профессиональная косметика из Бразилии\n"
            "📦 165 позиций · 12 линеек Home Care и Pro\n"
            "✅ Сертификат EU CPNP · 100% оригинал\n"
            "🏆 Работаем с салонами, мастерами и оптом\n\n"
            "Несколько быстрых вопросов для подбора условий 👇"
        ),
        "uz": (
            "👑 *MALINI BEAUTY GROUP*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Xush kelibsiz\\! Biz — O'zbekistonda *Donatti Professional* ning rasmiy distribyutorimiz\\.\n\n"
            "🇧🇷 Braziliyadan professional kosmetika\n"
            "📦 165 mahsulot · 12 liniya Home Care va Pro\n"
            "✅ EU CPNP sertifikati · 100% original\n"
            "🏆 Salonlar, ustalar va ulgurji savdo bilan ishlaymiz\n\n"
            "Shartlarni tanlash uchun bir necha savol 👇"
        ),
        "pt": (
            "👑 *MALINI BEAUTY GROUP*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Bem\\-vindo\\! Somos o distribuidor oficial da *Donatti Professional* no Uzbequistão\\.\n\n"
            "🇧🇷 Cosméticos profissionais do Brasil\n"
            "📦 165 produtos · 12 linhas Home Care e Pro\n"
            "✅ Certificado EU CPNP · 100% original\n"
            "🏆 Trabalhamos com salões, profissionais e atacado\n\n"
            "Algumas perguntas rápidas para selecionar as condições 👇"
        ),
    },
    "welcome_return": {
        "ru": "👑 *MALINI BEAUTY GROUP*\n\nС возвращением, {name}\\! 🙌\n\nЧем могу помочь сегодня?",
        "uz": "👑 *MALINI BEAUTY GROUP*\n\nXush kelibsiz, {name}\\! 🙌\n\nBugun qanday yordam beraman?",
        "pt": "👑 *MALINI BEAUTY GROUP*\n\nBem\\-vindo de volta, {name}\\! 🙌\n\nComo posso ajudar hoje?",
    },
    "who_are_you": {
        "ru": "🙋 *Кто вы?*\n\n_Выберите подходящий вариант:_",
        "uz": "🙋 *Siz kimsiz?*\n\n_Mos variantni tanlang:_",
        "pt": "🙋 *Quem é você?*\n\n_Escolha a opção adequada:_",
    },
    "type_salon":     {"ru": "💇 Салон красоты",   "uz": "💇 Go'zallik saloni", "pt": "💇 Salão de beleza"},
    "type_master":    {"ru": "✂️ Частный мастер",  "uz": "✂️ Xususiy usta",     "pt": "✂️ Profissional autônomo"},
    "type_school":    {"ru": "🎓 Учебный центр",   "uz": "🎓 O'quv markazi",    "pt": "🎓 Centro educacional"},
    "type_wholesale": {"ru": "🏭 Оптовый партнёр", "uz": "🏭 Ulgurji hamkor",   "pt": "🏭 Parceiro atacadista"},
    "ask_city": {
        "ru": "Отлично\\! {label} ✅\n\n📍 *Из какого вы города?*",
        "uz": "Ajoyib\\! {label} ✅\n\n📍 *Qaysi shahardan ekansiz?*",
        "pt": "Ótimo\\! {label} ✅\n\n📍 *De qual cidade você é?*",
    },
    "ask_source": {
        "ru": "И последнее: *как вы узнали о нас?*\n\n_(Instagram, Telegram, от знакомых)_",
        "uz": "Va oxirgi savol: *biz haqimizda qayerdan bildingiz?*\n\n_(Instagram, Telegram, tanishlar orqali)_",
        "pt": "E por último: *como você nos conheceu?*\n\n_(Instagram, Telegram, indicação)_",
    },
    "onboarding_done": {
        "ru": (
            "✅ *Готово! Добро пожаловать в MALINI BEAUTY GROUP.*\n\n"
            "Теперь вы можете:\n"
            "📦 Просматривать каталог из 165 товаров\n"
            "🧴 Получить консультацию от AI-эксперта\n"
            "🛒 Оформить заказ прямо в боте\n\n"
            "Выберите что вас интересует 👇"
        ),
        "uz": (
            "✅ *Tayyor! MALINI BEAUTY GROUP ga xush kelibsiz.*\n\n"
            "Endi siz:\n"
            "📦 165 mahsulotdan iborat katalogni ko'rishingiz\n"
            "🧴 AI-ekspertdan maslahat olishingiz\n"
            "🛒 Botda to'g'ridan-to'g'ri buyurtma berishingiz mumkin\n\n"
            "Qiziqtirganingizni tanlang 👇"
        ),
        "pt": (
            "✅ *Pronto! Bem\\-vindo ao MALINI BEAUTY GROUP.*\n\n"
            "Agora você pode:\n"
            "📦 Navegar pelo catálogo com 165 produtos\n"
            "🧴 Receber consultoria do especialista AI\n"
            "🛒 Fazer seu pedido diretamente no bot\n\n"
            "Escolha o que te interessa 👇"
        ),
    },

    # ── Main menu buttons ──────────────────────────────────────────
    "btn_shop":       {"ru": "🛍 Открыть магазин",  "uz": "🛍 Do'konni ochish",      "pt": "🛍 Abrir loja"},
    "btn_catalog":    {"ru": "📦 Каталог",           "uz": "📦 Katalog",               "pt": "📦 Catálogo"},
    "btn_cart":       {"ru": "🛒 Корзина",           "uz": "🛒 Savat",                 "pt": "🛒 Carrinho"},
    "btn_consultant": {"ru": "🧴 AI Консультант",    "uz": "🧴 AI Maslahatchi",        "pt": "🧴 Consultor AI"},
    "btn_faq":        {"ru": "❓ FAQ",                "uz": "❓ FAQ",                   "pt": "❓ FAQ"},
    "btn_order":      {"ru": "📝 Оставить заявку",   "uz": "📝 Ariza qoldirish",       "pt": "📝 Fazer pedido"},
    "btn_manager":    {"ru": "📞 Менеджер",          "uz": "📞 Menejer",               "pt": "📞 Gerente"},
    "btn_profile":    {"ru": "👤 Мой профиль",       "uz": "👤 Mening profilim",       "pt": "👤 Meu perfil"},
    "btn_favorites":  {"ru": "❤️ Избранное",         "uz": "❤️ Sevimlilar",            "pt": "❤️ Favoritos"},
    "main_menu_lbl":  {"ru": "Главное меню:",        "uz": "Asosiy menyu:",            "pt": "Menu principal:"},

    # ── Catalog ────────────────────────────────────────────────────
    "catalog_title": {
        "ru": "📦 *Каталог DONATTI Professional*\n━━━━━━━━━━━━━━━━━━━━━\n🇧🇷 {total} позиций · {count} линеек\n\nВыберите линейку для просмотра:",
        "uz": "📦 *DONATTI Professional Katalogi*\n━━━━━━━━━━━━━━━━━━━━━\n🇧🇷 {total} mahsulot · {count} liniya\n\nLiniyani tanlang:",
        "pt": "📦 *Catálogo DONATTI Professional*\n━━━━━━━━━━━━━━━━━━━━━\n🇧🇷 {total} produtos · {count} linhas\n\nEscolha uma linha:",
    },
    "products_in_section": {
        "ru": "📋 Позиций в линейке: *{count}*\n\nВыберите товар:",
        "uz": "📋 Liniyada mahsulotlar: *{count}*\n\nMahsulotni tanlang:",
        "pt": "📋 Produtos na linha: *{count}*\n\nEscolha um produto:",
    },
    "back_to_sections": {"ru": "⬅️ К линейкам",      "uz": "⬅️ Liniyalarga",       "pt": "⬅️ Às linhas"},
    "add_to_cart":      {"ru": "🛒 В корзину",        "uz": "🛒 Savatga",            "pt": "🛒 Carrinho"},
    "back_to_section":  {"ru": "⬅️ Назад к линейке", "uz": "⬅️ Liniyaga qaytish",  "pt": "⬅️ Voltar à linha"},
    "go_to_cart":       {"ru": "🛍 Перейти в корзину","uz": "🛍 Savatga o'tish",    "pt": "🛍 Ir ao carrinho"},
    "search_start":     {"ru": "🔍 Поиск по названию","uz": "🔍 Nom bo'yicha qidirish","pt": "🔍 Buscar por nome"},
    "search_prompt": {
        "ru": "🔍 *Поиск по каталогу*\n\nВведите название товара или линейки:\n_(например: шампунь, баобаб, кератин)_",
        "uz": "🔍 *Katalogda qidirish*\n\nMahsulot yoki liniya nomini kiriting:\n_(masalan: shampun, baoba, keratin)_",
        "pt": "🔍 *Busca no catálogo*\n\nDigite o nome do produto ou linha:\n_(ex: shampoo, baobá, queratina)_",
    },
    "nothing_found": {
        "ru": "😔 По запросу *\"{q}\"* ничего не найдено\.\n\nПопробуйте другой запрос или выберите линейку из каталога\.",
        "uz": "😔 *\"{q}\"* so'rovi bo'yicha hech narsa topilmadi\.\n\nBoshqa so'rov kiriting yoki katalogdan liniyani tanlang\.",
        "pt": "😔 Nenhum resultado para *\"{q}\"*\.\n\nTente outro termo ou escolha uma linha do catálogo\.",
    },
    "found_results": {
        "ru": "🔍 Найдено *{n}* позиций по запросу *\"{q}\"*:",
        "uz": "🔍 *\"{q}\"* so'rovi bo'yicha *{n}* ta mahsulot topildi:",
        "pt": "🔍 Encontrado *{n}* produto\\(s\\) para *\"{q}\"*:",
    },
    "item_added": {
        "ru": "✅ Арт.{num} добавлен в корзину!",
        "uz": "✅ Art.{num} savatga qo'shildi!",
        "pt": "✅ Art.{num} adicionado ao carrinho!",
    },

    # ── Cart ───────────────────────────────────────────────────────
    "cart_empty":      {"ru": "🛒 Корзина пуста",         "uz": "🛒 Savat bo'sh",              "pt": "🛒 Carrinho vazio"},
    "cart_title":      {"ru": "🛒 *Ваша корзина:*\n",     "uz": "🛒 *Sizning savatIngiz:*\n",  "pt": "🛒 *Seu carrinho:*\n"},
    "cart_qty":        {"ru": "📦 Позиций: {n} шт.",      "uz": "📦 Mahsulotlar: {n} dona",    "pt": "📦 Itens: {n} un."},
    "cart_discount":   {"ru": "💚 Скидка {pct}%: −{sum}", "uz": "💚 Chegirma {pct}%: −{sum}", "pt": "💚 Desconto {pct}%: −{sum}"},
    "cart_total":      {"ru": "\n💰 *Итого: {sum}*",      "uz": "\n💰 *Jami: {sum}*",          "pt": "\n💰 *Total: {sum}*"},
    "cart_checkout":   {"ru": "✅ Оформить заявку",       "uz": "✅ Ariza berish",             "pt": "✅ Fazer pedido"},
    "cart_clear_btn":  {"ru": "🗑 Очистить корзину",      "uz": "🗑 Savatni tozalash",         "pt": "🗑 Limpar carrinho"},
    "cart_to_catalog": {"ru": "📦 В каталог",             "uz": "📦 Katalogga",                "pt": "📦 Catálogo"},
    "cart_cleared":    {"ru": "🗑 Корзина очищена.",      "uz": "🗑 Savat tozalandi.",         "pt": "🗑 Carrinho limpo."},

    # ── Cart per-item controls ─────────────────────────────────────
    "cart_show_items": {"ru": "📋 Управление товарами",   "uz": "📋 Mahsulotlarni boshqarish", "pt": "📋 Gerenciar itens"},
    "cart_item_removed": {"ru": "✅ Товар удалён",        "uz": "✅ Mahsulot o'chirildi",       "pt": "✅ Item removido"},

    # ── Order form ─────────────────────────────────────────────────
    "order_ask_name": {
        "ru": "📝 *Оформление заявки*\n\nКак вас зовут? _(имя и фамилия)_",
        "uz": "📝 *Ariza rasmiylashtirish*\n\nIsmingiz? _(ism va familiya)_",
        "pt": "📝 *Fazendo o pedido*\n\nQual é o seu nome? _(nome e sobrenome)_",
    },
    "order_ask_company": {
        "ru": "🏢 Название вашего салона или компании?\n_(или напишите «Частный мастер»)_",
        "uz": "🏢 Salon yoki kompaniya nomingiz?\n_(yoki «Xususiy usta» deb yozing)_",
        "pt": "🏢 Nome do seu salão ou empresa?\n_(ou escreva «Profissional autônomo»)_",
    },
    "order_ask_city": {"ru": "📍 Ваш город?", "uz": "📍 Shahringiz?", "pt": "📍 Sua cidade?"},
    "order_ask_phone": {
        "ru": "📱 Ваш номер телефона?\n_(для связи менеджера)_",
        "uz": "📱 Telefon raqamingiz?\n_(menejer aloqa uchun)_",
        "pt": "📱 Seu número de telefone?\n_(para contato do gerente)_",
    },
    "order_ask_delivery": {
        "ru": "🚚 Выберите способ доставки:",
        "uz": "🚚 Yetkazib berish usulini tanlang:",
        "pt": "🚚 Escolha o método de entrega:",
    },
    "delivery_pickup":    {"ru": "🚗 Самовывоз (Ташкент)",    "uz": "🚗 O'zi olish (Toshkent)",  "pt": "🚗 Retirada (Tashkent)"},
    "delivery_tashkent":  {"ru": "🏠 Доставка по Ташкенту",   "uz": "🏠 Toshkent bo'yicha yetkazish", "pt": "🏠 Entrega em Tashkent"},
    "delivery_transport": {"ru": "📦 Транспортная компания",   "uz": "📦 Transport kompaniyasi",  "pt": "📦 Transportadora"},
    "order_confirmed": {
        "ru": (
            "✅ *Заявка №{id} принята!*\n\n"
            "Наш менеджер свяжется с вами в течение *2 часов*.\n\n"
            "📞 Телефон: {phone}\n"
            "💰 Сумма заказа: *{total}*\n\n"
            "Спасибо, что выбрали DONATTI! 🙏"
        ),
        "uz": (
            "✅ *№{id} ariza qabul qilindi!*\n\n"
            "Menejerimiz *2 soat* ichida siz bilan bog'lanadi.\n\n"
            "📞 Telefon: {phone}\n"
            "💰 Buyurtma summasi: *{total}*\n\n"
            "DONATTI ni tanlaganingiz uchun rahmat! 🙏"
        ),
        "pt": (
            "✅ *Pedido №{id} recebido!*\n\n"
            "Nosso gerente entrará em contato em *2 horas*.\n\n"
            "📞 Telefone: {phone}\n"
            "💰 Total do pedido: *{total}*\n\n"
            "Obrigado por escolher a DONATTI! 🙏"
        ),
    },
    "cart_empty_order": {"ru": "Корзина пуста!", "uz": "Savat bo'sh!", "pt": "Carrinho vazio!"},

    # ── Consultant ─────────────────────────────────────────────────
    "consultant_welcome": {
        "ru": (
            "🤖 *DONATTI AI — Эксперт по уходу за волосами*\n\n"
            "Я знаю всё о 12 линейках Donatti, трихологии и профессиональных процедурах.\n\n"
            "Выберите тему или задайте вопрос своими словами 👇"
        ),
        "uz": (
            "🤖 *DONATTI AI — Soch parvarishi bo'yicha ekspert*\n\n"
            "Men Donatti ning 12 ta liniyasi, trixologiya va professional protseduralar haqida hamma narsani bilaman.\n\n"
            "Mavzuni tanlang yoki savolingizni o'z so'zlaringiz bilan yozing 👇"
        ),
        "pt": (
            "🤖 *DONATTI AI — Especialista em cuidados capilares*\n\n"
            "Conheço tudo sobre as 12 linhas Donatti, tricologia e procedimentos profissionais.\n\n"
            "Escolha um tema ou faça sua pergunta 👇"
        ),
    },
    "consultant_ask": {
        "ru": "✍️ Напишите ваш вопрос о волосах:",
        "uz": "✍️ Soch haqidagi savolingizni yozing:",
        "pt": "✍️ Escreva sua pergunta sobre cabelo:",
    },
    "consultant_thinking": {"ru": "💭 _Думаю..._", "uz": "💭 _O'ylamoqda..._", "pt": "💭 _Pensando..._"},
    "consultant_cleared": {
        "ru": "🤖 *DONATTI AI — Эксперт по уходу за волосами*\n\nИстория разговора очищена. Выберите тему:",
        "uz": "🤖 *DONATTI AI — Soch parvarishi bo'yicha ekspert*\n\nSuhbat tarixi tozalandi. Mavzuni tanlang:",
        "pt": "🤖 *DONATTI AI — Especialista em cuidados capilares*\n\nHistórico limpo. Escolha um tema:",
    },
    "history_cleared": {"ru": "История очищена ✅", "uz": "Tarix tozalandi ✅", "pt": "Histórico limpo ✅"},
    "consultant_topic_menu": {
        "ru": "🤖 *DONATTI AI* — выберите тему:",
        "uz": "🤖 *DONATTI AI* — mavzuni tanlang:",
        "pt": "🤖 *DONATTI AI* — escolha um tema:",
    },
    "btn_free_question": {"ru": "✍️ Задать свой вопрос",    "uz": "✍️ O'z savolingizni yozing", "pt": "✍️ Fazer pergunta"},
    "btn_clear_history": {"ru": "🗑 Очистить историю",      "uz": "🗑 Tarixni tozalash",         "pt": "🗑 Limpar histórico"},
    "btn_main_menu":     {"ru": "⬅️ Главное меню",          "uz": "⬅️ Asosiy menyu",             "pt": "⬅️ Menu principal"},
    "btn_more_question": {"ru": "✍️ Ещё вопрос",           "uz": "✍️ Yana savol",               "pt": "✍️ Outra pergunta"},
    "btn_topics":        {"ru": "📋 Темы",                  "uz": "📋 Mavzular",                 "pt": "📋 Temas"},
    "btn_open_catalog":  {"ru": "🛍 Открыть каталог",       "uz": "🛍 Katalogni ochish",         "pt": "🛍 Abrir catálogo"},
    "chat_btn_question": {"ru": "💬 Ещё вопрос",           "uz": "💬 Yana savol",               "pt": "💬 Outra pergunta"},
    "chat_btn_topics":   {"ru": "📋 Темы консультанта",     "uz": "📋 Maslahat mavzulari",       "pt": "📋 Temas do consultor"},
    "chat_btn_back":     {"ru": "🔙 Главное меню",          "uz": "🔙 Asosiy menyu",             "pt": "🔙 Menu principal"},
    "view_in_catalog":   {"ru": "Смотреть {s} в каталоге", "uz": "{s} ni katalogda ko'rish",    "pt": "Ver {s} no catálogo"},

    # ── FAQ ────────────────────────────────────────────────────────
    "faq_title":   {"ru": "❓ *Частые вопросы*\n\nВыберите тему:", "uz": "❓ *Tez-tez so'raladigan savollar*\n\nMavzuni tanlang:", "pt": "❓ *Perguntas frequentes*\n\nEscolha um tema:"},
    "faq_back":    {"ru": "⬅️ Назад к FAQ",   "uz": "⬅️ FAQ ga qaytish",  "pt": "⬅️ Voltar ao FAQ"},
    "faq_catalog": {"ru": "📦 Каталог",        "uz": "📦 Katalog",          "pt": "📦 Catálogo"},
    "faq_contact": {"ru": "📞 Связаться",      "uz": "📞 Bog'lanish",       "pt": "📞 Contato"},
    "faq_unavail": {"ru": "Информация временно недоступна", "uz": "Ma'lumot vaqtincha mavjud emas", "pt": "Informação temporariamente indisponível"},
    "faq_btn_delivery": {"ru": "🚚 Доставка",         "uz": "🚚 Yetkazib berish",  "pt": "🚚 Entrega"},
    "faq_btn_payment":  {"ru": "💳 Оплата",           "uz": "💳 To'lov",           "pt": "💳 Pagamento"},
    "faq_btn_cert":     {"ru": "📋 Сертификаты",      "uz": "📋 Sertifikatlar",    "pt": "📋 Certificados"},
    "faq_btn_return":   {"ru": "↩️ Возврат",          "uz": "↩️ Qaytarish",        "pt": "↩️ Devolução"},
    "faq_btn_min":      {"ru": "📦 Минимальный заказ","uz": "📦 Minimal buyurtma", "pt": "📦 Pedido mínimo"},
    "btn_back_main":    {"ru": "⬅️ Главное меню",     "uz": "⬅️ Asosiy menyu",    "pt": "⬅️ Menu principal"},

    # ── Profile ────────────────────────────────────────────────────
    "profile_empty": {
        "ru": "👤 Профиль не заполнен.\n\nНапишите /start для регистрации.",
        "uz": "👤 Profil to'ldirilmagan.\n\nRo'yxatdan o'tish uchun /start yozing.",
        "pt": "👤 Perfil não preenchido.\n\nEscreva /start para se registrar.",
    },
    "profile_text": {
        "ru": (
            "👤 *Ваш профиль*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Тип: {type}\n"
            "📍 Город: {city}\n"
            "📱 Телефон: {phone}\n"
            "🌐 Язык: {lang}\n\n"
            "_Для изменения данных напишите /start_\n"
            "_Сменить язык: /lang_"
        ),
        "uz": (
            "👤 *Sizning profilingiz*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Turi: {type}\n"
            "📍 Shahar: {city}\n"
            "📱 Telefon: {phone}\n"
            "🌐 Til: {lang}\n\n"
            "_Ma'lumotlarni o'zgartirish uchun /start yozing_\n"
            "_Tilni o'zgartirish: /lang_"
        ),
        "pt": (
            "👤 *Seu perfil*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Tipo: {type}\n"
            "📍 Cidade: {city}\n"
            "📱 Telefone: {phone}\n"
            "🌐 Idioma: {lang}\n\n"
            "_Para alterar os dados escreva /start_\n"
            "_Mudar idioma: /lang_"
        ),
    },
    "lang_name_ru": {"ru": "Русский",    "uz": "Ruscha",       "pt": "Russo"},
    "lang_name_uz": {"ru": "Ўзбекча",   "uz": "O'zbekcha",    "pt": "Uzbeque"},
    "lang_name_pt": {"ru": "Português",  "uz": "Portugalcha",  "pt": "Português"},

    # ── Manager contact ────────────────────────────────────────────
    "manager_text": {
        "ru": (
            "📞 *Связь с менеджером*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👤 *MALINI BEAUTY GROUP*\n"
            "📱 Telegram: @donatti_manager\n\n"
            "🕐 Время работы: Пн–Сб, 9:00–18:00\n\n"
            "_Менеджер ответит в течение 1–2 часов_"
        ),
        "uz": (
            "📞 *Menejer bilan bog'lanish*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👤 *MALINI BEAUTY GROUP*\n"
            "📱 Telegram: @donatti_manager\n\n"
            "🕐 Ish vaqti: Du–Sha, 9:00–18:00\n\n"
            "_Menejer 1–2 soat ichida javob beradi_"
        ),
        "pt": (
            "📞 *Contato com o gerente*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👤 *MALINI BEAUTY GROUP*\n"
            "📱 Telegram: @donatti_manager\n\n"
            "🕐 Horário: Seg–Sáb, 9:00–18:00\n\n"
            "_O gerente responde em 1–2 horas_"
        ),
    },

    # ── Favorites ─────────────────────────────────────────────────
    "fav_added":     {"ru": "❤️ Добавлено в избранное",  "uz": "❤️ Sevimlilarga qo'shildi",    "pt": "❤️ Adicionado aos favoritos"},
    "fav_removed":   {"ru": "🤍 Удалено из избранного",  "uz": "🤍 Sevimlilardan o'chirildi",   "pt": "🤍 Removido dos favoritos"},
    "fav_empty": {
        "ru": "❤️ *Избранное пусто*\n\nДобавляйте товары из каталога кнопкой ❤️",
        "uz": "❤️ *Sevimlilar bo'sh*\n\nKatalogdan ❤️ tugmasi bilan mahsulot qo'shing",
        "pt": "❤️ *Favoritos vazios*\n\nAdicione produtos do catálogo com o botão ❤️",
    },
    "fav_title":     {"ru": "❤️ *Ваше избранное:*\n",   "uz": "❤️ *Sevimlilaringiz:*\n",      "pt": "❤️ *Seus favoritos:*\n"},
    "fav_remove_btn":{"ru": "🗑 Удалить из избранного",  "uz": "🗑 Sevimlilardan o'chirish",    "pt": "🗑 Remover dos favoritos"},
    "fav_add_btn":   {"ru": "❤️ В избранное",           "uz": "❤️ Sevimlilarga",               "pt": "❤️ Favoritos"},
    "fav_in_cart":   {"ru": "🛒 В корзину",             "uz": "🛒 Savatga",                    "pt": "🛒 Carrinho"},
    "fav_back":      {"ru": "⬅️ Назад",                 "uz": "⬅️ Orqaga",                    "pt": "⬅️ Voltar"},
    "fav_to_catalog":{"ru": "📦 В каталог",             "uz": "📦 Katalogga",                  "pt": "📦 Catálogo"},

    # ── Reviews ───────────────────────────────────────────────────
    "reviews_title": {
        "ru": "⭐ *Отзывы о линейке {section}*",
        "uz": "⭐ *{section} liniyasi haqida sharhlar*",
        "pt": "⭐ *Avaliações da linha {section}*",
    },
    "reviews_empty": {
        "ru": "Отзывов пока нет. Будьте первым! 🙌",
        "uz": "Hali sharh yo'q. Birinchi bo'ling! 🙌",
        "pt": "Sem avaliações ainda. Seja o primeiro! 🙌",
    },
    "reviews_write":  {"ru": "✍️ Оставить отзыв",    "uz": "✍️ Sharh yozish",      "pt": "✍️ Escrever avaliação"},
    "reviews_ask_rating": {
        "ru": "⭐ *Оставить отзыв о линейке {section}*\n\nПоставьте оценку:",
        "uz": "⭐ *{section} liniyasi haqida sharh*\n\nBaholang:",
        "pt": "⭐ *Avaliação da linha {section}*\n\nDê uma nota:",
    },
    "reviews_ask_text": {
        "ru": "Отлично, {stars}!\n\nТеперь напишите ваш отзыв:",
        "uz": "Ajoyib, {stars}!\n\nEndi sharhingizni yozing:",
        "pt": "Ótimo, {stars}!\n\nAgora escreva sua avaliação:",
    },
    "reviews_saved": {
        "ru": "✅ Спасибо за отзыв! Ваше мнение важно для нас 🙏",
        "uz": "✅ Sharh uchun rahmat! Sizning fikringiz bizga muhim 🙏",
        "pt": "✅ Obrigado pela avaliação! Sua opinião é importante para nós 🙏",
    },
    "btn_reviews":   {"ru": "⭐ Отзывы",             "uz": "⭐ Sharhlar",           "pt": "⭐ Avaliações"},
    "btn_write_review": {"ru": "✍️ Написать отзыв",  "uz": "✍️ Sharh yozish",      "pt": "✍️ Escrever avaliação"},

    # ── Admin ──────────────────────────────────────────────────────
    "admin_no_access": {
        "ru": "⛔ Нет доступа.",
        "uz": "⛔ Ruxsat yo'q.",
        "pt": "⛔ Sem acesso.",
    },

    # ── Misc ───────────────────────────────────────────────────────
    "pos_short":         {"ru": "поз.",       "uz": "dona",      "pt": "pos."},
    "art_short":         {"ru": "Арт.",       "uz": "Art.",      "pt": "Art."},
    "pcs_short":         {"ru": "шт.",        "uz": "dona",      "pt": "un."},
    "currency_uz":       {"ru": "сум",        "uz": "so'm",      "pt": "UZS"},
    "btn_detective":     {"ru": "🕵️ Детектив","uz": "🕵️ Detektiv","pt": "🕵️ Detetive"},
    "product_not_found": {"ru": "Товар не найден", "uz": "Mahsulot topilmadi", "pt": "Produto não encontrado"},
    "webapp_error":      {"ru": "⚠️ Ошибка при получении данных из магазина. Попробуйте снова.", "uz": "⚠️ Do'kondan ma'lumot olishda xato. Qayta urinib ko'ring.", "pt": "⚠️ Erro ao receber dados da loja. Tente novamente."},
    "webapp_cart_empty": {"ru": "⚠️ Корзина пуста. Добавьте товары и повторите заказ.", "uz": "⚠️ Savat bo'sh. Mahsulot qo'shib, qayta buyurtma bering.", "pt": "⚠️ Carrinho vazio. Adicione produtos e repita o pedido."},
}


def t(key: str, lang: str = "ru") -> str:
    entry = TEXTS.get(key)
    if not entry:
        return key
    return entry.get(lang) or entry.get("ru") or key


def all_variants(key: str) -> frozenset:
    """Returns all language variants for a translation key (for F.text.in_() filters)."""
    entry = TEXTS.get(key, {})
    return frozenset(v for v in entry.values() if v)


async def get_user_lang(user_id: int) -> str:
    from utils.database import get_user
    user = await get_user(user_id)
    if user and user["lang"]:
        return user["lang"]
    return "ru"


# ── Product name translation (mirrors webapp TERM_SUBS) ──────────────────────
_TERM_SUBS: dict[str, dict[str, str]] = {
    "pt": {
        "Супер серебро (Natural Blond)":           "Super Prata (Natural Louro)",
        "Платиновый (интенсивный серый)":          "Platinado (Cinza Intenso)",
        "Ультра светлый (интенсивный серый)":      "Ultra Claro (Cinza Intenso)",
        "Супер-осветлитель ультра светлый жемчуж": "Superclareador Ultra Claro Perolado",
        "Тёмно-русый интенсивный переливчатый":    "Louro Escuro Intenso Iridescente",
        "Тёмно-русый интенсивный красный":         "Louro Escuro Intenso Vermelho",
        "Специальный марсала красноватый":         "Especial Marsala Avermelhado",
        "Средне-русый интенсивный красный":        "Louro Médio Intenso Vermelho",
        "Средне-русый бежево-золотистый":          "Louro Médio Bege Dourado",
        "Очень светлый бежево-золотистый":         "Louro Muito Claro Bege Dourado",
        "Очень светлый золотистый блонд":          "Louro Muito Claro Dourado",
        "Очень светлый перламутровый":             "Louro Muito Claro Perolado",
        "Пепельный платиновый блонд":              "Louro Platinado Cinza",
        "Тёмно-русый золотисто-медный":            "Louro Escuro Dourado Cobre",
        "Тёмно-русый медно-пепельный":             "Louro Escuro Cobre Cinza",
        "Светло-каштановый пепельный":             "Castanho Claro Cinza",
        "Светло-каштановый золотистый":            "Castanho Claro Dourado",
        "Средне-каштановый шоколадный":            "Castanho Médio Chocolate",
        "Супер-усилитель осветления":              "Super Amplificador de Clareamento",
        "Платиновый блонд":                        "Louro Platinado",
        "Ледяной серый блонд":                     "Louro Cinza Gelo",
        "Ледяной серый":                           "Cinza Gelo",
        "Иссиня-чёрный":                           "Preto Azulado",
        "Тёмно-каштановый":                        "Castanho Escuro",
        "Средне-каштановый":                       "Castanho Médio",
        "Светло-каштановый":                       "Castanho Claro",
        "Тёмно-русый пепельный":                   "Louro Escuro Cinza",
        "Тёмно-русый золотистый":                  "Louro Escuro Dourado",
        "Тёмно-русый шоколадный":                  "Louro Escuro Chocolate",
        "Тёмно-русый":                             "Louro Escuro",
        "Средне-русый пепельный":                  "Louro Médio Cinza",
        "Средне-русый матовый":                    "Louro Médio Matte",
        "Средне-русый золотистый":                 "Louro Médio Dourado",
        "Средне-русый медный":                     "Louro Médio Cobre",
        "Средне-русый шоколадный":                 "Louro Médio Chocolate",
        "Средне-русый жемчужный":                  "Louro Médio Perolado",
        "Средне-русый":                            "Louro Médio",
        "Светло-русый пепельный":                  "Louro Claro Cinza",
        "Светло-русый жемчужный":                  "Louro Claro Perolado",
        "Специальный марсала":                     "Especial Marsala",
        "Очень светло-русый медный":               "Louro Muito Claro Cobre",
        "Очень светло-русый":                      "Louro Muito Claro",
        "Светло-русый":                            "Louro Claro",
        "Несмываемый уход":           "Leave In",
        "Осветляющий порошок":        "Pó Descolorante",
        "Осветляющий крем":           "Creme Descolorante",
        "Восполнитель углерода":      "Repositor de Carbono",
        "Восстанавливающий комплекс": "Complexo Restaurador",
        "Подкисляющий бальзам":       "Bálsamo Acidificante",
        "Реконструктор":              "Reconstrutor",
        "без сульфатов":              "Sulfato Free",
        "Профессиональная":           "Professionale",
        "Профессиональный":           "Professionale",
        "Кондиционер":                "Condicionador",
        "Текстуризатор":              "Texturizador",
        "Разглаживатель":             "Redutor",
        "Стабилизатор":               "Estabilizador",
        "Регенератор":                "Regenerador",
        "Реставратор":                "Restaurador",
        "Выравниватель":              "Realinhador",
        "Окислитель":                 "Oxidante",
        "Шампунь":                    "Shampoo",
        "Краска":                     "Coloração Permanente",
        "Тонирование":                "Tonalizante",
        "Маска":                      "Máscara",
        "Масло":                      "Óleo",
        "Бальзам":                    "Bálsamo",
        "Уход":                       "Manutenzione",
        "Шаг":                        "Passo",
        "Саше":                       "Sachê",
        "объёмов":                    "volumes",
        "рефил":                      "refil",
        "афро":                       "afro",
    },
    "uz": {
        "Иссиня-чёрный":              "Ko'k-qora",
        "Тёмно-каштановый":           "To'q kashtan",
        "Средне-каштановый":          "O'rta kashtan",
        "Светло-каштановый":          "Och kashtan",
        "Тёмно-русый":                "To'q sariq",
        "Средне-русый":               "O'rta sariq",
        "Светло-русый":               "Och sariq",
        "Очень светло-русый":         "Juda och sariq",
        "Платиновый блонд":           "Platinado sariq",
        "Ледяной серый":              "Muzli kulrang",
        "Супер-усилитель осветления": "Super Kuchaytirgich",
        "Несмываемый уход":           "Yuvilmaydigan parvarish",
        "Осветляющий порошок":        "Oqartiruvchi kukun",
        "Осветляющий крем":           "Oqartiruvchi krem",
        "Восполнитель углерода":      "Ko'mir to'ldiruvchi",
        "Восстанавливающий комплекс": "Tiklash kompleksi",
        "Подкисляющий бальзам":       "Kislotali balzam",
        "Реконструктор":              "Rekonstruktor",
        "без сульфатов":              "sulfatsiz",
        "Профессиональная":           "Professional",
        "Профессиональный":           "Professional",
        "Кондиционер":                "Konditsioner",
        "Текстуризатор":              "Teksturizator",
        "Разглаживатель":             "Kamaytiruvchi",
        "Стабилизатор":               "Stabilizator",
        "Регенератор":                "Regenerator",
        "Реставратор":                "Restorer",
        "Выравниватель":              "Tenglashtiruvchi",
        "Окислитель":                 "Oksidant",
        "Шампунь":                    "Shampun",
        "Краска":                     "Doimiy bo'yoq",
        "Тонирование":                "Tonlash",
        "Маска":                      "Maska",
        "Масло":                      "Moy",
        "Бальзам":                    "Balzam",
        "Уход":                       "Parvarish",
        "Шаг":                        "Bosqich",
        "Саше":                       "Sashshe",
        "объёмов":                    "hajm",
        "рефил":                      "refil",
        "афро":                       "afro",
    },
}


def translate_product_name(name: str, lang: str) -> str:
    """Translate product name from Russian to target language using term substitution."""
    if lang == "ru" or lang not in _TERM_SUBS:
        return name
    result = name
    for ru, local in _TERM_SUBS[lang].items():
        result = result.replace(ru, local)
    return result
