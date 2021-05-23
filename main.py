# -*- coding: utf-8 -*-
import config
import telebot
import datetime
import pymorphy2
from collections import Counter
import time
from config import token
# import re
# from telebot import types

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def delete_spam(message):
    # using dictinary to find spam
    morph = pymorphy2.MorphAnalyzer(lang="ru")
    msg = message.text.split(' ')
    print(msg)
    cnt = 0
    cnt2 = 0
    for i in msg:
        word = morph.parse(i)[0]
        print(word)
        tag_short = str(word.tag)[:4]
        type_dict = str(word).replace("methods_stack=((", "").replace(",", "").replace("()", "").split()[5]
        print(tag_short)
        if tag_short == "NUMB" or len(
                i) < 3 or tag_short == "LATN" or tag_short == "UNKN" or tag_short == "PREP" or tag_short == "ADJS" or tag_short == "PRCL" or tag_short == "NPRO" or tag_short == "ф" or type_dict == "FakeDictionary":
            cnt += 1
        else:
            cnt2 += 1
    print(cnt, cnt2)
    if cnt > cnt2:
        bot.delete_message(message.chat.id, message.message_id)



@bot.message_handler(content_types=['document'])
def delete_links_document(message):
    f = open('log.txt', 'a')
    f.write(str(datetime.datetime.now()) + ' user id:' + str(
        message.from_user.id) + ' del message content_types=[document] ' + '\n')
    f.close()
    bot.delete_message(message.chat.id, message.message_id)

"""
This code will delete audio:

@bot.message_handler(content_types=['audio'])
def delete_links_audio(message):
    if (str(message.from_user.id) not in user0):
         f = open('log.txt', 'a')
         f.write(str(datetime.datetime.now()) + ' user id:' + str(
             message.from_user.id) + ' del message content_types=[audio] ' + '\n')
         f.close()
         bot.delete_message(message.chat.id, message.message_id)
"""

@bot.message_handler(content_types=['video'])
def delete_links_video(message):
    f = open('log.txt', 'a')
    f.write(str(datetime.datetime.now()) + ' user id:' + str(
        message.from_user.id) + ' del message content_types=[video] ' + '\n')
    f.close()
    bot.delete_message(message.chat.id, message.message_id)

"""
This code will delete stickers
@bot.message_handler(content_types=['sticker'])
def delete_links_sticker(message):
     if (str(message.from_user.id) not in user0):
         f = open('log.txt', 'a')
         f.write(str(datetime.datetime.now()) + ' user id:' + str(
             message.from_user.id) + ' del message  content_types=[sticker] ' + '\n')
         f.close()
         bot.delete_message(message.chat.id, message.message_id)
"""

