from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Указываем, где лежат HTML файлы
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # Этот маршрут убирает "Not Found" и показывает твой магазин
    return templates.TemplateResponse("index.html", {"request": request})

# Скрытый эндпоинт для подключения бота
@app.post("/admin/connect_bot")
async def connect_bot(key: str):
    print(f"Подключение бота с ключом: {key}")
    return {"status": "success", "message": "FraerWasted Bot Connected"}

if __name__ == "__main__":
    import uvicorn
    # Render сам назначит порт через переменную окружения PORT
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
