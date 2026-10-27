import telebot
import os
TOKEN = os.getenv("9072572436:AAEgp75PS3eXbtWJcoyo6mj1ZU_nvoJM7Sc")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "اهلا بيك في بوت دهب 🌊 البوت شغال 24 ساعة!")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"انت قولت: {message.text}")

bot.infinity_polling()
