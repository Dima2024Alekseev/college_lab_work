import telebot 
from telebot import types 
from openpyxl import load_workbook
import string

 
token = "6212853265:AAFxQbHx61LOlq6qnZ8O9F7Yi0nMMhbzgag" 
bot = telebot.TeleBot(token) 


f_100 = open('C:/Users/aleks/Desktop/Новая папка/www_100.txt', 'r')
a_4 = f_100.read()
f_100.close

f_200 = open('C:/Users/aleks/Desktop/Новая папка/www_200.txt', 'r')
a_5 = f_200.read()
f_200.close

f_300 = open('C:/Users/aleks/Desktop/Новая папка/www_300.txt', 'r')
a_6 = f_300.read()
f_300.close

f_101_A = open('C:/Users/aleks/Desktop/Новая папка/www_101А.txt', 'r')
a_10 = f_101_A.read()
f_101_A.close

f_101_B = open('C:/Users/aleks/Desktop/Новая папка/www_101Б.txt', 'r')
a_11 = f_101_B.read()
f_101_B.close

f_201_A = open('C:/Users/aleks/Desktop/Новая папка/www_201А.txt', 'r')
a_12 = f_201_A.read()
f_201_A.close

f_201_B = open('C:/Users/aleks/Desktop/Новая папка/www_201Б.txt', 'r')
a_13 = f_201_B.read()
f_201_B.close

f_301_A = open('C:/Users/aleks/Desktop/Новая папка/www_301А.txt', 'r')
a_14 = f_301_A.read()
f_301_A.close

f_301_B = open('C:/Users/aleks/Desktop/Новая папка/www_301Б.txt', 'r')
a_15 = f_301_B.read()
f_301_B.close

f_102 = open('C:/Users/aleks/Desktop/Новая папка/www_102.txt', 'r')
a_7 = f_102.read()
f_102.close

f_202 = open('C:/Users/aleks/Desktop/Новая папка/www_202.txt', 'r')
a_8 = f_202.read()
f_202.close

f_302 = open('C:/Users/aleks/Desktop/Новая папка/www_302.txt', 'r')
a_9 = f_302.read()
f_302.close

f_103 = open('C:/Users/aleks/Desktop/Новая папка/www_103.txt', 'r')
a_1 = f_103.read()
f_103.close

f_203 = open('C:/Users/aleks/Desktop/Новая папка/www_203.txt', 'r')
a_2 = f_203.read()
f_203.close()

f_303 = open('C:/Users/aleks/Desktop/Новая папка/www_303.txt', 'r')
a_3 = f_303.read()
f_303.close()





@bot.message_handler(commands = ['fizvoz'])
def fizvoz(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton('100')
    item2 = types.KeyboardButton('200')
    item3 = types.KeyboardButton('300')
    back = types.KeyboardButton('🔙 назад')
    markup.add(item1, item2, item3,back)
    bot.send_message(message.chat.id, 'Выберите группу ',reply_markup=markup)

@bot.message_handler(commands = ['pk_100'])
def pk_100(message):
    bot.send_message(message.chat.id,a_4.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))

@bot.message_handler(commands = ['pk_200'])
def pk_200(message):
    bot.send_message(message.chat.id,a_5.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))

@bot.message_handler(commands = ['pk_300'])
def pk_300(message):
    bot.send_message(message.chat.id,a_6.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))

@bot.message_handler(commands = ['pk_101_A'])
def pk_101_A(message):
    bot.send_message(message.chat.id,a_10.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))

@bot.message_handler(commands = ['pk_101_B'])
def pk_101_B(message):
    bot.send_message(message.chat.id,a_11.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))

@bot.message_handler(commands = ['pk_201_A'])
def pk_201_A(message):
    bot.send_message(message.chat.id,a_12.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))

@bot.message_handler(commands = ['pk_201_B'])
def pk_201_B(message):
    bot.send_message(message.chat.id,a_13.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))

@bot.message_handler(commands = ['pk_301_A'])
def pk_301_A(message):
    bot.send_message(message.chat.id,a_14.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))

@bot.message_handler(commands = ['pk_301_B'])
def pk_301_B(message):
    bot.send_message(message.chat.id,a_15.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))

@bot.message_handler(commands = ['pk_102'])
def pk_102(message):
    bot.send_message(message.chat.id,a_7.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))

