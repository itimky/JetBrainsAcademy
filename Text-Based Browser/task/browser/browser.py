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


def save_to_dir(directory, file_name, text):
    try:
        file = open(directory + '\\' + file_name, 'w')
        file.write(text)
        file.close()
        return None
    except FileNotFoundError:
        return None


def check_for_cache(directory, file_name):
    try:
        file = open(directory + '\\' + file_name, 'r')
        cache = file.read()
        file.close()
        return cache
    except FileNotFoundError:
        return None


dir_name = sys.argv[1]

if dir_name:
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass

while True:
    url = input()
    if url.find('.') != -1:
        if url == 'bloomberg.com':
            print(bloomberg_com)
            if dir_name:
                save_to_dir(dir_name, url.split('.')[0], bloomberg_com)
        elif url == 'nytimes.com':
            print(nytimes_com)
            if dir_name:
                save_to_dir(dir_name, url.split('.')[0], nytimes_com)
        else:
            print('error, wrong url')
    elif url == 'exit':
        break
    else:
        cache = check_for_cache(dir_name, url.split('.')[0])
        if cache:
            print(cache)
        else:
            print('error wrong url without dot')
