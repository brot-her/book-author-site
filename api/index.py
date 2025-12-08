from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import sys

# Настраиваем пути
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)

app = FastAPI()

# Подключаем статические файлы из public
app.mount("/static", StaticFiles(directory=os.path.join(root_dir, "public")), name="static")

# Подключаем шаблоны
templates = Jinja2Templates(directory=os.path.join(root_dir, "templates"))

# Тестовые данные (позже заменим на импорт)
BOOKS = [
    {
        "id": 1,
        "title": "Первая книга",
        "cover_image": "/static/images/book1.jpg",
        "year": 2024,
        "genre": "Роман",
        "description": "Описание книги"
    }
]

AUTHOR_INFO = {
    "name": "Имя Автора",
    "bio": "Биография автора"
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
    else:
        return templates.TemplateResponse(
            "404.html",
            {"request": request, "page_title": "Не найдено"},
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

# Простой тестовый endpoint
@app.get("/api/test")
async def test():
    return {"message": "API работает", "status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)