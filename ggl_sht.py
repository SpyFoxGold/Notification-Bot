import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import config

    # Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'techgroup.json'
    # ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = config.spreadsheet_id
    #Название листа таблицы
SHEET_LIST_NAME = config.SHEET_LIST_NAME


def SHEET_INFO_GET(): #Возвращает список всех данных из таблицы

    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

    # Получение длины таблицы
    values_info = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=str(SHEET_LIST_NAME)+'!A1:A',
        majorDimension='ROWS'
    ).execute()

    Lenght = len((values_info['values']))


    #Чтение файла
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=str(SHEET_LIST_NAME)+'!A1:F'+str(Lenght),
        majorDimension='ROWS'
    ).execute()
    return(values['values'])

#для тестов
#print(SHEET_INFO_GET())
