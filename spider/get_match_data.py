import requests
from bs4 import BeautifulSoup

def get_data(url, map_no):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []

    if map_no == 2:
        for team_no in [1, 2]:
            for player_no in range(1, 6):
                player_name = soup.select_one(
                    f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div.vm-stats-game.mod-active > div:nth-child(2) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-player > div > a > div.text-of').text.strip()
                team_name = soup.select_one(
                    f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div.vm-stats-game.mod-active > div:nth-child(2) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-player > div > a > div.ge-text-light').text.strip()
                spans = soup.select(
                    f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div.vm-stats-game.mod-active > div:nth-child(2) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-agents > div > span')
                hero_count = len(spans)
                hero_name = []
                for j, span in enumerate(spans, start=1):
                    hero_name.append(span.find('img').get('title'))

                rating = float(soup.select_one(
                    f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div.vm-stats-game.mod-active > div:nth-child(2) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td:nth-child(3) > span > span.side.mod-side.mod-both').text.strip())
                acs = int(soup.select_one(
                    f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div.vm-stats-game.mod-active > div:nth-child(2) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td:nth-child(4) > span > span.side.mod-side.mod-both').text.strip())
                kill = int(soup.select_one(
                    f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div.vm-stats-game.mod-active > div:nth-child(2) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-stat.mod-vlr-kills > span > span.side.mod-side.mod-both').text.strip())
                death = int(soup.select_one(
                    f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div.vm-stats-game.mod-active > div:nth-child(2) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-stat.mod-vlr-deaths > span > span:nth-child(2) > span.side.mod-both').text.strip())
                assist = int(soup.select_one(
                    f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div.vm-stats-game.mod-active > div:nth-child(2) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-stat.mod-vlr-assists > span > span.side.mod-both').text.strip())
                kda = f'{kill}/{death}/{assist}'
                pm = kill - death

                kast = soup.select_one(
                    f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div.vm-stats-game.mod-active > div:nth-child(2) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td:nth-child(9) > span > span.side.mod-both').text.strip()
                adr = int(soup.select_one(
                    f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div.vm-stats-game.mod-active > div:nth-child(2) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td:nth-child(10) > span > span.side.mod-both').text.strip())
                hs = soup.select_one(
                    f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div.vm-stats-game.mod-active > div:nth-child(2) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td:nth-child(11) > span > span.side.mod-both').text.strip()

                fk = int(soup.select_one(
                    f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div.vm-stats-game.mod-active > div:nth-child(2) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-stat.mod-fb > span > span.side.mod-both').text.strip())
                fd = int(soup.select_one(
                    f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div.vm-stats-game.mod-active > div:nth-child(2) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-stat.mod-fd > span > span.side.mod-both').text.strip())
                fpm = fk - fd

                data.append(['all',player_name,team_name, hero_name, rating, acs, kda, pm, kast, adr, hs, fk, fd, fpm])

    else:
        map_element = soup.select_one(
            f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div:nth-child({map_no}) > div.vm-stats-game-header > div.map > div:nth-child(1)'
        )
        map_name = map_element.get_text(separator=' ', strip=True).split(' ')[0]
        for team_no in [1,2]:
            for player_no in range(1,6):
                player_name = soup.select_one(
                        f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div:nth-child({map_no}) > div:nth-child(4) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-player > div > a > div.text-of').text.strip()
                team_name = soup.select_one(
                        f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div:nth-child({map_no}) > div:nth-child(4) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-player > div > a > div.ge-text-light').text.strip()
                spans = soup.select(
                    f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div:nth-child({map_no}) > div:nth-child(4) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-agents > div > span')
                hero_count = len(spans)
                hero_name = []
                for j, span in enumerate(spans, start=1):
                    hero_name.append(span.find('img').get('title'))

                rating = float(soup.select_one(f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div:nth-child({map_no}) > div:nth-child(4) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td:nth-child(3) > span > span.side.mod-side.mod-both').text.strip())
                acs = int(soup.select_one(f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div:nth-child({map_no}) > div:nth-child(4) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td:nth-child(4) > span > span.side.mod-side.mod-both').text.strip())
                kill = int(soup.select_one(f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div:nth-child({map_no}) > div:nth-child(4) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-stat.mod-vlr-kills > span > span.side.mod-side.mod-both').text.strip())
                death = int(soup.select_one(f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div:nth-child({map_no}) > div:nth-child(4) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-stat.mod-vlr-deaths > span > span:nth-child(2) > span.side.mod-both').text.strip())
                assist = int(soup.select_one(f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div:nth-child({map_no}) > div:nth-child(4) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-stat.mod-vlr-assists > span > span.side.mod-both').text.strip())
                kda = f'{kill} / {death} / {assist}'
                pm = kill - death

                kast = soup.select_one(f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div:nth-child({map_no}) > div:nth-child(4) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td:nth-child(9) > span > span.side.mod-both').text.strip()
                adr = int(soup.select_one(f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div:nth-child({map_no}) > div:nth-child(4) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td:nth-child(10) > span > span.side.mod-both').text.strip())
                hs = soup.select_one(f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div:nth-child({map_no}) > div:nth-child(4) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td:nth-child(11) > span > span.side.mod-both').text.strip()

                fk = int(soup.select_one(f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div:nth-child({map_no}) > div:nth-child(4) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-stat.mod-fb > span > span.side.mod-both').text.strip())
                fd = int(soup.select_one(f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div.vm-stats-container > div:nth-child({map_no}) > div:nth-child(4) > div:nth-child({team_no}) > table > tbody > tr:nth-child({player_no}) > td.mod-stat.mod-fd > span > span.side.mod-both').text.strip())
                fpm = fk - fd
                data.append([map_name,player_name,team_name, hero_name, rating, acs, kda, pm, kast, adr, hs, fk, fd, fpm])

    return data

def coresponding_map_no(match_no):
    base_map_no = [2, 1, 3, 4, 5, 6]
    map_no = []
    l = len(match_no)
    for i in range(l):
        map_no.append(base_map_no[i])
    return map_no