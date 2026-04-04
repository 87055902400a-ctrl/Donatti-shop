/**
 * DONATTI — translations.js
 * Поддерживаемые языки: ru (русский), uz (ўзбекча)
 */

window.LANG = localStorage.getItem('donatti_lang') || 'ru';

const TRANSLATIONS = {

  /* ── Главная ── */
  home_desc: {
    ru: 'Профессиональная косметика из Бразилии<br>Официальный дистрибьютор в Узбекистане',
    uz: 'Braziliyadan professional kosmetika<br>O\'zbekistondagi rasmiy distribyutor'
  },
  stat_products: { ru: 'ТОВАРОВ',  uz: 'MAHSULOT' },
  stat_lines:    { ru: 'ЛИНЕЕК',   uz: 'LINIYA'   },
  stat_opt:      { ru: 'ОПТ',      uz: 'OPT'      },

  btn_catalog_title:    { ru: 'Каталог продукции',               uz: 'Mahsulotlar katalogi'             },
  btn_catalog_sub:      { ru: '165 позиций · 12 линеек',         uz: '165 ta mahsulot · 12 liniya'      },
  btn_consultant_title: { ru: 'AI Консультант',                  uz: 'AI Maslahatchi'                   },
  btn_consultant_sub:   { ru: 'Подбор по типу волос и проблеме', uz: 'Soch turi va muammosi bo\'yicha'  },
  btn_cart_title:       { ru: 'Моя корзина',                     uz: 'Mening savatim'                   },
  cart_empty_text:      { ru: 'Корзина пуста',                   uz: 'Savat bo\'sh'                     },

  /* ── Навигация ── */
  nav_home:       { ru: 'Главная',     uz: 'Asosiy'   },
  nav_catalog:    { ru: 'Каталог',     uz: 'Katalog'  },
  nav_consultant: { ru: 'Консультант', uz: 'Maslahat' },
  nav_cart:       { ru: 'Корзина',     uz: 'Savat'    },

  /* ── Каталог ── */
  catalog_title:      { ru: 'Каталог',                 uz: 'Katalog'                  },
  catalog_sub:        { ru: '12 линеек · 165 позиций', uz: '12 liniya · 165 mahsulot' },
  search_placeholder: { ru: '🔍 Поиск товара...',      uz: '🔍 Mahsulot qidirish...'  },
  back_to_sections:   { ru: '‹ Назад к линейкам',      uz: '‹ Liniyalarga qaytish'    },
  back:               { ru: '‹ Назад',                 uz: '‹ Orqaga'                 },
  section_label:      { ru: 'ЛИНЕЙКА',                 uz: 'LINIYA'                   },
  article_prefix:     { ru: 'АРТ.',                    uz: 'ART.'                     },
  sum_currency:       { ru: 'сум',                     uz: 'so\'m'                    },
  certificate:        { ru: '✅ Сертификат EU CPNP · 100% оригинал', uz: '✅ EU CPNP sertifikati · 100% original' },
  nothing_found:      { ru: 'Ничего не найдено',       uz: 'Hech narsa topilmadi'     },
  add_to_cart:        { ru: '+ В корзину',             uz: '+ Savatga'                },
  add_to_cart_detail: { ru: '🛒 Добавить в корзину',   uz: '🛒 Savatga qo\'shish'     },

  /* ── Корзина ── */
  cart_title:        { ru: 'Корзина',                    uz: 'Savat'                       },
  cart_empty_status: { ru: 'Пусто',                      uz: 'Bo\'sh'                      },
  cart_empty_h3:     { ru: 'Корзина пуста',              uz: 'Savat bo\'sh'                },
  cart_empty_p:      { ru: 'Добавьте товары из каталога',uz: 'Katalogdan mahsulot qo\'shing'},
  go_catalog_btn:    { ru: 'Перейти в каталог',          uz: 'Katalogga o\'tish'           },
  qty_label:         { ru: 'Товаров',                    uz: 'Mahsulotlar'                 },
  pcs:               { ru: 'шт.',                        uz: 'dona'                        },
  sum_label:         { ru: 'Сумма',                      uz: 'Summa'                       },
  total_label:       { ru: 'Итого',                      uz: 'Jami'                        },
  checkout_btn:      { ru: '✅ Оформить заказ',           uz: '✅ Buyurtma berish'          },
  max_discount:      { ru: '🏆 Максимальная скидка активна!', uz: '🏆 Maksimal chegirma faol!' },

  /* ── Скидочные тиры ── */
  tier_big:    { ru: 'Крупный опт', uz: 'Yirik ulgurji'  },
  tier_med:    { ru: 'Средний опт', uz: 'O\'rta ulgurji'  },
  tier_small:  { ru: 'Мелкий опт',  uz: 'Kichik ulgurji'  },
  tier_retail: { ru: 'Розница',     uz: 'Chakana'         },

  /* ── Консультант — UI ── */
  consultant_title: { ru: 'AI Консультант',               uz: 'AI Maslahatchi'              },
  consultant_sub:   { ru: 'Эксперт по уходу за волосами', uz: 'Soch parvarishi mutaxassisi' },
  chat_placeholder: { ru: 'Задайте вопрос о волосах...',  uz: 'Soch haqida savol bering...' },

  /* ── Быстрые темы — метки ── */
  qt_hairloss:   { ru: '💧 Выпадение',     uz: '💧 To\'kilish'    },
  qt_dandruff:   { ru: '❄️ Перхоть',       uz: '❄️ Kepak'         },
  qt_oily:       { ru: '💦 Жирные',        uz: '💦 Moyli'          },
  qt_dry:        { ru: '🌵 Сухие/ломкие',  uz: '🌵 Quruq/mo\'rt'  },
  qt_irritation: { ru: '🔴 Раздражение',   uz: '🔴 Qo\'zg\'alish' },
  qt_curly:      { ru: '🌀 Кудрявые',      uz: '🌀 Jingalak'      },
  qt_bleached:   { ru: '⚗️ После осветл.', uz: '⚗️ Oqartirilgan'  },
  qt_colored:    { ru: '🎨 Окрашенные',    uz: '🎨 Bo\'yalgan'    },

  /* ── Быстрые темы — запросы ── */
  qt_hairloss_q: {
    ru: 'волосы сильно выпадают, много волос на расчёске',
    uz: 'sochlarim juda to\'kilmoqda, taroqda ko\'p soch'
  },
  qt_dandruff_q: {
    ru: 'перхоть и зуд, белые чешуйки',
    uz: 'kepak va qichima, oq tangachalar'
  },
  qt_oily_q: {
    ru: 'волосы быстро жирнеют, кажутся сальными',
    uz: 'sochlar tez moylanadi, yog\'li ko\'rinadi'
  },
  qt_dry_q: {
    ru: 'волосы сухие, ломкие, сильно шелушится кожа головы',
    uz: 'sochlar quruq, mo\'rt, bosh terisi qattiq po\'chaydi'
  },
  qt_irritation_q: {
    ru: 'раздражение и покраснение кожи головы, жжение',
    uz: 'bosh terisida qizarish va yonish his etiladi'
  },
  qt_curly_q: {
    ru: 'у меня кудрявые волосы, пушатся и нет чёткого завитка',
    uz: 'jingalak sochlarim bor, pufaklanadi va aniq burama yo\'q'
  },
  qt_bleached_q: {
    ru: 'волосы повреждены после осветления, стали пористыми и тусклыми',
    uz: 'oqartirishdan keyin sochlar shikastlandi, g\'ovak va tutun bo\'ldi'
  },
  qt_colored_q: {
    ru: 'окрашенные волосы, цвет быстро вымывается, желтизна',
    uz: 'bo\'yalgan sochlar, rang tez yuviladi, sariqlik bor'
  },

  /* ── Консультант — сообщения движка ── */
  cons_greeting: {
    ru: '👋 Привет! Я *DONATTI AI* — трихологический консультант.\n\nОпишите вашу проблему своими словами — я задам пару уточняющих вопросов и подберу подходящий уход из линеек Donatti.\n\n_Или выберите тему выше_ 👆',
    uz: '👋 Salom! Men *DONATTI AI* — trixologik maslahatchi.\n\nMuammoingizni o\'z so\'zlaringiz bilan tasvirlab bering — men bir necha aniqlashtiruvchi savol beraman va Donatti liniyalaridan mos parvarishni tanlayman.\n\n_Yoki yuqoridagi mavzuni tanlang_ 👆'
  },
  cons_unclear: {
    ru: '🤔 Расскажите подробнее, что именно вас беспокоит.\n\nНапример: *«волосы быстро жирнеют»*, *«сильное выпадение»*, *«зуд и перхоть»*, *«тусклые после осветления»*.',
    uz: '🤔 Nima bezovta qilayotganini batafsilroq aytib bering.\n\nMasalan: *«sochlar tez moylanadi»*, *«kuchli to\'kilish»*, *«qichima va kepak»*, *«oqartirishdan so\'ng tutun soch»*.'
  },
  cons_clarify_prefix: {
    ru: 'Чтобы подобрать уход точнее, уточню пару деталей:',
    uz: 'Parvarishni aniqroq tanlash uchun bir necha tafsilotni aniqlayman:'
  },
  cons_diagnosis_label: {
    ru: '🔍 **Предположение:**',
    uz: '🔍 **Taxmin:**'
  },
  cons_causes_label: {
    ru: '📋 **Возможные причины:**',
    uz: '📋 **Mumkin bo\'lgan sabablar:**'
  },
  cons_helps_label: {
    ru: '**Что может помочь:**',
    uz: '**Nima yordam berishi mumkin:**'
  },
  cons_primary_label:   { ru: 'основная рекомендация', uz: 'asosiy tavsiya'   },
  cons_secondary_label: { ru: 'дополнительно',         uz: 'qo\'shimcha'      },
  cons_catalog_invite: {
    ru: '_Хотите посмотреть эти продукты в каталоге? 👇_',
    uz: '_Bu mahsulotlarni katalogda ko\'rmoqchimisiz? 👇_'
  },
};

