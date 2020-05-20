from selenium import webdriver
import time
from Utilites.SeleniumOperations import SeleniumOperations
from Utilites.ExcelOperations import ExcelOperations
from Utilites.DC4_Utility import DC4_Utility
from Applications.Workflows.ProcessTestFiles.AppResources import AppConstants
from Applications.Workflows.ProcessTestFiles.AppResources import CommonLocators
from Utilites.Login import Login


class QB_Setup_Util:

    def __init__(self, task_type, lo, username, input_wb, v_driver):
        self.v_task_type = task_type
        self.v_driver = v_driver
        self.v_input_wb = input_wb
        self.v_data_sheet = self.v_input_wb.get_sheet_by_name('QB_Setup')
        # self.v_data_wb = openpyxl.load_workbook(AppConstants.PROCESS_TEST_FILES_INPUT_PATH)
        self.lo = lo
        self.v_username = username

    def retailer_v_check(self, v_supplier, v_retailer, v_document_type, current_row):
            v_document_type_1 = str(v_document_type)
            v_document_type_2 = '875'
            self.lo.log_to_file("INFO", "Login in to DC4 Prod")
            login = Login(self.v_task_type, self.v_driver, self.v_input_wb, self.lo)
            selenium_operations = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)

            excel_operations = ExcelOperations(self.v_task_type, self.v_data_sheet)

            self.lo.log_to_file("INFO", "Login in to DC4 Prod")
            login = Login(self.v_task_type, self.v_driver, self.v_input_wb, self.lo)
            selenium_operations = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)

            selenium_operations.click_element_by_xpath(AppConstants.DC4_TAB)

            dc4_utility = DC4_Utility(self.v_task_type, self.v_driver, self.lo)
            self.v_driver.find_element_by_xpath(AppConstants.DC4_COMPANY_NAME_TEXT_FIELD).send_keys(v_retailer)
            self.v_driver.find_element_by_xpath(AppConstants.DC4_COMPANY_NAME_SEARCH_CLICK).click()
            select_retailer = self.v_driver.find_element_by_xpath('//*[@id="table1:10:commandLink2"]').click()

            click_relationship = selenium_operations.click_element_by_xpath(CommonLocators.Relationship_Prod_Tab)
            search_retailer_relationship = selenium_operations.send_text_by_xpath(
                CommonLocators.Trading_Partner_Name_text_Field, v_supplier)
            selenium_operations.click_element_by_xpath(CommonLocators.click_search)

            # Select the Retailer company profile and check for the FI setup
            select_retailer_profile = selenium_operations.click_element_by_xpath(CommonLocators.Supplier_Profile_Link)

            # Profile Page Display
            show_option_click = selenium_operations.click_element_by_xpath(CommonLocators.show_click)

            counter = 2
            path = '//*[@id="form1:table1:0:table2"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(counter) + ']/td[10]'
            while (selenium_operations.check_exists_by_xpath(path)):

                service = selenium_operations.get_text_by_xpath(
                    '//*[@id="form1:table1:0:table2"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(counter) + ']/td[10]')
                print(service)
                doc_type = selenium_operations.get_text_by_xpath(
                    '//*[@id="form1:table1:0:table2"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(counter) + ']/td[3]')
                counter = counter+1
                print(doc_type)

                if doc_type == v_document_type_1:
                    if service != 'DoNotRoute' and 'WEBtoService':
                        print("850 capability is available")

                        retailer_version = selenium_operations.get_text_by_xpath(
                            '//*[@id="form1:table1:0:table2"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(
                                counter) + ']/td[8]')
                        capability_name = selenium_operations.get_text_by_xpath(
                            '//*[@id="form1:table1:0:table2:' + str(counter) + ':outputText14"]')
                        print(retailer_version)
                        print(capability_name)

                        if retailer_version == " ":
                            retailer_version = self.retailer_ver_check(doc_type, capability_name)
                            excel_operations.set_value(current_row, 10, retailer_version)
                            retailer_capability_version = selenium_operations.get_text_by_xpath(
                                '//*[@id="form1:table1:0:table2"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(
                                    counter) + ']/td[6]')
                            excel_operations.set_value(current_row, 11, retailer_capability_version)
                            self.v_input_wb.save(AppConstants.INPUT_FILE_PATH)
                            break
                        else:
                            excel_operations.set_value(current_row, 10, retailer_version)
                            retailer_capability_version = selenium_operations.get_text_by_xpath(
                                '//*[@id="form1:table1:0:table2"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(
                                    counter) + ']/td[6]')
                            excel_operations.set_value(current_row, 11, retailer_capability_version)
                            self.v_input_wb.save(AppConstants.INPUT_FILE_PATH)
                            break

                    elif service == 'DoNotRoute':
                        print("850 capability is not available")

    def retailer_ver_check(self, doc_type, retailer_capability_name):

        self.lo.log_to_file("INFO", "Login in to DC4 Pre_Prod")
        login = Login(self.v_task_type, self.v_driver, self.v_input_wb, self.lo)
        selenium_operations = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)

        selenium_operations.click_element_by_xpath(CommonLocators.DC4_ADMIN_TAB)

        selenium_operations.send_text_by_xpath(CommonLocators.DATATYPE_NAME_TEXTFIELD, retailer_capability_name)

        selenium_operations.click_element_by_xpath(CommonLocators.DATATYPE_SEARCH_BUTTON)

        retailer_FEDS_capability_name = selenium_operations.get_text_by_xpath(CommonLocators.FEDS_CAPABILITY)

        selenium_operations.send_text_by_xpath(CommonLocators.DATATYPE_NAME_TEXTFIELD, retailer_FEDS_capability_name)

        table_rows = self.v_driver.find_elements_by_xpath('//*[@id="form1:table1"]/table[2]/tbody/tr[1]/th[1]')

        total_rows = len(table_rows)-1

        print(total_rows)

        for counter in range(0, total_rows):

            retailer_version_value = selenium_operations.get_text_by_xpath('//*[@id="form1:table1"]/table[2]/tbody/tr['+ str(counter) +']/td[7]')
            if retailer_version_value == " ":
                pass
            else:
                return retailer_version_value

    def Supplier_Setup_Check (self, v_supplier, v_retailer, v_document_type, v_erp, current_row):
        v_document_type_1 = str(v_document_type)
        v_document_type_2 = '875'
        self.lo.log_to_file("INFO", "Login in to DC4 Prod")
        login = Login(self.v_task_type, self.v_driver, self.v_input_wb, self.lo)
        selenium_operations = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)

        excel_operations = ExcelOperations(self.v_task_type, self.v_data_sheet)

        self.lo.log_to_file("INFO", "Login in to DC4 Prod")
        login = Login(self.v_task_type, self.v_driver, self.v_input_wb, self.lo)
        selenium_operations = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)

        selenium_operations.click_element_by_xpath(AppConstants.DC4_TAB)

        dc4_utility = DC4_Utility(self.v_task_type, self.v_driver, self.lo)
        self.v_driver.find_element_by_xpath(AppConstants.DC4_COMPANY_NAME_TEXT_FIELD).send_keys(v_supplier)
        self.v_driver.find_element_by_xpath(AppConstants.DC4_COMPANY_NAME_SEARCH_CLICK).click()
        select_retailer = self.v_driver.find_element_by_xpath('//*[@id="table1:10:commandLink2"]').click()

        click_relationship = selenium_operations.click_element_by_xpath(CommonLocators.Relationship_Prod_Tab)
        search_retailer_relationship = selenium_operations.send_text_by_xpath(
            CommonLocators.Trading_Partner_Name_text_Field, v_retailer)
        selenium_operations.click_element_by_xpath(CommonLocators.click_search)

        # Select the Retailer company profile and check for the FI setup
        select_retailer_profile = selenium_operations.click_element_by_xpath(CommonLocators.Supplier_Profile_Link)

        # Profile Page Display
        show_option_click = selenium_operations.click_element_by_xpath(CommonLocators.show_click)

        counter = 2
        path = '//*[@id="form1:table1:0:table2"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(counter) + ']/td[10]'
        while (selenium_operations.check_exists_by_xpath(path)):

            service = selenium_operations.get_text_by_xpath(
                '//*[@id="form1:table1:0:table2"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(counter) + ']/td[10]')
            print(service)
            doc_type = selenium_operations.get_text_by_xpath(
                '//*[@id="form1:table1:0:table2"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(counter) + ']/td[3]')
            counter = counter + 1
            print(doc_type)
            print(v_erp)

            if doc_type == v_document_type_1:
                if service != 'DoNotRoute'and service != 'WEBtoService':
                    print("850 capability is already available")
                    print(v_document_type_1)

                else:
                    print('add new capability')
                    add_existing_capability = selenium_operations.click_element_by_xpath('//*[@id="form1:table1:0:table2:addExistingCapability"]/img')
                    time.sleep(2)

                    self.v_driver.switch_to.window(self.v_driver.window_handles[-1])
                    time.sleep(3)
                    self.v_driver.switch_to.frame(0)
                    time.sleep(2)

                    self.v_driver.find_element_by_xpath('//*[@id="form1:showDetailHeader1"]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]').click()
                    self.v_driver.find_element_by_xpath('//*[@id="form1:inputText3"]').send_keys('FI%')

                    time.sleep(3)

                    if v_erp == 'QB':
                        self.v_driver.find_element_by_xpath('//*[@id="form1:inputText4"]').send_keys('SPS QuickBooks Adaptor | RSX 7.2 | 850 - Legacy')
                        selenium_operations.click_element_by_xpath('//*[@id="form1:commandButton2"]/img')
                        print('850 QB exists')
                        try:
                            self.v_driver.find_element_by_xpath('//*[@id="form1:table1:0:tableSelectMany1"]')
                            capability_flag = 0
                        except:
                            capability_flag = 1

                    elif v_erp == 'Dwyer':
                        self.v_driver.find_element_by_xpath('//*[@id="form1:inputText4"]').send_keys('Dwyer Adaptor V7 850 V2 XML')
                        selenium_operations.click_element_by_xpath('//*[@id="form1:commandButton2"]/img')
                        print('850 QB exists')
                        try:
                            self.v_driver.find_element_by_xpath('//*[@id="form1:table1:0:tableSelectMany1"]')
                            capability_flag = 0
                        except:
                            capability_flag = 1
                    else:
                        self.v_driver.find_element_by_xpath('//*[@id="form1:inputText4"]').send_keys('SPS Fishbowl Adaptor | RSX 7.2 | 850 - Legacy')
                        selenium_operations.click_element_by_xpath('//*[@id="form1:commandButton2"]/img')
                        print('850 QB exists')
                        try:
                            self.v_driver.find_element_by_xpath('//*[@id="form1:table1:0:tableSelectMany1"]')
                            capability_flag = 0
                        except:
                            capability_flag = 1

                    if capability_flag == 0:
                        self.v_driver.find_element_by_xpath('//*[@id="form1:table1:0:tableSelectMany1"]').click()
                        Choose = selenium_operations.double_click_by_xpath('//*[@id="form1:table1:commandButton1"]')
                        time.sleep(10)

                    else:
                        self.v_driver.close()
                        print ('Add new capability')

                        self.v_driver.switch_to.window(self.v_driver.window_handles[0])
                        time.sleep(2)
                        selenium_operations.click_element_by_xpath('//*[@id="form1:table1:0:table2:createCapability"]/img')
                        time.sleep(5)

                        self.v_driver.switch_to.window(self.v_driver.window_handles[-1])
                        time.sleep(3)
                        self.v_driver.switch_to.frame(0)
                        time.sleep(2)

                        self.v_driver.find_element_by_xpath('//*[@id="form1:findService"]').send_keys('1007')

                        if v_erp == 'QB':
                            self.v_driver.find_element_by_xpath('//*[@id="form1:findDataType"]').send_keys('106967')
                            selenium_operations.click_element_by_xpath('//*[@id="form1:commandButton1"]/img')

                        elif v_erp =='Dwwyer':
                            self.v_driver.find_element_by_xpath('//*[@id="form1:findDataType"]').send_keys('91552')
                            selenium_operations.click_element_by_xpath('//*[@id="form1:commandButton1"]/img')

                        else:
                            self.v_driver.find_element_by_xpath('//*[@id="form1:findDataType"]').send_keys('109095')
                            selenium_operations.click_element_by_xpath('//*[@id="form1:commandButton1"]/img')
                self.v_driver.switch_to.window(self.v_driver.window_handles[0])
                time.sleep(2)
                counter = 2
                path = '//*[@id="form1:table1:0:table2"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(
                    counter) + ']/td[10]'
                while (selenium_operations.check_exists_by_xpath(path)):
                    service = selenium_operations.get_text_by_xpath(
                        '//*[@id="form1:table1:0:table2"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(
                            counter) + ']/td[10]')
                    print(service)
                    doc_type = selenium_operations.get_text_by_xpath(
                        '//*[@id="form1:table1:0:table2"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(
                            counter) + ']/td[3]')
                    print(doc_type)
                    capability_uid = selenium_operations.get_text_by_xpath('//*[@id="form1:table1:0:table2:column24"]')
                    print(capability_uid)
                    profile_uid = selenium_operations.get_text_by_xpath('//*[@id="form1:table1:0:outputText1"]')
                    print(profile_uid)

                    if doc_type == v_document_type_1:
                        if service != 'DoNotRoute' and service != 'WEBtoService':
                            print("850 capability exist")
                            selenium_operations.click_element_by_xpath('//*[@id="form1:table1:0:table2:' + str(counter-2) + ':tableSelectMany1"]')
                            print("Capability selected")
                            selenium_operations.click_element_by_xpath('//*[@id="form1:table1:0:table2:disableCapability"]/img')
                            time.sleep(10)
                            break
                    counter = counter + 1
                path = 'Close'

