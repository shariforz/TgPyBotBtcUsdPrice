import requests
from datetime import datetime
import telebot
from auth_data import token

""" def get_data():
    req = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    response = req.json()
    print(response)
    sell_price = response["price"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nBTC USD price: {sell_price}") """


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(
            message.chat.id, 
            "Hello there! Type the 'price' to find out the BTC exchange price!")

    
    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
                response = req.json()
                sell_price = response["price"]
                bot.send_message(
                    message.chat.id, 
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nBTC USD price: {sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Damn... Something went wrong..."
                )
        else:
            bot.send_message(message.chat.id, "Whaaat??? Check the command dude!")

    
    bot.polling()


if __name__ == '__main__':
    #get_data()
    telegram_bot(token)