
'''

@ Author - Aditya Datar
@ Creation date - 09/14/2018
@ Description - Main Script of Review Setup
'''
from Applications.Workflows.ProcessTestFiles.Scripts.Process_Test_Files_Utility import Process_Test_Files_Utility
from Utilites import AppConstants
import time
from Utilites.TransactionTrackerOperations2 import TransactionTrackerOperations
from Applications.Workflows.ProcessTestFiles.AppResources import CommonLocators
from Applications.Workflows.ProcessTestFiles.Scripts.File_upload_autoit import File_upload_autoit

class Process_Test_file_850:

    def __init__(self, task_type, lo, username,input_wb, v_driver):
        self.v_task_type = task_type
        self.v_driver = v_driver
        self.v_input_wb = input_wb
        self.v_data_sheet = self.v_input_wb.get_sheet_by_name('PROCESS_TEST_FILES_INPUT')
        self.lo = lo
        self.v_username = username


    def execute_main(self,v_supplier,v_retailer, v_doc_type, row_count,v_date):
        self.lo.log_to_file("INFO", "Executing Process_Test_file_850.execute_main()")
        service_name = "FItoService"
        ptf = Process_Test_Files_Utility(self.v_task_type,self.lo, self.v_driver, self.v_input_wb)
        self.v_driver.switch_to.window("tab2")
        time.sleep(3)
        ptf.supplier_setup_check(v_supplier,v_retailer,v_doc_type,row_count, service_name)
        ptf.retailer_setup_check(v_supplier,v_retailer,v_doc_type,row_count)
        flag = ptf.check_extensions(v_supplier, v_retailer, v_doc_type, row_count, service_name)

        if flag == 0:
            time.sleep(3)
            self.v_driver.get(CommonLocators.TRANSACTION_TRACKER_PROD_LINK)
            time.sleep(5)
            tto = TransactionTrackerOperations(self.v_task_type, self.v_driver, self.lo)
            tto.search_process_for_process_test_file(v_supplier, v_retailer, v_doc_type, v_date)
            with open(CommonLocators.FIRST_FIVE_PARCELS_FILE_PATH) as f:
                for line in f:
                    tto.search_by_parcel_id_and_download(line.replace('\n', ''))
                    if 'str' in line:
                        break
            fua = File_upload_autoit(self.v_task_type, self.lo, self.v_username, self.v_driver)


            with open(CommonLocators.FIRST_FIVE_PARCELS_FILE_PATH) as f:
                for line in f:
                    #Temporary hardcoding the value to download
                    parcel="11052807388"
                    fua.remove_delimiters(parcel)
                    flag=fua.validation(parcel,AppConstants.INPUT_FILE_PATH)
                    self.v_driver.switch_to.window("tab3")
                    time.sleep(3)
                    if flag==1:
                        fua.upload_file(self.v_driver,parcel)
                        time.sleep(2)
                        self.v_driver.switch_to.window(self.v_driver.window_handles[0])
                        time.sleep(1)
                        tto.check_status_in_TT_preprod(v_supplier,v_retailer,v_doc_type)


                    if 'str' in line:
                        break