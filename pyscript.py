import requests
from bs4 import BeautifulSoup
import re
import urllib

for number in range(1, 1700):
    page = requests.get('http://xkcd.com/' + str(number))
    #print page.status_code
    html_page = page.text
    soup = BeautifulSoup(html_page, 'html.parser')

    for url in soup.find_all('img', src=re.compile('imgs.xkcd.com/comics')):
        #print url['src']
        image_url = "http:" + url['src']
        print image_url
        urllib.urlretrieve(image_url,image_url.split('/')[-1])