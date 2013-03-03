from sys import argv
from urllib.request import urlopen
from lxml import etree
from lxml.html import fromstring


class Fanfic:
    def __init__(self, main_url):
        self.main = main_url
        self.author = ''
        self.title = ''
        self.genre = ''
        self.rate = ''
        self.chapters = 0
        self.updated = 0
        self.pages = []

    def parse_fanfic(self):
        html = urlopen(self.main).read().decode('utf8')
        page = fromstring(html)
        page.make_links_absolute(URL)
        #1. определить количество глав
        #2. определить параметры фика
        count = 0
        while count < page.chapters:
            chapter = self.parse_page(count)
            self.pages.append(chapter)
            count += 1

    def parse_page(self):
        html = urlopen(self.main + '/%d/' % count).read().decode('utf8')
        page = fromstring(html)
        page.make_links_absolute(URL)
        table = page.iter(tag="table")[0]
        #1. Извлечь из таблицы текст
        return text

    def create(type):
        #1. Создать из полученного фанфика документ определенного формата
        pass


def main():
    main_url = argv[1]
    fic = Fanfic(main_url)
    fic.parse_fanfic()
    fic.create(argv[2])
