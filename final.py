import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token = 'input token')
url='input url'

def mov_function():
    html= requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    date_list = soup.select('#slider > div > ul > li > div > a > strong')
    for i in date_list:
        dates = i.get_text()
        print(dates)
        if "24" in dates:
            bot.sendMessage(chat_id = '5065719186', text = "24일 예매가 시작되었습니다.")

sched = BlockingScheduler()
sched.add_job(mov_function, 'interval', seconds=30)
sched.start()
