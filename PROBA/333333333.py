import telebot 
from telebot import types 
 
 
token = "6212853265:AAFxQbHx61LOlq6qnZ8O9F7Yi0nMMhbzgag" 
 
 
 
bot = telebot.TeleBot(token) 
 
@bot.message_handler(commands = ['start']) 
def start (message): 
     markup = types.ReplyKeyboardMarkup(resize_keyboard = True) 
     item1 = types.KeyboardButton('🏋️ Физическое культура') 
     item2 = types.KeyboardButton('👼 Дошкольное образование') 
     item3 = types.KeyboardButton('👩‍🏫 Преподавание в начальных классах') 
     item4 = types.KeyboardButton('💻 Прикладная информатика') 
 
     markup.add(item1, item2, item3, item4) 
 
     bot.send_message(message.chat.id, 'Привет, {0.first_name}!'. format(message.from_user), reply_markup = markup) 
 
 
@bot.message_handler(contecnt_types = ['text']) 
def bot_message(message): 
     if message.chat.type == 'private':   
          if message.text == '👩‍🏫 Преподавание в начальных классах':  
               markup = types.ReplyKeyboardMarkup(resize_keyboard = True) 
               item1 = types.KeyboardButton('101A') 
               item2 = types.KeyboardButton('101Б') 
               item3 = types.KeyboardButton('201А') 
               item4 = types.KeyboardButton('201Б') 
               item5 = types.KeyboardButton('301А') 
               item6 = types.KeyboardButton('301Б') 
               back = types.KeyboardButton('👩‍🏫 Назад') 
               markup.add(item1, item2, item3, item4, item5, item6, back) 
 
               bot.send_message(message.chat.id, '👩‍🏫 Преподавание в начальных классах', relply_markup = markup) 
 
 
 
 
 
 
 
 
 
bot.polling(none_stop = True)