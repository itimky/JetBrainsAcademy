import os
import sys

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


class Browser:
    def __init__(self):
        self.dir = self.make_dir()
        self.history = []

    def make_dir(self):
        if len(sys.argv) > 1:
            dir_name = sys.argv[1] + '\\'
            try:
                os.mkdir(dir_name)
            except FileExistsError:
                pass
        else:
            dir_name = ''
        return dir_name

    def save_to_dir(self, file_name, text=''):
        try:
            file = open(self.dir + file_name, 'w')
            file.write(text)
            file.close()
            return None
        except FileNotFoundError:
            return None

    def check_for_cache(self, file_name):
        try:
            file = open(self.dir + file_name, 'r')
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
        return url.split('.')[0]

    def show(self, url):
        if self.valid_url(url):
            if url == 'bloomberg.com':
                self.save_to_dir(self.short_url(url), bloomberg_com)
                self.history.append(self.short_url(url))
                return bloomberg_com
            elif url == 'nytimes.com':
                self.save_to_dir(self.short_url(url), nytimes_com)
                self.history.append(self.short_url(url))
                return nytimes_com
            else:
                return 'error, wrong url'
        else:
            if url == 'exit':
                exit()
            elif url == 'back':
                if self.history:
                    self.history.pop()
                    return self.show(self.history.pop())
                return None
            cache = self.check_for_cache(self.short_url(url))
            if cache:
                return cache
            else:
                return 'error, wrong url without dot'


safari = Browser()
while True:
    print(safari.show(input()))
