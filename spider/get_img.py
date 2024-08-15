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
team_src = []

img_elements = soup.find_all('img')

for img in img_elements:
    img_src = img.get('src')

    # 检查是否以 "/img/vlr/game/agents/" 开头
    if img_src and img_src.startswith('/img/vlr/game/agents/'):
        hero_src.add(img_src)
    if img_src and img_src.startswith('//owcdn.net/img') and img_src != '//owcdn.net/img/63067806d167d.png':
        if img_src not in team_src:
            team_src.append(img_src)

# print(team_src)

for img in hero_src:
    # print(img)
    hero_full_src = 'https://www.vlr.gg'+img
    img_response = requests.get(hero_full_src)
    img_name = img.split('/')[-1]
    print(img_name)
    img_path = os.path.join('../img/hero_img',f'{img_name}')
    with open(img_path, 'wb') as file:
        file.write(img_response.content)

team_names = [
    "EDward Gaming",
    "KRÜ Esports",
    "Sentinels",
    "Trace Esports",
    "FNATIC",
    "DRX",
    "Gen.G",
    "LEVIATÁN",
    "Team Vitality",
    "Paper Rex",
    "Team Heretics",
    "FunPlus Phoenix",
    "G2 Esports",
    "Bilibili Gaming",
    "Talon Esports",
    "FUT Esports"
]

team_no = 0

for img in team_src:
    team_full_src = 'https:'+img
    img_response = requests.get(url = team_full_src, headers = headers)
    sanitized_team_name = team_names[team_no].replace(' ', '_')
    img_path = os.path.join('../img/team_img', f'{sanitized_team_name}.png')
    # os.makedirs(os.path.dirname(img_path), exist_ok=True)
    with open(img_path, 'wb') as file:
        file.write(img_response.content)
    team_no +=1


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

# for team_number in range(2,39):
#     img_element = soup.select_one(
#         f'#wrapper > div.col-container > div > div.pr-matrix-container > div:nth-child(1) > div > table > tbody > tr:nth-child({team_number}) > td:nth-child(1) > a > span'
#     )
#     print(img_element.text.strip())
