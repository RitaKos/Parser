from bs4 import BeautifulSoup
import urllib.request


class Parser:
    raw_html = ''
    html = ''
    results = []

    def __init__(self,url, path):
        self.url = url
        self.path = path

    def get_html(self):
        request = urllib.request.urlopen(self.url)
        self.raw_html = request.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news = self.html.find_all('td', class_='stat-results__link')
        for item in news:
            web = 'head_of_link'
            space = '\n'
            play = item.a.get('title')
            if play:
                link = web + item.a.get('href')
                self.results.append({
                    'play_name': play,
                    'link': link
                }
                )

    def save_in_file(self):
        with open(self.path, mode='w', encoding='UTF-8') as file:
            for match in self.results:
                file.write(f'{match["play_name"]}\nПодробнее о матче: {match["link"]}\n\n')
            file.close()
            file = open(self.path, mode='r', encoding='UTF-8')
            context = file.read()
            file.close()

    def run(self):
        self.get_html()
        self.parsing()
        self.save_in_file()
