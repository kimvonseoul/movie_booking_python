import telegram
bot = telegram.Bot(token = 'input token')
for i in bot.getUpdates():
    print(i.message)
bot.sendMessage(chat_id = 'input id', text = "test.")