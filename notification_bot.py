import telebot
import config
import event_library
import time
import datetime

#event_library.Next_Event_Info()

bot=telebot.TeleBot(config.TOKEN)
start_working_status = 0




@bot.message_handler(commands=['ne_trogat_suka'])
def start(message):
    global start_working_status
    start_working_status+=1
    if start_working_status>0:
        while True:
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
            time.sleep(config.seconds)




@bot.message_handler(commands=['setting'])
def setting(message):
    bot.send_message(message.chat.id, "Тут будут настройки".format(message.from_user, bot.get_me()),
                 parse_mode='html')




bot.polling(none_stop=True)
