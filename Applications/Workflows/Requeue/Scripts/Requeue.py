'''

@ Author - Karan Pandya
@ Creation date - 08/29/2018
@ Description - Main Script of Production Data Monitoring
'''
import time
import math
import datetime
import openpyxl
from Utilites.Login import Login
from Utilites import AppConstants
from selenium import webdriver
from Utilites.LogFileUtility import LogFileUtility
from Utilites.DC4_Utility import DC4_Utility
from Utilites.SeleniumOperations import SeleniumOperations
from Utilites.ReportFileUtility import ReportFileUtility
from Applications.Workflows.Requeue.AppResources import LocalElementLocator
from Utilites.SeleniumOperations import SeleniumOperations
from Utilites.ExcelOperations import ExcelOperations
import re
class Requeue:
    def __init__(self, task_type, lo, username):
        self.v_task_type = task_type
        self.v_driver = webdriver.Chrome(AppConstants.BROWSER_DRIVER)
        self.v_input_wb = openpyxl.load_workbook(AppConstants.INPUT_FILE_PATH)
        self.lo = lo
        self.v_username = username

    def requeue(self, parcel_list):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        flag = 0
        for index in range(0, len(parcel_list)):
            i = (index+1)%5
            if i == 0:
                i = 5
            parcel_path = '//*[@id="form1:inputText'+str(i)+'"]'
            flag = 0
            if so.check_exists_by_xpath(parcel_path):
                parcel_uid = parcel_list[index]
                if isinstance(parcel_uid, str):
                    if " " in parcel_uid:
                        parcel_uid = re.sub('\W+','', parcel_uid)
                        parcel_uid.strip()
                        parcel_uid = parcel_uid.replace("  ","")
                        print(parcel_uid)
                so.send_text_by_xpath(parcel_path,parcel_uid)
            if i == 5:
                so.click_element_by_id(LocalElementLocator.REQUEUE_PARCEL_BUTTON_ID)
                flag = 1
            print(index)

        if flag == 0:
            so.click_element_by_id(LocalElementLocator.REQUEUE_PARCEL_BUTTON_ID)




    def execute_main(self):
        v_start_time = time.time()
        self.lo.log_to_file("INFO", "Login in to DC4 Prod")
        lg = Login(self.v_task_type, self.v_driver, self.v_input_wb, self.lo)
        so = SeleniumOperations(self.v_task_type,self.v_driver,self.lo)
        rf = ReportFileUtility(self.v_task_type)
        input_sheet = self.v_input_wb.get_sheet_by_name('Input')
        eo = ExcelOperations(self.v_task_type, input_sheet)
        parcel_list = []
        i = 2
        while(eo.get_value(i,1) != None):
            parcel_list.append(eo.get_value(i,1))
            i=i+1

        lg.login("DC4 Prod")
        so.click_element_by_id(LocalElementLocator.ERROR_HOSPITAL_TAB_ID)
        so.click_element_by_xpath(LocalElementLocator.REQUEUE_PARCEL_TAB_XPATH)
        self.requeue(parcel_list)

        time.sleep(2)

        self.v_driver.close()
        v_end_time = time.time()
        rf.update_sheet(self.v_username, i, math.floor(v_end_time - v_start_time), str(datetime.date.today()))





