import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.vlr.gg/event/agents/2097/valorant-champions-2024'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

hero_src = set()

img_elements = soup.find_all('img')
for img in img_elements:
    img_src = img.get('src')

    # 检查是否以 "/img/vlr/game/agents/" 开头
    if img_src and img_src.startswith('/img/vlr/game/agents/'):
        hero_src.add(img_src)

for img in hero_src:
    # print(img)
    hero_full_src = 'https://www.vlr.gg'+img
    img_response = requests.get(hero_full_src)
    img_name = img.split('/')[-1]
    img_path = os.path.join('.../img/hero_img',f'{img_name}')
    with open(img_path, 'wb') as file:
        file.write(img_response.content)


# for hero_number in range(3,27):
#     img_element = soup.select_one(
#         f'#wrapper > div.col-container > div > div.pr-matrix-container > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > th:nth-child({hero_number})'
#     ).find('src')
#     print(img_element)
#
#     if img_element:
#         img_src = 'https://www.vlr.gg' + img_element['src']
#         img_response = requests.get(img_src)
#         img_name = img_element['src'].split('/')[-1]
#         img_path = os.path.join('../img',f'{img_name}')
#         with open(img_path, 'wb') as file:
#             file.write(img_response.content)
