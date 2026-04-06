/**
 * DONATTI AI — База знаний трихологического консультанта
 * Структура: проблема кожи головы → симптомы → уточняющие вопросы → рекомендации
 */

const SCALP_CONDITIONS = {

  fatty_seborrhea: {
    name: 'Жирная себорея кожи головы',
    emoji: '💦',
    symptoms: [
      'жирн', 'сальн', 'маслян', 'блест', 'быстро грязн', 'жирная кожа',
      'жирная голова', 'часто мою', 'каждый день мою', 'к вечеру жирн',
      'лоснит', 'sebore', 'себорея', 'жирная себорея'
    ],
    clarifyingQuestions: [
      'Как быстро волосы становятся жирными после мытья головы — в тот же день, на следующий или через 2–3 дня?',
      'Есть ли при этом зуд или ощущение «забитости» кожи головы?',
      'Бывает ли перхоть или мелкие жёлтоватые чешуйки?'
    ],
    clarifyingQuestions_uz: [
      'Bosh yuvganingizdan keyin sochlar qanchalik tezda moylanadi — o\'sha kuni, ertasiga yoki 2–3 kundan keyin?',
      'Bunda qichima yoki bosh terisida «bitib qolgandek» his bormi?',
      'Kepak yoki mayda sargishtob tangachalar bo\'ladimi?'
    ],
    clarifyingQuestions_pt: [
      'Com que rapidez o cabelo fica oleoso após a lavagem — no mesmo dia, no dia seguinte ou em 2–3 dias?',
      'Há coceira ou sensação de "poros entupidos" no couro cabeludo?',
      'Aparece caspa ou pequenas escamas amareladas?'
    ],
    empathy: 'Понимаю, это довольно неприятно — когда волосы теряют свежесть уже к середине дня.',
    empathy_uz: 'Tushunaman, bu juda noqulay — sochlar kunning o\'rtasiga bormasdan yangiligini yo\'qotganda.',
    empathy_pt: 'Entendo, é bem desconfortável quando o cabelo perde a frescura já no meio do dia.',
    problemDescription: 'по описанию это может быть связано с гиперактивностью сальных желёз кожи головы. Иногда это называют жирной себореей.',
    problemDescription_uz: 'tavsifga ko\'ra, bu bosh terisining yog\' bezlari giperfaholligi bilan bog\'liq bo\'lishi mumkin. Bu ba\'zan yog\'li seboreya deb ataladi.',
    problemDescription_pt: 'pela descrição, pode estar relacionado à hiperatividade das glândulas sebáceas do couro cabeludo. Às vezes isso é chamado de dermatite seborreica oleosa.',
    causes: 'Подобное состояние может возникать из-за гормональных колебаний, стресса, неправильно подобранного ухода (особенно если шампунь слишком агрессивный — кожа «защищается» усиленной выработкой себума) или питания.',
    causes_uz: 'Bunday holat gormonalv tebranishlar, stress, noto\'g\'ri tanlangan parvarish (ayniqsa shampun juda agressiv bo\'lsa — teri ko\'proq sebum ishlab chiqarish orqali himoyalanadi) yoki ovqatlanish tufayli yuzaga kelishi mumkin.',
    causes_pt: 'Esse estado pode surgir devido a flutuações hormonais, estresse, cuidado inadequado (especialmente se o shampoo for muito agressivo — a pele se "defende" produzindo mais sebo) ou alimentação.',
    disclaimer: '⚠️ Я не медицинский специалист. Если симптомы сильные или длительные — рекомендую обратиться к дерматологу или трихологу.',
    disclaimer_uz: '⚠️ Men tibbiy mutaxassis emasman. Agar belgilar kuchli yoki uzoq davom etsa — dermatolog yoki trixologa murojaat qilishni tavsiya etaman.',
    disclaimer_pt: '⚠️ Não sou especialista médico. Se os sintomas forem intensos ou prolongados, recomendo consultar um dermatologista ou tricologista.',
    products: [
      {
        section: 'BIODETOX',
        role: 'primary',
        reason: 'Активированный уголь способствует глубокому очищению пор и может помочь нормализовать работу сальных желёз. Подходит для регулярного использования 1–2 раза в неделю.',
        reason_uz: 'Faollashtirilgan ko\'mir g\'ovaklarni chuqur tozalashga yordam beradi va yog\' bezlari ishini normallashtirishga ko\'maklashadi. Haftada 1–2 marta muntazam foydalanish mumkin.',
        reason_pt: 'O carvão ativado promove uma limpeza profunda dos poros e pode ajudar a normalizar a atividade das glândulas sebáceas. Indicado para uso regular 1–2 vezes por semana.'
      },
      {
        section: 'SPECIALE',
        role: 'secondary',
        reason: 'Помогает восстановить pH-баланс кожи головы после очищения, что может способствовать снижению жирности со временем.',
        reason_uz: 'Tozalashdan keyin bosh terisi pH-balansini tiklashga yordam beradi, bu esa vaqt o\'tishi bilan moyliqni kamaytirishga ko\'maklashadi.',
        reason_pt: 'Ajuda a restaurar o equilíbrio de pH do couro cabeludo após a limpeza, o que pode contribuir para reduzir a oleosidade com o tempo.'
      }
    ]
  },

  dry_scalp: {
    name: 'Сухость и обезвоженность кожи головы',
    emoji: '🌵',
    symptoms: [
      'сух', 'стянутост', 'шелушен', 'зуд', 'перхот', 'чешуйк', 'чешет',
      'белые хлопья', 'мелкая перхот', 'сухая кожа', 'обезвожен',
      'трещин', 'раздражен', 'красн', 'чувствительн'
    ],
    clarifyingQuestions: [
      'Чешуйки белые и сухие, или желтоватые и жирноватые на ощупь?',
      'Ощущается ли стянутость или жжение кожи головы, особенно после мытья?',
      'Были ли в последнее время частые окрашивания или химические процедуры?'
    ],
    clarifyingQuestions_uz: [
      'Tangachalar oq va quruqmi yoki sargishtob va yog\'simonmi?',
      'Yuvganingizdan keyin bosh terisida tortishish yoki yonish seziladi?',
      'So\'nggi paytlarda tez-tez bo\'yash yoki kimyoviy jarayonlar bo\'ldimi?'
    ],
    clarifyingQuestions_pt: [
      'As escamas são brancas e secas, ou amareladas e gordurosas ao toque?',
      'Há sensação de tensão ou ardência no couro cabeludo, especialmente após a lavagem?',
      'Houve colorações ou procedimentos químicos frequentes recentemente?'
    ],
    empathy: 'Сухость и зуд кожи головы — это действительно некомфортно, особенно когда это происходит постоянно.',
    empathy_uz: 'Bosh terisining quruligi va qichimasi doim bo\'laversa, bu haqiqatan ham noqulay.',
    empathy_pt: 'Couro cabeludo seco e com coceira é realmente desconfortável, especialmente quando acontece com frequência.',
    problemDescription: 'по описанию это может быть связано с сухостью кожи головы или нарушением её защитного барьера.',
    problemDescription_uz: 'tavsifga ko\'ra, bu bosh terisining quruligi yoki himoya to\'sig\'ining buzilishi bilan bog\'liq bo\'lishi mumkin.',
    problemDescription_pt: 'pela descrição, pode estar relacionado à secura do couro cabeludo ou ao comprometimento de sua barreira protetora.',
    causes: 'Причиной может быть агрессивный шампунь, жёсткая вода, частое мытьё горячей водой, последствия окрашивания или просто недостаточное увлажнение.',
    causes_uz: 'Sababi agressiv shampun, qattiq suv, issiq suv bilan tez-tez yuvish, bo\'yash oqibatlari yoki yetarli namlanmaganlik bo\'lishi mumkin.',
    causes_pt: 'A causa pode ser shampoo agressivo, água dura, lavagem frequente com água quente, consequências de coloração ou simplesmente hidratação insuficiente.',
    disclaimer: '⚠️ Я не медицинский специалист. При выраженном зуде, покраснении или воспалении рекомендую проконсультироваться с дерматологом.',
    disclaimer_uz: '⚠️ Men tibbiy mutaxassis emasman. Kuchli qichima, qizarish yoki yallig\'lanishda dermatologga murojaat qilishni tavsiya etaman.',
    disclaimer_pt: '⚠️ Não sou especialista médico. Em caso de coceira intensa, vermelhidão ou inflamação, recomendo consultar um dermatologista.',
    products: [
      {
        section: 'SPECIALE',
        role: 'primary',
        reason: 'Линейка Nutri может помочь восстановить питание и увлажнение кожи головы, способствуя снижению чувства стянутости и шелушения.',
        reason_uz: 'Nutri liniyasi bosh terisini oziqlantirish va namlashni tiklashga yordam beradi, tortishish va po\'chayish hissini kamaytiradi.',
        reason_pt: 'A linha Nutri pode ajudar a restaurar a nutrição e hidratação do couro cabeludo, reduzindo a sensação de tensão e descamação.'
      },
      {
        section: 'BIODETOX',
        role: 'secondary',
        reason: 'Мягко очищает кожу головы, сохраняя её естественный баланс, что может помочь при сухой перхоти.',
        reason_uz: 'Bosh terisini tabiiy balansini saqlagan holda yumshoq tozalaydi, quruq kepakka yordam berishi mumkin.',
        reason_pt: 'Limpa suavemente o couro cabeludo preservando seu equilíbrio natural, o que pode ajudar na caspa seca.'
      }
    ]
  },

  hair_loss: {
    name: 'Выпадение волос',
    emoji: '💧',
    symptoms: [
      'выпадени', 'выпадают', 'выпадает', 'лысе', 'облысен', 'редеют',
      'потер волос', 'алопец', 'залысин', 'поредел', 'меньше волос',
      'на расчёске', 'в душе', 'на подушке', 'много выпадает'
    ],
    clarifyingQuestions: [
      'Выпадение началось недавно (до 3 месяцев) или это длится уже давно?',
      'Есть ли ощущение, что волосы стали тоньше у основания?',
      'Были ли в последние месяцы сильный стресс, смена питания или болезнь?'
    ],
    clarifyingQuestions_uz: [
      'To\'kilish yaqinda boshlandi (3 oydan kam) yoki bu allaqachon uzoq davom etmoqda?',
      'Sochlar tubida ingichkalashayotgandek his bormi?',
      'So\'nggi oylar ichida kuchli stress, ovqatlanish o\'zgarishi yoki kasallik bo\'ldimi?'
    ],
    clarifyingQuestions_pt: [
      'A queda começou recentemente (menos de 3 meses) ou já dura há mais tempo?',
      'Há a sensação de que os fios ficaram mais finos na raiz?',
      'Houve estresse intenso, mudança alimentar ou doença nos últimos meses?'
    ],
    empathy: 'Выпадение волос — это стрессовая ситуация, и вполне понятно ваше беспокойство.',
    empathy_uz: 'Soch to\'kilishi stressli vaziyat va sizning tashvishingiz tushuniladi.',
    empathy_pt: 'A queda de cabelo é uma situação estressante e é completamente compreensível a sua preocupação.',
    problemDescription: 'по описанию это может быть связано с диффузным выпадением волос, которое бывает реакцией организма на внутренние или внешние факторы.',
    problemDescription_uz: 'tavsifga ko\'ra, bu diffuz soch to\'kilishi bo\'lishi mumkin — u ichki yoki tashqi omillarga organizmning reaktsiyasi sifatida yuzaga keladi.',
    problemDescription_pt: 'pela descrição, pode estar relacionado à queda difusa de cabelo, que costuma ser uma reação do organismo a fatores internos ou externos.',
    causes: 'Среди возможных причин — стресс, дефицит железа или витаминов, гормональные изменения (в том числе после родов), а также неправильный уход, перегружающий кожу головы.',
    causes_uz: 'Mumkin bo\'lgan sabablar: stress, temir yoki vitaminlar yetishmovchiligi, gormonalv o\'zgarishlar (jumladan tug\'ruqdan keyin), noto\'g\'ri parvarish.',
    causes_pt: 'Entre as possíveis causas estão estresse, deficiência de ferro ou vitaminas, alterações hormonais (inclusive pós-parto), além de cuidados inadequados que sobrecarregam o couro cabeludo.',
    disclaimer: '⚠️ Я не медицинский специалист. При интенсивном или длительном выпадении настоятельно рекомендую обратиться к трихологу для диагностики.',
    disclaimer_uz: '⚠️ Men tibbiy mutaxassis emasman. Kuchli yoki uzoq davom etadigan to\'kilishda tashxis uchun trixologa murojaat qilishni tavsiya etaman.',
    disclaimer_pt: '⚠️ Não sou especialista médico. Em caso de queda intensa ou prolongada, recomendo fortemente consultar um tricologista para diagnóstico.',
    products: [
      {
        section: 'SPECIALE',
        role: 'primary',
        reason: 'Профессиональная система Nutri способствует укреплению волос у основания и питанию кожи головы, что может поддержать волосяные фолликулы.',
        reason_uz: 'Nutri professional tizimi sochlarni tubida mustahkamlashga va bosh terisini oziqlantirishga yordam beradi, bu soch follikulalarini qo\'llab-quvvatlashi mumkin.',
        reason_pt: 'O sistema profissional Nutri contribui para fortalecer os fios na raiz e nutrir o couro cabeludo, o que pode apoiar os folículos capilares.'
      },
      {
        section: 'BIODETOX',
        role: 'secondary',
        reason: 'Детокс кожи головы помогает очистить поры и улучшить микроциркуляцию, создавая лучшие условия для роста волос.',
        reason_uz: 'Bosh terisi detoksi g\'ovaklarni tozalash va mikrosirkulyatsiyani yaxshilashga yordam beradi, soch o\'sishi uchun yaxshi sharoit yaratadi.',
        reason_pt: 'O detox do couro cabeludo ajuda a limpar os poros e melhorar a microcirculação, criando melhores condições para o crescimento capilar.'
      }
    ]
  },

  damaged_hair: {
    name: 'Повреждённые и ослабленные волосы',
    emoji: '⚗️',
    symptoms: [
      'повреждён', 'ломк', 'хрупк', 'пористые', 'после химии', 'после осветлени',
      'после окрашивани', 'слабые', 'тусклые', 'тускл', 'без блеска',
      'шершавые', 'обесцвеченные', 'секущ', 'кончики', 'сеченые'
    ],
    clarifyingQuestions: [
      'Вы делали недавно осветление, окрашивание или химическую завивку?',
      'Волосы ломаются у корней или секутся по длине?',
      'Как часто вы используете термоприборы (фен, плойка, утюжок)?'
    ],
    clarifyingQuestions_uz: [
      'Yaqinda oqartirish, bo\'yash yoki kimyoviy to\'lqinlash qildingizmi?',
      'Sochlar tubida sindiradi yoki uzunligi bo\'ylab uchlanada?',
      'Termoapparatlarni (fen, o\'rama, dazmol) qanchalik tez-tez ishlatasiz?'
    ],
    clarifyingQuestions_pt: [
      'Você fez descoloração, coloração ou permanente recentemente?',
      'Os fios quebram na raiz ou as pontas se abrem pelo comprimento?',
      'Com que frequência você usa ferramentas de calor (secador, chapinha, babyliss)?'
    ],
    empathy: 'Повреждённые волосы — это частая проблема при активном окрашивании или тепловых укладках, и это вполне можно исправить.',
    empathy_uz: 'Shikastlangan sochlar aktiv bo\'yash yoki issiqlik bilan ishlashda ko\'p uchraydigan muammo va buni tuzatish mumkin.',
    empathy_pt: 'Cabelo danificado é um problema comum com colorações frequentes ou uso de calor, e é totalmente possível de recuperar.',
    problemDescription: 'по описанию это может быть связано с нарушением структуры волоса — когда внутренние связи в волосе ослаблены или разрушены.',
    problemDescription_uz: 'tavsifga ko\'ra, bu soch tuzilishidagi buzilish bo\'lishi mumkin — ichki aloqalar zaif yoki buzilgan.',
    problemDescription_pt: 'pela descrição, pode estar relacionado ao comprometimento da estrutura capilar — quando as ligações internas do fio estão enfraquecidas ou quebradas.',
    causes: 'Основные причины: осветление, частое окрашивание, тепловое воздействие без защиты, агрессивные шампуни или механические повреждения.',
    causes_uz: 'Asosiy sabablar: oqartirish, tez-tez bo\'yash, himoyasiz issiqlik ta\'siri, agressiv shampunlar yoki mexanik shikastlanishlar.',
    causes_pt: 'Principais causas: descoloração, coloração frequente, calor sem proteção térmica, shampoos agressivos ou danos mecânicos.',
    disclaimer: '⚠️ Я не медицинский специалист. Для оценки состояния волос на профессиональном уровне рекомендую обратиться к трихологу.',
    disclaimer_uz: '⚠️ Men tibbiy mutaxassis emasman. Sochlar holatini professional darajada baholash uchun trixologga murojaat qilishni tavsiya etaman.',
    disclaimer_pt: '⚠️ Não sou especialista médico. Para avaliação profissional do estado do cabelo, recomendo consultar um tricologista.',
    products: [
      {
        section: 'DNAVANZE',
        role: 'primary',
        reason: 'Технология Mimetecnol может способствовать восстановлению внутренних связей волоса, улучшая его эластичность и прочность — используется как аналог Olaplex.',
        reason_uz: 'Mimetecnol texnologiyasi sochning ichki aloqalarini tiklashga yordam beradi, elastiklik va mustahkamlikni oshiradi — Olaplex analogi sifatida ishlatiladi.',
        reason_pt: 'A tecnologia Mimetecnol pode contribuir para a reconstrução das ligações internas do fio, melhorando elasticidade e resistência — usado como alternativa ao Olaplex.'
      },
      {
        section: 'SPECIALE',
        role: 'secondary',
        reason: 'Маска и несмываемый уход Nutri помогают восполнить питание и снизить пористость волоса после химических процедур.',
        reason_uz: 'Nutri niqobi va yuvilmaydigan parvarishi kimyoviy jarayonlardan keyin sochni oziqlantirish va g\'ovaklikni kamaytirishi mumkin.',
        reason_pt: 'A máscara e o leave-in Nutri ajudam a repor a nutrição e reduzir a porosidade do fio após procedimentos químicos.'
      }
    ]
  },

  scalp_irritation: {
    name: 'Раздражение и чувствительность кожи головы',
    emoji: '🔴',
    symptoms: [
      'раздражен', 'покрасн', 'воспален', 'болит кожа', 'жжен',
      'чувствительн', 'реагирует', 'аллерги', 'высыпани', 'корочк',
      'зуд сильный', 'нестерпимый зуд', 'жжение'
    ],
    clarifyingQuestions: [
      'Раздражение появилось после смены шампуня или другого продукта?',
      'Есть ли заметное покраснение или видимое воспаление на коже головы?',
      'Зуд постоянный или появляется после определённых ситуаций (стресс, пот, жара)?'
    ],
    clarifyingQuestions_uz: [
      'Qo\'zg\'alish shampun yoki boshqa mahsulotni almashtirgandan keyin paydo bo\'ldimi?',
      'Bosh terisida ko\'rinadigan qizarish yoki yallig\'lanish bormi?',
      'Qichima doimiy yoki ma\'lum holatlarda (stress, ter, issiq) paydo bo\'ladimi?'
    ],
    clarifyingQuestions_pt: [
      'A irritação surgiu após trocar de shampoo ou outro produto?',
      'Há vermelhidão visível ou inflamação no couro cabeludo?',
      'A coceira é constante ou aparece após certas situações (estresse, suor, calor)?'
    ],
    empathy: 'Раздражённая кожа головы — это довольно неприятные ощущения, которые мешают в повседневной жизни.',
    empathy_uz: 'Qo\'zg\'algan bosh terisi kundalik hayotga xalaqit beruvchi juda noqulay sezgi.',
    empathy_pt: 'O couro cabeludo irritado causa sensações bem desagradáveis que atrapalham o dia a dia.',
    problemDescription: 'по описанию это может быть связано с повышенной чувствительностью или реактивностью кожи головы.',
    problemDescription_uz: 'tavsifga ko\'ra, bu bosh terisining oshirilgan sezgirligi yoki reaktivligi bilan bog\'liq bo\'lishi mumkin.',
    problemDescription_pt: 'pela descrição, pode estar relacionado à hipersensibilidade ou reatividade aumentada do couro cabeludo.',
    causes: 'Возможные причины: агрессивные ингредиенты в косметике, аллергическая реакция, контактный дерматит, нарушение микробиома кожи или стресс.',
    causes_uz: 'Mumkin bo\'lgan sabablar: kosmetikedagi agressiv ingredientlar, allergik reaktsiya, kontakt dermatit, teri mikrobbiomining buzilishi yoki stress.',
    causes_pt: 'Possíveis causas: ingredientes agressivos na cosmética, reação alérgica, dermatite de contato, desequilíbrio do microbioma cutâneo ou estresse.',
    disclaimer: '⚠️ Я не медицинский специалист. При выраженном воспалении, покраснении или кожных высыпаниях необходимо обратиться к дерматологу.',
    disclaimer_uz: '⚠️ Men tibbiy mutaxassis emasman. Belgilangan yallig\'lanish, qizarish yoki teri toshmalarida dermatologga murojaat qilish zarur.',
    disclaimer_pt: '⚠️ Não sou especialista médico. Em caso de inflamação acentuada, vermelhidão ou erupções cutâneas, é necessário consultar um dermatologista.',
    products: [
      {
        section: 'NATURALE',
        role: 'primary',
        reason: 'Мягкая формула без агрессивных компонентов может подойти для чувствительной кожи головы, способствуя снижению раздражения.',
        reason_uz: 'Agressiv tarkibsiz yumshoq formula sezgir bosh terisi uchun mos bo\'lishi va qo\'zg\'alishni kamaytirishi mumkin.',
        reason_pt: 'A fórmula suave sem componentes agressivos pode ser adequada para couro cabeludo sensível, contribuindo para reduzir a irritação.'
      },
      {
        section: 'BIODETOX',
        role: 'secondary',
        reason: 'Мягкое очищение активированным углём может помочь успокоить кожу и восстановить её микробаланс.',
        reason_uz: 'Faollashtirilgan ko\'mir bilan yumshoq tozalash terini tinchlantirish va mikrobalansini tiklashga yordam berishi mumkin.',
        reason_pt: 'A limpeza suave com carvão ativado pode ajudar a acalmar a pele e restaurar seu microequilíbrio.'
      }
    ]
  },

  curly_hair: {
    name: 'Уход за кудрявыми и волнистыми волосами',
    emoji: '🌀',
    symptoms: [
      'кудрявые', 'кудри', 'вьются', 'вьющие', 'волнистые', 'завитки',
      'пушатся', 'пушист', 'фриз', 'лохматые', 'curly', 'ricci',
      'непослушные', 'объём мешает', 'разлетаются'
    ],
    clarifyingQuestions: [
      'Ваши кудри от природы или появились после химической завивки?',
      'Основная проблема — сухость, пушистость или отсутствие чёткого завитка?',
      'Используете ли вы сейчас специальный уход для кудрявых?'
    ],
    clarifyingQuestions_uz: [
      'Sizning jingalaklaringiz tabiiymi yoki kimyoviy to\'lqinlashdan keyin paydo bo\'ldimi?',
      'Asosiy muammo — quruqlik, pufaklanishmi yoki aniq burama yo\'qligi?',
      'Jingalak sochlar uchun maxsus parvarishdan foydalanasizmi?'
    ],
    clarifyingQuestions_pt: [
      'Seu cabelo é naturalmente cacheado ou ficou assim após uma permanente?',
      'O principal problema é secura, frizz ou falta de definição dos cachos?',
      'Você já usa atualmente algum cuidado específico para cabelos cacheados?'
    ],
    empathy: 'Кудрявые волосы — это особый тип, который при правильном уходе может быть очень красивым.',
    empathy_uz: 'Jingalak sochlar — to\'g\'ri parvarish bilan juda chiroyli bo\'lishi mumkin bo\'lgan alohida tur.',
    empathy_pt: 'Cabelo cacheado é um tipo especial que, com os cuidados certos, pode ser lindíssimo.',
    problemDescription: 'судя по описанию, вам нужен специальный уход, рассчитанный на особенности кудрявых волос.',
    problemDescription_uz: 'tavsifga ko\'ra, sizga jingalak sochlarning xususiyatlarini hisobga olgan holda mo\'ljallangan maxsus parvarish kerak.',
    problemDescription_pt: 'pelo que você descreveu, você precisa de um cuidado específico desenvolvido para as particularidades dos cabelos cacheados.',
    causes: 'Кудрявые волосы от природы более сухие у длины, так как себум сложнее распределяется по спирали. Они чувствительны к сульфатам и силиконам.',
    causes_uz: 'Jingalak sochlar tabiatan uzunligi bo\'yicha quriroqdir, chunki sebum spiral bo\'ylab tarqalishi qiyinroq. Ular sulfatlar va silikonlarga sezgir.',
    causes_pt: 'O cabelo cacheado é naturalmente mais seco ao longo do comprimento, pois o sebo tem dificuldade de se distribuir pelo espiral. É sensível a sulfatos e silicones.',
    disclaimer: '⚠️ Я не медицинский специалист. Для диагностики состояния кожи головы рекомендую обратиться к трихологу.',
    disclaimer_uz: '⚠️ Men tibbiy mutaxassis emasman. Bosh terisi holatini tashxislash uchun trixologga murojaat qilishni tavsiya etaman.',
    disclaimer_pt: '⚠️ Não sou especialista médico. Para diagnóstico do couro cabeludo, recomendo consultar um tricologista.',
    products: [
      {
        section: 'MIO RICCI',
        role: 'primary',
        reason: 'Линейка создана специально для кудрявых волос — без сульфатов и силиконов, совместима с методом Curly Girl. Может помочь определить завиток и убрать пушистость.',
        reason_uz: 'Liniya jingalak sochlar uchun maxsus yaratilgan — sulfatsiz va siliconsiz, Curly Girl usuli bilan mos keladi. Burzmani aniqlashtirish va pufaklanishni kamaytirishga yordam berishi mumkin.',
        reason_pt: 'A linha é criada especialmente para cabelos cacheados — sem sulfatos e silicones, compatível com o Método Curly Girl. Pode ajudar a definir os cachos e eliminar o frizz.'
      }
    ]
  },

  color_treated: {
    name: 'Уход за окрашенными волосами',
    emoji: '🎨',
    symptoms: [
      'окрашен', 'краска', 'цвет вымывается', 'тускнеет цвет',
      'желтизна', 'желтеют', 'блонд', 'осветлён', 'тонирован',
      'после окрашивани', 'цвет уходит', 'нейтрализация'
    ],
    clarifyingQuestions: [
      'Это натуральное окрашивание или осветление/обесцвечивание?',
      'Цвет вымывается быстро или волосы стали повреждёнными после процедуры?',
      'Есть ли нежелательная желтизна или нежелательный тон?'
    ],
    clarifyingQuestions_uz: [
      'Bu tabiiy bo\'yashmi yoki oqartirish/rangini ketkazishmi?',
      'Rang tez yuviladi yoki jarayondan keyin sochlar shikastlangimi?',
      'Noxush sariqlik yoki noxush ton bormi?'
    ],
    clarifyingQuestions_pt: [
      'É uma coloração natural ou descoloração/descolorimento?',
      'A cor desbota rápido ou os fios ficaram danificados após o procedimento?',
      'Há amarelamento indesejado ou tom indesejado?'
    ],
    empathy: 'Поддерживать красивый цвет — это целое искусство, и нужен правильный уход.',
    empathy_uz: 'Chiroyli rangni saqlash butun bir san\'at va to\'g\'ri parvarish kerak.',
    empathy_pt: 'Manter uma cor bonita é uma verdadeira arte e requer os cuidados certos.',
    problemDescription: 'судя по описанию, волосам нужна защита цвета и уход с учётом химического воздействия окрашивания.',
    problemDescription_uz: 'tavsifga ko\'ra, sochlarga rang himoyasi va bo\'yash kimyoviy ta\'sirini hisobga olgan holda parvarish kerak.',
    problemDescription_pt: 'pelo que você descreveu, o cabelo precisa de proteção de cor e cuidados que considerem o impacto químico da coloração.',
    causes: 'Окрашивание делает волос более пористым — цвет вымывается быстрее. Желтизна появляется из-за остаточного пигмента, жёсткой воды или ультрафиолета.',
    causes_uz: 'Bo\'yash sochni ko\'proq g\'ovak qiladi — rang tezroq yuviladi. Sariqlik qoldiq pigment, qattiq suv yoki ultrabinafsha nurlanish tufayli paydo bo\'ladi.',
    causes_pt: 'A coloração torna o fio mais poroso — a cor desbota mais rápido. O amarelamento surge por causa do pigmento residual, água dura ou radiação ultravioleta.',
    disclaimer: '⚠️ Я не медицинский специалист. Для оценки состояния волос после агрессивных процедур рекомендую проконсультироваться со специалистом.',
    disclaimer_uz: '⚠️ Men tibbiy mutaxassis emasman. Agressiv jarayonlardan keyin sochlar holatini baholash uchun mutaxassisga murojaat qilishni tavsiya etaman.',
    disclaimer_pt: '⚠️ Não sou especialista médico. Para avaliação do estado do cabelo após procedimentos agressivos, recomendo consultar um especialista.',
    products: [
      {
        section: 'COLORE',
        role: 'primary',
        reason: 'Специальная система для окрашенных волос — может помочь дольше сохранить яркость цвета и добавить блеск.',
        reason_uz: 'Bo\'yalgan sochlar uchun maxsus tizim — rang yorqinligini uzoqroq saqlash va porloqlik qo\'shishga yordam berishi mumkin.',
        reason_pt: 'Sistema especial para cabelos coloridos — pode ajudar a preservar a vivacidade da cor por mais tempo e adicionar brilho.'
      },
      {
        section: 'PREMIUM VIOLET',
        role: 'secondary',
        reason: 'Если есть нежелательная желтизна на блонде — фиолетовый пигмент может помочь её нейтрализовать.',
        reason_uz: 'Blondda noxush sariqlik bo\'lsa — binafsha pigment uni neytrallashtirishga yordam berishi mumkin.',
        reason_pt: 'Se houver amarelamento indesejado no loiro — o pigmento violeta pode ajudar a neutralizá-lo.'
      }
    ]
  }

};

