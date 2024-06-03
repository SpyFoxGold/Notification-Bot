from ggl_sht import SHEET_INFO_GET
import datetime
from datetime import date


def NormalDate(Date):
    date = Date.split('.')
    if len(date)==1:
        date = list(date[0].split())

    year = int(date[2])
    month = int(date[1])
    day = int(date[0])
    date_obj = datetime.date(year,month,day)
    return date_obj

def Difference(Date):
    Date = NormalDate(Date)
    #Поулчение сегодняшней даты
    current_date = date.today()
    #Поулчение разницы между временем
    daytime_difference = Date - current_date
    return daytime_difference.days

def normal_len(A):
    while len(A)<6:
        A.append("")
    return(A)

def Next_Event_Info():
    # # Поулчение даты у элемента
    A = SHEET_INFO_GET()
    for i in range(0,len(A)):
        try:
            if A[i] != []:
                Date = ((A[i][0])[0:10])
            Day_Difference = Difference(Date)
            if Day_Difference >0:
                A[i]=normal_len(A[i])
                A[i].append(Day_Difference)
                Dict = {
                'time':A[i][0],
                'event': A[i][1],
                'place':A[i][2],
                'person':A[i][3],
                'helper':A[i][4],
                'need':A[i][5],
                'days_before':A[i][6]
                }
                return(Dict)
                break
        except: pass
