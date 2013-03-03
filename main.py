from sys import argv
from urllib.request import urlopen
from lxml import etree
from lxml.html import fromstring


class Fanfic:
    def __init__(self, main_url):
        self.main = main_url
        self.author = ''
        self.name = ''
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
        tree = etree.parse(page)
        tmp = tree.xpath('//*[@id="gui_table1i"]/tbody/tr[1]/td/b')
        self.name = tmp.text
        tmp = tree.xpath('//*[@id="gui_table1i"]/tbody/tr[1]/td/a[1]')
        self.author = tmp.text
        tmp = tree.xpath('//*[@id="chap_select"]')
        self.chapters = len(tmp)
        count = 0
        while count < page.chapters:
            chapter = self.parse_page(count)
            self.pages.append(chapter)
            count += 1

    def parse_page(self):
        html = urlopen(self.main + '/%d/' % count).read().decode('utf8')
        page = fromstring(html)
        page.make_links_absolute(URL)
        tree = etree.parse(page)
        text = ''
        tmp = tree.xpath('//*[@id="storytext"]')
        for p in tmp.iter(tag="p"):
            text.append(p.text + '\n')
        return text

    def create_txt(self):
        return self.get_title() + '\n' + '\n\n'.join(self.pages)

    def create_pdf(self):
        text = self.create_txt()
        #1. Сгенерировать pdf
        return pdf

    def get_creater(self, output_type="txt"):
        types = dict(txt=create_txt, pdf=create_pdf)
        return self.types[output_type]()


def main():
    main_url = argv[1]
    fic = Fanfic(main_url)
    fic.parse_fanfic()
    res = fic.get_creater(argv[2])
    if argv[2] == 'txt':
        #1. Сохранить
        pass


if __name__ == '__main__':
    main()
