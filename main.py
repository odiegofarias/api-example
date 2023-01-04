import requests
import json


ticker = input('Ticker: ')

url = f'https://brapi.dev/api/quote/{ticker}'
response = requests.get(url)
data = json.loads(response.content)

if response.status_code == 200:
    preco_compra = 21
    quantidade = 10
    data_market_price = data['results'][0]['regularMarketPrice']
    lucro_prejuizo = round(preco_compra - data_market_price, 2) * quantidade
    
    if 'longName' not in data['results'][0]:
        print(data['results'][0]['shortName'])
    else:
        print(data['results'][0]['longName'])
    
    print(data['results'][0]['longName'])
    print('R$ ', data_market_price)
    if preco_compra > data_market_price:
        print(f'Prejuízo: - R$ {str(lucro_prejuizo)}')
    else:
        print(f'Lucro: + R$ {str(lucro_prejuizo).replace("-", "")}')
else:
    print('Página não encontrada')
