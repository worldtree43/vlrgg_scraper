# Vlrgg_scraper(Updating)
a scraper for [vlr.gg](https://www.vlr.gg/), now scraping Valorant Champions 2024

## Introduction

## Installation
### Source
```
git clone https://github.com/worldtree43/vlrgg_scraper.git
```
### Usage
```
python3 main_menu.py
```

## Structure
### app

User Interface implemented by [tkinter](https://docs.python.org/3/library/tkinter.html).

- `main_menu.py`: Display the main window of app, consisting list of matches played
- `match_ui.py`: Display the match results

### spider

Scraper programs implemented mainly by [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/). Program already run, results see `/data` and `/img` folder.

- `get_img.py`: Scraping team image and hero image, putting the image under `/img/hero_img` and `/img/team_img`
- `get_match_data.py`: Scraping match data from match url
- `get_url.py`: getting detailed match url from home page of match event
- `save.py`: saving the data to csv
- `main.py`: main program of spider module

### analysis

Some analysis of the data scraped.

- `hero_classifier.py`: Basic classifer to judge if two players are in contraposition matchup