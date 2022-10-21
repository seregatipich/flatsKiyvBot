import os

import requests
from dotenv import load_dotenv
from PIL import Image

from walls import wall_types

load_dotenv()
api_token = os.getenv('TOKEN_RIA')


def get_post_content():
    search_url = f'https://developers.ria.com/dom/search?api_key={api_token}&category=1&realty_type=2&operation_type=1&state_id=10&city_id=10&exclude_agencies=1'
    search_response = requests.get(f'{search_url}')
    id_list = sorted(search_response.json()['items'], reverse=True)
    id_adv = id_list[0]

    def get_info():
        id_url = f'https://developers.ria.com/dom/info/{id_adv}?api_key={api_token}'
        not_specified = 'Не указано'
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
            living_square_meters = f"Жилая площадь: {not_specified}"
        try:
            kitchen_square_meters = f"Площадь кухни: {characteristcs['218']}м²"
        except KeyError:
            kitchen_square_meters = f"Площадь кухни: {not_specified}"
        wall_type = f"Тип стен: {wall_types[wall_type_id]['name']}"
        rooms_count = f"Количество комнат: {properties['rooms_count']}"
        if properties['description'] != '':
            description = f"Описание: {properties['description']}"
        else:
            description = f"Описание: {not_specified}"

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
        return '\n\n'.join(adv_list)

    def get_photo():
        left = 0
        top = 52
        id_url = f"https://developers.ria.com/dom/info/{id_adv}?api_key={api_token}"
        response = requests.get(id_url).json()
        beautiful_photo_url = response['beautiful_url'].replace(
            f'-{id_adv}', '').replace('.html', '')
        photo_id_list = list(response['photos'].keys())
        for i in range(0, len(photo_id_list)):
            photo_id = photo_id_list[i]
            img_url = f"https://cdn.riastatic.com/photosnew/dom/photo/{beautiful_photo_url}__{photo_id}xg.webp"
            p = requests.get(img_url)
            out = open(f"{beautiful_photo_url}__{i}raw.webp", "wb")
            out.write(p.content)
            out.close()

        for i in range(0, len(photo_id_list)):
            im = Image.open(f"{beautiful_photo_url}__{i}raw.webp")
            right = im.size[0]
            bottom = im.size[1]
            im1 = im.crop((left, top, right, bottom))
            im1.save(f"photo_{i}cleaned.webp")
            os.remove(f"{beautiful_photo_url}__{i}raw.webp")

    get_photo()
    return str(get_info())


def remove_files():
    fileExt = '.webp'
    files_list = [_ for _ in os.listdir() if _.endswith(fileExt)]
    for i in range(0, len(files_list)):
        os.remove(files_list[i])
