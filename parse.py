import os

import requests
from dotenv import load_dotenv

from walls import wall_types


def get_info():
    load_dotenv()
    api_token = os.getenv('TOKEN_RIA')
    search_url = f'https://developers.ria.com/dom/search?api_key={api_token}&category=1&realty_type=2&operation_type=1&state_id=10&city_id=10'
    search_response = requests.get(f'{search_url}')
    id_list = sorted(search_response.json()['items'], reverse=True)
    id_adv = id_list[0]
    id_adv = 24322777
    id_url = f'https://developers.ria.com/dom/info/{id_adv}?api_key={api_token}'
    id_response = requests.get(f'{id_url}')
    properties = id_response.json()
    characteristcs = properties['characteristics_values']
    wall_type_id = str(characteristcs['118'])

    price = f"Цена: {properties['price']}$"
    district = f"Район: {properties['district_name']}"
    floor = f"Этаж: {properties['floor']}"
    floor_count = f"Этажность: {properties['floors_count']}"
    total_square_meters = f"Общая площадь: {properties['total_square_meters']}м²"
    try:
        living_square_meters = f"Жилая площадь: {characteristcs['216']}м²"
    except KeyError:
        living_square_meters = "Жилая площадь: Не указано"
    try:
        kitchen_square_meters = f"Площадь кухни: {characteristcs['218']}м²"
    except KeyError:
        kitchen_square_meters = "Площадь кухни: Не указано"
    wall_type = f"Тип стен: {wall_types[wall_type_id]['name']}"
    rooms_count = f"Количество комнат: {properties['rooms_count']}"
    description = f"Описание: {properties['description']}"
    adv_list = [
        price,
        district,
        floor,
        floor_count,
        total_square_meters,
        living_square_meters,
        kitchen_square_meters,
        wall_type,
        rooms_count,
        description
    ]
    info = []
    for i in range(0, len(adv_list)):
        info.append(adv_list[i])

    return '\n\n'.join(info)


print(get_info())
