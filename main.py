import requests
import json
from colorama import Fore
from http import HTTPStatus


def lucros_prejuizos(ticker):
    url = f'https://brapi.dev/api/quote/{ticker}'
    response = requests.get(url)
    data = json.loads(response.content)

    if response.status_code == HTTPStatus.NOT_FOUND:
        print('Página não encontrada')
    elif response.status_code == HTTPStatus.OK:
        preco_compra = 21.04
        quantidade = 10
        data_market_price = data['results'][0]['regularMarketPrice']
        lucro_prejuizo = round((preco_compra - data_market_price) * quantidade, 2) 
    
        if 'longName' not in data['results'][0]:
            print(data['results'][0]['shortName'])
        else:
            print(data['results'][0]['longName'])
            
        print('R$ ', data_market_price)
        if preco_compra > data_market_price:
            print(Fore.RED + f'Prejuízo: R$ {str(lucro_prejuizo)}')
        elif preco_compra < data_market_price:
            print(Fore.GREEN + f'Lucro: R$ {str(lucro_prejuizo).replace("-", "")}')
        else:
            print(f'R$ {str(lucro_prejuizo).replace("-", "")}')


lucros_prejuizos('ITUB3')
