import telebot
from threading import *
from random import *
import time

bot = telebot.TeleBot('')

print('Bot started')

users = {}
user = []
rooms = {'обсуждение игр': 77, 'выплёскивание гнева': 13, 'просто чат': 1}
print(rooms.keys())
#------------------------------------------------------------------------------------------/function random--------------------------------
def random():
    while True:
        user_copy = user.copy()
        while len(user_copy) > 0:
            z = True
            while z:
                k = randint(0, 1000)
                if k in list(users.values()):
                    pass
                else:
                    z = False
            
            x = randint(0, len(user_copy) - 1)
            people1 = user_copy.pop(x)
            if len(user_copy) == 0:
                users[people1] = None
                bot.send_message(people1, 'тебя обделил рандом, сорян. подключишься через минутки две')
                print(users)
                break
            x =randint(0,len(user_copy) - 1)
            people2 = user_copy.pop(x)
            users[people1] = k
            users[people2] = k
            bot.send_message(people1, 'подключено успешно')
            bot.send_message(people1, 'подключение успешно')
            print(users)

        time.sleep(30)

#-------------------------------------------------------------------------------------/второй поток-------------------------------------
t = Thread(target = random)


t.start()


#--------------------------------------------------------------------------------/printmessage---------------------------------
# @bot.message_handler(content_types=["text"])
# def get_text_messages(message):
#     print(f'{message.chat.username} написал {message.chat.id}({users.get(message.chat.id)}):\n-{message.text}')

    
    

#-----------------------------------------------------------------------------/start----------------------------------------------------------
@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!!! этот бот ')

#------------------------------------------------------------------------------/connect-----------------------------------------------------
@bot.message_handler(commands = ['connect'])
def connect(message):
    user.append(message.chat.id)
    print(user)
    bot.send_message(message.chat.id, 'подключение...')

#-------------------------------------------------------------------------------/shutdown-----------------------------------------    
@bot.message_handler(commands = ['shutdown'])
def discon(message):
    if message.chat.id in users:
        users[message.chat.id] = None
    if message.chat.id in user:
        user.remove(message.chat.id)
    bot.send_message(message.chat.id, 'отключение успешно')
    print(user)
    print(users)
#---------------------------------------------------------------------------------/showrooms-----------------------------------------------
@bot.message_handler(commands = ['showrooms'])
def showrooms(message):
    bot.send_message(message.chat.id, f'обсуждение игр, выплёскивание гнева, просто чат')

#---------------------------------------------------------------------------------/connectToServ-------------------------------
@bot.message_handler(commands = ['contoserv'])
def conserv(message):
    v = message.text[11:]
    if v == '':
        bot.send_message(message.chat.id, 'ваш ввод is инвалид или такой комнаты нет,\nвведите команду правильно,\nпример:\n/contoserv название комнаты')
        return
    else:
        users[message.chat.id] = rooms[v]
        bot.send_message(message.chat.id, f'вы подключены к комнате\n"{v}"')
#---------------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(content_types=["text"])
def get_text_messages(message):  
    if message.chat.id not in users or users[message.chat.id] == None:
            bot.send_message(message.chat.id, 'вы не подключены')
            return
    for u in users.keys():
        if users.get(message.chat.id) == users.get(u) and u != message.chat.id and users.get(message.chat.id) != None:
            bot.send_message(u, f'{u%10_000}: {message.text}')

        
       

        


bot.polling(none_stop=True, interval=0)









