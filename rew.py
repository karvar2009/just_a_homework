# import requests
# from requests.exceptions import HTTPError
# try:
#     responce = requests.get('https://api.github.com/search/repositories', params={'q': 'requests+language:cpp'})
#     responce.raise_for_status()
#     print('успешное подключение')
#     json_r = responce.json()
#     for repo in json_r['items']:
#         print(repo['description'])
# except HTTPError as http_e:
#     print(f'HTTP  error occurred')
# except Exception as err:
#     print(f'other error occurred')

import requests

url = "https://imdb8.p.rapidapi.com/title/find"

querystring = {"q":"squid game"}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "86e4e079cemshba17a82d5ffe9afp16ac0bjsnab4c30b8c551"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
json_responce = response.json()

for line in json_responce['results']:
    print(line)