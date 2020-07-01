from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import requests


class Model:
    def __init__(self):
        self._url = ''
        self._parser = ''
        self._path = ''
        self._api = ''

    @property
    def url(self) -> str: return self._url

    @url.setter
    def url(self, url): self._url = url

    @property
    def parser(self) -> str: return self._parser

    @parser.setter
    def parser(self, parser): self._parser = parser

    @property
    def path(self) -> str: return self._path

    @path.setter
    def path(self, path): self._path = path

    @property
    def api(self) -> str: return self._api

    @api.setter
    def api(self, api): self._api = api


class Service:
    def __init__(self):
        pass

    def bugs_music(self, payload):
        soup = BeautifulSoup(urlopen(payload.url), payload.parser)
        n_artist = 0
        n_title = 0
        for i in soup.find_all(name='p', attrs=({'class': 'title'})):
            n_title += 1
            print(str(n_title) + '위')
            print('노래제목:{}'.format(i.text))

    def naver_movie(self, payload):
        driver = webdriver.Chrome(payload.path)
        driver.get(payload.url)
        soup = BeautifulSoup(urlopen(payload.url), payload.parser)
        arr = [div.a.string for div in soup.find_all('div', attrs={'class': 'tit3'})]
        for i in arr:
            print(i)
        driver.close

    def old_car(self, payload):

        driver = webdriver.Chrome(payload.path)
        driver.get(payload.url)
        soup = BeautifulSoup(urlopen(payload.url), payload.parser)
        arr = [td.strong.string for td in soup.find_all('td', attrs={'class': 'prc_hs'})]
        for i in arr:
            print(i)
        driver.close


class Controller:
    def __init__(self):
        self.service = Service()
        self.model = Model()

    def bugs_music(self, url):
        self.model.url = url
        self.model.parser = 'lxml'
        self.service.bugs_music(self.model)

    def naver_movie(self, url):
        self.model.url = url
        self.model.parser ='html.parser'
        self.model.path = '/Users/kwakky/PycharmProjects/basic/basic/data/chromedriver'
        self.service.naver_movie(self.model)
        pass

    def old_car(self, url):
        self.model.url = url
        self.model.parser = 'html.parser'
        self.service.old_car(self.model)


def print_menu():
    print('0. 종료')
    print('1. 벅스뮤직')
    print('2. 네이버영화')
    print('3. 중고차')
    return input('Menu\n')

    # html.parser


app = Controller()

while 1:
    menu = print_menu()
    if menu == '0':
        break
    if menu == '1':
        app.bugs_music('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20200625&charthour=14')
    if menu == '2':
        app.naver_movie('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
    if menu == '3':
        app.old_car('http://www.encar.com/dc/dc_carsearchlist.do?carType=kor#!%7B%22action%22%3A%22(And.Hidden.N._.CarType.Y._.FuelType.%EC%A0%84%EA%B8%B0.)%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A20%7D')
        pass
