import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token = 'input token')
url='http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0059&date=20211224'

#print(html.text)
def movinf_function():
    html= requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    title_list = soup.select('div.info-movie > a > strong')
    for i in title_list:
        text = i.text 
        finder = text.find('스파이더맨')
        print(text.strip())
        #print(finder)
        if finder > -1:
            bot.sendMessage(chat_id = '5065719186', text = "24일 스파이더맨 예매가 시작되었습니다.")
        #else: 
            #print('no')

sched = BlockingScheduler()
sched.add_job(movinf_function, 'interval', seconds=60)
sched.start()