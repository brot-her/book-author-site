from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from datetime import datetime

app = FastAPI(title="Ящик с ушами")

# Настройка путей
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)

# Статические файлы
app.mount("/static", StaticFiles(directory=os.path.join(root_dir, "public")), name="static")

# Шаблоны
templates = Jinja2Templates(directory=os.path.join(root_dir, "templates"))


# Добавляем фильтр для года в шаблонах
def current_year():
    return datetime.now().year


templates.env.globals["current_year"] = current_year

# ДАННЫЕ О КНИГЕ
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

    "full_story": """<h3>История первая: Тайна картонного ящика</h3>

    <p>На большом белом корабле, который плыл к далёким тёплым островам, случилась странная история. 
    Каждое утро пропадали бананы из кают-компании. Сначала думали, что это крысы, но крыс на корабле 
    не было. Потом решили, что кто-то из матросов шутит, но все матросы клялись, что не при чём.</p>

    <p>А из картонного ящика, который стоял в углу каюты, иногда доносилось странное шуршание. 
    И если прислушаться очень внимательно, можно было услышать тихое-тихое посапывание...</p>

    <h3>Вторая история: Пингвин-моряк</h3>

    <p>В самом холодном порту Антарктики жил пингвин по имени Пинги. Все пингвины вокруг ныряли 
    за рыбой, грелись на льдинах и воспитывали птенцов. А Пинги мечтал стать моряком.</p>

    <p>"Пингвины не бывают моряками!" - говорили ему друзья. "У нас ласты, а у моряков руки!"</p>

    <p>Но Пинги не слушал. Каждый день он приходил в порт и смотрел, как большие корабли уходят 
    в открытое море. И однажды...</p>""",

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


# Главная страница
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


# Страница со всеми историями
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


# Страница об авторе
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


# Здоровье API
@app.get("/health")
async def health():
    return {"status": "healthy", "book": BOOK["title"]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)