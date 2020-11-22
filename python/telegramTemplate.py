from telegram.ext import Updater
# import logging
from telegram.ext import CommandHandler
import os
import requests
from bs4 import BeautifulSoup

updater = Updater(token='token', use_context=True)

dispatcher = updater.dispatcher
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                      level=logging.INFO)


def message(update, context):
    ip = os.popen("curl https://ipecho.net/plain")
    print("ip")
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=ip.read())
    print("ip bitti")

def video(update, context):
    context.bot.sendVideo(chat_id=update.effective_chat.id, video=open('/Users/furkan/Documents/cutted.mp4', 'rb'), timeout=20000)
    print("video bitti")


def photo(update, context):
    context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=open('/Users/furkan/Desktop/white.png', 'rb'))
    print("photo bitti")


def document(update, context):
    context.bot.sendDocument(chat_id=update.effective_chat.id, document=open('/Users/furkan/Desktop/Oblivion.2013.1080p.BluRay.x264.YIFY.srt', 'rb'))
    print("document bitti")

def location(update, context):
    context.bot.sendLocation(chat_id=update.effective_chat.id, latitude=41.008240, longitude=28.978359)
    print("location bitti")


def sendContact(update, context):
    context.bot.sendContact(chat_id=update.effective_chat.id, phone_number="+90 539 565 1337", first_name="furkan")
    print("sendContact bitti")

def isitdown(update, context):
    downOrNot = requests.get("https://www.isitdownrightnow.com/")
    print(downOrNot.text)

# def setChatPhoto(update, context):
#     context.bot.setChatPhoto(chat_id=update.effective_chat.id, photo=open('/Users/furkan/Desktop/white.png', 'rb'))

# def setChatDescription(update, context):
#     context.bot.setChatDescription(chat_id=update.effective_chat.id, description="testing")

# def deleteMessage(update, context):
#     context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=message.message_id[-1])

"""
send document according to username =
    if(update.message.from_user.username == "FurkanKsgn"):

"""
message_handler = CommandHandler('message', message)
dispatcher.add_handler(message_handler)
updater.start_polling()

video_handler = CommandHandler('video', video)
dispatcher.add_handler(video_handler)
updater.start_polling()

photo_handler = CommandHandler('photo', photo)
dispatcher.add_handler(photo_handler)
updater.start_polling()

document_handler = CommandHandler('document', document)
dispatcher.add_handler(document_handler)
updater.start_polling()

location_handler = CommandHandler('location', location)
dispatcher.add_handler(location_handler)
updater.start_polling()

sendContact_handler = CommandHandler('sendcontact', sendContact)
dispatcher.add_handler(sendContact_handler)
updater.start_polling()

isitdown_handler = CommandHandler('isitdown', isitdown)
dispatcher.add_handler(isitdown_handler)
updater.start_polling()

# setChatPhoto_handler = CommandHandler('setchatphoto', setChatPhoto)
# dispatcher.add_handler(setChatPhoto_handler)
# updater.start_polling()

# setChatDescription_handler = CommandHandler('setchatdescription', setChatDescription)
# dispatcher.add_handler(setChatDescription_handler)
# updater.start_polling()

# deleteMessage_handler = CommandHandler('deletemessage', deleteMessage)
# dispatcher.add_handler(deleteMessage_handler)
# updater.start_polling()
