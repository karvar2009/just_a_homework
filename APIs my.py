import os
import requests
from requests.exceptions import HTTPError


def fetch_horoscope(sigh: str, day: str) -> str or None:
    """
    позволяет получить предсказание
    :param sigh: знак зодиака
    :param day:день например(today)
    :return:предсказание
    """
    url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
    headers = {
        'x-rapidapi-host': "sameer-kumar-aztro-v1.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get('API_KEY')
    }
    sighs = {
        'овен': 'aries',
        'телец': 'taurus',
        'близнецы': 'gemini',
        'рак': 'cancer',
        'лев': 'leo',
        'дева': 'virgo',
        'весы': 'libra',
        'скорпион': 'scorpio',
        'стрелец': 'sagittarius',
        'козерог': 'capricorn',
        'водолей': 'aquarius',
        'рыбы': 'pisces'
    }
    days = {
        'вчера': 'yesterday',
        'сегодня': 'today',
        'завтра': 'tomorrow'
    }
    try:
        sigh = sighs[sigh]
        day = days[day]

        query = {'sign': sigh, 'day': day}
        responce_g = requests.post(url, headers=headers, params=query)
        json_responce_g = responce_g.json()
        horoscope = json_responce_g['description']
        return horoscope
    except KeyError:
        print('Вы ввели неправильный знак/день')
        return None
    except HTTPError as HTTP_err:
        print(f'Возникла ошибка сервера: {HTTP_err}')
    except Exception as err:
        print(f'Возникла ошибка: {err}')


def translate(text: str, lang: str) -> str or None:
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = f"q={text}&target={lang}&source=en"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept-encoding': "application/gzip",
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get('API_TRANSLATE_KEY')
    }
    try:
        responce_t = requests.post(url, data=payload, headers=headers)
        json_responce_t = responce_t.json()
        translated = json_responce_t['data']['translations'][0]['translatedText']
        return translated
    except HTTPError as HTTP_err:
        print(f'Возникла ошибка сервера: {HTTP_err}')
    except Exception as err:
        print(f'Возникла ошибка: {err}')


znak = input('Введите ваш знак зодиака (весы|скорпион): ').lower()
day_h = input('Введите день для предсказания (вчера|сегодня|завтра): ').lower()

print(translate(fetch_horoscope(znak, day_h), 'ru'))
