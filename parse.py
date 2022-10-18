import sqlite3
import os

import requests
from dotenv import load_dotenv

load_dotenv()


api_token = os.getenv('TOKEN_RIA')


id_url = 'https://developers.ria.com/dom/info/22476055?api_key='


def get_info(id_url):
    response = requests.get(f'{id_url}{api_token}')
    properties = response.json().get('characteristics_values')
    print(type(properties))
    info = f"""Цена: {properties['234']}\n
            Метро: {response.get('metro_station_name')}\n
            Этаж: {properties['227']}\n
            Этажность: {properties['228']}\n
            Общая площадь: {properties['214']}\n
            Жилая площадь: {properties['216']}\n
            Площадь кухни: {properties['218']}\n
            Тип стен"""
    print(info)


get_info(id_url)
