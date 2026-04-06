/**
 * DONATTI — translations.js
 * Поддерживаемые языки: ru (русский), uz (ўзбекча), pt (português)
 */

window.LANG = localStorage.getItem('donatti_lang') || 'ru';

const TRANSLATIONS = {

  /* ── Главная ── */
  home_desc: {
    ru: 'Профессиональная косметика из Бразилии<br>Официальный дистрибьютор в Узбекистане',
    uz: 'Braziliyadan professional kosmetika<br>O\'zbekistondagi rasmiy distribyutor',
    pt: 'Cosméticos profissionais do Brasil<br>Distribuidor oficial no Uzbequistão'
  },
  stat_products: { ru: 'ТОВАРОВ',  uz: 'MAHSULOT', pt: 'PRODUTOS'  },
  stat_lines:    { ru: 'ЛИНЕЕК',   uz: 'LINIYA',   pt: 'LINHAS'    },
  stat_opt:      { ru: 'ОПТ',      uz: 'OPT',      pt: 'ATACADO'   },

  btn_catalog_title:    { ru: 'Каталог продукции',               uz: 'Mahsulotlar katalogi',            pt: 'Catálogo de produtos'            },
  btn_catalog_sub:      { ru: '165 позиций · 12 линеек',         uz: '165 ta mahsulot · 12 liniya',     pt: '165 posições · 12 linhas'        },
  btn_consultant_title: { ru: 'AI Консультант',                  uz: 'AI Maslahatchi',                  pt: 'Consultor AI'                    },
  btn_consultant_sub:   { ru: 'Подбор по типу волос и проблеме', uz: 'Soch turi va muammosi bo\'yicha', pt: 'Seleção por tipo e problema capilar' },
  btn_cart_title:       { ru: 'Моя корзина',                     uz: 'Mening savatim',                  pt: 'Meu carrinho'                    },
  cart_empty_text:      { ru: 'Корзина пуста',                   uz: 'Savat bo\'sh',                    pt: 'Carrinho vazio'                  },

  /* ── Навигация ── */
  nav_home:       { ru: 'Главная',     uz: 'Asosiy',   pt: 'Início'   },
  nav_catalog:    { ru: 'Каталог',     uz: 'Katalog',  pt: 'Catálogo' },
  nav_consultant: { ru: 'Консультант', uz: 'Maslahat', pt: 'Consultor'},
  nav_cart:       { ru: 'Корзина',     uz: 'Savat',    pt: 'Carrinho' },

  /* ── Каталог ── */
  catalog_title:      { ru: 'Каталог',                 uz: 'Katalog',                   pt: 'Catálogo'                  },
  catalog_sub:        { ru: '12 линеек · 165 позиций', uz: '12 liniya · 165 mahsulot',  pt: '12 linhas · 165 posições'  },
  search_placeholder: { ru: '🔍 Поиск товара...',      uz: '🔍 Mahsulot qidirish...',   pt: '🔍 Buscar produto...'      },
  back_to_sections:   { ru: '‹ Назад к линейкам',      uz: '‹ Liniyalarga qaytish',     pt: '‹ Voltar às linhas'        },
  back:               { ru: '‹ Назад',                 uz: '‹ Orqaga',                  pt: '‹ Voltar'                  },
  section_label:      { ru: 'ЛИНЕЙКА',                 uz: 'LINIYA',                    pt: 'LINHA'                     },
  article_prefix:     { ru: 'АРТ.',                    uz: 'ART.',                      pt: 'ART.'                      },
  sum_currency:       { ru: 'сум',                     uz: 'so\'m',                     pt: 'UZS'                       },
  certificate:        { ru: '✅ Сертификат EU CPNP · 100% оригинал', uz: '✅ EU CPNP sertifikati · 100% original', pt: '✅ Certificado EU CPNP · 100% original' },
  nothing_found:      { ru: 'Ничего не найдено',       uz: 'Hech narsa topilmadi',      pt: 'Nada encontrado'           },
  add_to_cart:        { ru: '+ В корзину',             uz: '+ Savatga',                 pt: '+ Carrinho'                },
  add_to_cart_detail: { ru: '🛒 Добавить в корзину',   uz: '🛒 Savatga qo\'shish',      pt: '🛒 Adicionar ao carrinho'  },

  /* ── Корзина ── */
  cart_title:        { ru: 'Корзина',                    uz: 'Savat',                        pt: 'Carrinho'                    },
  cart_empty_status: { ru: 'Пусто',                      uz: 'Bo\'sh',                       pt: 'Vazio'                       },
  cart_empty_h3:     { ru: 'Корзина пуста',              uz: 'Savat bo\'sh',                 pt: 'Carrinho vazio'              },
  cart_empty_p:      { ru: 'Добавьте товары из каталога',uz: 'Katalogdan mahsulot qo\'shing', pt: 'Adicione produtos do catálogo'},
  go_catalog_btn:    { ru: 'Перейти в каталог',          uz: 'Katalogga o\'tish',             pt: 'Ir ao catálogo'              },
  qty_label:         { ru: 'Товаров',                    uz: 'Mahsulotlar',                   pt: 'Produtos'                    },
  pcs:               { ru: 'шт.',                        uz: 'dona',                          pt: 'un.'                         },
  sum_label:         { ru: 'Сумма',                      uz: 'Summa',                         pt: 'Valor'                       },
  total_label:       { ru: 'Итого',                      uz: 'Jami',                          pt: 'Total'                       },
  checkout_btn:      { ru: '✅ Оформить заказ',           uz: '✅ Buyurtma berish',            pt: '✅ Fazer pedido'              },
  max_discount:      { ru: '🏆 Максимальная скидка активна!', uz: '🏆 Maksimal chegirma faol!', pt: '🏆 Desconto máximo ativo!'   },

  /* ── Скидочные тиры ── */
  tier_big:    { ru: 'Крупный опт', uz: 'Yirik ulgurji',  pt: 'Atacado grande'  },
  tier_med:    { ru: 'Средний опт', uz: 'O\'rta ulgurji',  pt: 'Atacado médio'   },
  tier_small:  { ru: 'Мелкий опт',  uz: 'Kichik ulgurji',  pt: 'Atacado pequeno' },
  tier_retail: { ru: 'Розница',     uz: 'Chakana',          pt: 'Varejo'          },

  /* ── Консультант — UI ── */
  consultant_title: { ru: 'AI Консультант',               uz: 'AI Maslahatchi',               pt: 'Consultor AI'                    },
  consultant_sub:   { ru: 'Эксперт по уходу за волосами', uz: 'Soch parvarishi mutaxassisi',   pt: 'Especialista em cuidados capilares'},
  chat_placeholder: { ru: 'Задайте вопрос о волосах...',  uz: 'Soch haqida savol bering...',   pt: 'Faça uma pergunta sobre cabelo...' },

  /* ── Быстрые темы — метки ── */
  qt_hairloss:   { ru: '💧 Выпадение',     uz: '💧 To\'kilish',    pt: '💧 Queda'           },
  qt_dandruff:   { ru: '❄️ Перхоть',       uz: '❄️ Kepak',          pt: '❄️ Caspa'           },
  qt_oily:       { ru: '💦 Жирные',        uz: '💦 Moyli',           pt: '💦 Oleoso'          },
  qt_dry:        { ru: '🌵 Сухие/ломкие',  uz: '🌵 Quruq/mo\'rt',   pt: '🌵 Seco/quebradiço' },
  qt_irritation: { ru: '🔴 Раздражение',   uz: '🔴 Qo\'zg\'alish',  pt: '🔴 Irritação'       },
  qt_curly:      { ru: '🌀 Кудрявые',      uz: '🌀 Jingalak',        pt: '🌀 Cacheado'        },
  qt_bleached:   { ru: '⚗️ После осветл.', uz: '⚗️ Oqartirilgan',   pt: '⚗️ Pós-descoloração'},
  qt_colored:    { ru: '🎨 Окрашенные',    uz: '🎨 Bo\'yalgan',      pt: '🎨 Tingido'         },

  /* ── Быстрые темы — запросы ── */
  qt_hairloss_q: {
    ru: 'волосы сильно выпадают, много волос на расчёске',
    uz: 'sochlarim juda to\'kilmoqda, taroqda ko\'p soch',
    pt: 'cabelo cai muito, muitos fios na escova'
  },
  qt_dandruff_q: {
    ru: 'перхоть и зуд, белые чешуйки',
    uz: 'kepak va qichima, oq tangachalar',
    pt: 'caspa e coceira, flocos brancos'
  },
  qt_oily_q: {
    ru: 'волосы быстро жирнеют, кажутся сальными',
    uz: 'sochlar tez moylanadi, yog\'li ko\'rinadi',
    pt: 'cabelo fica oleoso rapidamente, parece gorduroso'
  },
  qt_dry_q: {
    ru: 'волосы сухие, ломкие, сильно шелушится кожа головы',
    uz: 'sochlar quruq, mo\'rt, bosh terisi qattiq po\'chaydi',
    pt: 'cabelo seco, quebradiço, couro cabeludo descamando'
  },
  qt_irritation_q: {
    ru: 'раздражение и покраснение кожи головы, жжение',
    uz: 'bosh terisida qizarish va yonish his etiladi',
    pt: 'irritação e vermelhidão no couro cabeludo, ardência'
  },
  qt_curly_q: {
    ru: 'у меня кудрявые волосы, пушатся и нет чёткого завитка',
    uz: 'jingalak sochlarim bor, pufaklanadi va aniq burama yo\'q',
    pt: 'tenho cabelo cacheado, aranha e sem cacho definido'
  },
  qt_bleached_q: {
    ru: 'волосы повреждены после осветления, стали пористыми и тусклыми',
    uz: 'oqartirishdan keyin sochlar shikastlandi, g\'ovak va tutun bo\'ldi',
    pt: 'cabelo danificado após descoloração, ficou poroso e sem brilho'
  },
  qt_colored_q: {
    ru: 'окрашенные волосы, цвет быстро вымывается, желтизна',
    uz: 'bo\'yalgan sochlar, rang tez yuviladi, sariqlik bor',
    pt: 'cabelo tingido, a cor desboa rápido, amarelamento'
  },

  /* ── Консультант — сообщения движка ── */
  cons_greeting: {
    ru: '👋 Привет! Я *DONATTI AI* — трихологический консультант.\n\nОпишите вашу проблему своими словами — я задам пару уточняющих вопросов и подберу подходящий уход из линеек Donatti.\n\n_Или выберите тему выше_ 👆',
    uz: '👋 Salom! Men *DONATTI AI* — trixologik maslahatchi.\n\nMuammoingizni o\'z so\'zlaringiz bilan tasvirlab bering — men bir necha aniqlashtiruvchi savol beraman va Donatti liniyalaridan mos parvarishni tanlayman.\n\n_Yoki yuqoridagi mavzuni tanlang_ 👆',
    pt: '👋 Olá! Sou o *DONATTI AI* — consultor de tricologia.\n\nDescreva seu problema com suas próprias palavras — vou fazer algumas perguntas e indicar o cuidado adequado das linhas Donatti.\n\n_Ou escolha um tema acima_ 👆'
  },
  cons_unclear: {
    ru: '🤔 Расскажите подробнее, что именно вас беспокоит.\n\nНапример: *«волосы быстро жирнеют»*, *«сильное выпадение»*, *«зуд и перхоть»*, *«тусклые после осветления»*.',
    uz: '🤔 Nima bezovta qilayotganini batafsilroq aytib bering.\n\nMasalan: *«sochlar tez moylanadi»*, *«kuchli to\'kilish»*, *«qichima va kepak»*, *«oqartirishdan so\'ng tutun soch»*.',
    pt: '🤔 Conte mais detalhes sobre o que está te incomodando.\n\nPor exemplo: *«cabelo fica oleoso rápido»*, *«queda intensa»*, *«coceira e caspa»*, *«sem brilho após descoloração»*.'
  },
  cons_clarify_prefix: {
    ru: 'Чтобы подобрать уход точнее, уточню пару деталей:',
    uz: 'Parvarishni aniqroq tanlash uchun bir necha tafsilotni aniqlayman:',
    pt: 'Para indicar o cuidado mais preciso, vou esclarecer alguns detalhes:'
  },
  cons_diagnosis_label: {
    ru: '🔍 **Предположение:**',
    uz: '🔍 **Taxmin:**',
    pt: '🔍 **Hipótese:**'
  },
  cons_causes_label: {
    ru: '📋 **Возможные причины:**',
    uz: '📋 **Mumkin bo\'lgan sabablar:**',
    pt: '📋 **Possíveis causas:**'
  },
  cons_helps_label: {
    ru: '**Что может помочь:**',
    uz: '**Nima yordam berishi mumkin:**',
    pt: '**O que pode ajudar:**'
  },
  cons_primary_label:   { ru: 'основная рекомендация', uz: 'asosiy tavsiya',  pt: 'recomendação principal' },
  cons_secondary_label: { ru: 'дополнительно',         uz: 'qo\'shimcha',     pt: 'complementar'          },
  cons_catalog_invite: {
    ru: '_Хотите посмотреть эти продукты в каталоге? 👇_',
    uz: '_Bu mahsulotlarni katalogda ko\'rmoqchimisiz? 👇_',
    pt: '_Quer ver esses produtos no catálogo? 👇_'
  },

  /* ── Отзывы ── */
  reviews_title:  { ru: 'Отзывы',             uz: 'Sharhlar',          pt: 'Avaliações'          },
  reviews_write:  { ru: 'Оставить отзыв',      uz: 'Sharh yozish',      pt: 'Escrever avaliação'  },
  reviews_empty:  { ru: 'Отзывов пока нет',    uz: 'Hali sharh yo\'q',  pt: 'Sem avaliações ainda'},
  reviews_name:   { ru: 'Ваше имя',            uz: 'Ismingiz',          pt: 'Seu nome'            },
  reviews_ph:     { ru: 'Ваш отзыв...',        uz: 'Sharhingiz...',     pt: 'Sua avaliação...'    },
  reviews_send:   { ru: 'Отправить',           uz: 'Yuborish',          pt: 'Enviar'              },
  reviews_cancel: { ru: 'Отмена',              uz: 'Bekor',             pt: 'Cancelar'            },
  reviews_thanks: { ru: 'Спасибо за отзыв!',   uz: 'Sharh uchun rahmat!', pt: 'Obrigado pela avaliação!' },

  /* ── Misc ── */
  guest:          { ru: 'Гость',    uz: 'Mehmon',      pt: 'Convidado'  },
  positions_word: { ru: 'позиций', uz: 'ta mahsulot', pt: 'posições'   },
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
  // Кнопка показывает язык, НА который переключит
  const nextLang = { ru: 'UZ', uz: 'PT', pt: 'RU' };
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.textContent = nextLang[window.LANG] || 'UZ';
  });
}

/**
 * Переключает язык RU → UZ → PT → RU и перерисовывает интерфейс.
 */
function toggleLang() {
  const langs = ['ru', 'uz', 'pt'];
  window.LANG = langs[(langs.indexOf(window.LANG) + 1) % 3];
  localStorage.setItem('donatti_lang', window.LANG);
  applyLang();
  // Перерисовать динамические компоненты (функции объявлены в webapp.html)
  if (typeof renderSections    === 'function') renderSections();
  if (typeof renderCart        === 'function') renderCart();
  if (typeof updateHomeCart    === 'function') updateHomeCart();
  if (typeof renderQuickTopics === 'function') renderQuickTopics();
}
