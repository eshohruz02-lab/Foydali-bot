 
import os
import telebot

TOKEN = "8786803334:AAF9KtzQMBx5vGnDeFy6wG6Mfr7Uz6gOBz"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men sizning 24/7 ishlaydigan botingizman!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()

