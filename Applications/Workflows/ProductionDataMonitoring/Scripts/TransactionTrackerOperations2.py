'''

@ Author - Yogesh Pawar
@ Creation date - 09/21/2018
@ Description - Common Transaction Tracker Operation
'''

from Utilites.SeleniumOperations import SeleniumOperations
from Utilites.ExcelOperations import ExcelOperations
from Applications.Workflows.ProductionDataMonitoring.AppResources import LocalElementLocator
import time
from selenium.common.exceptions import NoSuchElementException

class TransactionTrackerOperations:
    def __init__(self, task_type, driver, lo):
        self.v_task_type = task_type
        self.driver = driver
        self.lo = lo


    # generic method to search supplier and retailer with customer_type as parameter i.e. "Company" OR "Trading Partner"
    def select_customer(self, customer_type, customer_name):
        self.lo.log_to_file("INFO", "Executing TransactionTrackerOperations.select_customer()")
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        print("Search for: " + str(customer_name))
        time.sleep(2)
        if customer_type == "Company":
            so.send_text_by_xpath(LocalElementLocator.COMPANY_SEARCH_INPUTBOX,customer_name)
        if customer_type == "Trading Partner":
            so.send_text_by_xpath(LocalElementLocator.TRADING_SEARCH_INPUTBOX,customer_name)
        time.sleep(2)
        count = self.driver.find_elements_by_xpath(LocalElementLocator.DROP_DOWN_LIST)
        for i in range(len(count)):
            if customer_type == "Company":
                customer_from_TT=so.get_text_by_xpath(LocalElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_1 + str(
                        i) + LocalElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_2)
            if customer_type == "Trading Partner":
                customer_from_TT=so.get_text_by_xpath(LocalElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_1 + str(
                        i) + LocalElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_2)
            if customer_name.lower() == customer_from_TT.lower():
                if customer_type == "Company":
                    so.click_element_by_xpath(LocalElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_1 + str(
                        i) + LocalElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_2)
                if customer_type == "Trading Partner":
                    so.click_element_by_xpath(LocalElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_1 + str(
                        i) + LocalElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_2)
                break
        time.sleep(2)

    # method for collect Credit Memo unique parcels and fill input sheet as per result data
    def get_CM_parcels(self,input_sheet,row):
        self.lo.log_to_file("INFO", "Executing TransactionTrackerOperations.get_CM_parcels()")
        whilevalue=1
        while(whilevalue):
            try:
                so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
                eo = ExcelOperations(self.v_task_type, input_sheet)
                error_parcel_comment = ''
                without_error_parcel_comment = ''
                without_error_parcel_count = 0
                error_parcel_count = 0
                j = 1
                while (1):
                    i = 1
                    parcel_id = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(i) + LocalElementLocator.PARCEL_ID_2)
                    while (parcel_id.is_enabled()):
                        try:
                            parcel_id1 = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(i) + LocalElementLocator.PARCEL_ID_2).text
                        except NoSuchElementException:
                            break
                        status = so.get_text_by_xpath(LocalElementLocator.STATUS_1 + str(i) + LocalElementLocator.STATUS_2)
                        document_id = so.get_text_by_xpath(LocalElementLocator.DOCUMENT_ID_1 + str(i) + LocalElementLocator.DOCUMENT_ID_2)
                        parcel_date_time = so.get_text_by_xpath(LocalElementLocator.PARCEL_DATE_TIME_1 + str(i) + LocalElementLocator.PARCEL_DATE_TIME_2)
                        if "CM" in document_id:
                            if "Completed w/o Errors" in status:
                                without_error_parcel_count = without_error_parcel_count + 1
                                without_error_parcel_comment = without_error_parcel_comment + str(
                                    without_error_parcel_count) + ") Parcel ID: " + str(parcel_id1) + " (Document ID: " + str(
                                    document_id) + ") with status: " + str(status)+" ["+parcel_date_time+"]" + "\n"
                            if "Completed w/Errors" in status:
                                error_parcel_count = error_parcel_count + 1
                                error_parcel_comment = error_parcel_comment + str(error_parcel_count) + ") Parcel ID: " + str(
                                    parcel_id1) + " (Document ID: " + str(document_id) + ") with status: " + str(status)+" ["+parcel_date_time+"]" + "\n"
                        i = i + 1
                        j = j + 1
                        try:
                            parcel_id = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(i) + LocalElementLocator.PARCEL_ID_2)
                        except NoSuchElementException:
                            self.lo.log_to_file("INFO","NoSuchElementException in TransactionTrackerOperations.get_CM_parcels()")
                    next_button = self.driver.find_element_by_xpath(LocalElementLocator.NEXT_SEARCH_BTN)

                    if (next_button.is_enabled()):
                        next_button = self.driver.find_element_by_xpath(LocalElementLocator.NEXT_SEARCH_BTN)
                        next_button.click()
                        time.sleep(2)

                    else:
                        eo.set_value(row, 6, without_error_parcel_count)
                        eo.set_value(row, 7, without_error_parcel_comment)
                        eo.set_value(row, 8, error_parcel_comment)
                        self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
                        break
            except NoSuchElementException:
                break
        try:
            parcel_id1 = self.driver.find_element_by_xpath(LocalElementLocator.LAST_PARCEL_ID).text
        except NoSuchElementException:
            self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
            whilevalue==0
            time.sleep(2)



    # method for collect all unique parcels and fill input sheet as per result data
    def get_all_parcels(self, input_sheet, row):
        self.lo.log_to_file("INFO", "Executing TransactionTrackerOperations.get_all_parcels()")
        time.sleep(2)
        whilevalue = 1
        while (whilevalue):
            try:
                so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
                eo = ExcelOperations(self.v_task_type, input_sheet)
                error_parcel_comment = ''
                without_error_parcel_comment = ''
                without_error_parcel_count = 0
                error_parcel_count = 0
                j = 1
                while (1):
                    i = 1
                    parcel_id = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(i) + LocalElementLocator.PARCEL_ID_2)
                    while (parcel_id.is_enabled()):
                        try:
                            parcel_id1 = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(i) + LocalElementLocator.PARCEL_ID_2).text
                        except NoSuchElementException:
                            break

                        status= so.get_text_by_xpath(LocalElementLocator.STATUS_1 + str(i) + LocalElementLocator.STATUS_2)
                        document_id=so.get_text_by_xpath(LocalElementLocator.DOCUMENT_ID_1 + str(i) + LocalElementLocator.DOCUMENT_ID_2)
                        parcel_date_time = so.get_text_by_xpath(LocalElementLocator.PARCEL_DATE_TIME_1 + str(i) + LocalElementLocator.PARCEL_DATE_TIME_2)
                        if "Completed w/o Errors" in status:
                            without_error_parcel_count = without_error_parcel_count + 1
                            without_error_parcel_comment = without_error_parcel_comment + str(
                                without_error_parcel_count) + ") Parcel ID: " + str(
                                parcel_id1) + " (Document ID: " + str(
                                document_id) + ") with status: " + str(status) + " [" + parcel_date_time + "]" + "\n"
                        if "Completed w/Errors" in status:
                            error_parcel_count = error_parcel_count + 1
                            error_parcel_comment = error_parcel_comment + str(
                                error_parcel_count) + ") Parcel ID: " + str(
                                parcel_id1) + " (Document ID: " + str(document_id) + ") with status: " + str(
                                status) + " [" + parcel_date_time + "]" + "\n"
                        i = i + 1
                        j = j + 1
                        try:
                            parcel_id = self.driver.find_element_by_xpath(LocalElementLocator.PARCEL_ID_1 + str(i) + LocalElementLocator.PARCEL_ID_2)
                        except NoSuchElementException:
                            self.lo.log_to_file("INFO",
                                                "NoSuchElementException in TransactionTrackerOperations.get_all_parcels()")

                    next_button = self.driver.find_element_by_xpath(LocalElementLocator.NEXT_SEARCH_BTN)

                    if (next_button.is_enabled()):
                        next_button = self.driver.find_element_by_xpath(LocalElementLocator.NEXT_SEARCH_BTN)
                        next_button.click()
                        time.sleep(2)

                    else:
                        eo.set_value(row, 6, without_error_parcel_count)
                        eo.set_value(row, 7, without_error_parcel_comment)
                        eo.set_value(row, 8, error_parcel_comment)
                        self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
                        break
            except NoSuchElementException:
                break
        try:
            parcel_id1 = self.driver.find_element_by_xpath(LocalElementLocator.LAST_PARCEL_ID).text
        except NoSuchElementException:
            self.driver.get(LocalElementLocator.TRANSACTION_TRACKER_PROD_LINK)
            whilevalue==0
            time.sleep(2)


    # method for searching Credit Memo data with supplier,retailer,doc_type,date,input_sheet,row parameters
    def search_process_for_CMPDM(self,supplier,retailer,doc_type,date, input_sheet,row):
        try:
            self.lo.log_to_file("INFO", "Executing TransactionTrackerOperations.search_process_for_CMPDM() for: "+str(supplier)+"|"+str(retailer)+"|"+str(doc_type))
            self.driver.switch_to.frame(0)
            so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
            self.select_customer("Company",supplier)
            self.select_customer("Trading Partner",retailer)
            so.send_text_by_xpath(LocalElementLocator.START_DATE,date)
            so.click_element_by_xpath(LocalElementLocator.SERVICE)
            so.click_element_by_xpath(LocalElementLocator.DC4ROUTER)
            so.send_text_by_xpath(LocalElementLocator.DOCUMENT_TYPE,doc_type)
            so.click_element_by_xpath(LocalElementLocator.SEARCH_BTN)
            time.sleep(2)
            self.get_CM_parcels(input_sheet, row)
        except NoSuchElementException:
            self.lo.log_to_file("ERROR",
                                "Fail in TransactionTrackerOperations.search_process_for_CMPDM() for: " + str(
                                    supplier) + "|" + str(retailer) + "|" + str(doc_type))

    # method for searching all unique data with supplier,retailer,doc_type,date,input_sheet,row parameters
    def search_process_for_PDM(self,supplier,retailer,doc_type,date, input_sheet,row):
        try:
            self.lo.log_to_file("INFO",
                                "Executing TransactionTrackerOperations.search_process_for_PDM() for: " + str(
                                    supplier) + "|" + str(retailer) + "|" + str(doc_type))
            self.driver.switch_to.frame(0)
            so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
            self.select_customer("Company", supplier)
            self.select_customer("Trading Partner", retailer)
            so.send_text_by_xpath(LocalElementLocator.START_DATE, date)
            so.click_element_by_xpath(LocalElementLocator.SERVICE)
            so.click_element_by_xpath(LocalElementLocator.DC4ROUTER)
            so.send_text_by_xpath(LocalElementLocator.DOCUMENT_TYPE, doc_type)
            so.click_element_by_xpath(LocalElementLocator.SEARCH_BTN)
            self.get_all_parcels(input_sheet, row)
            time.sleep(2)
        except NoSuchElementException:
            self.lo.log_to_file("ERROR",
                                "Fail in TransactionTrackerOperations.search_process_for_PDM() for: " + str(
                                    supplier) + "|" + str(retailer) + "|" + str(doc_type))

