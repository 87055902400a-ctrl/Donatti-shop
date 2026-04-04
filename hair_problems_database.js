// База знаний: проблемы волос и рекомендуемые продукты
const HAIR_PROBLEMS_DATABASE = {
    'секущиеся кончики': {
        keywords: ['секущиеся', 'кончики', 'посеченные', 'ломкие', 'сухие кончики'],
        description: 'Секущиеся кончики',
        recommendations: [
            {
                section: 'DNAVANZE',
                reason: 'Восстанавливает структуру волос, запечатывает кончики'
            },
            {
                section: 'BIODETOX',
                reason: 'Масло и несмываемый уход для защиты кончиков'
            },
            {
                section: 'SPECIALE',
                reason: 'Питательная маска Nutri восстанавливает поврежденные кончики'
            }
        ]
    },
    
    'выпадение волос': {
        keywords: ['выпадение', 'выпадают', 'редеют', 'потеря волос', 'облысение', 'выпадают волосы'],
        description: 'Выпадение волос',
        recommendations: [
            {
                section: 'BAOBÁ REDUCE',
                products: ['Vigore — Капсулы для волос', 'Vigore — Тоник против выпадения'],
                reason: 'Специальный комплекс Vigore против выпадения, стимулирует рост новых волос'
            }
        ]
    },
    
    'сухие волосы': {
        keywords: ['сухие', 'сухость', 'обезвоженные', 'жесткие', 'жёсткие', 'пересушенные'],
        description: 'Сухие и обезвоженные волосы',
        recommendations: [
            {
                section: 'SPECIALE',
                reason: 'Линия Nutri - интенсивное питание и увлажнение'
            },
            {
                section: 'NATURALE',
                reason: 'Ультра-увлажняющие маски Monoi Tahiti и Ojon'
            },
            {
                section: 'BIODETOX',
                reason: 'Масло для питания и блеска сухих волос'
            }
        ]
    },
    
    'поврежденные волосы': {
        keywords: ['поврежденные', 'повреждённые', 'ломкие', 'слабые', 'после химии', 'после окрашивания'],
        description: 'Поврежденные и ослабленные волосы',
        recommendations: [
            {
                section: 'DNAVANZE',
                reason: 'Глубокая регенерация и восстановление структуры'
            },
            {
                section: 'BIODETOX',
                reason: 'Восполнение углерода и реконструкция волос'
            },
            {
                section: 'SPECIALE',
                reason: 'Питание и восстановление поврежденных волос'
            }
        ]
    },
    
    'желтизна': {
        keywords: ['желтизна', 'желтый', 'жёлтый', 'нежелательный оттенок', 'желтые волосы'],
        description: 'Нежелательная желтизна блонд',
        recommendations: [
            {
                section: 'PREMIUM VIOLET',
                reason: 'Фиолетовый шампунь и бальзам нейтрализуют желтизну'
            },
            {
                section: 'THEION',
                reason: 'Защита и сохранение холодного оттенка блонд'
            }
        ]
    },
    
    'вьющиеся волосы': {
        keywords: ['вьющиеся', 'кудри', 'кудрявые', 'волнистые', 'пушистые', 'пушатся'],
        description: 'Вьющиеся и кудрявые волосы',
        recommendations: [
            {
                section: 'MIO RICCI',
                reason: 'Специальная линия для кудрей без сульфатов'
            },
            {
                section: 'BAOBÁ REDUCE',
                reason: 'Сокращение объёма и разглаживание (для афро-волос)'
            }
        ]
    },
    
    'пористые волосы': {
        keywords: ['пористые', 'пористость', 'пушистые', 'не гладкие', 'торчащие'],
        description: 'Пористые и непослушные волосы',
        recommendations: [
            {
                section: 'BAOBÁ REDUCE',
                reason: 'K-Drive Technology - сокращение объёма и гладкость'
            },
            {
                section: 'BIODETOX',
                reason: 'Выравнивание структуры и разглаживание'
            }
        ]
    },
    
    'окрашенные волосы': {
        keywords: ['окрашенные', 'окраска', 'цвет', 'после окрашивания', 'краска'],
        description: 'Окрашенные волосы',
        recommendations: [
            {
                section: 'COLORE',
                reason: 'Профессиональная система окрашивания и уход'
            },
            {
                section: 'THEION',
                reason: 'Защита цвета блонд'
            },
            {
                section: 'PREMIUM VIOLET',
                reason: 'Уход за окрашенными блонд волосами'
            }
        ]
    },
    
    'жирные волосы': {
        keywords: ['жирные', 'жирность', 'быстро грязнятся', 'сальные', 'масляные'],
        description: 'Жирные волосы и кожа головы',
        recommendations: [
            {
                section: 'BIODETOX',
                reason: 'Глубокое очищение и детоксикация кожи головы'
            },
            {
                section: 'EXTRA',
                products: ['pH Equilíbrio'],
                reason: 'Балансирующий шампунь нормализует pH'
            }
        ]
    },
    
    'тонкие волосы': {
        keywords: ['тонкие', 'без объема', 'без объёма', 'плоские', 'жидкие'],
        description: 'Тонкие волосы без объёма',
        recommendations: [
            {
                section: 'DNAVANZE',
                reason: 'Уплотнение и восстановление структуры'
            },
            {
                section: 'SPECIALE',
                reason: 'Питание без утяжеления'
            }
        ]
    },
    
    'перхоть': {
        keywords: ['перхоть', 'зуд', 'раздражение', 'чешуйки'],
        description: 'Перхоть и раздражение кожи головы',
        recommendations: [
            {
                section: 'BIODETOX',
                reason: 'Детоксикация и очищение кожи головы'
            },
            {
                section: 'EXTRA',
                products: ['Vigore — Скраб'],
                reason: 'Скраб для глубокого очищения кожи головы'
            }
        ]
    },
    
    'осветление': {
        keywords: ['осветление', 'обесцвечивание', 'блонд', 'светлые', 'осветлить'],
        description: 'Осветление волос',
        recommendations: [
            {
                section: 'CREAM BLOND',
                reason: 'Безопасный осветляющий крем (15× безопаснее порошка)'
            },
            {
                section: 'COLORE',
                products: ['Осветляющий порошок Azzurro', 'Осветляющий порошок Bianco'],
                reason: 'Профессиональные осветляющие порошки'
            },
            {
                section: 'THEION',
                reason: 'Защита и уход после осветления'
            }
        ]
    },
    
    'металлы': {
        keywords: ['металлы', 'металл', 'зеленый', 'зелёный', 'пятна', 'неровный цвет'],
        description: 'Удаление металлов из волос',
        recommendations: [
            {
                section: 'EXTRA',
                products: ['pH Equilíbrio'],
                reason: 'Подготовка к окрашиванию, удаление металлов'
            }
        ]
    },
    
    'разглаживание': {
        keywords: ['разглаживание', 'выпрямление', 'гладкие', 'прямые', 'кератин'],
        description: 'Разглаживание и выпрямление',
        recommendations: [
            {
                section: 'BAOBÁ REDUCE',
                reason: 'K-Drive Technology для профессионального разглаживания'
            },
            {
                section: 'BIODETOX',
                reason: 'Выравнивание и разглаживание волос'
            }
        ]
    }
};

// Экспорт для использования в других файлах
if (typeof module !== 'undefined' && module.exports) {
    module.exports = HAIR_PROBLEMS_DATABASE;
}
