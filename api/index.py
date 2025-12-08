from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from pathlib import Path

app = FastAPI()

# Пути для Vercel
BASE_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# Импортируем данные
import sys
sys.path.append(str(BASE_DIR))
from data.books import BOOKS, AUTHOR_INFO

# Добавляем фильтр для года в шаблонах
import datetime
templates.env.filters["now"] = lambda: datetime.datetime.now()

# Статические файлы - Vercel будет обслуживать их через routes
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

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
async def all_books(request: Request):
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
    if not book:
        return templates.TemplateResponse(
            "404.html",
            {"request": request, "page_title": "Книга не найдена"},
            status_code=404
        )
    
    return templates.TemplateResponse(
        "book_detail.html",
        {
            "request": request,
            "book": book,
            "author": AUTHOR_INFO,
            "page_title": book["title"]
        }
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

# Для Vercel важно иметь этот обработчик
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)