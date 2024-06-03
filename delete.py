# import event_library
#
# A = event_library.Next_Event_Info()
#
# print(f'{A["person"]} \nДата: {(A["time"])[0:10]} \nВремя:{(A["time"])[10:]} \nМероприятие: {A["event"]} \nМесто: {A["place"]}')
import datetime

c = (datetime.datetime.now()).time()
a = datetime.time(9,00,00)
b = datetime.time(21,00,00)
print(c)
print(a)
print(b)

if a == c:
    print(12)
else: print(21)
#time.sleep(config.seconds)
