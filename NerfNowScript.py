import os
import urllib

from time import sleep
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve

nerf_now_url = "http://www.nerfnow.com/comic/"

# First comic to be downloaded
start = 10

# Upper border of comics, this one isn't downloaded
finish = 12

# Time in seconds
delay = 5

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "html.parser")

def get_image(number):
    soup = make_soup(nerf_now_url + number)
    found_div = soup.find('div', attrs = {'id': 'comic'})
    found_div = found_div.find('img')
    image_url = found_div['src']
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
    comic_numbers = list(range(start, finish))
    prep_work()
    for number in comic_numbers:
        get_image(str(number))
        sleep(delay)
        
