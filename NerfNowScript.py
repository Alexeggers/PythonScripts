import os

from requests import get
from time import sleep
from bs4 import BeautifulSoup

nerf_now_url = "http://www.nerfnow.com/comic/"
dir_name = "NerfNowComics"

# First comic to be downloaded. Do not go lower than 4,
# it is the first for some reason.
start = 10

# Last comic to be downloaded
finish = 20

# Time in seconds
delay = 1

def make_soup(url):
    html = get(url).text
    return BeautifulSoup(html, "html.parser")

def get_image(number):
    soup = make_soup(nerf_now_url + number)
    found_div = soup.find('div', attrs = {'id': 'comic'})
    image_element = found_div.find('img')
    image_url = image_element['src']
    image_content = get(image_url).content
    with open(number + ".jpg", "wb") as handler:
        handler.write(image_content)
    print(image_url)

def prep_work():
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    os.chdir(dir_name)

if __name__ == "__main__":
    comic_numbers = list(range(start, finish + 1))
    prep_work()
    for number in comic_numbers:
        get_image(str(number))
        sleep(delay)
        
