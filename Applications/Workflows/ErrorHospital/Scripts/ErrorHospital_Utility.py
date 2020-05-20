'''

@ Author - Karan Pandya
@ Creation date - 09/14/2018
@ Description - Error Hospital Operations
'''
from Utilites.SeleniumOperations import SeleniumOperations
from Applications.Workflows.ErrorHospital.AppResources import LocalElementLocator
import time
import easygui

class ErrorHospital_Utility:
    def __init__(self, task_type, driver, log_file_object, error_hospital_machine_learning_object):
        self.v_task_type = task_type
        self.v_driver = driver
        self.log_file_object = log_file_object
        self.error_hospital_machine_learning_object = error_hospital_machine_learning_object

    #search for error tickets
    def document_rejected_error_search(self, v_ticket_uid, v_start_date, v_TPID, v_error_title, v_doc_type):
        selenium_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        selenium_operation_object.click_element_by_id(LocalElementLocator.ERROR_HOSPITAL_TAB_ID1)
        selenium_operation_object.send_text_by_id(LocalElementLocator.TICKET_UID_ID, v_ticket_uid)
        selenium_operation_object.send_text_by_id(LocalElementLocator.TITLE_ID, v_error_title)
        selenium_operation_object.send_text_by_id(LocalElementLocator.DESCRIPTION_ID, '%No entry in the web trading partnership table%'+v_TPID+'%')
        selenium_operation_object.send_text_by_id(LocalElementLocator.START_DATE_ID, v_start_date)
        selenium_operation_object.send_text_by_id(LocalElementLocator.EH_DOC_TYPE_ID, v_doc_type)
        selenium_operation_object.click_element_by_id(LocalElementLocator.SEARCH_BUTTON_ID)

    #Get Error Ticket UID
    def get_ticket_uid(self, v_index):
        selenium_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        v_ticket_uid_path = '//*[@id="form1:table1"]/table[2]/tbody/tr['+str(v_index)+']/td[3]'
        if selenium_operation_object.check_exists_by_xpath(v_ticket_uid_path):
            return selenium_operation_object.get_text_by_xpath(v_ticket_uid_path)
        else:
            return False

    #Get all failed parcel UID's
    def get_parcel_uid(self, v_index):
        selenium_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        v_ticket_uid_path = '//*[@id="form1:table1"]/table[2]/tbody/tr['+str(v_index)+']/td[9]'
        if selenium_operation_object.check_exists_by_xpath(v_ticket_uid_path):
            return selenium_operation_object.get_text_by_xpath(v_ticket_uid_path)
        else:
            return False

    # Get Sender's name
    def get_sender_name(self, v_index):
        selenium_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        v_sender_path = '//*[@id="form1:table1"]/table[2]/tbody/tr['+str(v_index)+']/td[6]'
        if selenium_operation_object.check_exists_by_xpath(v_sender_path):
            return selenium_operation_object.get_text_by_xpath(v_sender_path)
        else:
            return False

    #Get Receiver's Name
    def get_receiver_name(self, v_index):
        selenium_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        v_receiver_path = '//*[@id="form1:table1"]/table[2]/tbody/tr[' + str(v_index) + ']/td[7]'
        if selenium_operation_object.check_exists_by_xpath(v_receiver_path):
            return selenium_operation_object.get_text_by_xpath(v_receiver_path)
        else:
            return False

    #Get Document type and v_TPID from error description
    def get_info_from_description(self, v_index):
        selenium_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        v_path = '//*[@id="form1:table1:' + str(50 + v_index) + ':commandLink1"]'
        if selenium_operation_object.check_exists_by_xpath(v_path) == True:
            v_path = v_path
        else:
            v_path = '//*[@id="form1:table1:'+str(v_index)+':commandLink1"]'
        selenium_operation_object.click_element_by_xpath(v_path)
        v_doctype = selenium_operation_object.get_text_by_xpath(LocalElementLocator.EH_DOCTYPE_INFO_XPATH)
        v_doctype = v_doctype.split(' ')[0]
        v_TPID = selenium_operation_object.get_text_by_xpath(LocalElementLocator.EH_DESCRIPTION_INFO_XPATH)
        if 'Document:' in v_TPID:
            v_TPID = v_TPID.split('Document: ')[1]
            v_TPID = v_TPID.split('\n')[0]
        else:
            v_TPID = 'Invalid v_TPID'
        return v_TPID, v_doctype

    #Get unique doc types from all related tickets
    def get_unique_doc_types(self, v_doc_type):
        list_doc_type = []
        list_doc_type.append(v_doc_type)
        selenium_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        v_index = 2
        while(1):
            v_path = '//*[@id="form1:table1"]/table[2]/tbody/tr['+str(v_index)+']/td[8]/text()[1]'
            if selenium_operation_object.check_exists_by_xpath(v_path):
                if v_doc_type != selenium_operation_object.get_text_by_xpath(v_path):
                    list_doc_type.append(selenium_operation_object.get_text_by_xpath(v_path))
            else:
                break
            v_index = v_index+1
        return list_doc_type

    #Add Trading Partnership
    def add_trading_partnership(self, v_error_tiltle, v_TPID, doc_type_list, sender, receiver, v_status):
        selenium_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        v_present = 0
        supplier_web_id = ''
        retailer_web_id = ''
        selenium_operation_object.click_element_by_id(LocalElementLocator.DC4_WEBFORM_TAB_ID)
        selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_SEARCH_TRADING_PARTNERSHIP_LINK_XPATH)
        selenium_operation_object.send_text_by_id(LocalElementLocator.DC4_EVISION_KEY_ID, v_TPID)
        selenium_operation_object.click_element_by_id(LocalElementLocator.DC4_TRADING_PARTNERSHIP_SEARCH_BUTTON_ID)
        #Check for existing trading partnership
        if selenium_operation_object.check_exists_by_xpath(LocalElementLocator.DC4_FIRST_TRADING_PARTNERSHIP_XPATH):
            v_present = 1
            doc_type_list, supplier_web_id, retailer_web_id = self.validate_existing_trading_partnership(v_error_tiltle,doc_type_list)

        if len(doc_type_list) == 0:
            v_status = v_status+'Trading Partnership is already v_present'
            selenium_operation_object.click_element_by_id(LocalElementLocator.ERROR_HOSPITAL_TAB_ID2)
            flag = 1
            return v_status, flag

        if LocalElementLocator.ADHOC_ERROR_TITLE == v_error_tiltle:
            #Determine supplier and retailer
            sender, receiver = self.check_supplier_retailer(sender, receiver, doc_type_list[0])
        #If Valid Trading Partnership is not present
        if len(doc_type_list)!=0:

            if supplier_web_id == '':
                if v_present == 1:
                    selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_CREATE_TRADING_PARTNERSHIP_BUTTON1)
                else:
                    selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_CREATE_TRADING_PARTNERSHIP_BUTTON2)

                selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_SENDER_TORCH)

                v_status, flag = self.add_web_company(sender, v_status)
                if flag == 0 or flag == 2:
                    selenium_operation_object.click_element_by_xpath(LocalElementLocator.ERROR_HOSPITAL_TAB_XPATH)
                    return v_status, flag

                selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_RECEIVER_TORCH)
                v_status, flag = self.add_web_company(receiver, v_status)

                if flag == 0 or flag == 2:
                    selenium_operation_object.click_element_by_xpath(LocalElementLocator.ERROR_HOSPITAL_TAB_XPATH)
                    return v_status, flag

                if flag == 1:
                    supp_web_id = self.v_driver.find_element_by_id(
                        LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_SENDER_TEXT_ID).get_attribute('value')
                    ret_web_id = self.v_driver.find_element_by_id(
                        LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_RECEIVER_TEXT_ID).get_attribute('value')
                    self.error_hospital_machine_learning_object.add_to_library(sender, supp_web_id)
                    self.error_hospital_machine_learning_object.add_to_library(receiver, ret_web_id)
                    selenium_operation_object.send_text_by_id(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_EVISION_KEY_ID, v_TPID)
                    selenium_operation_object.send_text_by_id(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_FORM_NUMBER_ID, (', ').join(doc_type_list))
                    if LocalElementLocator.ADHOC_ERROR_TITLE == v_error_tiltle:
                        selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_BILLING_CODE_ZERO)
                    else:
                        selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_BILLING_CODE_ONE)
                    selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_CREATE_BUTTON)
                    selenium_operation_object.click_element_by_xpath(LocalElementLocator.ERROR_HOSPITAL_TAB_XPATH)
                    v_status = v_status+'\nAdded web trading partnership'
                    return v_status, 1
            else:
                selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_CREATE_TRADING_PARTNERSHIP_BUTTON1)
                if v_error_tiltle == LocalElementLocator.ADHOC_ERROR_TITLE:
                    selenium_operation_object.send_text_by_id(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_SENDER_TEXT_ID, retailer_web_id)
                    selenium_operation_object.send_text_by_id(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_RECEIVER_TEXT_ID, supplier_web_id)
                else:
                    if doc_type_list[0] == '810' or doc_type_list[0] == '846' or doc_type_list[0] == '855' or doc_type_list[0] == '856' or doc_type_list[0] == '940':
                        selenium_operation_object.send_text_by_id(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_SENDER_TEXT_ID,
                                           supplier_web_id)
                        selenium_operation_object.send_text_by_id(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_RECEIVER_TEXT_ID,
                                           retailer_web_id)
                    else:
                        selenium_operation_object.send_text_by_id(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_SENDER_TEXT_ID,
                                           retailer_web_id)
                        selenium_operation_object.send_text_by_id(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_RECEIVER_TEXT_ID,
                                           supplier_web_id)
                selenium_operation_object.send_text_by_id(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_EVISION_KEY_ID, v_TPID)
                selenium_operation_object.send_text_by_id(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_FORM_NUMBER_ID,
                                   (', ').join(doc_type_list))
                if LocalElementLocator.ADHOC_ERROR_TITLE == v_error_tiltle:
                    selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_BILLING_CODE_ZERO)
                else:
                    selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_BILLING_CODE_ONE)

                selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_CREATE_BUTTON)
                selenium_operation_object.click_element_by_xpath(LocalElementLocator.ERROR_HOSPITAL_TAB_XPATH)
                v_status = v_status + '\nAdded web trading partnership'
                return v_status, 1

    #Validating Existing Trading Partnership
    def validate_existing_trading_partnership(self, error_title, doc_type_list):
        selenium_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        supplier_web_id = ''
        retailer_web_id = ''
        for v_index in range(0,len(doc_type_list)):
            temp_doc = doc_type_list[v_index]
            i = 2
            while(1):
                form_path = '//*[@id="resultTable"]/table/tbody/tr[3]/td/table/tbody/tr['+str(i)+']/td[9]'
                status_path = '//*[@id="resultTable"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(i) + ']/td[12]'
                if selenium_operation_object.check_exists_by_xpath(form_path):
                    if temp_doc == selenium_operation_object.get_text_by_xpath(form_path):

                        if temp_doc == '810' or temp_doc == '846' or temp_doc == '855' or temp_doc == '856' or temp_doc == '940':
                            supplier_web_id = selenium_operation_object.get_text_by_xpath('//*[@id="resultTable"]/table/tbody/tr[3]/td/table/tbody/tr['+str(i)+']/td[5]')
                            retailer_web_id = selenium_operation_object.get_text_by_xpath('//*[@id="resultTable"]/table/tbody/tr[3]/td/table/tbody/tr['+str(i)+']/td[7]')
                        else:
                            supplier_web_id = selenium_operation_object.get_text_by_xpath(
                                '//*[@id="resultTable"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(i) + ']/td[7]')
                            retailer_web_id = selenium_operation_object.get_text_by_xpath(
                                '//*[@id="resultTable"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(i) + ']/td[5]')

                        if selenium_operation_object.get_text_by_xpath(status_path) == 'true':
                            del doc_type_list[v_index]

                            break
                    #Find supplier and retailer web company uid
                    if temp_doc == '810' or temp_doc == '846' or temp_doc == '855' or temp_doc == '856' or temp_doc == '940':
                        supplier_web_id = selenium_operation_object.get_text_by_xpath(
                            '//*[@id="resultTable"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(i) + ']/td[5]')
                        retailer_web_id = selenium_operation_object.get_text_by_xpath(
                            '//*[@id="resultTable"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(i) + ']/td[7]')
                    else:
                        supplier_web_id = selenium_operation_object.get_text_by_xpath(
                            '//*[@id="resultTable"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(i) + ']/td[7]')
                        retailer_web_id = selenium_operation_object.get_text_by_xpath(
                            '//*[@id="resultTable"]/table/tbody/tr[3]/td/table/tbody/tr[' + str(i) + ']/td[5]')

                else:
                    break
                i = i+1
        return doc_type_list, supplier_web_id, retailer_web_id

    #Determine supplier and retailer on the basis of document type
    def check_supplier_retailer(self, company_name1, company_name2, temp_doc):
        if temp_doc == '810' or temp_doc == '846' or temp_doc == '855' or temp_doc == '856' or temp_doc == '940':
            supplier = company_name2
            receiver = company_name1
        else:
            supplier = company_name1
            receiver = company_name2
        return supplier, receiver

    #Add web company uid
    def add_web_company(self, sender, v_status):
        flag = 0
        selenium_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        time.sleep(2)
        default_handle = self.v_driver.current_window_handle
        self.v_driver.switch_to.window(self.v_driver.window_handles[-1])
        time.sleep(2)
        self.v_driver.switch_to.frame(0)
        time.sleep(2)
        #Check in library for web company uid
        web_uid = self.error_hospital_machine_learning_object.get_supplier_info(sender)
        if web_uid != False:
            selenium_operation_object.send_text_by_id(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_COMPANYUID_ID, web_uid)
            selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_COMPANY_NAME_SEARCH_BUTTON)
            time.sleep(3)
            if selenium_operation_object.check_exists_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_FIRST_WEB_COMPANY):
                selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_SELECT_BUTTON)
                flag = 1
                v_status = v_status + '\nFound web company from previous results'
                self.v_driver.switch_to.window(self.v_driver.window_handles[0])
                time.sleep(2)
                return v_status, flag


        selenium_operation_object.send_text_by_id(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_COMPANY_NAME_SEARCH_ID, sender)
        selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_COMPANY_NAME_SEARCH_BUTTON)
        time.sleep(2)
        if selenium_operation_object.check_exists_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_FIRST_WEB_COMPANY):
            i = 2
            web_id = ' '
            path = '//*[@id="_idJsp13"]/table/tbody/tr[2]/td/table/tbody/tr[' + str(i) + ']/td[2]'
            while (1):
                if selenium_operation_object.check_exists_by_xpath(path):
                    temp_web_id = selenium_operation_object.get_text_by_xpath(path)
                    if temp_web_id != web_id and flag == 0:
                        web_id = temp_web_id
                        flag = 1
                    elif temp_web_id != web_id:
                        flag = 2
                        break
                else:
                    break
                i = i + 1
                path = '//*[@id="_idJsp13"]/table/tbody/tr[2]/td/table/tbody/tr[' + str(i) + ']/td[2]'
            if flag == 2:
                v_status = v_status+'\nMultiple web companies'
            else:
                selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_SELECT_BUTTON)
        else:
            sender = '%' + sender.replace(' ', '%') + '%'
            selenium_operation_object.send_text_by_id(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_COMPANY_NAME_SEARCH_ID, sender)
            selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_COMPANY_NAME_SEARCH_BUTTON)
            time.sleep(2)
            if selenium_operation_object.check_exists_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_FIRST_WEB_COMPANY):
                i = 2
                web_id = ' '
                path = '//*[@id="_idJsp13"]/table/tbody/tr[2]/td/table/tbody/tr[' + str(i) + ']/td[2]'
                while (1):
                    if selenium_operation_object.check_exists_by_xpath(path):
                        temp_web_id = selenium_operation_object.get_text_by_xpath(path)
                        if temp_web_id != web_id and flag == 0:
                            web_id = temp_web_id
                            flag = 1
                        elif temp_web_id != web_id:
                            flag = 2
                            break
                    else:
                        break
                    i = i + 1
                    path = '//*[@id="_idJsp13"]/table/tbody/tr[2]/td/table/tbody/tr[' + str(i) + ']/td[2]'
                if flag == 2:
                    v_status = v_status + '\nMultiple web companies'
                else:
                    selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_SELECT_BUTTON)
            else:
                v_status = v_status+"No web company found"

        if flag == 0 or flag == 2:

            if easygui.ynbox("Deadpool is unable to find web company. Do you want to add it manually?\n\nNote:- Add correct web comapany manually then select 'Yes' else 'No'"):
                flag = 1
                selenium_operation_object.click_element_by_xpath(LocalElementLocator.DC4_ADD_TRADING_PARTNERSHIP_SELECT_BUTTON)
            else:
                handles = list(self.v_driver.window_handles)
                handles.remove(default_handle)
                self.v_driver.close()
                time.sleep(2)

                self.v_driver.switch_to.window(default_handle)


        if flag == 1:
            self.v_driver.switch_to.window(self.v_driver.window_handles[0])
        time.sleep(2)
        return v_status, flag

    #Requeue failed parcels
    def requeue(self, parcel_list):

        selenium_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        selenium_operation_object.click_element_by_xpath(LocalElementLocator.REQUEUE_PARCEL_TAB_XPATH)
        flag = 0
        for v_index in range(0, len(parcel_list)):
            i = (v_index + 1) % 5
            if i == 0:
                i = 5
            parcel_path = '//*[@id="form1:inputText' + str(i) + '"]'
            flag = 0
            if selenium_operation_object.check_exists_by_xpath(parcel_path):
                selenium_operation_object.send_text_by_xpath(parcel_path, parcel_list[v_index])
            if i == 5:
                selenium_operation_object.click_element_by_id(LocalElementLocator.REQUEUE_PARCEL_BUTTON_ID)
                flag = 1
        if flag == 0:
            selenium_operation_object.click_element_by_id(LocalElementLocator.REQUEUE_PARCEL_BUTTON_ID)
        selenium_operation_object.click_element_by_id(LocalElementLocator.ERROR_HOSPITAL_TAB_ID1)

    #Check failed parcel status after requeuing
    def error_status(self, parcel_uid, error_title):
        self.v_driver.switch_to.window(self.v_driver.window_handles[-1])
        time.sleep(3)
        link = 'https://commerce.spscommerce.com/transaction-tracker/prod/transactions/'+parcel_uid+'/'
        self.v_driver.get(link)
        time.sleep(15)
        self.v_driver.switch_to.frame(0)
        time.sleep(2)

        selenium_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        time.sleep(2)
        if error_title == LocalElementLocator.ADHOC_ERROR_TITLE:

            path = '//*[@id="parcel-'+parcel_uid+'"]/div[2]/div/div/div[2]/form/div/button[2]'
            if not selenium_operation_object.check_exists_by_xpath(path):
                time.sleep(2)
                self.v_driver.get(link)
                time.sleep(10)
                self.v_driver.switch_to.frame(0)
                time.sleep(2)
                if not selenium_operation_object.check_exists_by_xpath(path):
                    return 0

            selenium_operation_object.click_element_by_xpath(path)
            i = 1
            while (1):

                path1 = '/html/body/app-reporting/div/div/div/div/div[2]/div/section/div[2]/div[2]/div['+str(i)+']'
                temp = selenium_operation_object.get_text_by_xpath(path1)
                time.sleep(1)
                if parcel_uid in temp:
                    ans = self.v_driver.find_element_by_xpath(
                        '/html/body/app-reporting/div/div/div/div/div[2]/div/section/div[2]/div[2]/div[' + str(
                            i + 1) + ']').text
                    id = ans.split('AdhocReporting ')[1]
                    id = id.split('\n')[0]
                    break
                i = i + 1

            selenium_operation_object.click_element_by_xpath('//*[@id="parcel-' + id + '"]/div/div/div[1]/a/span/i[2]')
            status = selenium_operation_object.get_text_by_xpath('//*[@id="parcel-'+id+'"]/div/ng-include/div/div/div[1]/div/div[2]/dl/div[2]/dd')
            if status == 'Accepted':
                return 1
            else:
                return 0

        else:
            return 1