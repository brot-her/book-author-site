from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Получаем корневую директорию
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)

# Настраиваем статические файлы
static_dir = os.path.join(root_dir, "public")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Настраиваем шаблоны
templates_dir = os.path.join(root_dir, "templates")
templates = Jinja2Templates(directory=templates_dir)

# Простые тестовые данные
BOOKS = [
    {
        "id": 1,
        "title": "Первая книга",
        "cover_image": "/static/images/book1.jpg",
        "year": 2024,
        "genre": "Роман",
        "description": "Описание первой книги автора.",
        "full_text": "Здесь будет текст книги..."
    },
    {
        "id": 2,
        "title": "Вторая книга",
        "cover_image": "/static/images/book2.jpg",
        "year": 2023,
        "genre": "Фантастика",
        "description": "Описание второй книги.",
        "full_text": "Текст второй книги..."
    }
]

AUTHOR_INFO = {
    "name": "Иван Иванов",
    "bio": "Русский писатель, автор множества бестселлеров."
}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "books": BOOKS[:3],
            "author": AUTHOR_INFO,
            "page_title": "Главная"
        }
    )


@app.get("/books", response_class=HTMLResponse)
async def books_page(request: Request):
    return templates.TemplateResponse(
        "books.html",
        {
            "request": request,
            "books": BOOKS,
            "author": AUTHOR_INFO,
            "page_title": "Все книги"
        }
    )


@app.get("/book/{book_id}", response_class=HTMLResponse)
async def book_detail(request: Request, book_id: int):
    try:
        book_id = int(book_id)
        book = next((b for b in BOOKS if b["id"] == book_id), None)

        if book:
            return templates.TemplateResponse(
                "book_detail.html",
                {
                    "request": request,
                    "book": book,
                    "author": AUTHOR_INFO,
                    "page_title": book["title"]
                }
            )
    except:
        pass

    # Если книга не найдена
    return templates.TemplateResponse(
        "404.html",
        {"request": request, "page_title": "Книга не найдена"},
        status_code=404
    )


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {
            "request": request,
            "author": AUTHOR_INFO,
            "page_title": "Об авторе"
        }
    )


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse(
        "contact.html",
        {
            "request": request,
            "author": AUTHOR_INFO,
            "page_title": "Контакты"
        }
    )


# Тестовый endpoint для проверки работы
@app.get("/api/status")
async def status():
    return {
        "status": "ok",
        "service": "Book Author Website",
        "version": "1.0.0"
    }


# Простая проверка здоровья
@app.get("/health")
async def health():
    return {"status": "healthy"}