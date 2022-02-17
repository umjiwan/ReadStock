import requests
from bs4 import BeautifulSoup

class StockData:
    def __init__(self, StockCode):
        url = "https://finance.naver.com/item/main.naver?code=" + StockCode
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        self.soup = soup
        self.StockCode = StockCode

    def NowPrice(self, shim=False):
        selector = "#chart_area > div.rate_info > div > p.no_today > em > span"
        result = self.soup.select_one(selector).text

        if shim:
            return result
        else:
            return int(result.replace(",", ""))