
import telebot
import random




token = "5677778843:AAHKEL83nNr2ZKK7Pt8snkAsmzGv40WIAGs"



SL = dict()


HELP = '''
Список команд
*для получения поздравления от бота используй команды
/mart
/video
'''

random_anecdot = ['Заходит как-то скелет в бар заказывает пиво и швабру','Как называют человека без печени ? Обеспеченный !','Колобок повесился','Шаман-извращенец вызвал золотой дождь', 'Тема - Лучший !!!', 'Шланг постоянно падает! Эта точечная фраза объясняет почему у Владимира до сих пор нет девушки', 'i am michael jordan !!!' ]
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,HELP)


names = []






@bot.message_handler(commands=['add_student'])
def add_student(message):
    _,name=message.text.split()
    names.append(name)
    bot.send_message(message.chat.id, f'Студент {name} добавлен в список')



@bot.message_handler(commands=['view'])
def view(message):
    for i in range(len(names)):
        bot.send_message(message.chat.id,names[i])






@bot.message_handler(commands=['video'])
def video(message):
     video = open('/home/DimaBumblebee2022/video_2023-03-08_18-30-27.mp4', 'rb')
     bot.send_video(message.chat.id, video)

@bot.message_handler(commands=['mart'])
def mart(message):
    bot.send_message(message.chat.id, 'С 8 марта, родная ♥ !')
    bot.send_photo(message.chat.id, 'https://ibb.co/PmN5711')
    bot.send_photo(message.chat.id, 'https://ibb.co/CPd2tnM')
    bot.send_photo(message.chat.id, 'https://ibb.co/RCXWn4M')
    bot.send_photo(message.chat.id, 'https://ibb.co/f9ycGPM')
    bot.send_photo(message.chat.id, 'https://ibb.co/dtympqg')
    bot.send_photo(message.chat.id, 'https://ibb.co/vcv0Cxm')
    bot.send_photo(message.chat.id, 'https://ibb.co/GkWQZYJ')
    bot.send_photo(message.chat.id, 'https://ibb.co/sVK3Mm7')


@bot.message_handler(commands=['anecdot'])
def anecdot(message):
    bot.send_message(message.chat.id,random.choice(random_anecdot))


@bot.message_handler(content_types = ['text'])
def echo(message):
     if  message.text == 'я тебя люблю' or  message.text == 'Я тебя люблю' or message.text == 'i love you':
         bot.send_message(message.chat.id, 'я тебя люблю  ♥')

     else:
         bot.send_message(message.chat.id, message.text)




bot.polling(none_stop=True)