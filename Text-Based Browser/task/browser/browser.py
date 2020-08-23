import os
import sys
import requests
from bs4 import BeautifulSoup


class Browser:
    def __init__(self):
        self.dir = self.make_dir()
        self.history = []

    def make_dir(self):
        if len(sys.argv) > 1:
            dir_name = sys.argv[1] + '\\'
        else:
            dir_name = 'tmp\\'
        try:
            os.mkdir(dir_name)
        except FileExistsError:
            pass
        return dir_name

    def save_to_dir(self, file_name, text=''):
        try:
            file = open(self.dir + file_name, 'w', encoding='utf-8')
            file.write(text)
            file.close()
            return None
        except FileNotFoundError:
            return None

    def check_for_cache(self, file_name):
        try:
            file = open(self.dir + file_name, 'r', encoding='utf-8')
            cache = file.read()
            file.close()
            return cache
        except FileNotFoundError:
            return None

    def valid_url(self, url):
        if '.' in url:
            return True
        return False

    def short_url(self, url):
        short_url = url.replace('https://', '')
        short_url = short_url.replace('www.', '')
        short_url = short_url.replace('.', '_')
        return short_url

    def show(self, url):
        if self.valid_url(url):
            if not url.startswith('https://'):
                url = 'https://' + url
            r = requests.get(url)
            self.save_to_dir(self.short_url(url), self.soupify(r))
            self.history.append(self.short_url(url))
            return self.soupify(r)
        else:
            if url == 'exit':
                sys.exit()
            elif url == 'back':
                if self.history:
                    self.history.pop()
                    return self.show(self.history.pop())
                return None
            cache = self.check_for_cache(url)
            if cache:
                return cache
            else:
                return 'error, wrong url without dot'

    def soupify(self, request):
        soup = BeautifulSoup(request.content, 'html.parser')
        paragraphs = soup.find_all(['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li'])
        result = ''
        for p in paragraphs:
            result += p.text + '\n'
        return result

    def start(self):
        while True:
            print(safari.show(input()))


safari = Browser()
safari.start()
