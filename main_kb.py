from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
)
from config import WEBAPP_URL
from utils.i18n import t, translate_product_name

# ── Главное меню ────────────────────────────────────────────────
def main_menu_kb(lang: str = "ru") -> ReplyKeyboardMarkup:
    webapp_btn = (
        KeyboardButton(text=t("btn_shop", lang), web_app=WebAppInfo(url=WEBAPP_URL))
        if WEBAPP_URL else
        KeyboardButton(text=t("btn_shop", lang))
    )
    return ReplyKeyboardMarkup(
        keyboard=[
            [webapp_btn],
            [KeyboardButton(text=t("btn_catalog", lang)),    KeyboardButton(text=t("btn_cart", lang))],
            [KeyboardButton(text=t("btn_consultant", lang)), KeyboardButton(text=t("btn_faq", lang))],
            [KeyboardButton(text=t("btn_order", lang)),      KeyboardButton(text=t("btn_manager", lang))],
            [KeyboardButton(text=t("btn_profile", lang)),    KeyboardButton(text=t("btn_favorites", lang))],
            [KeyboardButton(text=t("btn_detective", lang))],
        ],
        resize_keyboard=True
    )

# ── Выбор языка ─────────────────────────────────────────────────
def lang_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇷🇺 Русский",   callback_data="setlang:ru"),
            InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="setlang:uz"),
            InlineKeyboardButton(text="🇧🇷 Português", callback_data="setlang:pt"),
        ]
    ])

# ── Квалификация: тип клиента ───────────────────────────────────
def client_type_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("type_salon",     lang), callback_data="type:salon")],
        [InlineKeyboardButton(text=t("type_master",    lang), callback_data="type:master")],
        [InlineKeyboardButton(text=t("type_school",    lang), callback_data="type:school")],
        [InlineKeyboardButton(text=t("type_wholesale", lang), callback_data="type:wholesale")],
    ])

# ── Линейки каталога ────────────────────────────────────────────
SECTION_ICONS = {
    "SPECIALE":       "✨",
    "THEION":         "⚗️",
    "COLORE":         "🎨",
    "CREAM BLOND":    "💛",
    "BAOBÁ REDUCE":   "🌿",
    "DNAVANZE":       "🧬",
    "BIODETOX":       "🍃",
    "MIO RICCI":      "🌀",
    "NATURALE":       "🌸",
    "GLAMOROUS LUXURY": "👑",
    "PREMIUM VIOLET": "💜",
    "EXTRA":          "⭐",
}

def sections_kb(sections: list, lang: str = "ru") -> InlineKeyboardMarkup:
    rows = []
    for s in sections:
        icon = SECTION_ICONS.get(s["id"], "•")
        rows.append([InlineKeyboardButton(
            text=f"{icon} {s['id']}  ({s['product_count']} {t('pos_short', lang)})",
            callback_data=f"section:{s['id']}"
        )])
    rows.append([InlineKeyboardButton(text=t("search_start", lang), callback_data="catalog:search")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

# ── Список товаров в линейке ────────────────────────────────────
def products_kb(products: list, section_id: str, page: int = 0, per_page: int = 8,
                lang: str = "ru") -> InlineKeyboardMarkup:
    start = page * per_page
    chunk = products[start:start + per_page]
    rows = []
    for p in chunk:
        price = f"{p['price_sum']:,}".replace(",", " ") if p.get('price_sum') else ""
        name_tr = translate_product_name(p['name'], lang)
        name = name_tr[:32] + "…" if len(name_tr) > 32 else name_tr
        label = f"{t('art_short', lang)}{p['number']} · {name}"
        if price:
            label += f" — {price} {t('currency_uz', lang)}"
        rows.append([InlineKeyboardButton(
            text=label,
            callback_data=f"product:{p['number']}"
        )])
    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton(text="◀️", callback_data=f"section_page:{section_id}:{page-1}"))
    total_pages = (len(products) - 1) // per_page + 1
    if total_pages > 1:
        nav.append(InlineKeyboardButton(text=f"{page+1}/{total_pages}", callback_data="noop"))
    if start + per_page < len(products):
        nav.append(InlineKeyboardButton(text="▶️", callback_data=f"section_page:{section_id}:{page+1}"))
    if nav:
        rows.append(nav)
    rows.append([InlineKeyboardButton(text=t("back_to_sections", lang), callback_data="catalog:sections")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

# ── Карточка товара ─────────────────────────────────────────────
def product_card_kb(product_num: int, section_id: str, is_fav: bool = False,
                    lang: str = "ru") -> InlineKeyboardMarkup:
    fav_btn = InlineKeyboardButton(
        text=("🗑 " + t("fav_remove_btn", lang)) if is_fav else t("fav_add_btn", lang),
        callback_data=f"fav:{'remove' if is_fav else 'add'}:{product_num}"
    )
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("add_to_cart", lang), callback_data=f"cart_add:{product_num}")],
        [fav_btn],
        [InlineKeyboardButton(text=t("btn_write_review", lang), callback_data=f"review:write:{section_id}")],
        [InlineKeyboardButton(text=t("back_to_section", lang), callback_data=f"section:{section_id}")],
        [InlineKeyboardButton(text=t("go_to_cart", lang), callback_data="cart:view")],
    ])

