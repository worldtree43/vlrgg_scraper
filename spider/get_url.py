import requests
from bs4 import BeautifulSoup

def get_match_url(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        url_data = []

        for match_count in range(5, 40):
            url_tag1 = soup.select_one(
                f'#wrapper > div.col-container > div > div:nth-child({match_count}) > a.wf-module-item.match-item.mod-color.mod-bg-after-striped_purple.mod-first')
            status_tag1 = soup.select_one(
                f'#wrapper > div.col-container > div > div:nth-child({match_count}) > a.wf-module-item.match-item.mod-color.mod-bg-after-striped_purple.mod-first > div.match-item-eta > div > div.ml-status'
            )

            url_tag2 = soup.select_one(
                f'#wrapper > div.col-container > div > div:nth-child({match_count}) > a:nth-child(2)'
            )
            status_tag2 = soup.select_one(
                f'#wrapper > div.col-container > div > div:nth-child({match_count}) > a:nth-child(2) > div.match-item-eta > div > div.ml-status'
            )



            if url_tag1 and status_tag1:
                web_url1 = url_tag1.get('href')
                status = status_tag1.text.strip()
                url_data.append({"web_url": web_url1, "status": status})

            if url_tag2 and status_tag2:
                web_url2 = url_tag2.get('href')
                status = status_tag2.text.strip()
                url_data.append({"web_url": web_url2, "status": status})

    return url_data

def get_completed_url(url_data):

    completed_urls = [item['web_url'] for item in url_data if item['status'] == 'Completed']
    return completed_urls

def get_match_name(url_data):
    match_name = [item['web_url'].split('/')[-1] for item in url_data]
    return match_name

def get_match_no(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        enabled_maps = soup.select(
            f'#wrapper > div.col-container > div.col.mod-3 > div:nth-child(6) > div > div:nth-child(1) > div.vm-stats-gamesnav-container > div > div:not(.mod-disabled)'
        )
        match_no = []
        for enabled_map in enabled_maps:
            match_no.append(enabled_map.get('data-game-id'))

    return match_no

def splice_url(urls):
    base_url = 'https://www.vlr.gg'
    spliced_url = []
    for url in urls:
        spliced_url.append(base_url+url)
    return spliced_url

def splice_match_no(url, match_nos):
    spliced_match_url = []
    for match_no in match_nos:
        spliced_match_url.append(url+'/?game='+match_no+'&tab=overview')
    return spliced_match_url