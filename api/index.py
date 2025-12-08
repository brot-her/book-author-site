from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from datetime import datetime

app = FastAPI(title="Ящик с ушами")

# Настройка путей для Vercel
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)

# Статические файлы
static_dir = os.path.join(root_dir, "public")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Шаблоны
templates_dir = os.path.join(root_dir, "templates")
templates = Jinja2Templates(directory=templates_dir)


# Добавляем фильтр для года в шаблонах
def current_year():
    return datetime.now().year


templates.env.globals["current_year"] = current_year

# ВСЯ ИНФОРМАЦИЯ О КНИГЕ ПРЯМО ЗДЕСЬ
BOOK = {
    "title": "Ящик с ушами",
    "author": "Ваше имя",  # Вставьте своё имя
    "author_bio": "Автор детских сказок, отец двух сыновей",
    "cover_image": "/static/images/book-cover.jpg",
    "year": 2019,
    "genre": "Детская литература, Сказки",
    "pages": 64,
    "illustrator": "Дарья Мартынова",
    "illustrator_bio": "Известная художница-иллюстратор детской литературы",

    "description": """В этой небольшой книге 2019 года - несколько историй, которые я рассказывал, 
    сочиняя на ходу, моим младшим сыновьям - Тимуру и Бориславу. "Ящик с ушами" - мой первый опыт 
    публикации детских сказок. Хотя мне порой кажется, что это не совсем сказки. И, может быть, 
    даже не вполне детские. Зато все они добрые и с хорошим концом. Как и должно быть в жизни!""",

    "stories": [
        {
            "title": "Ящик с ушами",
            "description": "Кто прячется в картонном ящике на корабле и ворует бананы?",
            "image": "/static/images/illustrations/box.jpg"
        },
        {
            "title": "Пингвин-моряк",
            "description": "История о пингвине, который решил стать профессиональным моряком",
            "image": "/static/images/illustrations/penguin.jpg"
        },
        {
            "title": "Воздушный говорящий змей",
            "description": "Большой воздушный змей, который умеет разговаривать",
            "image": "/static/images/illustrations/kite.jpg"
        },
        {
            "title": "Тайна знаков препинания",
            "description": "Возможно, мы разгадаем тайну знаков препинания!",
            "image": "/static/images/illustrations/punctuation.jpg"
        },
        {
            "title": "Пятая сказка",
            "description": "Ещё одна добрая история с хорошим концом",
            "image": "/static/images/illustrations/story5.jpg"
        }
    ],

    "quotes": [
        "«Ящик с ушами наполнен добром и любовью»",
        "«Все истории добрые и с хорошим концом. Как и должно быть в жизни!»",
        "«Это даже больше ящик с любовью, чем с ушами»"
    ],

    "characters": [
        "Тайный обитатель ящика",
        "Пингвин Пинги",
        "Воздушный змей",
        "Знаки препинания",
        "Братья Тимур и Борислав"
    ],

    "links": [
        {
            "name": "📖 Читать онлайн",
            "url": "https://drive.google.com/open?id=18Pxthlic4JkAbdLE8bMWSp6vFuhjTymJ",
            "icon": "book-open"
        },
        {
            "name": "🎧 Аудиоверсия",
            "url": "#",
            "icon": "headphones"
        },
        {
            "name": "🖼️ Иллюстрации",
            "url": "#illustrations",
            "icon": "palette"
        }
    ],

    "facts": [
        "Первый опыт публикации детских сказок автора",
        "Истории сочинялись на ходу для сыновей",
        "Иллюстрации создавались с помощью картонных моделей",
        "Книга родилась из вечерних сказок детям"
    ]
}


# Маршруты
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "book": BOOK,
            "page_title": "Главная"
        }
    )


@app.get("/stories", response_class=HTMLResponse)
async def stories(request: Request):
    return templates.TemplateResponse(
        "stories.html",
        {
            "request": request,
            "book": BOOK,
            "page_title": "Все истории"
        }
    )


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {
            "request": request,
            "book": BOOK,
            "page_title": "Об авторе и художнике"
        }
    )


@app.get("/health")
async def health():
    return {"status": "healthy", "book": BOOK["title"]}


# Простой обработчик для favicon (частая ошибка на Vercel)
@app.get("/favicon.ico")
async def favicon():
    from fastapi.responses import FileResponse
    favicon_path = os.path.join(static_dir, "images", "favicon.ico")
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path)
    return {"message": "No favicon"}


# Обработчик для Vercel Serverless Functions
@app.get("/api/{path:path}")
async def api_handler():
    return {"message": "API endpoint"}


# Главная функция для запуска (для локальной разработки)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)