// ── Ключевые слова-«сигналы» для первичного определения темы ─────
const TOPIC_KEYWORDS = {
  fatty_seborrhea:  ['жирн', 'сальн', 'быстро грязн', 'часто мою', 'к вечеру', 'маслян', 'себорея'],
  dry_scalp:        ['сух', 'шелушен', 'стянутост', 'зуд', 'перхот', 'чешейк', 'белые', 'чешет'],
  hair_loss:        ['выпадени', 'выпадают', 'лысе', 'редеют', 'потер', 'облысен', 'меньше волос'],
  damaged_hair:     ['ломк', 'повреждён', 'пористые', 'хрупк', 'после осветлени', 'тускл', 'секущ'],
  scalp_irritation: ['раздражен', 'покрасн', 'жжен', 'болит кожа', 'чувствительн', 'воспален'],
  curly_hair:       ['кудрявые', 'кудри', 'вьются', 'пушатся', 'фриз', 'завитки', 'волнистые'],
  color_treated:    ['окрашен', 'краска', 'цвет', 'желтизна', 'блонд', 'осветлён', 'тонирован']
};

/**
 * Анализирует текст пользователя и возвращает список вероятных проблем с баллами.
 * @param {string} text - текст от пользователя
 * @returns {Array} [{conditionKey, score, condition}] отсортированный по убыванию
 */
function analyzeSymptoms(text) {
  const lower = text.toLowerCase();
  const scores = {};

  // Основная оценка по симптомам из базы
  for (const [key, condition] of Object.entries(SCALP_CONDITIONS)) {
    scores[key] = 0;
    for (const kw of condition.symptoms) {
      if (lower.includes(kw)) scores[key] += 2;
    }
  }

  // Дополнительные баллы по ключевым словам-сигналам
  for (const [key, keywords] of Object.entries(TOPIC_KEYWORDS)) {
    for (const kw of keywords) {
      if (lower.includes(kw)) scores[key] = (scores[key] || 0) + 1;
    }
  }

  return Object.entries(scores)
    .filter(([, score]) => score > 0)
    .sort(([, a], [, b]) => b - a)
    .map(([key, score]) => ({ key, score, condition: SCALP_CONDITIONS[key] }));
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { SCALP_CONDITIONS, TOPIC_KEYWORDS, analyzeSymptoms };
}
