import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TELEGRAM_TOKEN = ("5097104342:AAEuKw3O5TekOID2qabNOj2y-SOmTOzQX9c")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="https://t.me/tech95lkofficial"),
                               InlineKeyboardButton("No", callback_data="https://t.me/tech95lkofficial"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "https://t.me/tech95lkofficial":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "https://t.me/tech95lkofficial":
        bot.answer_callback_query(call.id, "Answer is No")

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())

bot.polling()
