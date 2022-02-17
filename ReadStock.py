"""
mabyul / 2022-02-16
https://github.com/umjiwan/ReadStock.git
"""


import requests
from bs4 import BeautifulSoup

class StockData: # 주식 데이터 클래스
    def __init__(self, StockCode): # StockCode = 주식 종목코드
        url = "https://finance.naver.com/item/main.naver?code=" + StockCode
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        self.soup = soup
        self.StockCode = StockCode

    def NowPrice(self, shim=False): # 현재가 가져오는 함수
        selector = "#chart_area > div.rate_info > div > p.no_today > em > span"
        result = self.soup.select_one(selector)

        if not result: # 해당 종목이 없을 경우
            return None

        # shim은 현재가를 문자열로 쉼표를 붙여서 출력하는 옵션
        # True가 쉼표가 있는것

        if shim:
            return result.text
        else:
            return int(result.text.replace(",", ""))