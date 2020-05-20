'''

@ Author - Karan Pandya
@ Creation date - 10/19/2018
@ Description - Main Script of Web Fulfillment
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
from Applications.Workflows.ErrorHospital.Scripts.ErrorHospital_Utility import ErrorHospital_Utility
from Utilites.ExcelOperations import ExcelOperations
from Applications.Workflows.Covalent_Web_Fulfillment.AppResources import LocalElementLocator
from openpyxl import load_workbook
from Applications.Workflows.ErrorHospital.Scripts.Error_Document_rejected import Error_Document_rejected
import re
import easygui
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Web_Fulfillment_Utility:

    def __init__(self, task_type, driver, input_wb, lo, username, db_object, driver_mv):
        self.v_task_type = task_type
        self.v_input_wb = input_wb
        self.lo = lo
        self.v_username = username
        self.v_driver = driver
        self.db_object = db_object
        self.v_username = username
        self.v_driver_mv = driver_mv

    def get_info_from_JIRA(self):
        v_supplier_name = ''

        v_email_address = ''
        v_phone_number = ''
        v_retailer_name = ''
        v_billing_address = ''
        v_vendor_number = ''
        v_retailer_web_company_uid = ''
        v_account_number = ''
        v_retailer_dc4_company_uid = ''
        v_contact_name = ''
        selenium_operation_obj = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)

        v_salesforce_id = selenium_operation_obj.get_text_by_xpath(LocalElementLocator.JIRA_SALESFORCE_ID_XPATH)

        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.JIRA_SUPPLIER_NAME_XPATH):
            v_supplier_name = selenium_operation_obj.get_text_by_xpath(LocalElementLocator.JIRA_SUPPLIER_NAME_XPATH)
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.JIRA_EMAIL_ADDRESS_XPATH):
            v_email_address = selenium_operation_obj.get_text_by_xpath(LocalElementLocator.JIRA_EMAIL_ADDRESS_XPATH)
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.JIRA_PHONE_NUMBER_XPATH):
            v_phone_number = selenium_operation_obj.get_text_by_xpath(LocalElementLocator.JIRA_PHONE_NUMBER_XPATH)
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.JIRA_RETAILER_NAME_XPATH):
            v_retailer_name = selenium_operation_obj.get_text_by_xpath(LocalElementLocator.JIRA_RETAILER_NAME_XPATH)
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.JIRA_BILLING_ADDRESS_XPATH):
            v_billing_address = selenium_operation_obj.get_text_by_xpath(LocalElementLocator.JIRA_BILLING_ADDRESS_XPATH)
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.JIRA_VENDOR_NUMBER_XPATH):
            v_vendor_number = selenium_operation_obj.get_text_by_xpath(LocalElementLocator.JIRA_VENDOR_NUMBER_XPATH)
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.JIRA_RETAILER_COMPANY_WEB_UID_XPATH):
            v_retailer_web_company_uid = selenium_operation_obj.get_text_by_xpath(LocalElementLocator.JIRA_RETAILER_COMPANY_WEB_UID_XPATH)
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.JIRA_ACCOUNT_NUMBER_XPATH):
            v_account_number = selenium_operation_obj.get_text_by_xpath(LocalElementLocator.JIRA_ACCOUNT_NUMBER_XPATH)
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.JIRA_RETAILER_DC4_ID_XPATH):
            v_retailer_dc4_company_uid = selenium_operation_obj.get_text_by_xpath(LocalElementLocator.JIRA_RETAILER_DC4_ID_XPATH)
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.JIRA_CONTACT_NAME_XPATH):
            v_contact_name = selenium_operation_obj.get_text_by_xpath(LocalElementLocator.JIRA_CONTACT_NAME_XPATH)

        print(v_salesforce_id+"\n"+v_supplier_name+"\n"+v_email_address+"\n"+v_phone_number+"\n"+v_retailer_name+"\n"+v_billing_address+"\n"+v_vendor_number+"\n"+v_retailer_web_company_uid+"\n"+v_account_number+"\n"+v_retailer_dc4_company_uid+"\n"+v_contact_name)

        return v_supplier_name, v_email_address, v_phone_number, v_retailer_name, v_billing_address, v_vendor_number, v_retailer_web_company_uid, v_account_number, v_retailer_dc4_company_uid, v_contact_name, v_salesforce_id

    def get_info_from_salesforce(self, v_salesforce_id):

        v_supplier_name = ''
        v_email_address = ''
        v_phone_number = ''
        v_retailer_name = ''
        client_uid = ''
        v_billing_address = []
        v_vendor_number = ''
        v_retailer_web_company_uid = ''
        v_account_number = ''
        v_retailer_dc4_company_uid = ''
        v_contact_name = ''
        selenium_operation_obj = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        salesforce_link = 'https://spscommerce.my.salesforce.com/'+ v_salesforce_id
        self.v_driver.get(salesforce_link)
        v_supplier_name = selenium_operation_obj.get_text_by_id(LocalElementLocator.SUPPLIER_NAME_ID)
        v_retailer_name = selenium_operation_obj.get_text_by_id(LocalElementLocator.RETAILER_NAME_ID)
        v_contact_name = selenium_operation_obj.get_text_by_id(LocalElementLocator.CONTACT_NAME_ID)
        v_email_address = selenium_operation_obj.get_text_by_id(LocalElementLocator.EMAIL_ADDRESS_ID)
        selenium_operation_obj.scroll_into_view_by_id(LocalElementLocator.STATUS_DESCRIPTION_ID)
        selenium_operation_obj.double_click_by_id(LocalElementLocator.STATUS_DESCRIPTION_ID)
        time.sleep(1)
        status_description_pre = selenium_operation_obj.get_attribute_value_by_id('00N50000001MXp7')
        print(status_description_pre)
        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.STATUS_DESCRIPTION_OK_BUTTON_XPATH)
        if 'ID' in status_description_pre:
            client_uid = status_description_pre.split('ID')[1]
            client_uid = client_uid.split('Retailer')[0]
            client_uid = re.sub('[^A-Za-z0-9]+', '', client_uid)
            retailer_uid = status_description_pre.split('ID')[2]
            if '\n' in retailer_uid:
                retailer_uid = retailer_uid.split('\n')[0]
            retailer_uid = re.sub('[^A-Za-z0-9]+', '', retailer_uid)
            print("Retailer UID: " + str(retailer_uid))
            print(client_uid)
        selenium_operation_obj.scroll_into_view_by_id(LocalElementLocator.VENDOR_NUMBER_ID)
        v_vendor_number = selenium_operation_obj.get_text_by_id(LocalElementLocator.VENDOR_NUMBER_ID)
        #self.v_driver.find_element_by_link_text(v_supplier_name).click()
        selenium_operation_obj.click_element_by_link_text(v_supplier_name)
        v_account_number = selenium_operation_obj.get_text_by_id(LocalElementLocator.ACCOUNT_NUMBER_ID)
        v_phone_number = selenium_operation_obj.get_text_by_id(LocalElementLocator.PHONE_NUMBER_ID)
        selenium_operation_obj.double_click_by_id(LocalElementLocator.FULL_ADDRESS_ID)
        v_billing_address.append(selenium_operation_obj.get_text_by_id(LocalElementLocator.STREET_ADDRESS_ID))
        v_billing_address.append(selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.CITY_ADDRESS_ID))
        v_billing_address.append(selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.STATE_ADDRESS_ID))
        v_billing_address.append(selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.ZIPCODE_ADDRESS_ID))
        print(v_billing_address)
        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.ADDRESS_CANCEL_BUTTON_XPATH)
        self.v_driver.get(salesforce_link)
        selenium_operation_obj.click_element_by_link_text(v_retailer_name)
        if selenium_operation_obj.get_text_by_id(LocalElementLocator.RETAILER_DC4_UID_ON_RETAILER_PAGE) != None:
            v_retailer_dc4_company_uid = selenium_operation_obj.get_text_by_id(LocalElementLocator.RETAILER_DC4_UID_ON_RETAILER_PAGE)
        #selenium_operation_obj.scroll_into_view_by_xpath(LocalElementLocator.RETAILER_SETUP_LINK_PATH)
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.RETAILER_SETUP_LINK_PATH):
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.RETAILER_SETUP_LINK_PATH)
            v_retailer_web_company_uid = selenium_operation_obj.get_text_by_id(LocalElementLocator.RETAILER_WEB_COMPANY_UID)
            if selenium_operation_obj.get_text_by_id(LocalElementLocator.RETAILER_DC4_UID_ON_SETUP_PAGE) != None:
                v_retailer_dc4_company_uid = selenium_operation_obj.get_text_by_id(LocalElementLocator.RETAILER_DC4_UID_ON_SETUP_PAGE)
        return v_supplier_name, v_email_address, v_phone_number, v_retailer_name, v_billing_address, v_vendor_number, v_retailer_web_company_uid, v_account_number, v_retailer_dc4_company_uid, v_contact_name, client_uid, retailer_uid

    def run_setup_tool(self, v_salesforce_id, v_jira_supplier_name, v_email_address, v_phone_number, v_jira_retailer_name, v_billing_address, v_vendor_number, v_retailer_web_company_uid, v_account_number, v_retailer_dc4_company_uid, v_contact_name, client_uid, retailer_uid):
        selenium_operation_obj = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        supplier_info = []
        retailer_info = []
        supplier_dc4_company_info = []
        retailer_dc4_company_info = []
        v_phone_number = re.sub('[^0-9]+', '', v_phone_number)
        if len(v_phone_number) >= 10:
            v_phone_number = v_phone_number[len(v_phone_number) - 10:]

        dc4_company_name_check_query = "SELECT * from supplier_info where jira_name = %s"
        dc4_company_name_data_query = (v_jira_supplier_name,)
        supplier_info = self.db_object.get_data_query(dc4_company_name_check_query, dc4_company_name_data_query)
        print(supplier_info)
        #print(v_supplier_dc4_name_list[0][0])
        if len(supplier_info) == 0:
            v_supplier_dc4_uid = easygui.enterbox("We don't have supplier DC4 UID in our system\nKindly provide accurate supplier DC4 UID so that we can update it in our system for future use.")
        else:
            dc4_uid_get_query = "SELECT * from dc4_company_info where company_name = %s"
            dc4_uid_get_data = (supplier_info[0][1],)
            supplier_dc4_company_info = self.db_object.get_data_query(dc4_uid_get_query, dc4_uid_get_data)

            if len(supplier_dc4_company_info) == 0:
                v_supplier_dc4_uid = easygui.enterbox("We don't have supplier DC4 UID in our system\nKindly provide accurate supplier DC4 UID so that we can update it in our system for future use.")
            else:
                v_supplier_dc4_uid = supplier_dc4_company_info[0][1]
        dc4_company_name_check_query = "SELECT * from retailer_info where jira_name = %s"
        dc4_company_name_data_query = (v_jira_retailer_name,)
        retailer_info = self.db_object.get_data_query(dc4_company_name_check_query,
                                                                 dc4_company_name_data_query)
        print(retailer_info)
        if len(retailer_info) == 0:
            if len(v_retailer_dc4_company_uid) <=2:
                v_retailer_dc4_company_uid = easygui.enterbox(
                "We don't have retailer DC4 UID in our system\nKindly provide accurate supplier DC4 UID so that we can update it in our system for future use.")
        else:
            dc4_uid_get_query = "SELECT * from dc4_company_info where company_name = %s"
            dc4_uid_get_data = (retailer_info[0][1],)
            retailer_dc4_company_info = self.db_object.get_data_query(dc4_uid_get_query, dc4_uid_get_data)

            if len(retailer_dc4_company_info) != 0:
                v_retailer_dc4_company_uid = retailer_dc4_company_info[0][1]
        if selenium_operation_obj.check_exists_by_id(LocalElementLocator.DC4_ACTIVE_TAB_ID) == True:
            selenium_operation_obj.click_element_by_id(LocalElementLocator.DC4_ACTIVE_TAB_ID)
        elif selenium_operation_obj.check_exists_by_id(LocalElementLocator.DC4_INACTIVE_TAB_ID) == True:
            selenium_operation_obj.click_element_by_id(LocalElementLocator.DC4_INACTIVE_TAB_ID)
        elif selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.DC4_TAB_XPATH) == True:
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.DC4_TAB_XPATH)
        # if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.DC4_TIME_OUT_XPATH) == True:
        #     selenium_operation_obj.click_element_by_xpath(LocalElementLocator.DC4_TIME_OUT_XPATH)
        selenium_operation_obj.send_text_by_id(LocalElementLocator.DC4_SEARCH_COMPANY_UID_ID, v_supplier_dc4_uid)
        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.DC4_COMPANY_SEARCH_BUTTON_XPATH)
        if selenium_operation_obj.check_exists_by_id(LocalElementLocator.DC4_FIRST_COMPANY_ID) == True:
            selenium_operation_obj.click_element_by_id(LocalElementLocator.DC4_FIRST_COMPANY_ID)

        else:
            selenium_operation_obj.click_element_by_xpath('//*[@id="table1:1:commandLink2"]')

        v_supplier_dc4_name = selenium_operation_obj.get_text_by_xpath(LocalElementLocator.DC4_COMPANY_NAME_XPATH).split('Summary - ')[1]



        self.edi_creation(client_uid, v_supplier_dc4_name, v_jira_retailer_name)



        #selenium_operation_obj.click_element_by_xpath(LocalElementLocator.DC4_SETUP_TOOL_TAB_XPATH)
        selenium_operation_obj.click_element_by_id(LocalElementLocator.SETUP_TOOL_WEBFORMS_CHECK_BOX_ID)
        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.BEGIN_SETUP_BUTTON_XPATH)
        selenium_operation_obj.send_text_by_id(LocalElementLocator.RETAILER_COMPANY_UID_ID, v_retailer_dc4_company_uid)
        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.TRADING_PARTNER_NEXT_BUTTON_XPATH)
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.MULTIPLE_RETAILER_WEB_COMPANY_UID_XPATH) == True:
            index = 2
            retailer_web_company_path = '//*[@id="_idJsp24"]/table/tbody/tr/td/table/tbody/tr['+str(index)+']/td[3]'
            while(selenium_operation_obj.check_exists_by_xpath(retailer_web_company_path) != False):
                print(retailer_dc4_company_info)
                if len(retailer_dc4_company_info) == 0:
                    easygui.msgbox("We don't have retailer web company info in our library. Please select correct web comapny and click on OK")
                    selenium_operation_obj.click_element_by_xpath(
                        LocalElementLocator.TRADING_PARTNER_NEXT_BUTTON_XPATH_2)
                    break
                elif selenium_operation_obj.get_text_by_xpath(retailer_web_company_path) == str(retailer_dc4_company_info[0][2]):
                    selenium_operation_obj.click_element_by_xpath('//*[@id="_idJsp24:'+str(index-2)+':_idJsp29"]')
                    selenium_operation_obj.click_element_by_xpath(LocalElementLocator.TRADING_PARTNER_NEXT_BUTTON_XPATH_2)
                    break
                index = index+1
                retailer_web_company_path = '//*[@id="_idJsp24"]/table/tbody/tr/td/table/tbody/tr['+str(index)+']/td[3]'
        while selenium_operation_obj.check_exists_by_id(LocalElementLocator.RETAILER_COMPANY_UID_ID) != False:
            easygui.msgbox(
                "We don't have supplier DC4 UID in our system\nKindly provide accurate supplier DC4 UID so that we can update it in our system for future use.")
            v_retailer_dc4_company_uid = selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.RETAILER_COMPANY_UID_ID)
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.TRADING_PARTNER_NEXT_BUTTON_XPATH)

        qly_value = None
        envID_value = None
        grpID_value = None
        TPID = []
        profile_flag = 0
        number_of_profile, qly_value, envID_value, grpID_value, TPID, profile_flag = self.begin_setup(v_salesforce_id, v_jira_supplier_name, v_email_address, v_phone_number, v_jira_retailer_name, v_billing_address, v_vendor_number, v_retailer_web_company_uid, v_account_number, v_retailer_dc4_company_uid, v_contact_name, supplier_info, supplier_dc4_company_info, retailer_info, retailer_dc4_company_info, 0, v_supplier_dc4_name, qly_value, grpID_value, envID_value, TPID, client_uid, profile_flag, retailer_uid)
        if number_of_profile == 0:
            self.v_driver.switch_to.window(self.v_driver.window_handles[0])
            time.sleep(2)
            return
        flag1 = 1
        while selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.ANOTHER_PROFILE_XPATH) == 1:


            flag1 = easygui.ynbox('It seems there are more profiles to be filled. Let us begin.')
            if (flag1):
                temp_setup_summary = selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.TEMP_SETUP_SUMMARY_ID)
                self.get_info_from_summary(temp_setup_summary, v_jira_supplier_name, v_jira_retailer_name,
                                           v_retailer_dc4_company_uid, v_salesforce_id)

                dc4_company_name_check_query = "SELECT * from supplier_info where jira_name = %s"
                dc4_company_name_data_qu3ery = (v_jira_supplier_name,)
                supplier_info = self.db_object.get_data_query(dc4_company_name_check_query, dc4_company_name_data_query)

                dc4_uid_get_query = "SELECT * from dc4_company_info where company_name = %s"
                dc4_uid_get_data = (supplier_info[0][1],)
                supplier_dc4_company_info = self.db_object.get_data_query(dc4_uid_get_query, dc4_uid_get_data)

                dc4_company_name_check_query = "SELECT * from retailer_info where jira_name = %s"
                dc4_company_name_data_query = (v_jira_retailer_name,)
                retailer_info = self.db_object.get_data_query(dc4_company_name_check_query,
                                                              dc4_company_name_data_query)

                dc4_uid_get_query = "SELECT * from dc4_company_info where company_name = %s"
                dc4_uid_get_data = (retailer_info[0][1],)
                retailer_dc4_company_info = self.db_object.get_data_query(dc4_uid_get_query, dc4_uid_get_data)


                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.SELECT_ANOTHER_PROFILE_XPATH)
                number_of_profile, qly_value, envID_value, grpID_value, TPID, profile_flag = self.begin_setup(v_salesforce_id,
                                                                                                v_jira_supplier_name,
                                                                                                v_email_address,
                                                                                                v_phone_number,
                                                                                                v_jira_retailer_name,
                                                                                                v_billing_address,
                                                                                                v_vendor_number,
                                                                                                v_retailer_web_company_uid,
                                                                                                v_account_number,
                                                                                                v_retailer_dc4_company_uid,
                                                                                                v_contact_name,
                                                                                                supplier_info,
                                                                                                supplier_dc4_company_info,
                                                                                                retailer_info,
                                                                                                retailer_dc4_company_info,
                                                                                                number_of_profile, v_supplier_dc4_name,
                                                                                                qly_value, grpID_value,
                                                                                                envID_value, TPID, client_uid, profile_flag, retailer_uid)
            else:
                flag1 = 2
                break

        if flag1 == 1:
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.NO_ANOTHER_PROFILE_NEXT_BUTTON_XPATH)
        else:
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.ANOTHER_PROFILE_NEXT_BUTTON_XPATH)


        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.DC4_SETUP_SUMMARY_SAVE_XPATH) == True:
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.DC4_SETUP_SUMMARY_SAVE_XPATH)
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.NEXT_BUTTON_XPATH) == True:
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.NEXT_BUTTON_XPATH)

        setup_summary, email_summary = self.copy_email_and_setup_summary()
        email_summary_string = "\n\n==================================================================== \n\nEmail Summary:\n\n" + '\n\n==================================================================== \n\nEmail Summary:\n\n'.join(
            email_summary)
        print(email_summary_string)
        dc4_setup_summary = "Hi,\n\nPFB the Setup details \n\n==========================*SUMMARY*================================== \n\n*PROD SETUP TOOL SUMMARY*\n\n"+setup_summary+"\n"+email_summary_string+"\n\nThank You"
        print(dc4_setup_summary)
        self.get_info_from_summary(setup_summary, v_jira_supplier_name, v_jira_retailer_name, v_retailer_dc4_company_uid, v_salesforce_id)
        ISA_ID = qly_value+' / '+envID_value+' / '+grpID_value
        print(ISA_ID)
        print(TPID)

        self.v_driver.switch_to.window(self.v_driver.window_handles[0])
        time.sleep(2)
        t1 = threading.Thread(target=self.update_salesforce_project, args = (v_salesforce_id, ISA_ID, TPID, v_supplier_dc4_uid, dc4_setup_summary))
        t2 = threading.Thread(target=self.minivan_route, args= (client_uid, retailer_uid, TPID[0]))
        t1.start()
        t2.start()

        t1.join()
        t2.join()

        #self.update_salesforce_project(v_salesforce_id, ISA_ID, TPID, v_supplier_dc4_uid, dc4_setup_summary)


    def begin_setup(self,  v_salesforce_id, v_jira_supplier_name, v_email_address, v_phone_number, v_jira_retailer_name, v_billing_address, v_vendor_number, v_retailer_web_company_uid, v_account_number, v_retailer_dc4_company_uid, v_contact_name, supplier_info, supplier_dc4_company_info, retailer_info, retailer_dc4_company_info, number_of_profile, v_supplier_dc4_name, qly_value, grpID_value, envID_value, TPID, client_uid, profile_flag, retailer_uid):

        selenium_operation_obj = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)

        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.MULTIPLE_PROFILES_XPATH) == True:
            if len(retailer_info) != 0 and profile_flag == 0:
                correct_profiles = retailer_info[0][2]
                correct_profiles_list = correct_profiles.split(' ')
                profile_uid = correct_profiles_list[number_of_profile].split('-')[0]
                index = 2
                profile_uid_xpath = '//*[@id="profilesTable"]/table/tbody/tr[2]/td/table/tbody/tr['+str(index)+']/td[3]'
                while selenium_operation_obj.check_exists_by_xpath(profile_uid_xpath) != False:
                    if profile_uid == selenium_operation_obj.get_text_by_xpath(profile_uid_xpath):
                        selenium_operation_obj.click_element_by_xpath('//*[@id="profilesTable:'+str(index-2)+':_idJsp19"]')
                        break
                    index = index+1
                    profile_uid_xpath = '//*[@id="profilesTable"]/table/tbody/tr[2]/td/table/tbody/tr[' + str(
                        index) + ']/td[3]'
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.SELECT_PROFILE_XPATH)
                TPID_value = selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.TPID_VALUE_ID)
                TPID.append(TPID_value[:3]+correct_profiles_list[number_of_profile].split('-')[1]+TPID_value[6:])
                selenium_operation_obj.send_text_by_id(LocalElementLocator.TPID_VALUE_ID, TPID[number_of_profile])
                easygui.msgbox('Please Verify TPID')
            else:
                profile_flag = 1
                flag = easygui.ynbox('Please click YES if you know which profile to choose else click NO')
                if (flag):
                    easygui.msgbox('Please select the correct profile and click on OK')
                    selenium_operation_obj.click_element_by_xpath(LocalElementLocator.SELECT_PROFILE_XPATH)
                    TPID.append(selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.TPID_VALUE_ID))
                    easygui.msgbox('Please Verify TPID')
                    profile_flag = 1

                else:
                    self.v_driver.save_screenshot(AppConstants.APP_RUNNER_PATH + v_salesforce_id + '.png')
                    return 0, None, None, None, None, None


        elif selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.ONLY_PROFILE_XPATH) == True:
            profile_flag = 1
            id = selenium_operation_obj.get_text_by_xpath(LocalElementLocator.RETAILER_PROFILE_ISA_ID_XPATH)
            retailer_profile_isa_id = id.split('Qual: ')[1]
            qly = retailer_profile_isa_id.split('\n')[0]
            env_id = retailer_profile_isa_id.split('ID: ')[1]
            env_id = env_id.split('\n')[0]
            retailer_profile_isa_id = qly + env_id
            print(retailer_profile_isa_id)
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.ONLY_PROFILE_XPATH)
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.SELECT_PROFILE_XPATH)
            if retailer_profile_isa_id == retailer_uid:
                TPID.append(selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.TPID_VALUE_ID))
            else:
                easygui.msgbox('Please Verify TPID')
                TPID.append(selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.TPID_VALUE_ID))

        else:

            self.v_driver.save_screenshot(AppConstants.APP_RUNNER_PATH + v_salesforce_id + '.png')
            return 0, None, None, None, None, None
        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.PROFILE_SELECTION_NEXT_BUTTON_XPATH)
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.CHECK_EXISTING_WEB_COMPANY_XPATH) == True:
            if '*' in selenium_operation_obj.get_text_by_xpath(LocalElementLocator.WEB_COMPANY_VENDOR_NUMBER_TAG_XPATH):
                if len(v_vendor_number) <= 1:
                    selenium_operation_obj.send_text_by_xpath(LocalElementLocator.WC_VENDOR_NUMBER_TEXT_XPATH, client_uid[2:])
                    # flag = easygui.ynbox('If you have correct vendor number click YES else NO')
                    # if (flag):
                    #     easygui.msgbox('Please Enter valid vendor number and click on OK')
                    #
                    # else:
                    #     self.v_driver.save_screenshot(AppConstants.APP_RUNNER_PATH + v_salesforce_id + '.png')
                    #     return 0, None, None, None, None, None
                else:
                    selenium_operation_obj.send_text_by_xpath(LocalElementLocator.WC_VENDOR_NUMBER_TEXT_XPATH, v_vendor_number)
            if '*' in selenium_operation_obj.get_text_by_xpath(LocalElementLocator.WEB_COMPANY_LOCATION_NAME_TAG_XPATH):
                selenium_operation_obj.send_text_by_xpath(LocalElementLocator.WC_LOCATION_NAME_TEXT_XPATH, 'USA')
            if '*' in selenium_operation_obj.get_text_by_xpath(LocalElementLocator.WC_ACCOUNT_NUMBER_TEXT_XPATH):
                selenium_operation_obj.send_text_by_xpath(LocalElementLocator.WC_ACCOUNT_NUMBER_TEXT_XPATH, v_account_number)

            if v_billing_address[3] != '':
                selenium_operation_obj.send_text_by_xpath(LocalElementLocator.WC_ZIP_CODE_TEXT_XPATH, v_billing_address[3])
            else:
                selenium_operation_obj.send_text_by_xpath(LocalElementLocator.WC_ZIP_CODE_TEXT_XPATH, '0000')
            selenium_operation_obj.send_text_by_xpath(LocalElementLocator.WC_TELEPHONE_TEXT_XPATH, v_phone_number)
            selenium_operation_obj.send_text_by_xpath(LocalElementLocator.WC_FACSIMILE_TEXT_XPATH, v_phone_number)
            if v_billing_address[0] != '' and v_billing_address[1] != '' and v_billing_address[2] != '':
                selenium_operation_obj.send_text_by_xpath(LocalElementLocator.WC_ADDRESS_TEXT_XPATH,
                                                          v_billing_address[0])
                selenium_operation_obj.send_text_by_xpath(LocalElementLocator.WC_CITY_TEXT_XPATH, v_billing_address[1])
                selenium_operation_obj.send_text_by_xpath(LocalElementLocator.WC_STATE_TEXT_XPATH, v_billing_address[2])
            else:
                easygui.msgbox("Please add billing address manually and click OK")
            # if '*' in selenium_operation_obj.get_text_by_xpath(LocalElementLocator.WM_DUNS_NUMBER_TAG_XPATH):
            #     flag = easygui.ynbox('If you have correct Duns number click YES else NO')
            #     if (flag):
            #         easygui.msgbox('Please Enter valid vendor number and click on OK')
            #
            #     else:
            #         self.v_driver.save_screenshot(AppConstants.APP_RUNNER_PATH + v_salesforce_id + '.png')
            #         return 0, None, None, None, None, None
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.WC_CREATE_NEXT_BUTTON_XPATH)

            while selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.WC_CREATE_NEXT_BUTTON_XPATH) != False:
                easygui.msgbox('Please enter valid data and click on OK')
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.WC_CREATE_NEXT_BUTTON_XPATH)
            contact_name = selenium_operation_obj.get_attribute_value_by_id('_idJsp28')
            if 'unknown' in v_contact_name.lower():
                easygui.msgbox('Please enter conatct name manually and click on OK')
                # if v_contact_name not in contact_name:
                #     selenium_operation_obj.send_text_by_id('_idJsp28',
                #                                                contact_name + " " + v_contact_name)
            else:
                selenium_operation_obj.send_text_by_id('_idJsp28', v_contact_name)
            email_address = selenium_operation_obj.get_attribute_value_by_id('_idJsp29')
            if email_address != None:
                if v_email_address not in email_address:
                    selenium_operation_obj.send_text_by_id('_idJsp29',
                                                           email_address + " " + v_email_address)
            else:
                selenium_operation_obj.send_text_by_id('_idJsp29', v_email_address)
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.USE_EXISTING_WC_XPATH)


        else:
            if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.MULTIPLE_WEB_COMPANY_XPATH) == True:
                index = 2
                wc_company_xpath = '//*[@id="_idJsp24"]/table/tbody/tr/td/table/tbody/tr['+str(index)+']/td[2]'
                while selenium_operation_obj.check_exists_by_xpath(wc_company_xpath) != False:
                    if len(supplier_dc4_company_info) != 0:
                        if selenium_operation_obj.get_text_by_xpath(wc_company_xpath) == supplier_dc4_company_info[0][2]:
                            selenium_operation_obj.click_element_by_xpath('//*[@id="_idJsp24:'+str(index-2)+':_idJsp25"]')
                            break
                    else:
                        easygui.msgbox("Please select correct web company and click on OK")
                        break
                    index = index+1
                    wc_company_xpath = '//*[@id="_idJsp24"]/table/tbody/tr/td/table/tbody/tr[' + str(index) + ']/td[2]'
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.USE_EXISTING_WC_XPATH)
            if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.USE_EXISTING_WC_XPATH) == True:
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.USE_EXISTING_WC_XPATH)
            if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.WEB_MEMBER_SELECT_BUTTON_XPATH) == True:
                if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.MULTIPLE_WEB_MEMBER_XPATH) == True:
                    index = 2
                    web_member_uid_xpath = '//*[@id="_idJsp19"]/table/tbody/tr[2]/td/table/tbody/tr['+str(index)+']/td[2]'
                    while selenium_operation_obj.check_exists_by_xpath(web_member_uid_xpath) != False:
                        if len(supplier_dc4_company_info) != 0:
                            if selenium_operation_obj.get_text_by_xpath(web_member_uid_xpath) == supplier_dc4_company_info[0][3]:
                                selenium_operation_obj.click_element_by_xpath('//*[@id="_idJsp19:'+str(index - 2)+':_idJsp20"]')

                                break
                        else:
                            easygui.msgbox("Please select correct web member UID and click on OK")
                            break
                        index = index + 1
                        web_member_uid_xpath = '//*[@id="_idJsp19"]/table/tbody/tr[2]/td/table/tbody/tr[' + str(
                            index) + ']/td[2]'
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.WEB_MEMBER_SELECT_BUTTON_XPATH)

            contact_name = selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.WM_INFO_CONTACT_NAME_ID)
            if contact_name != None:
                if v_contact_name not in contact_name and 'unknown' not in v_contact_name.lower():
                    selenium_operation_obj.send_text_by_id(LocalElementLocator.WM_INFO_CONTACT_NAME_ID, contact_name+" "+v_contact_name)

            elif 'unknown' not in v_contact_name.lower():
                selenium_operation_obj.send_text_by_id(LocalElementLocator.WM_INFO_CONTACT_NAME_ID, v_contact_name)
            else:
                easygui.msgbox('Please enter contact name mannually and click on OK')
            email_address = selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.WM_INFO_EMAIL_ID)
            if email_address != None:
                if v_email_address not in email_address:
                    selenium_operation_obj.send_text_by_id(LocalElementLocator.WM_INFO_EMAIL_ID, email_address+" "+v_email_address)
            else:
                selenium_operation_obj.send_text_by_id(LocalElementLocator.WM_INFO_EMAIL_ID, v_email_address)

            if '*' in selenium_operation_obj.get_text_by_xpath(LocalElementLocator.WM_ACCOUNT_ID_TAG_XPATH):
                selenium_operation_obj.send_text_by_id(LocalElementLocator.WM_ACCOUNT_ID_TEXT_ID, v_account_number)
            if '*' in selenium_operation_obj.get_text_by_xpath(LocalElementLocator.WM_VENDOR_NUMBER_TAG_XPATH):
                if len(v_vendor_number) <= 1:
                    selenium_operation_obj.send_text_by_id(LocalElementLocator.WM_VENDOR_NUMBER_TEXT_ID,
                                                           client_uid[2:])
                else:
                    selenium_operation_obj.send_text_by_id(LocalElementLocator.WM_VENDOR_NUMBER_TEXT_ID, v_vendor_number)

            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.WM_INFO_NEXT_BUTTON_XPATH)
            while selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.WM_INFO_NEXT_BUTTON_XPATH) != False:
                easygui.msgbox("Please enter valid information and click on OK")
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.WM_INFO_NEXT_BUTTON_XPATH)
        xref_flag = 0
        while selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.VENDOR_XREF_XPATH) != False:
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.VENDOR_XREF_XPATH)
            selenium_operation_obj.send_text_by_id(LocalElementLocator.V_XREF_VENDOR_NUMBER_ID, v_vendor_number)
            selenium_operation_obj.send_text_by_id(LocalElementLocator.V_XREF_TPID_ID, TPID[number_of_profile])
            selenium_operation_obj.send_text_by_id(LocalElementLocator.V_XREF_RECEIVER_ID, v_supplier_dc4_name)
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.V_XREF_NEXT_BUTTON_XPATH)
            if len(v_vendor_number) <= 1:
                easygui.msgbox('Please Enter valid vendor number and click on OK')
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.V_XREF_NEXT_BUTTON_XPATH)
            while selenium_operation_obj.check_exists_by_id(LocalElementLocator.V_XREF_VENDOR_NUMBER_ID) != False:
                easygui.msgbox('Please Enter valid Info and click on OK')
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.V_XREF_NEXT_BUTTON_XPATH)
            xref_flag = 1
        if xref_flag == 1:
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.V_XREF_NEXT_BUTTON_XPATH)
        if number_of_profile == 0:
            if selenium_operation_obj.check_exists_by_xpath('//*[@id="_idJsp19"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[4]') == True:
                check_index = 2
                existing_env_id_xpath = '//*[@id="_idJsp19"]/table/tbody/tr[2]/td/table/tbody/tr['+str(check_index)+']/td[4]'
                while(selenium_operation_obj.check_exists_by_xpath(existing_env_id_xpath) != False):
                    if client_uid[:2] == selenium_operation_obj.get_text_by_xpath('//*[@id="_idJsp19"]/table/tbody/tr[2]/td/table/tbody/tr['+str(check_index)+']/td[3]') and client_uid[2:] == selenium_operation_obj.get_text_by_xpath('//*[@id="_idJsp19"]/table/tbody/tr[2]/td/table/tbody/tr['+str(check_index)+']/td[4]') and client_uid[2:] == selenium_operation_obj.get_text_by_xpath('//*[@id="_idJsp19"]/table/tbody/tr[2]/td/table/tbody/tr['+str(check_index)+']/td[5]'):
                        print('I --------------')
                        selenium_operation_obj.click_element_by_xpath('//*[@id="_idJsp19:'+str(check_index-2)+':_idJsp42"]')
                        envID_value = client_uid[2:]
                        grpID_value = client_uid[2:]
                        qly_value = client_uid[:2]
                        break
                    check_index =check_index+1
                    existing_env_id_xpath = '//*[@id="_idJsp19"]/table/tbody/tr[2]/td/table/tbody/tr[' + str(
                        check_index) + ']/td[4]'
            else:
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.CREATE_EDI_INFO_XPATH)
                time.sleep(2)
                self.v_driver.switch_to.window(self.v_driver.window_handles[-1])
                time.sleep(2)
                self.v_driver.switch_to.frame(0)

                # driver.switch_to.window(driver.window_handles.)#switchtolatestwindow
                time.sleep(2)
                envID_val = selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.EDI_INFO_ENVID_ID)

                selenium_operation_obj.send_text_by_id(LocalElementLocator.EDI_INFO_ENVID_ID, client_uid[2:])
                selenium_operation_obj.send_text_by_id(LocalElementLocator.EDI_INFO_GRPID_ID, client_uid[2:])
                selenium_operation_obj.send_text_by_id(LocalElementLocator.EDI_INFO_QUALIFIER_ID, client_uid[:2])
                easygui.ynbox('Continue?')
                qly_value = selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.EDI_INFO_QUALIFIER_ID)
                envID_val = selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.EDI_INFO_ENVID_ID)
                grpID_val = selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.EDI_INFO_GRPID_ID)
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.EDI_INFO_SAVE_XPATH)
                time.sleep(2)
                while len(self.v_driver.window_handles) == 3:
                    if "The value failed to meet the following validations: Must end with 'YK'" in selenium_operation_obj.get_text_by_xpath(LocalElementLocator.EDI_INFO_ERROR_TEXT_XPATH):
                        envID_val = selenium_operation_obj.send_text_by_id(LocalElementLocator.EDI_INFO_ENVID_ID, client_uid[2:]+"YK")
                        grpID_val = selenium_operation_obj.send_text_by_id(LocalElementLocator.EDI_INFO_GRPID_ID, client_uid[2:]+"YK")
                        envID_val = selenium_operation_obj.get_text_by_id(LocalElementLocator.EDI_INFO_ENVID_ID)
                        grpID_val = selenium_operation_obj.get_text_by_id(LocalElementLocator.EDI_INFO_GRPID_ID)
                        qly_value = selenium_operation_obj.get_text_by_id(LocalElementLocator.EDI_INFO_QUALIFIER_ID)
                        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.EDI_INFO_ERROR_SAVE_XPATH)
                    elif "The value failed to meet the following validations: Length of 10 characters is required, Must end with 'YK'" in selenium_operation_obj.get_text_by_xpath(LocalElementLocator.EDI_INFO_ERROR_TEXT_XPATH):

                        envID_val = selenium_operation_obj.send_text_by_id(LocalElementLocator.EDI_INFO_ENVID_ID,
                                                                           client_uid[2:] + LocalElementLocator.ZERO_LIST[9-len(client_uid[2:])] + "YK")
                        grpID_val = selenium_operation_obj.send_text_by_id(LocalElementLocator.EDI_INFO_GRPID_ID,
                                                                           client_uid[2:] + LocalElementLocator.ZERO_LIST[9-len(client_uid[2:])]+ "YK")
                        envID_val = selenium_operation_obj.get_text_by_id(LocalElementLocator.EDI_INFO_ENVID_ID)
                        grpID_val = selenium_operation_obj.get_text_by_id(LocalElementLocator.EDI_INFO_GRPID_ID)
                        qly_value = selenium_operation_obj.get_text_by_id(LocalElementLocator.EDI_INFO_QUALIFIER_ID)
                        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.EDI_INFO_ERROR_SAVE_XPATH)
                    else:
                        easygui.msgbox("Please enter correct EDI info and click on OK")
                        envID_val = selenium_operation_obj.get_text_by_id(LocalElementLocator.EDI_INFO_ENVID_ID)
                        grpID_val = selenium_operation_obj.get_text_by_id(LocalElementLocator.EDI_INFO_GRPID_ID)
                        qly_value = selenium_operation_obj.get_text_by_id(LocalElementLocator.EDI_INFO_QUALIFIER_ID)
                        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.EDI_INFO_ERROR_SAVE_XPATH)
                envID_value = envID_val
                grpID_value = grpID_val
                time.sleep(2)

                self.v_driver.switch_to.window(self.v_driver.window_handles[1])
                time.sleep(2)
        number_of_profile = number_of_profile + 1
        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.EDI_INFO_NEXT_BUTTON_XPATH)

        # while selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.EDI_INFO_NEXT_BUTTON_XPATH) != False:
        #     easygui.msgbox("Please try to resolve an error and move the setup to next page manually")
        print(qly_value)
        print(envID_value)
        print(grpID_value)
        print(TPID)
        return number_of_profile, qly_value, envID_value, grpID_value, TPID, profile_flag


    def get_data_for_library(self, salesforce_id, jira_supplier_name, jira_retailer_name, retailer_dc4_id, fics_number):
        #Web_Fulfillment_machine_learning_obj = Web_Fulfillment_machine_learning(self.v_task_type, self.v_username, self.v_output_wb)
        selenium_operation_obj = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        salesforce_link = 'https://spscommerce.my.salesforce.com/'+salesforce_id
        self.v_driver.get(salesforce_link)
        i = 2
        path1 = '//*[@id="'+salesforce_id+'_RelatedNoteList_title"]'
        path = '//*[@id="'+salesforce_id+'_RelatedNoteList_body"]/table/tbody/tr['+str(i)+']/td[2]/a'
        # time.sleep(5)
        # element = self.v_driver.find_element_by_xpath(path1)
        # self.v_driver.execute_script("arguments[0].scrollIntoView();", element)
        supplier_dc4_id = ''
        supplier_web_member_uid = ''
        supplier_web_company_uid = ''
        dc4_company_name = ''
        retailer_web_company_uid = ''
        retailer_name = ''
        TPID = []
        selenium_operation_obj.scroll_into_view_by_xpath(path1)

        while(selenium_operation_obj.check_exists_by_xpath(path)):
            dc4_setup_summary_link_text = selenium_operation_obj.get_text_by_xpath(path)
            #print(dc4_setup_summary_link_text)

            if 'Setup' in dc4_setup_summary_link_text and 'Summary' in dc4_setup_summary_link_text:

                selenium_operation_obj.click_element_by_xpath(path)
                setup_summary = selenium_operation_obj.get_text_by_xpath('//*[@id="ep"]/div[2]/div[2]/table/tbody/tr[5]/td[2]')
                self.get_info_from_summary(setup_summary, jira_supplier_name, jira_retailer_name, retailer_dc4_id, fics_number)

                break


            i =i+1
            path = '//*[@id="' + salesforce_id + '_RelatedNoteList_body"]/table/tbody/tr[' + str(i) + ']/td[2]/a'

        # Web_Fulfillment_machine_learning_obj.add_supplier_data_to_library(jira_supplier_name, dc4_company_name, supplier_dc4_id, supplier_web_company_uid, supplier_web_member_uid, fics_number)
        # Web_Fulfillment_machine_learning_obj.add_retailer_data_to_library(jira_retailer_name, retailer_name, retailer_dc4_id, retailer_web_company_uid, TPID, fics_number)


    def get_info_from_summary(self, setup_summary, jira_supplier_name, jira_retailer_name, retailer_dc4_id, fics_number):
        supplier_dc4_id = ''
        supplier_web_member_uid = ''
        supplier_web_company_uid = ''
        dc4_company_name = ''
        retailer_web_company_uid = ''
        retailer_name = ''
        TPID = []
        #setup_summary = selenium_operation_obj.get_text_by_xpath('//*[@id="ep"]/div[2]/div[2]/table/tbody/tr[5]/td[2]')
        if setup_summary is not None:
            if 'CompanyUid: ' in setup_summary:
                supplier_web_company_uid = setup_summary.split('CompanyUid: ')[1]
                supplier_web_company_uid = supplier_web_company_uid.split('\n')[0]
            if 'CompanyName: ' in setup_summary:
                dc4_company_name = setup_summary.split('CompanyName: ')[1]
                dc4_company_name = dc4_company_name.split('\n')[0]
            if ' DC4 CompanyUid ' in setup_summary:
                supplier_dc4_id = setup_summary.split(' DC4 CompanyUid ')[1]
                supplier_dc4_id = supplier_dc4_id.split('\n')[0]
            if 'MemberUid: ' in setup_summary:
                supplier_web_member_uid = setup_summary.split('MemberUid: ')[1]
                supplier_web_member_uid = supplier_web_member_uid.split('\n')[0]
            setup_summary = setup_summary.split('CompanyName: ' + dc4_company_name)
            for k in range(0, len(setup_summary)):
                setup_summary1 = setup_summary[k]
                if 'Created DC4 Profile for vendor:' in setup_summary1:
                    created_dc4_profile = setup_summary1.split('Created DC4 Profile for vendor:')[1]
                    profile_uid1 = created_dc4_profile.split('ProfileName:')[0]
                    retailer_name = created_dc4_profile.split('ProfileName:')[1]
                    retailer_name = retailer_name.split(' | ')[1]
                    profile_uid1 = profile_uid1.split('\n')[1]

                    TPID1 = created_dc4_profile.split('TPID: ')[1]
                    TPID2 = TPID1.split('\n')[0]
                    profile_uid = TPID1.split(profile_uid1)[1]
                    profile_uid = profile_uid.split('ReceiverProfileUid: ')[1]
                    profile_uid = profile_uid.split('\n')[0]
                    TPID.append(profile_uid + '-' + TPID2[3:6])
                    temp1 = 'SenderUid: ' + supplier_web_company_uid
                    temp2 = 'ReceiverUid: ' + supplier_web_company_uid

                    if temp1 in TPID1:
                        retailer_web_company_uid = TPID1.split(temp1)[1]

                        retailer_web_company_uid = retailer_web_company_uid.split('ReceiverUid: ')[1]
                        retailer_web_company_uid = retailer_web_company_uid.split('\n')[0]

                    else:
                        retailer_web_company_uid = TPID1.split(temp2)[0]
                        retailer_web_company_uid = retailer_web_company_uid.split('SenderUid: ')[1]
                        retailer_web_company_uid = retailer_web_company_uid.split('\n')[0]
                    supplier_dc4_id = re.sub(r'[^0-9]', '', supplier_dc4_id)
        today = datetime.datetime.now()
        today_str = today.strftime("%Y-%m-%d")
        TPID_str = ' '.join(TPID)
        dc4_company_info_check_query = "SELECT * from dc4_company_info where company_name = %s"
        dc4_company_info_check_query_data = (dc4_company_name,)
        if self.db_object.get_data_query(dc4_company_info_check_query, dc4_company_info_check_query_data):
            print('I am in for sup dc4 update')
            dc4_company_info_update_query = "UPDATE dc4_company_info SET dc4_company_uid = %s, web_company_uid = %s, web_member_uid = %s, fics_number = %s, username = %s, date = %s WHERE company_name = %s"
            # dc4_company_info_insert_query = "INSERT INTO dc4_company_info(company_name, dc4_company_uid, web_company_uid, web_member_uid, fics_number, username, date) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            dc4_company_info_update_query_data = (
            supplier_dc4_id, supplier_web_company_uid, supplier_web_member_uid, fics_number, self.v_username, today_str,
            dc4_company_name)
            self.db_object.insert_and_update_data_query(dc4_company_info_update_query,
                                                        dc4_company_info_update_query_data)
        else:
            print('I am in else sup for dc4 insert')
            dc4_company_info_insert_query = "INSERT INTO dc4_company_info(company_name, dc4_company_uid, web_company_uid, web_member_uid, fics_number, username, date) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            dc4_company_info_insert_query_data = (
            dc4_company_name, supplier_dc4_id, supplier_web_company_uid, supplier_web_member_uid, fics_number,
            self.v_username, today_str)
            self.db_object.insert_and_update_data_query(dc4_company_info_insert_query,
                                                        dc4_company_info_insert_query_data)

        supplier_info_check_query = "SELECT * from supplier_info where jira_name = %s"
        supplier_info_check_query_data = (jira_supplier_name,)
        if self.db_object.get_data_query(supplier_info_check_query, supplier_info_check_query_data):
            print('I am in else sup update')
            supplier_info_update_query = "UPDATE supplier_info SET dc4_name = %s, fics_number = %s, username = %s, date = %s WHERE jira_name = %s"
            supplier_info_update_query_data = (dc4_company_name, fics_number, self.v_username, today_str, jira_supplier_name)
            self.db_object.insert_and_update_data_query(supplier_info_update_query, supplier_info_update_query_data)
        else:
            print('I am in else sup insert')
            supplier_info_insert_query = "INSERT INTO supplier_info(jira_name, dc4_name, fics_number, username, date) VALUES (%s, %s, %s, %s, %s);"
            supplier_info_insert_query_data = (jira_supplier_name, dc4_company_name, fics_number, self.v_username, today_str)
            self.db_object.insert_and_update_data_query(supplier_info_insert_query, supplier_info_insert_query_data)

        dc4_company_info_check_query = "SELECT * from dc4_company_name where company_name = %s"
        dc4_company_info_check_query_data = (retailer_name,)
        if self.db_object.get_data_query(dc4_company_info_check_query, dc4_company_info_check_query_data):
            dc4_company_info_update_query = "UPDATE dc4_company_info SET dc4_company_uid = %s, web_company_uid = %s, web_member_uid = %s, fics_number = %s, username = %s, date = %s WHERE company_name = %s"
            # dc4_company_info_insert_query = "INSERT INTO dc4_company_info(company_name, dc4_company_uid, web_company_uid, web_member_uid, fics_number, username, date) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            dc4_company_info_update_query_data = (
                retailer_dc4_id, retailer_web_company_uid, None, fics_number, self.v_username,
                today_str,
                retailer_name)
            self.db_object.insert_and_update_data_query(dc4_company_info_update_query,
                                                        dc4_company_info_update_query_data)
        else:
            dc4_company_info_insert_query = "INSERT INTO dc4_company_info(company_name, dc4_company_uid, web_company_uid, web_member_uid, fics_number, username, date) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            dc4_company_info_insert_query_data = (
                retailer_name, retailer_dc4_id, retailer_web_company_uid, None, fics_number,
                self.v_username, today_str)
            self.db_object.insert_and_update_data_query(dc4_company_info_insert_query,
                                                        dc4_company_info_insert_query_data)

        retailer_info_check_query = "SELECT * from retailer_info where jira_name = %s"
        retailer_info_check_query_data = (jira_retailer_name,)
        if self.db_object.get_data_query(retailer_info_check_query, retailer_info_check_query_data):
            retailer_info_update_query = "UPDATE retailer_info SET dc4_name = %s, profile_info = %s, fics_number = %s, username = %s, date = %s WHERE jira_name = %s"
            retailer_info_update_query_data = (
            retailer_name, TPID_str, fics_number, self.v_username, today_str, jira_retailer_name)
            self.db_object.insert_and_update_data_query(retailer_info_update_query, retailer_info_update_query_data)
        else:
            retailer_info_insert_query = "INSERT INTO retailer_info (jira_name, dc4_name, profile_info, fics_number, username, date) VALUES (%s, %s, %s, %s, %s, %s);"
            retailer_info_insert_query_data = (
            jira_retailer_name, retailer_name, TPID_str, fics_number, self.v_username, today_str)
            self.db_object.insert_and_update_data_query(retailer_info_insert_query, retailer_info_insert_query_data)

    def copy_email_and_setup_summary(self):
        email_summary = []
        selenium_operation_obj = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        setup_summary = selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.SETUP_SUMMARY_INFO_ID)
        print(setup_summary)
        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.ACTUAL_SETUP_SUMMARY_XPATH)
        i = 0
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.REVIEW_EMAIL_XPATH):
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.REVIEW_EMAIL_XPATH)
        if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.REMOVE_JUST_SEND_TO_ME_BUTTON_XPATH):

            rem = self.v_driver.find_element_by_xpath(LocalElementLocator.REMOVE_JUST_SEND_TO_ME_BUTTON_XPATH).get_attribute('href')

            while rem is not None:
                email_summary.append(selenium_operation_obj.get_text_by_xpath(LocalElementLocator.EMAIL_TO_XPATH)+'\n'+selenium_operation_obj.get_text_by_xpath(LocalElementLocator.EMAIL_FROM_XPATH)+'\n'+selenium_operation_obj.get_text_by_xpath(LocalElementLocator.EMAIL_BCC_XPATH)+'\n'+selenium_operation_obj.get_text_by_xpath(LocalElementLocator.EMAIL_SUBJECT_XPATH)+'\n\n--------------------------------------------\n\n'+selenium_operation_obj.get_attribute_value_by_id(LocalElementLocator.FULL_EMAIL_ID)+'___________________________________________________________________________________________')
                print(email_summary[i])
                i = i + 1
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.REMOVE_JUST_SEND_TO_ME_BUTTON_XPATH)
                rem = self.v_driver.find_element_by_xpath(
                LocalElementLocator.REMOVE_JUST_SEND_TO_ME_BUTTON_XPATH).get_attribute('href')

            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.CANCEL_SEND_NONE_XPATH)

        return setup_summary, email_summary

    def update_salesforce_project(self, v_salesforce_id, ISA_ID, TPID, v_supplier_dc4_uid, dc4_setup_summary):
        selenium_operation_obj = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)

        supplier_web_company_uid = ''
        status_description = ''
        time.sleep(2)
        self.v_driver.get('https://spscommerce.my.salesforce.com/'+v_salesforce_id)
        if 'CompanyUid: ' in dc4_setup_summary:
            supplier_web_company_uid = dc4_setup_summary.split('CompanyUid: ')[1]
            supplier_web_company_uid = supplier_web_company_uid.split('\n')[0]
            print(supplier_web_company_uid)
        if 'Portal vendor rollout added:' in dc4_setup_summary:
            status_description = dc4_setup_summary.split('Portal vendor rollout added:')[1]
            status_description = status_description.split('CommId:')[0]
            Qly = status_description.split('EnvQualifier: ')[1]
            Qly = Qly.split('\n')[0]
            Env_id = status_description.split('EnvId: ')[1]
            Env_id = Env_id.split('\n')[0]
            Grp_id = status_description.split('GrpId: ')[1]
            Grp_id = Grp_id.split('\n')[0]
            ISA_ID = Qly + ' / ' + Env_id +' / ' +Grp_id
            print(ISA_ID)
            print(status_description)
        selenium_operation_obj.scroll_into_view_by_xpath(LocalElementLocator.ADD_NEW_NOTE_BUTTON_XPATH)
        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.ADD_NEW_NOTE_BUTTON_XPATH)
        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.NOTE_TITLE_XPATH, 'DC4 Setup Summary')
        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.NOTE_BODY_XPATH, dc4_setup_summary)
        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.NOTE_SAVE_BUTTON_XPATH)
        selenium_operation_obj.scroll_into_view_by_id(LocalElementLocator.STATUS_DESCRIPTION_ID)
        selenium_operation_obj.double_click_by_id(LocalElementLocator.STATUS_DESCRIPTION_ID)
        time.sleep(1)
        selenium_operation_obj.scroll_into_view_by_id(LocalElementLocator.STATUS_DESCRIPTION_ID)
        selenium_operation_obj.double_click_by_id(LocalElementLocator.STATUS_DESCRIPTION_ID)
        time.sleep(1)
        status_description_pre = selenium_operation_obj.get_attribute_value_by_id('00N50000001MXp7')
        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.STATUS_DESCRIPTION_TEXT_XPATH, status_description_pre+'\n\n'+status_description)
        #self.v_driver.find_element_by_xpath(LocalElementLocator.STATUS_DESCRIPTION_TEXT_XPATH).send_keys(status_description_pre+'\n\n'+status_description)
        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.STATUS_DESCRIPTION_OK_BUTTON_XPATH)

        selenium_operation_obj.scroll_into_view_by_id(LocalElementLocator.PROD_ISA_ID_ID)
        selenium_operation_obj.double_click_by_id(LocalElementLocator.PROD_ISA_ID_ID)
        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.PROD_ISA_ID_TEXT_XPATH, ISA_ID)

        selenium_operation_obj.scroll_into_view_by_id(LocalElementLocator.DC4_PROD_COMPANY_UID_ID)
        selenium_operation_obj.double_click_by_id(LocalElementLocator.DC4_PROD_COMPANY_UID_ID)
        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.DC4_PROD_COMPANY_UID_TEXT_XPATH, v_supplier_dc4_uid)

        selenium_operation_obj.double_click_by_id(LocalElementLocator.DC4_WEB_COMPANY_UID_ID)
        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.DC4_WEB_COMPANY_UID_TEXT_XPATH, supplier_web_company_uid)

        selenium_operation_obj.scroll_into_view_by_id(LocalElementLocator.SF_TPID_ID_LIST[0])
        i = 0
        while(i<len(TPID)):
            selenium_operation_obj.double_click_by_id(LocalElementLocator.SF_TPID_ID_LIST[i])
            selenium_operation_obj.send_text_by_id(LocalElementLocator.SF_TPID_VALUE_ID_LIST[i], TPID[i])
            print(TPID[i])
            i = i+1
        selenium_operation_obj.scroll_into_view_by_xpath(LocalElementLocator.SF_IMP_PROJ_SAVE_BUTTON)
        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.SF_IMP_PROJ_SAVE_BUTTON)

    def edi_creation(self, clientuid, supplier_name, retailer_name):
        selenium_operation_obj = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.DC4_EDI_INFO_TAB_XPATH)
        index = 2

        while(selenium_operation_obj.check_exists_by_xpath('//*[@id="_idJsp4:_idJsp19"]/table[2]/tbody/tr['+str(index)+']/td[5]') != False):
            if clientuid[2:] == selenium_operation_obj.get_text_by_xpath('//*[@id="_idJsp4:_idJsp19"]/table[2]/tbody/tr['+str(index)+']/td[5]'):
                if clientuid[:2] == selenium_operation_obj.get_text_by_xpath('//*[@id="_idJsp4:_idJsp19"]/table[2]/tbody/tr['+str(index)+']/td[4]'):
                    if clientuid[2:] == selenium_operation_obj.get_text_by_xpath('//*[@id="_idJsp4:_idJsp19"]/table[2]/tbody/tr['+str(index)+']/td[6]'):
                        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.DC4_SETUP_TOOL_TAB_XPATH)
                        return

            index = index+1

        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.DC4_ADD_EDI_INFO_XPATH)
        time.sleep(2)
        self.v_driver.switch_to.window(self.v_driver.window_handles[-1])
        time.sleep(2)
        self.v_driver.switch_to.frame(0)
        time.sleep(2)

        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.DC4_EDI_INFO_DESCRIPTION, supplier_name+' | '+retailer_name+ ' | SR')
        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.DC4_EDI_INFO_QLY, clientuid[:2])
        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.DC4_EDI_INFO_ENV, clientuid[2:])
        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.DC4_EDI_INFO_GRP, clientuid[2:])
        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.DC4_EDI_INFO_SEG_DELI, 10)
        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.DC4_EDI_INFO_ELE_DELI, 42)
        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.DC4_EDI_INFO_SUB_DELI, 125)
        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.DC4_EDI_INFO_DEC_CHAR, 0)
        selenium_operation_obj.send_text_by_xpath(LocalElementLocator.DC4_EDI_INFO_REL_CHAR, 0)
        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.DC4_EDI_INFO_SAVE)
        time.sleep(2)

        self.v_driver.switch_to.window(self.v_driver.window_handles[1])
        time.sleep(2)

        selenium_operation_obj.click_element_by_xpath(LocalElementLocator.DC4_SETUP_TOOL_TAB_XPATH)

    def minivan_route(self, from_route_id, to_route_id, tpid):
        try:
            self.v_driver_mv.get(LocalElementLocator.MINIVAN_ROUTES_URL)
            time.sleep(8)
            self.v_driver_mv.switch_to.frame(0)
            time.sleep(5)
            selenium_operation_obj = SeleniumOperations(self.v_task_type, self.v_driver_mv, self.lo)
            if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.FROM_ROUTE_INFO_XPATH) == False:
                login_obj = Login(self.v_task_type, self.v_driver_mv, self.v_input_wb, self.lo)
                login_obj.login('Launchpad')
                self.v_driver_mv.get(LocalElementLocator.MINIVAN_ROUTES_URL)
                time.sleep(8)
                self.v_driver_mv.switch_to.frame(0)
                time.sleep(5)
            selenium_operation_obj.send_text_by_xpath(LocalElementLocator.FROM_ROUTE_INFO_XPATH, from_route_id)
            time.sleep(1)
            selenium_operation_obj.send_text_by_xpath(LocalElementLocator.TO_ROUTE_INFO_XPATH, to_route_id)
            selenium_operation_obj.click_element_by_xpath(LocalElementLocator.MV_SEARCH_BUTTON_XPATH)
            time.sleep(10)
            if selenium_operation_obj.check_exists_by_xpath(LocalElementLocator.MV_FIRST_ROUTE_XPATH) == True:
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.MV_UPDATE_ROUTE_BUTTON_XPATH)
                time.sleep(2)
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.MV_EDIT_ROUTE_BUTTON_XPATH)
                time.sleep(10)
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.UPDATE_MV_TO_MAILBOX_XPATH)
                selenium_operation_obj.send_text_by_xpath(LocalElementLocator.UPDATE_TEXT_MV_TO_MAILBOX_XPATH, 'junk')
                time.sleep(2)
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.UPDATE_MV_TO_MAILBOX_JUNK_XPATH)
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.UPDATE_MV_CONFIRM_CHANGES_XPATH)
            else:
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.MV_CREATE_NEW_BUTTON_XPATH)
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.MV_FROM_MAILBOX_DROP_DOWN_XPATH)
                selenium_operation_obj.send_text_by_xpath(LocalElementLocator.MV_FROM_MAILBOX_TEXT_BOX_XPATH, 'dc4')
                time.sleep(2)
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.MV_FROM_MAILBOX_DC4_XPATH)
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.MV_TO_MAILBOX_DROP_DOWN_XPATH)
                selenium_operation_obj.send_text_by_xpath(LocalElementLocator.MV_TO_MAILBOX_TEXT_BOX_XPATH, 'junk')
                time.sleep(2)
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.MV_TO_MAILBOX_JUNK_XPATH)
                selenium_operation_obj.send_text_by_xpath(LocalElementLocator.MV_FROM_ROUTE_INFO_TEXT_BOX_XPATH,
                                                          from_route_id)
                selenium_operation_obj.send_text_by_xpath(LocalElementLocator.MV_TO_ROUTE_INFO_TEXT_BOX_XPATH, to_route_id)
                selenium_operation_obj.send_text_by_xpath(LocalElementLocator.MV_DESCRIPTION_XPATH, tpid)
                selenium_operation_obj.click_element_by_xpath(LocalElementLocator.MV_SUBMIT_BUTTON_XPATH)

            print('MV Done')
        except:
            easygui.msgbox("Unable to update minivan routes please do it manually")
