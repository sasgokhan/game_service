import requests
import json
from bs4 import BeautifulSoup


class Parser:
    #constructor of the Parser class to initialize the URL and heders
    def __init__(self):

        self.URL = 'https://www.metacritic.com/game/playstation-4'
        self.header = {
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}


    def parse_url(self):
        page = requests.get(self.URL, headers=self.header)
        soup = BeautifulSoup(page.content, 'html.parser')
        games_info = soup.findAll('td', {"class":"clamp-summary-wrap"})
        return games_info


    def store_games_info(self):
        data = {'game': []}
        games_info = self.parse_url()
        for info in games_info:
            title = info.find('h3')
            score = info.find('div', {"class": "metascore_w large game positive"})
            description = info.find('div', {"class": "summary"})
            data['game'].append({
                'title': title.text.strip(),
                'score': score.text,
                'description': description.text.strip()
            })

        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)

# create an Parser object
game_parser = Parser()
