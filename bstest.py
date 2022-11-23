import requests
from bs4 import BeautifulSoup
url='http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0059&date=20211224'
html= requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
a = soup.find_all('.on')
print(a) 