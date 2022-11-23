import requests
from bs4 import BeautifulSoup
url='http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0059&date=20211224'
html= requests.get(url)
#print(html.text)
def movinf_function():
    soup = BeautifulSoup(html.text, 'html.parser')
    title_list = soup.select('div.info-movie > a > strong')
    for i in title_list:
        print(i.text.strip())
        if "뮤지컬" in i:
            print('true')

movinf_function()