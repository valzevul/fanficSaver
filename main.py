from sys import argv
from urllib.request import urlopen
from lxml import etree
from lxml.html import fromstring


URL = 'http://www.fanfiction.net/'
TEMPLATE = '''Author: %s
Title: %s
Chapters: %s'''
PARSING = 'Page №%d is parsing'


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
        tmp = page.xpath('//*[@id="gui_table1i"]/tbody/tr[1]/td/b')
        self.name = tmp[0].text
        tmp = page.xpath('//*[@id="gui_table1i"]/tbody/tr[1]/td/a[1]')
        self.author = tmp[0].text
        tmp = page.xpath('//*[@id="chap_select"]')
        for elem in tmp:
            for idx in elem:
                self.chapters += 1
        self.chapters //= 2
        print(self.chapters)
        count = 1
        while count <= self.chapters:
            print(PARSING % count)
            chapter = self.parse_page(count)
            self.pages.append(chapter)
            count += 1

    def parse_page(self, count):
        html = urlopen(self.main + '/%d/' % count).read().decode('utf8')
        page = fromstring(html)
        page.make_links_absolute(URL)
        text = []
        tmp = page.xpath('//*[@id="storytext"]')[0]
        for p in tmp.iter(tag="p"):
            if p.text == None:
                for i in p.iter(tag="i"):
                    text.append(str(i.text) + '\n')
            text.append(str(p.text) + '\n')
        return ''.join(text)

    def get_title(self):
        return TEMPLATE % (self.author, self.name, str(self.chapters))

    def create_txt(self):
        return self.get_title() + '\n' + '\n\n'.join(self.pages)

    def create_pdf(self):
        text = self.create_txt()
        #1. Generate pdf
        return pdf

    def get_creater(self, output_type="txt"):
        types = dict(txt=self.create_txt, pdf=self.create_pdf)
        return types[output_type]()


def main():
    main_url = argv[1]
    fic = Fanfic(main_url)
    fic.parse_fanfic()
    res = fic.get_creater(argv[2])
    if argv[2] == 'txt':
        fout = open('%s.txt' % fic.name.replace(' ', '_'), 'w')
        print(res, file=fout)
        fout.close()


if __name__ == '__main__':
    main()
