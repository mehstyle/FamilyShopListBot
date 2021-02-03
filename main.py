import telebot
import sqlite3

try:
    connect = sqlite3.connect('shoppinglists.bd')
    bd_cursor_obj = connect.cursor()
except FileNotFoundError:
    connect.close()


try:
    file = open("token.txt", encoding='utf-8')
    token = file.read().strip()
finally:
    file.close()

bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id, "Привет, друг! Я телеграм-бот, который помогает сохранять список покупок!")
    if message.chat.type == "group":
        bot.send_message(message.chat.id, "Приветствую вас, друзья! Я телеграм-бот, который помогает сохранять список покупок!")


bot.polling()
