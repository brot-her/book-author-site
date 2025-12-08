BOOKS = [
    {
        "id": 1,
        "title": "Название первой книги",
        "author": "Имя автора",
        "cover_image": "/static/images/book1.jpg",
        "year": 2023,
        "genre": "Роман",
        "description": "Подробное описание книги о чём она, основные темы и идеи.",
        "full_text": """Здесь размещается текст для сайта. 
        Это может быть отрывок из книги, рецензия или мысли автора.

        Можно размещать несколько абзацев.

        Текст будет отображаться на отдельной странице книги.""",
        "links": [
            {"name": "Купить на OZON", "url": "https://ozon.ru/..."},
            {"name": "Читать на Литрес", "url": "https://litres.ru/..."}
        ]
    },
    {
        "id": 2,
        "title": "Название второй книги",
        "author": "Имя автора",
        "cover_image": "/static/images/book2.jpg",
        "year": 2022,
        "genre": "Фантастика",
        "description": "Описание второй книги автора.",
        "full_text": "Текст второй книги...",
        "links": [
            {"name": "Купить на OZON", "url": "#"}
        ]
    },
    # Добавьте остальные книги здесь
]

AUTHOR_INFO = {
    "name": "Полное имя автора",
    "bio": """Биография автора. Расскажите о его творческом пути, 
    наградах, основных темах в произведениях.""",
    "photo": "/static/images/author.jpg",
    "awards": ["Премия 1", "Премия 2", "Премия 3"],
    "contact": {
        "email": "author@example.com",
        "social": {
            "vk": "https://vk.com/author",
            "telegram": "https://t.me/author",
            "youtube": "https://youtube.com/author"
        }
    }
}