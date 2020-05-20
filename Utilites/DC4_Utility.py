'''

@ Author - Karan Pandya
@ Creation date - 08/31/2018
@ Description - Common DC4 Prod Operation
'''
from Utilites import AppConstants
from Utilites.SeleniumOperations import SeleniumOperations
class DC4_Utility:
    def __init__(self, task_type, driver, log_file_object):
        self.v_task_type = task_type
        self.v_driver = driver
        self.log_file_object = log_file_object


    def company_search_by_name(self, v_company_name):
        selenum_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        selenum_operation_object.click_element_by_xpath(AppConstants.DC4_TAB)
        selenum_operation_object.send_text_by_xpath(AppConstants.DC4_COMPANY_NAME_TEXT_FIELD, v_company_name)
        selenum_operation_object.click_element_by_xpath(AppConstants.DC4_COMPANY_NAME_SEARCH_CLICK)

    def company_search_by_ISA_ID(self, v_ISA_ID):
        selenum_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        selenum_operation_object.click_element_by_xpath(AppConstants.DC4_TAB)
        selenum_operation_object.click_element_by_id(AppConstants.DC4_COMPANY_SEARCH_BY_EDI_INFO_TAB)
        selenum_operation_object.send_text_by_id(AppConstants.DC4_COMPANY_SEARCH_BY_ISA_ID_TEXT_FIELD, v_ISA_ID)
        selenum_operation_object.click_element_by_id(AppConstants.DC4_COMPANY_SEARCH_BY_ISA_ID_SEARCH_TAB)

    def company_search_by_TPID(self, v_TPID):
        selenum_operation_object = SeleniumOperations(self.v_task_type, self.v_driver, self.log_file_object)
        selenum_operation_object.click_element_by_xpath(AppConstants.DC4_TAB)
        selenum_operation_object.click_element_by_id(AppConstants.DC4_COMPANY_SEARCH_BY_TPID_TAB)
        selenum_operation_object.send_text_by_id(AppConstants.DC4_COMPANY_SEARCH_BY_TPID_TEXT_FIELD, v_TPID)
        selenum_operation_object.click_element_by_id(AppConstants.DC4_COMPANY_SEARCH_BY_TPID_SEARCH_TAB)