@bot.message_handler(commands = ['pk_202'])
def pk_202(message):
    bot.send_message(message.chat.id,a_8.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))

@bot.message_handler(commands = ['pk_302'])
def pk_302(message):
    bot.send_message(message.chat.id,a_9.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))

@bot.message_handler(commands = ['pk_103'])
def pk_103(message):
    bot.send_message(message.chat.id,a_1.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))


@bot.message_handler(commands = ['pk_203'])
def pk_203(message):
    bot.send_message(message.chat.id,a_2.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))

@bot.message_handler(commands = ['pk_303'])
def pk_303(message):
    bot.send_message(message.chat.id,a_3.replace("понедельник","📌понедельник").replace("вторник","📌вторник").replace("среда","📌среда").replace("четверг","📌четверг").replace("пятница","📌пятница").replace("суббота","📌суббота").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣"))



@bot.message_handler(commands = ['pk'])
def pk(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton('103')
    item2 = types.KeyboardButton('203')
    item3 = types.KeyboardButton('303')
    back = types.KeyboardButton('🔙 назад')
    markup.add(item1, item2, item3,back)
    bot.send_message(message.chat.id, 'Выберите группу ',reply_markup=markup)

@bot.message_handler(commands = ['elementary_grades'])
def elementary_grades(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton('101 А')
    item2 = types.KeyboardButton('101 Б')
    item3 = types.KeyboardButton('201 А')
    item4 = types.KeyboardButton('201 Б')
    item5 = types.KeyboardButton('301 А')
    item6 = types.KeyboardButton('301 Б')
    back = types.KeyboardButton('🔙 назад')
    markup.add(item1, item2, item3, item4, item5, item6, back)
    bot.send_message(message.chat.id, 'Выберите группу ',reply_markup=markup)

@bot.message_handler(commands = ['preschool_education'])
def preschool_education(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton('102')
    item2 = types.KeyboardButton('202')
    item3 = types.KeyboardButton('302')
    back = types.KeyboardButton('🔙 назад')
    markup.add(item1, item2, item3, back)
    bot.send_message(message.chat.id, 'Выберите группу ',reply_markup=markup)


@bot.message_handler(commands = ['close'])
def close(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton('🏋️ Физическая культура')
    item2 = types.KeyboardButton('👼 Дошкольное образование')
    item3 = types.KeyboardButton('👩‍🏫 Преподавание в начальных классах')
    item4 = types.KeyboardButton('💻 Прикладная информатика')
    

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,'Вы в главном меню', reply_markup= markup)
 
@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton('🏋️ Физическая культура')
    item2 = types.KeyboardButton('👼 Дошкольное образование')
    item3 = types.KeyboardButton('👩‍🏫 Преподавание в начальных классах')
    item4 = types.KeyboardButton('💻 Прикладная информатика')
    markup.add(item1, item2, item3, item4) 
    bot.send_message(message.chat.id,'Привет, {0.first_name}!'.format(message.from_user), reply_markup= markup)
    
    
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🏋️ Физическая культура':
            fizvoz(message)
        elif message.text == '🔙 назад':
           close(message) 
        elif message.text == '💻 Прикладная информатика':
            pk(message)
        elif message.text == '103':
            pk_103(message)
        elif message.text == '102':
            pk_102(message)
        elif message.text == '202':
            pk_202(message)
        elif message.text == '302':
            pk_302(message)
        elif message.text == '100':
            pk_100(message)
        elif message.text == '200':
            pk_200(message)
        elif message.text == '300':
            pk_300(message)
        elif message.text == '101 А':
            pk_101_A(message)
        elif message.text == '101 Б':
            pk_101_B(message)
        elif message.text == '201 А':
            pk_201_A(message)
        elif message.text == '201 Б':
            pk_201_B(message)
        elif message.text == '301 А':
            pk_301_A(message)
        elif message.text == '301 Б':
            pk_301_B(message)
        elif message.text == '203':
              pk_203(message)
        elif message.text == '303':
              pk_303(message)
        elif message.text == '👩‍🏫 Преподавание в начальных классах':
            elementary_grades(message)
        elif message.text == '👼 Дошкольное образование':
            preschool_education(message)


bot.polling(none_stop = True)