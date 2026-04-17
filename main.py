from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.get("/")
async def index(request: Request):
    # Здесь рендерится дизайн MADE BY MEMORY
    return templates.TemplateResponse("index.html", {"request": request})

# Скрытый эндпоинт только для тебя (ffame/Saymon)
@app.post("/admin/connect_bot")
async def connect_bot(key: str):
    # Кнопка на сайте отправляет твой golden_key сюда
    # Бот запускается и начинает цикл проверки FunPay
    return {"status": "FraerWasted Bot Connected"}
