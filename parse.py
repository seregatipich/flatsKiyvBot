import logging
import os

import requests
from dotenv import load_dotenv
from PIL import Image, UnidentifiedImageError

from post_info import uniqueness_test
from walls import wall_types

load_dotenv()
api_token = os.getenv('TOKEN_RIA')


def get_adv_id(op_type):
    '''Content recieving from ria.com API'''
    print(op_type, 'get')
    search_url = f'https://developers.ria.com/dom/search?api_key={api_token}&category=1&realty_type=2&operation_type={op_type}&state_id=10&city_id=10&with_photo=True&exclude_agencies=10'
    search_response = requests.get(f'{search_url}')
    id_list = sorted(search_response.json()['items'], reverse=True)
    id_adv = str(id_list[0])
    return id_adv


def get_info(id_adv):
    '''
    Recieving text info about newest advertisement
    (IF the main.py time-condition is passed)
    '''
    id_url = f'https://developers.ria.com/dom/info/{id_adv}?api_key={api_token}'
    not_specified = 'Не указано'
    id_response = requests.get(f'{id_url}')
    properties = id_response.json()
    characteristcs = properties['characteristics_values']

    try:
        price = f"Цена: {properties['price']}$"
        district = f"Район: {properties['district_name']}"
        floor = f"Этаж: {properties['floor']}"
        floor_count = f"Этажность: {properties['floors_count']}"
        total_square_meters = f"Общая площадь: {properties['total_square_meters']}м²"
    except KeyError:
        return 'bad advertisement'

    try:
        living_square_meters = f"Жилая площадь: {characteristcs['216']}м²"
    except KeyError:
        living_square_meters = f"Жилая площадь: {not_specified}"
    try:
        kitchen_square_meters = f"Площадь кухни: {characteristcs['218']}м²"
    except KeyError:
        kitchen_square_meters = f"Площадь кухни: {not_specified}"

    wall_type = f"Тип стен: {properties['wall_type']}"
    rooms_count = f"Количество комнат: {properties['rooms_count']}"
    if properties['description'] != '':
        description = f"Описание:\n{properties['description']}"
    else:
        description = f"Описание: {not_specified}"
    contacts = [
        'Контакты:\n'
        'Телефон/Вайбер: 0933030690',
        'Телеграмм: @kkkinua',
        'Вотсапп: kkkinua',
        'Инст: https://instagram.com/kypit_kvartiry_kiev/',
        '---------------------------------------'
    ]

    adv_list = [
        id_adv,
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

    if uniqueness_test(adv_list) == 'recurring post':
        return 'recurring post'

    adv_list[0] = 'Назовите этот ID: ' + adv_list[0]
    adv_list.append('\n'.join(contacts))
    return '\n\n'.join(adv_list)


def get_photo(id_adv):
    '''Photos downloading from advertisment'''
    left = 0
    top = 52
    id_url = f"https://developers.ria.com/dom/info/{id_adv}?api_key={api_token}"
    response = requests.get(id_url).json()
    beautiful_photo_url = response['beautiful_url'].replace(
        f'-{id_adv}', '').replace('.html', '')
    try:
        photo_id_list = list(response['photos'].keys())
        photo_amount = len(photo_id_list)
        if len(photo_id_list) > 10:
            photo_amount = 8

        for i in range(0, photo_amount):  # photos downloading
            img_url = f"https://cdn.riastatic.com/photosnew/dom/photo/{beautiful_photo_url}__{photo_id_list[i]}xg.webp"
            p = requests.get(img_url)
            out = open(f"{beautiful_photo_url}__{i}raw.webp", "wb")
            out.write(p.content)
            out.close()

        for i in range(0, photo_amount):  # photos cropping
            im = Image.open(f"{beautiful_photo_url}__{i}raw.webp")
            right = im.size[0]
            bottom = im.size[1]
            im1 = im.crop((left, top, right, bottom))
            im1.save(f"photo_{i}cleaned.webp")
            os.remove(f"{beautiful_photo_url}__{i}raw.webp")

    except KeyError:
        pass


def get_media_names():
    '''Photos filenames reading'''
    fileExt = '.webp'
    files_list = [_ for _ in os.listdir() if _.endswith(fileExt)]

    return files_list


def remove_files():
    '''Removing photos'''
    files_list = get_media_names()
    for i in range(0, len(files_list)):
        os.remove(files_list[i])


def get_post_content(type):
    '''main post creation logic'''
    op_type = type
    id_adv = get_adv_id(op_type)
    text = ''
    try:
        text = get_info(id_adv)
        if text == 'recurring post' or text == 'bad advertisement':
            pass
        else:
            get_photo(id_adv)
            return text
    except UnidentifiedImageError:
        pass