@bot.message_handler(content_types=['location'])
def delete_links_location(message):
    f = open('log.txt', 'a')
    f.write(str(datetime.datetime.now()) + ' user id:' + str(
        message.from_user.id) + ' del message content_types=[location] ' + '\n')
    f.close()
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['contact'])
def delete_links_contact(message):
    f = open('log.txt', 'a')
    f.write(str(datetime.datetime.now()) + ' user id:' + str(
        message.from_user.id) + ' del message content_types=[contact] ' + '\n')
    f.close()
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['caption'])
def delete_links_caption(message):
    f = open('log.txt', 'a')
    f.write(str(datetime.datetime.now()) + ' user id:' + str(
        message.from_user.id) + ' del message content_types=[caption] ' + '\n')
    f.close()
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['venue'])
def delete_links_venue(message):
    f = open('log.txt', 'a')
    f.write(str(datetime.datetime.now()) + ' user id:' + str(
        message.from_user.id) + ' del message content_types=[venue] ' + '\n')
    f.close()
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['photo'])
def delete_links_photo(message):
    f = open('log.txt', 'a')
    f.write(str(datetime.datetime.now()) + ' user id:' + str(
        message.from_user.id) + ' del message content_types=[photo] ' + '\n')
    f.close()
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['left_chat_member'])
def delete_links_left_chat_member(message):
    f = open('log.txt', 'a')
    f.write(str(datetime.datetime.now()) + ' user id:' + str(
        message.from_user.id) + ' del message content_types=[left_chat_member] ' + '\n')
    f.close()
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['new_chat_members'])
def delete_links_new_chat_members(message):
    f = open('log.txt', 'a')
    f.write(str(datetime.datetime.now()) + ' user id:' + str(
        message.from_user.id) + ' del message content_types=[new_chat_members] ' + '\n')
    f.close()
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(func=lambda message: message.entities is not None)
def delete_links(message):
    j = 0
    for entity in message.entities:  # Пройдёмся по всем entities в поисках ссылок
        j = j + 1
        if (j == 1):
            if (entity.type in ["url"]):
                f = open('log.txt', 'a')
                f.write(str(datetime.datetime.now()) + ' user id:' + str(
                    message.from_user.id) + " del message type == 'url'" + '\n')
                f.close()
                bot.delete_message(message.chat.id, message.message_id)
            if (entity.type in ["text_link"]):
                f = open('log.txt', 'a')
                f.write(str(datetime.datetime.now()) + ' user id:' + str(
                    message.from_user.id) + " del message type == 'text_link'" + '\n')
                f.close()
                bot.delete_message(message.chat.id, message.message_id)
            if (entity.type in ["pre"]):
                f = open('log.txt', 'a')
                f.write(str(datetime.datetime.now()) + ' user id:' + str(
                    message.from_user.id) + " del message type == 'pre'" + '\n')
                f.close()
                bot.delete_message(message.chat.id, message.message_id)
            if entity.type in ["hashtag"]:
                f = open('log.txt', 'a')
                f.write(str(datetime.datetime.now()) + ' user id:' + str(
                    message.from_user.id) + " del message type == 'hashtag'" + '\n')
                f.close()
                bot.delete_message(message.chat.id, message.message_id)
            if entity.type in ["email"]:
                f = open('log.txt', 'a')
                f.write(str(datetime.datetime.now()) + ' user id:' + str(
                    message.from_user.id) + " del message type == 'email'" + '\n')
                f.close()
                bot.delete_message(message.chat.id, message.message_id)
            if entity.type in ["code"]:
                f = open('log.txt', 'a')
                f.write(str(datetime.datetime.now()) + ' user id:' + str(
                    message.from_user.id) + " del message type == 'code'" + '\n')
                f.close()
            if entity.type in ["bold"]:
                f = open('log.txt', 'a')
                f.write(str(datetime.datetime.now()) + ' user id:' + str(
                    message.from_user.id) + " del message type == 'bold'" + '\n')
                f.close()
                bot.delete_message(message.chat.id, message.message_id)
            if entity.type in ["mention"]:
                f = open('log.txt', 'a')
                f.write(str(datetime.datetime.now()) + ' user id:' + str(
                    message.from_user.id) + " del message type == 'mention'" + '\n')
                f.close()
                bot.delete_message(message.chat.id, message.message_id)
            if (entity.type in ["italic"]):
                f = open('log.txt', 'a')
                f.write(str(datetime.datetime.now()) + ' user id:' + str(
                    message.from_user.id) + " del message type == 'italic'" + '\n')
                f.close()
                bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if message.forward_from_chat:
        f = open('log.txt', 'a')
        f.write(str(datetime.datetime.now()) + ' user id:' + str(
            message.from_user.id) + ' del message with buttons ' + '\n')
        f.close()
        bot.delete_message(message.chat.id, message.message_id)
    else:
        for e in message.json:
            if e in 'reply_markup':
                f = open('log.txt', 'a')
                f.write(str(datetime.datetime.now()) + ' user id:' + str(
                    message.from_user.id) + " del message json, del message 'reply_markup'" + '\n')
                f.close()
                bot.delete_message(message.chat.id, message.message_id)


if __name__ == '__main__':
    bot.polling(none_stop=True)

f = open('log.txt', 'a')
f.close()

if __name__ == '__main__':
    bot.polling(none_stop=True)

    
