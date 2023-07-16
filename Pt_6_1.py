import requests
from bs4 import BeautifulSoup
from loguru import logger

while True:
    try:
        link = input("Введите ссылку на исполнителя на Яндекс Музыке: ")
        URL = requests.get(link)
        break
    except requests.exceptions.MissingSchema:
        logger.error("Incorrect URL! Follow the example\nExample: https://music.yandex.ru/artist/XXXXXX")

    except requests.exceptions.InvalidSchema:
        logger.error("Use the correct scheme in the request URL.\nExample: https://music.yandex.ru/artist/XXXXXX")

    except requests.exceptions.RequestException as e:
        logger.error(e)

tracks_URL = link + "/tracks"
page = requests.get(tracks_URL)
soup = BeautifulSoup(page.text, "lxml")
artist = soup.find("h1", class_="page-artist__title typo-h1 typo-h1_big").text
tracks_info = soup.find_all("a", class_="d-track__title deco-link deco-link_stronger")
print(f"10 самых популярных песен исполнителя - {artist}\n")
for i in range(10):
    print(i + 1, "-", tracks_info[i].text.strip())
