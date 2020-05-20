'''
@ Author - Karan Pandya
@ Creation date - 08/31/2018
@ Description - Train bot and make decision based on previous results
'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Utilites import AppConstants
import datetime

class Error_Hospital_Machine_Learning:

    def __init__(self, task_type, username):
        self.v_task_type = task_type
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(AppConstants.CLIENT_SECRET_JSON_FILE_PATH, scope)
        client = gspread.authorize(creds)
        sht = client.open("Error Hospital")
        self.G_sheet = sht.worksheet(task_type)
        values_list = self.G_sheet.col_values(1)
        Row_Count = len(values_list)
        self.Row_Count = Row_Count + 1
        self.v_username = username

    #Add data to library
    def add_to_library(self, company_name, web_company_uid):
        flag = 0
        for i in range(1, self.Row_Count):
            if self.G_sheet.cell(i, 1).value == company_name:
                self.G_sheet.update_cell(i,2,web_company_uid)
                flag = 1
                break
        if flag == 1:
            return
        else:
            val = []
            val.append(company_name)
            val.append(web_company_uid)
            val.append(self.v_username)
            val.append(str(datetime.date.today()))
            self.G_sheet.append_row(val)

    #Retrive data from library
    def get_supplier_info(self, company_name):
        for i in range(1, self.Row_Count):
            if self.G_sheet.cell(i,1).value == company_name:
                return self.G_sheet.cell(i,2).value

        return False