# ── Корзина — основная ───────────────────────────────────────────
def cart_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("cart_checkout", lang),  callback_data="order:start")],
        [InlineKeyboardButton(text=t("cart_show_items", lang), callback_data="cart:items")],
        [InlineKeyboardButton(text=t("cart_clear_btn", lang),  callback_data="cart:clear")],
        [InlineKeyboardButton(text=t("cart_to_catalog", lang), callback_data="catalog:sections")],
    ])

# ── Корзина — управление товарами (per-item) ─────────────────────
def cart_items_kb(items: list, lang: str = "ru") -> InlineKeyboardMarkup:
    """
    items: list of (product_num, name_short, qty)
    """
    rows = []
    for product_num, name_short, qty in items:
        rows.append([
            InlineKeyboardButton(text=f"📦 {name_short} × {qty}", callback_data="noop"),
        ])
        rows.append([
            InlineKeyboardButton(text="➖", callback_data=f"cart:dec:{product_num}"),
            InlineKeyboardButton(text=str(qty), callback_data="noop"),
            InlineKeyboardButton(text="➕", callback_data=f"cart:inc:{product_num}"),
            InlineKeyboardButton(text="✖️", callback_data=f"cart:del:{product_num}"),
        ])
    rows.append([InlineKeyboardButton(text="✅ " + t("cart_checkout", lang), callback_data="order:start")])
    rows.append([InlineKeyboardButton(text="⬅️ " + t("btn_back_main", lang).replace("⬅️ ", ""),
                                      callback_data="cart:view")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

# ── Доставка ────────────────────────────────────────────────────
def delivery_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("delivery_pickup",    lang), callback_data="delivery:pickup")],
        [InlineKeyboardButton(text=t("delivery_tashkent",  lang), callback_data="delivery:tashkent")],
        [InlineKeyboardButton(text=t("delivery_transport", lang), callback_data="delivery:transport")],
    ])

# ── FAQ ─────────────────────────────────────────────────────────
def faq_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("faq_btn_delivery", lang), callback_data="faq:delivery")],
        [InlineKeyboardButton(text=t("faq_btn_payment",  lang), callback_data="faq:payment")],
        [InlineKeyboardButton(text=t("faq_btn_cert",     lang), callback_data="faq:cert")],
        [InlineKeyboardButton(text=t("faq_btn_return",   lang), callback_data="faq:return")],
        [InlineKeyboardButton(text=t("faq_btn_min",      lang), callback_data="faq:min_order")],
        [InlineKeyboardButton(text=t("btn_back_main",    lang), callback_data="menu:main")],
    ])

# ── Избранное ───────────────────────────────────────────────────
def favorites_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("fav_to_catalog", lang), callback_data="catalog:sections")],
        [InlineKeyboardButton(text=t("btn_back_main",  lang), callback_data="menu:main")],
    ])

def fav_item_kb(product_num: int, section_id: str, lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("fav_remove_btn", lang), callback_data=f"fav:remove:{product_num}")],
        [InlineKeyboardButton(text=t("fav_in_cart",    lang), callback_data=f"cart_add:{product_num}")],
        [InlineKeyboardButton(text=t("fav_back",       lang), callback_data="fav:list")],
    ])
