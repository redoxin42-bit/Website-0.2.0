import httpx
from bs4 import BeautifulSoup

class FunPayBot:
    def __init__(self, golden_key):
        self.cookies = {"golden_key": golden_key}
        self.base_url = "https://funpay.com/orders/trade"

    async def check_new_orders(self):
        async with httpx.AsyncClient(cookies=self.cookies) as client:
            r = await client.get(self.base_url)
            soup = BeautifulSoup(r.text, 'html.parser')
            # Ищем все заказы со статусом "Оплачен"
            orders = soup.find_all('a', class_='tc-order')
            for order in orders:
                status = order.find('div', class_='tc-status').text
                if "Оплачен" in status:
                    item_name = order.find('div', class_='tc-desc').text
                    # Передаем данные в БД сайта для разблокировки контента
                    return item_name