/**
 * Возвращает строку на текущем языке.
 * @param {string} key
 * @returns {string}
 */
function t(key) {
  const entry = TRANSLATIONS[key];
  if (!entry) return key;
  return entry[window.LANG] ?? entry.ru ?? key;
}

/**
 * Применяет переводы к DOM:
 *   data-i18n="key"     → textContent
 *   data-i18n-html="key"→ innerHTML (для строк с тегами)
 *   data-i18n-ph="key"  → placeholder
 */
function applyLang() {
  document.querySelectorAll('[data-i18n]').forEach(el => {
    el.textContent = t(el.getAttribute('data-i18n'));
  });
  document.querySelectorAll('[data-i18n-html]').forEach(el => {
    el.innerHTML = t(el.getAttribute('data-i18n-html'));
  });
  document.querySelectorAll('[data-i18n-ph]').forEach(el => {
    el.placeholder = t(el.getAttribute('data-i18n-ph'));
  });
  // Обновить лейбл кнопки: показывает язык, НА который переключит
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.textContent = window.LANG === 'ru' ? 'UZ' : 'RU';
  });
}

/**
 * Переключает язык и перерисовывает интерфейс.
 */
function toggleLang() {
  window.LANG = window.LANG === 'ru' ? 'uz' : 'ru';
  localStorage.setItem('donatti_lang', window.LANG);
  applyLang();
  // Перерисовать динамические компоненты (функции объявлены в webapp.html)
  if (typeof renderSections   === 'function') renderSections();
  if (typeof renderCart       === 'function') renderCart();
  if (typeof updateHomeCart   === 'function') updateHomeCart();
  if (typeof renderQuickTopics=== 'function') renderQuickTopics();
}
