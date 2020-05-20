'''

@ Author - Karan Pandya
@ Creation date - 08/29/2018
@ Description - Main Script of Error Hospital
'''
import time
import math
import datetime
import openpyxl
from Utilites.Login import Login
from Utilites import AppConstants
from selenium import webdriver
from Utilites.ReportFileUtility import ReportFileUtility
from Utilites.ExcelOperations import ExcelOperations
from Applications.Workflows.ErrorHospital.AppResources import LocalElementLocator
from Applications.Workflows.ErrorHospital.Scripts.Error_Document_rejected import Error_Document_rejected
from Applications.Workflows.ErrorHospital.Scripts.Error_Hospital_Machine_Learning import Error_Hospital_Machine_Learning
class ErrorHospital:
    def __init__(self, task_type, log_file_object, username):
        self.v_task_type = task_type
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")
        self.v_driver = webdriver.Chrome(AppConstants.BROWSER_DRIVER, chrome_options= chrome_options)
        self.v_input_wb = openpyxl.load_workbook(AppConstants.INPUT_FILE_PATH)
        self.log_file_object = log_file_object
        self.v_username = username

    #Error Hospital Main Function
    def execute_main(self):


        login_object = Login(self.v_task_type, self.v_driver, self.v_input_wb, self.log_file_object)
        error_hospital_machine_learning_object = Error_Hospital_Machine_Learning(self.v_task_type, self.v_username)
        report_file_object = ReportFileUtility(self.v_task_type)
        output_sheet = self.v_input_wb.get_sheet_by_name('Output')
        input_sheet = self.v_input_wb.get_sheet_by_name('Input')
        excel_operation_object = ExcelOperations(self.v_task_type, input_sheet)
        #Login into DC4 Prod
        login_object.login("DC4 Prod")
        self.log_file_object.log_to_file("INFO", "Login in to DC4 Prod")
        self.v_driver.execute_script("window.open('https://commerce.spscommerce.com/transaction-tracker/prod/transactions/', 'new_window')")
        self.v_driver.switch_to.window(self.v_driver.window_handles[-1])
        time.sleep(2)
        #Login into Launchpad
        login_object.login("Launchpad")
        self.log_file_object.log_to_file("INFO", "Login in to Launchpad")
        self.v_driver.switch_to.window(self.v_driver.window_handles[0])
        time.sleep(2)
        #Extract data from input sheet
        for index in range(2,input_sheet.max_row+1):
            today = datetime.datetime.now()
            DD = datetime.timedelta(days=6)
            earlier = today - DD
            earlier_str = earlier.strftime("%Y-%m-%d")
            earlier_str = earlier_str+' 00:00:00'

            v_error_title = excel_operation_object.get_value(index, 1)
            #Searching data as per error title
            if v_error_title == LocalElementLocator.ADHOC_ERROR_TITLE:
                self.log_file_object.log_to_file("INFO", "Seaching tickets for error title:- AdhocReporting: document rejected")
                v_start_time = time.time()
                v_ticket_uid = excel_operation_object.get_value(index, 2)
                if v_ticket_uid is None:
                    v_ticket_uid = ' '
                Error_Document_rejected_obj = Error_Document_rejected(self.v_task_type, self.v_driver, self.log_file_object,
                                                                      self.v_input_wb, error_hospital_machine_learning_object)
                v_count = Error_Document_rejected_obj.execute_main(v_error_title, v_ticket_uid, output_sheet, earlier_str)
                v_end_time = time.time()
                report_file_object.update_sheet(self.v_username, v_count, math.floor(v_end_time - v_start_time), str(datetime.date.today()))
            if v_error_title == LocalElementLocator.WEB_DOC_REJECTED_ERROR_TITLE:
                self.log_file_object.log_to_file("INFO",
                                                 "Seaching tickets for error title:- WebForms-ToService: document rejected")
                v_start_time = time.time()
                v_ticket_uid = excel_operation_object.get_value(index, 2)
                if v_ticket_uid is None:
                    v_ticket_uid = ' '
                Error_Document_rejected_obj = Error_Document_rejected(self.v_task_type, self.v_driver, self.log_file_object, self.v_input_wb, error_hospital_machine_learning_object)
                v_count = Error_Document_rejected_obj.execute_main(v_error_title, v_ticket_uid, output_sheet, earlier_str)
                v_end_time = time.time()
                report_file_object.update_sheet(self.v_username, v_count, math.floor(v_end_time - v_start_time),
                                str(datetime.date.today()))
            else:
                self.log_file_object.log_to_file("ERROR",
                                                 "Invalid error title ErrorHospital.execute_main()")
        time.sleep(3)
        self.v_driver.close()







