'''

@ Author - Yogesh Pawar
@ Creation date - 09/21/2018
@ Description - Common Transaction Tracker Operation
'''

from Utilites import AppConstants
from Utilites.SeleniumOperations import SeleniumOperations
from Utilites.LogFileUtility import LogFileUtility
from Utilites.ExcelOperations import ExcelOperations
import time

class TransactionTrackerOperations:
    def __init__(self, task_type, driver, lo):
        self.v_task_type = task_type
        self.driver = driver
        self.lo = lo


    def select_customer(self, customer_type, customer_name):

        self.lo.log_to_file("INFO", "Executing method 'select_customer' from TransactionTrackerOperations")
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        print("Search for: " + str(customer_name))

        time.sleep(2)
        #driver.switch_to.frame(0)
        if customer_type == "Company":
            #self.driver.switch_to.frame(0)
            self.driver.find_element_by_xpath(
                "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/label/chosen-company/div/ul/li/input").send_keys(
                customer_name)
        if customer_type == "Trading Partner":
            #self.driver.switch_to.frame(0)
            TP_name = self.driver.find_element_by_xpath(
                "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[4]/label/chosen-trading-partner/div/ul/li/input")
            time.sleep(2)
            # driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[4]/label/chosen-trading-partner/div/ul").click()
            TP_name.send_keys(customer_name)

        time.sleep(2)
        count = self.driver.find_elements_by_xpath(".//*[contains(@id,'ui-select-choices-row-')]")
        for i in range(len(count)):
            if customer_type == "Company":
                customer_from_TT = self.driver.find_element_by_xpath(
                    ".//*[@id='ui-select-choices-row-0-" + str(i) + "']").text
            if customer_type == "Trading Partner":
                customer_from_TT = self.driver.find_element_by_xpath(
                    ".//*[@id='ui-select-choices-row-1-" + str(i) + "']").text
            if customer_name == customer_from_TT:
                if customer_type == "Company":
                    self.driver.find_element_by_xpath(".//*[@id='ui-select-choices-row-0-" + str(i) + "']").click()
                if customer_type == "Trading Partner":
                    self.driver.find_element_by_xpath(".//*[@id='ui-select-choices-row-1-" + str(i) + "']").click()
                print("Found matching customer name at position: " + str(i + 1))
        time.sleep(2)

    def get_parcel(self, input_sheet,row):
        self.lo.log_to_file("INFO", "Executing method 'get_parcel' from TransactionTrackerOperations")
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        eo = ExcelOperations(self.v_task_type, input_sheet)
        comment = ' '
        #print("========================================================================================")
        parcel_count = int(self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/spsui-feedback-container[4]/result-feedback/div/div/div/div[1]/strong").text)
        print("Total unique parcel count is: "+str(parcel_count))
        for i in range (parcel_count):
            document_id=self.driver.find_element_by_xpath(".//*[@id='parentTablesContainer']/div[2]/table/tbody[1]/tr["+str(i+1)+"]/td[5]").text
            status=self.driver.find_element_by_xpath(".//*[@id='parentTablesContainer']/div[2]/table/tbody[1]/tr["+str(i+1)+"]/td[1]").text
            parcel_ID=self.driver.find_element_by_xpath(".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr["+str(i+1)+"]/td[2]/span/a").text

            print(str(i+1)+") Parcel ID: "+str(parcel_ID)+" (Document ID: "+str(document_id)+") with status: "+str(status))
            comment=comment+str(i+1)+") Parcel ID: "+str(parcel_ID)+" (Document ID: "+str(document_id)+") with status: "+str(status)+"\n"
            if "CM" in document_id:
                eo.set_value(row, 8, "Data found for CREDIT MEMO")

                #comment=comment+"Credir Memo not found in Search result"+"\n"
                #comment = comment + str(i + 1) + ") Parcel ID: " + str(parcel_ID) + " (Document ID: " + str(document_id) + ") with status: " + str(status)

        #print("========================================================================================")
        eo.set_value(row,6,parcel_count)
        eo.set_value(row, 7, comment)
        self.driver.get("https://commerce.spscommerce.com/transaction-tracker/prod/transactions/")
        #so.click_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/a")
        time.sleep(5)

    def search_process_for_PDM(self,supplier,retailer,doc_type,date, input_sheet,row):

        print("=====================================Task Number: "+str(row)+"===================================")
        print("============================================================================================")
        self.lo.log_to_file("INFO", "Executing method 'search_process' from TransactionTrackerOperations")
        self.driver.switch_to.frame(0)
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        self.select_customer("Company",supplier)
        self.select_customer("Trading Partner",retailer)

        start_date = self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/label/input")
        time.sleep(2)
        start_date.clear()
        start_date.send_keys(date)
        time.sleep(2)
        service=self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/label/select")
        service.send_keys("DC4Router")
        time.sleep(2)
        document_type=self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/label/input")
        document_type.send_keys(doc_type)
        time.sleep(2)
        search_btn = self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/button")
        search_btn.click()
        time.sleep(3)
        clear_btn = self.driver.find_element_by_xpath("html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/a")
        #clear_btn.click()
        self.get_parcel(input_sheet,row)

    def search_process_for_process_test_file(self, supplier, retailer, doc_type,date, input_sheet,row):

        print("=====================================Task Number: " + str(row-1) + "===================================")
        print("============================================================================================")
        self.lo.log_to_file("INFO", "Executing method 'search_process_for_process_test_file' from TransactionTrackerOperations")
        self.driver.switch_to.frame(0)
        so = SeleniumOperations(self.v_task_type, self.driver, self.lo)
        self.select_customer("Company", supplier)
        self.select_customer("Trading Partner", retailer)

        start_date = self.driver.find_element_by_xpath(
            "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/label/input")
        time.sleep(2)
        start_date.clear()
        start_date.send_keys(date)
        time.sleep(2)
        service = self.driver.find_element_by_xpath(
            "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/label/select")
        service.send_keys("DC4Router")
        time.sleep(2)
        document_type = self.driver.find_element_by_xpath(
            "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/label/input")
        document_type.send_keys(doc_type)
        time.sleep(2)
        search_btn = self.driver.find_element_by_xpath(
            "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/button")
        search_btn.click()
        time.sleep(3)
        clear_btn = self.driver.find_element_by_xpath(
            "html/body/div[1]/section/section/div/div/section/div/div[1]/div[2]/div[5]/div/a")
        # clear_btn.click()
        #self.get_parcel(input_sheet, row)