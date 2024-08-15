import requests
from lxml import etree
import openpyxl

url = 'https://www.vlr.gg/event/agents/2097/valorant-champions-2024'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

response = requests.get(url=url,headers=headers)
e = etree.HTML(response.text)

team_name = e.xpath('//*[@id="wrapper"]/div[2]/div/div[3]/div[1]/div/table/tbody/tr[39]/td[1]/a/span/text()')

print(team_name)