from currency_converter import CurrencyConverter
import requests
from bs4 import BeautifulSoup

cc = CurrencyConverter()
print(cc.currencies) #통화목록
cc = CurrencyConverter('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip') 
print(cc.convert(1, 'USD', 'KRW')) #약간의 오차가 있음

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',  # 브라우저 User-Agent 설정
        'Content-Type': 'text/html; charset=utf-8'
    }

    proxies = {
        # 프록시 서버 설정
        'http': 'http://50.172.75.120:80'
    }


    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers, proxies=proxies)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    print(content)

get_exchange_rate('usd', 'krw')