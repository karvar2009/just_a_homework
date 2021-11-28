import json
import requests

url = 'https://api.coinbase.com/v2/exchange-rates'
responce = requests.get(url)
rates = json.loads(responce.text)
for code, value in rates['data']['rates'].items():
    print(f'1 $ это в {code} будет {value}')