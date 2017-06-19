import os
import urllib

from time import sleep
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve

nerf_now_url = "http://www.nerfnow.com/comic/"

# First comic to be downloaded. Do not go lower than 4,
# it is the first for some reason.
start = 4

# Last comic to be downloaded
finish = 4

# Time in seconds
delay = 5

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "html.parser")

def get_image(number):
    soup = make_soup(nerf_now_url + number)
    found_div = soup.find('div', attrs = {'id': 'comic'})
    image_element = found_div.find('img')
    image_url = image_element['src']
    urlretrieve(image_url, number + ".jpg")

def prep_work():
    dir_name = "NerfNowComics"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    os.chdir(dir_name)
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

if __name__ == "__main__":
    comic_numbers = list(range(start, finish + 1))
    prep_work()
    for number in comic_numbers:
        get_image(str(number))
        sleep(delay)
        
