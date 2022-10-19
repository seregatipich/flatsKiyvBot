import os

import requests
from dotenv import load_dotenv

from walls import wall_types

load_dotenv()


api_token = os.getenv('TOKEN_RIA')


id_url = f'https://developers.ria.com/dom/search?api_key={api_token}&category=1&realty_type=2&operation_type=1&state_id=10&city_id=10'


def get_info(id_url, wall_types):
    response = requests.get(f'{id_url}')
    properties = response.json().get('characteristics_values')
    wall_type_id = str(properties['118'])
    info = f"""
            Цена: {properties['234']}\n
            Метро: {response.json().get('metro_station_name')}\n
            Этаж: {properties['227']}\n
            Этажность: {properties['228']}\n
            Общая площадь: {properties['214']}\n
            Жилая площадь: {properties['216']}\n
            Площадь кухни: {properties['218']}\n
            Тип стен: {wall_types[wall_type_id]['name']}\n
            Количество комнат: {properties['209']}
            """
    return info
