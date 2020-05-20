from selenium import webdriver

from Utilites.SeleniumOperations import SeleniumOperations
from Applications.Workflows.DC4Setup.AppResources import LocalElementLocator
from Utilites import AppConstants
import time

class DC4_Utility_Local:
    def __init__(self, task_type, driver, lo, v_input_wb):
        self.v_task_type = task_type
        self.v_driver = driver
        self.lo = lo
        self.v_input_wb = v_input_wb


        # max_row = capabilities_sheet.max_row
        # max_col = capabilities_sheet.max_column

    #Function to Click on Searched Company Name
    def click_on_searched_company_name(self):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_COMPANY_BY_NAME_SEARCH_TABLE)

    #Function to Click on Relationships Tab
    def click_on_preprod_relationships_tab(self):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_RELATIONSHIPS_TAB)


    #Function to Enter Company Name in TradingPartnerName under Relationships Tab
    def search_trading_partner_name_in_relationships(self, retailer_name):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        so.send_text_by_xpath(LocalElementLocator.DC4_PREPROD_TRADING_PARTNER_NAME_TEXTFIELD,retailer_name)
        so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_SEARCH_BUTTON)

    #Function to click on searched Profile Name under Relationships.
    #######To be made to function for 2 profile results by matching ISA ID
    def click_on_profile_name_via_relationships(self):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        searched_profiles_relationships=so.list_elements_by_xpath(LocalElementLocator.DC4_PREPROD_SEARCH_TABLE_CONTENT_TR)
        count_searched_profiles_relationships=len(searched_profiles_relationships)
        print(count_searched_profiles_relationships)
        if count_searched_profiles_relationships !=2:
            return
        else:
            so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_RELATIONSHIPS_PROFILE_NAME)

    #Function to click on Show Link of Searched Profile
    def click_on_show_link_of_searched_profile(self):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_CLICKED_PROFILE_SHOW_LINK)

    #Function to Add Existing Capability in Profile
    def add_existing_capability(self):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        capabilities_sheet = so.call_excel_sheet('Capabilities')
        for row_counter in range(5, 6):
            for col_counter in range (2,(capabilities_sheet.max_column)+1):
                so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_ADD_EXISTING_CAPABILITY_BUTTON)
                time.sleep(2)
                so.switch_child_window_handle()
                so.switch_to_default_frame()
                so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_PLUS_SEARCH_BUTTON)
                capability_uid=capabilities_sheet.cell(row=row_counter,column=col_counter).value
                so.send_text_by_xpath(LocalElementLocator.DC4_PREPROD_CAPABILITY_UID,capability_uid)
                so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_FEC_SEARCH_BUTTON)
                so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_SEARCHED_CAPABILITY_UID_CHECKBOX)
                so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_FEC_CHOOSE_BUTTON)
                so.switch_parent_window_handle()


    #Function to Add New Capability in Capabilities Tab
    def add_new_capability(self):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        po_service_uid="1007"
        return_documents_service_uid="1006"

        #capabilities_sheet=so.call_excel_sheet('Capabilities')
        capabilities_sheet = self.v_input_wb.get_sheet_by_name('Capabilities')

        #Loop to Iterate through the Capabilities Excel Sheet
        #for row_counter in range (1,(capabilities_sheet.max_row)+1):
        for row_counter in range(1, 2):
            for col_counter in range (2,(capabilities_sheet.max_column)+1):
                so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_CAPABILITY_TAB)
                so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_ADD_CAPABILITY_BUTTON)
                sheet_value=capabilities_sheet.cell(row=row_counter,column=col_counter).value

                #Switch to Create Capability Child Window;
                so.switch_child_window_handle()
                so.switch_to_default_frame()
                time.sleep(2)
                #Click on the Search Service Torch; Switch to the Search Service Child Window
                so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_CREATE_CAPABILITY_SERVICE_TORCH)
                time.sleep(2)
                so.switch_child_window_handle()
                so.switch_to_default_frame()

                #If Condition to validate serviceUID input based on Inbound/Outbound Documents
                if str(sheet_value) == "850" or str(sheet_value)== "850 Outbound":
                    so.send_text_by_xpath(LocalElementLocator.DC4_PREPROD_CREATE_CAPABILITY_SERVICE_SERVICE_UID,po_service_uid)
                else:
                    so.send_text_by_xpath(LocalElementLocator.DC4_PREPROD_CREATE_CAPABILITY_SERVICE_SERVICE_UID,return_documents_service_uid)
                so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_SEARCH_SERVICES_SEARCH_BUTTON)
                so.get_text_by_xpath(LocalElementLocator.DC4_PREPROD_SEARCH_SERVICES_SEARCH_RESULT_SERVICE_UID)
                #print(so.get_text_by_xpath(LocalElementLocator.DC4_PREPROD_CREATE_CAPABILITY_SERVICE_SERVICE_UID))
                #print(so.get_text_by_xpath(LocalElementLocator.DC4_PREPROD_SEARCH_SERVICES_SEARCH_RESULT_SERVICE_UID))
                sheet_value_service_uid_validation=str(capabilities_sheet.cell(row=row_counter+1,column=col_counter).value)
                print("Adding Capability")
                print(so.get_text_by_xpath(LocalElementLocator.DC4_PREPROD_SEARCH_SERVICES_SEARCH_RESULT_SERVICE_UID))

                #Validating ServiceUID Input with the SearchResult & Clicking Choose
                if sheet_value_service_uid_validation==str(so.get_text_by_xpath(LocalElementLocator.DC4_PREPROD_SEARCH_SERVICES_SEARCH_RESULT_SERVICE_UID)):
                    so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_SEARCH_SERVICES_CHOOSE_BUTTON)
                else:
                    print("Service Validation Failed")
                    return
                time.sleep(1)
                so.switch_child_window_handle()
                so.switch_to_default_frame()
                so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_CREATE_CAPABILITY_CAPABILITY_TORCH)
                time.sleep(1)
                so.switch_child_window_handle()
                so.switch_to_default_frame()
                sheet_value_capability_name=str(capabilities_sheet.cell(row=row_counter+2,column=col_counter).value)
                print(sheet_value_capability_name)
                so.send_text_by_xpath(LocalElementLocator.DC4_PREPROD_CREATE_CAPABILITY_SEARCH_DATATYPES_DATATYPE_NAME,sheet_value_capability_name)
                so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_CREATE_CAPABILITY_SEARCH_DATATYPES_SEARCH_BUTTON)
                datatype_name_result_table_count=len(so.list_elements_by_xpath(LocalElementLocator.DC4_PREPROD_CREATE_CAPABILITY_SEARCH_DATATYPES_DATATYPE_NAME_RESULT_TABLE))
                #print(datatype_name_result_table_count)
                if datatype_name_result_table_count>2:
                    self.v_driver.close()
                    so.switch_child_window_handle()
                    self.v_driver.close()
                    return
                else:
                    so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_CREATE_CAPABILITY_SEARCH_DATATYPES_SEARCHED_CAPABILITY_CHECKBOX)
                    so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_CREATE_CAPABILITY_SEARCH_DATATYPES_CHOOSE_BUTTON)
                time.sleep(1)
                so.switch_child_window_handle()
                so.switch_to_default_frame()
                sheet_value_capability_notes = str(capabilities_sheet.cell(row=row_counter + 3, column=col_counter).value)
                so.send_text_by_xpath(LocalElementLocator.DC4_PREPROD_CREATE_CAPABILITY_NOTES,sheet_value_capability_notes)
                so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_CREATE_CAPABILITY_SUBMIT_BUTTON)
                so.switch_parent_window_handle()
                #so.switch_to_default_frame()
            print("Great! New Capabilities have been Added :) ")

    def return_capability_uid(self):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        #capabilities_sheet = so.call_excel_sheet('Capabilities')
        capabilities_sheet = self.v_input_wb.get_sheet_by_name('Capabilities')
        for row_counter in range(5, 6):
            for col_counter in range (2,(capabilities_sheet.max_column)+1):
                so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_CAPABILITY_TAB)
                sheet_value_capability_notes = str(capabilities_sheet.cell(row=row_counter -1, column=col_counter).value)
                so.send_text_by_xpath(LocalElementLocator.DC4_PREPROD_CAPABILITY_TAB_NOTES,sheet_value_capability_notes)
                so.click_element_by_xpath(LocalElementLocator.DC4_PREPROD_CAPABILITY_TAB_SEARCH)
                #print(len(so.list_elements_by_xpath(LocalElementLocator.DC4_PREPROD_CAPABILITY_TAB_SEARCHED_RESULT_TABLE)))
                if len(so.list_elements_by_xpath(LocalElementLocator.DC4_PREPROD_CAPABILITY_TAB_SEARCHED_RESULT_TABLE))==2:
                    notes_content=str(so.get_text_by_xpath(LocalElementLocator.DC4_PREPROD_CAPABILITY_TAB_SEARCHED_RESULT_NOTES))
                    if sheet_value_capability_notes==notes_content:
                        print("New Capability UID Created:")
                        print(so.get_text_by_xpath(LocalElementLocator.DC4_PREPROD_CAPABILITY_TAB_SEARCHED_RESULT_CAPABILITY_UID))
                        capability_uid=str(so.get_text_by_xpath(LocalElementLocator.DC4_PREPROD_CAPABILITY_TAB_SEARCHED_RESULT_CAPABILITY_UID))
                        capabilities_sheet.cell(row=row_counter, column=col_counter).value=capability_uid
                        #self.v_input_wb.save(AppConstants.INPUT_FILE_PATH)
                    else:
                        print("Mess is done, Clean It :/ The Note that caused Issue")
                        print(sheet_value_capability_notes)
                else:
                    print("No Result Found for:")
                    print(sheet_value_capability_notes)
        self.v_input_wb.save(AppConstants.INPUT_FILE_PATH)

    def add_map_extensions(self):
        so = SeleniumOperations(self.v_task_type, self.v_driver, self.lo)
        

























        #so.switch_child_window_handle()
        #so.switch_to_default_frame()








