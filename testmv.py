import requests
from bs4 import BeautifulSoup
url='http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0059&date=20211224'
html= requests.get(url)
#print(html.text)
soup = BeautifulSoup(html.text, 'html.parser')
date_list = soup.select('#slider > div > ul > li > div > a > strong')
for i in date_list:
    dates = i.get_text()
    print(dates)
    if "24" in dates:
        print('yes')