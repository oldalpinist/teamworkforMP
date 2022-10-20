import requests
from bs4 import BeautifulSoup
import json
import csv

URL = "https://egrul.itsoft.ru/%s.xml"
PREFIX = "https://egrul.itsoft.ru/EGRUL_406/01.01.2022_FULL/"

def get_html(url, params=""):
    r = requests.get(url=url, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("СвЮЛ", "СвНаимЮЛ")
    contragents = []
    for item in items:
        contragents.append(
            {

            }
       )



