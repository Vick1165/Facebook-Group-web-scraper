import gspread
from oauth2client.service_account import ServiceAccountCredentials
import  pprint

#https://www.youtube.com/watch?v=cnPlKLEGR7E
#link


def send_to_Drive(keyword,name,type,link):
    try:
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file",
                 "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('clientsecret.json', scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("Fb group data").get_worksheet(0)

        # Extract and print all of the values
        #results = sheet.get_all_records()
        #pp = pprint.PrettyPrinter()
        #pp.pprint(results)

        # inserting Row
        row = [keyword,name,type,link]
        sheet.append_row(row)
        
    except Exception as e: 
        print(e)


def send_to_Drive_Sheet2(keyword, name, type, link):
    try:
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file",
                 "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('clientsecret.json', scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("Fb group data").get_worksheet(1)

        # Extract and print all of the values
        # results = sheet.get_all_records()
        # pp = pprint.PrettyPrinter()
        # pp.pprint(results)

        # inserting Row
        row = [keyword, name, type, link]
        sheet.append_row(row)

    except Exception as e:
        print(e)


#send_to_Drive('test','test','test','test')
#send_to_Drive_Sheet2('test','test','test','test')