import telebot
import config
import event_library
import time
import datetime

#event_library.Next_Event_Info()

bot=telebot.TeleBot(config.TOKEN)
start_working_status = 0
stop = 0



@bot.message_handler(commands=['start'])
def start(message):
    global start_working_status
    global stop
    start_working_status+=1
    stop=0
    memory_time = 0
    if start_working_status==1:
        print('Функция запущена')
        while start_working_status>0:
            time_now = int((str((datetime.datetime.now()).time()))[:2])

            if time_now in config.time_list and memory_time!=time_now:
                memory_time = time_now
                if (event_library.Next_Event_Info())["days_before"] == config.day_before_notification:
                    A = event_library.Next_Event_Info()
                    push = config.names(A["person"])
                    text = f'{A["person"]} {push} \nДата: {(A["time"])[0:10]} \nВремя:{(A["time"])[10:]} \nМероприятие: {A["event"]} \nМесто: {A["place"]}'
                    if A["helper"] !="":
                        text = text + f'\nПомощь: {A["helper"]}'
                    if A['need'] !="":
                        text = text + f'\nНужно: {A["need"]}'
                    bot.send_message(message.chat.id, text.format(message.from_user, bot.get_me()),
                             parse_mode='html')

            print('Проверка номер', time_now, 'выполнена')
            time.sleep(config.seconds)
            if stop==1:
                break
    else:
        print('Никакой второй функции')

@bot.message_handler(commands=['stop'])
def stop(message):
    global start_working_status
    global stop
    start_working_status=0
    stop=1
    print('Функция остановлена')
    bot.send_message(message.chat.id, "СТОЯТЬ".format(message.from_user, bot.get_me()),
                 parse_mode='html')





bot.polling(none_stop=True)
