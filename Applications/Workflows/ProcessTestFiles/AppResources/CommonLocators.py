'''
@ Author - Aditya Datar
@ Creation date - 24/09/2018
@ Description - Declares all the constants to be used at the Process Level.
'''

# XPath for Supplier Link
Company_Select_Link = '//*[@id="table1:10:commandLink2"]'

# Document type
PO_File = 850

# Common Locators of Customer View Page

Relationship_Tab = '//*[@id="form1:panelPage1"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]/a'
Profile_tab = '//*[@id="form1:panelPage1"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[5]/a'

# Trading Partner search XPath for relationship

Trading_Partner_Name_text_Field = '//*[@id="form1:inputText1"]'
Trading_Partner_Name = '//*[@id="form1:table1:0:commandLink2"]'
click_search = '//*[@id="form1:commandButton1"]'
Trading_Partner_Profile_Name = '//*[@id="form1:table1:0:outputText3"]'
Supplier_EDI_Info = '//*[@id="form1:table1"]/table[2]/tbody/tr[2]/td[5]'
Retailer_EDI_Info = '//*[@id="form1:table1"]/table[2]/tbody/tr[2]/td[7]'
Supplier_Profile_Link= '//*[@id="form1:table1:0:commandLink3"]'
Table_Path = '//*[@id="form1:table1"]/table[2]/tbody/tr[2]/td[3]'
extensions_cancel_button = '//*[@id="form1:commandButton3"]'

# Profile Page XPaths
show_click = '//*[@id="form1:table1"]/table[2]/tbody/tr[2]/td[2]/div/a[2]'
Service_Name = 'FItoService'
Document_Type = '850'

# Setup Aggregator Link
Setup_Aggregator_Link = "https://commerce.spscommerce.com/setup-aggregator/aggregator/"

# XPaths of Setup Aggregator
Select_Environment = '/html/body/sa-root/div[2]/sa-aggregator-container/div/div[1]/sa-aggregator-preview/div/div[2]/div/div[1]/form/div[1]/p-dropdown/div/div[2]/span'
Select_Pre_Prod_Env = '/html/body/sa-root/div[2]/sa-aggregator-container/div/div[1]/sa-aggregator-preview/div/div[2]/div/div[1]/form/div[1]/p-dropdown/div/div[3]/div/ul/li[1]'
Retailer_Profile_Text_Field = '//input[@placeholder= "Search profile by name"]'

Select_Required_Profile = '/html/body/sa-root/div[2]/sa-aggregator-container/div/div[1]/sa-aggregator-preview/div/div[2]/div/div[1]/form/div[2]/div/p-autocomplete/span/div/ul/li'



TRANSACTION_TRACKER_PROD_LINK = 'https://commerce.spscommerce.com/transaction-tracker/prod/transactions/'

#T ransaction Tracker UI xpath
COMPANY_SEARCH_INPUTBOX=".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[2]/div[1]/div/companies-chosen-select/div/ul/li/input"
TRADING_SEARCH_INPUTBOX= ".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[2]/div[3]/div/trading-partner-chosen-select/div/ul/li/input"
START_DATE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/label[2]/input"
END_DATE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div/div[1]/label[2]/input"
DOCUMENT_TYPE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[3]/div[3]/div/input"
SERVICE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[3]/div[1]/div/sps-select/div/a/span[2]/span"
SEARCH_BTN=".//*[@id='advanced_search_dropdown']/div[2]/div/div/button[2]"
DC4ROUTER=".//*[contains(text(),'DC4Router')]"
PARCEL_ID_SEARCH_BOX=".//*[@id='advanced_search_by_input']"

xpath=".//*[@id='ui-select-choices-row-2-"
PARCEL_COUNT="html/body/app-reporting/div/div/div/div/div/section/sps-search-results-bar/div/div/div/div/span/span[3]"
VIEW="html/body/app-reporting/div/div/div/div/div/section/div[3]/div[1]/span/sps-select/div/a"
# SELECT_100=".//*[contains(text(),'100')]"
SELECT_100=".//*[@id='ui-select-choices-row-11-3']/div/div"
NEXT_SEARCH_BTN="html/body/app-reporting/div/div/div/div/div/section/div[3]/form/div/button[2]"

DROP_DOWN_LIST=".//*[contains(@id,'ui-select-choices-row-')]"
CUSTOMER_FROM_TT_FOR_COMPANY_1=".//*[@id='ui-select-choices-row-1-"
CUSTOMER_FROM_TT_FOR_COMPANY_2="']/div/div"
CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_1=".//*[@id='ui-select-choices-row-2-"
CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_2="']/div/div"

#def get_CM_parcels(self,input_sheet,row)

PARCEL_ID_1=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr["
PARCEL_ID_2="]/td[2]"
STATUS_1=".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr["
STATUS_2="]/td[1]"
DOCUMENT_ID_1=".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr["
DOCUMENT_ID_2="]/td[5]"


LAST_PARCEL_ID=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[1]/td[2]"

#process test files
FIRST_FIVE_PARCELS_FILE_PATH="..\Applications\Workflows\ProcessTestFiles\AppResources\parcelIDsforSearch.txt"
FIRST_PARCEL_ID=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[1]/td[2]/a"
PARCEL_FIRST_STAGE="//h4[contains(text(),'Transformations ')]/following::i[4]"
PARCEL_FIRST_STAGE_ID="//h4[contains(text(),'Transformations ')]/following::span[3]"
DOWNLOAD_LOGO_BUTTON=".//*[@id='parcels_drop']/following::i"

CLIENT_SECRET_JSON_FILE_PATH= '../Applications/Workflows/ProcessTestFiles/AppResources/Process Test File-7df61375a764.json'


#from App constant


#Common Constants
BROWSER_DRIVER = "../BrowserDrivers/chromedriver.exe"
LOG_FILE_BASE_PATH = "../Logs"
REPORT_FILE_BASE_PATH = "../Reports"
RUNNER_ENVIRONMENT = "../X-Runner/RunnerEnv.xlsx"
LOGIN_ENVIRONMENT_LOCATOR_FILE_PATH = "../Resources/Login_Locators_Environment_File.xlsx"

INPUT_FILE_PATH = "../X-Runner/Input.xlsx"
CLIENT_SECRET_JSON_FILE_PATH = '../Resources/client_secret.json'
AUTOIT_FTP_UPLOAD_SCRIPT= '"D://SPS_Automation_v1//Applications//Workflows//ProcessTestFiles//Autoit_script//Open.exe " '
# AUTOIT_FTP_UPLOAD_SCRIPT= "D://SPS_Automation_v1/Applications/Workflows/ProcessTestFiles/Autoit_script/File_upload.exe"


#Workflow wise Constants
#------------------------------------------------------------------------------------------

#Team and track list
TRACK_LIST = ['Production Data Monitoring', 'Error Hospital', 'Netsuite 850 Pre-PROD Setup','Process Test Files']
TEAM_LIST = ['WAIT', 'DNI', 'NETSUITE', '3PL', 'ICE', 'PREMIER', 'TRANSACTION TRIAGE', 'BCM', 'QUICK BOOKS',
                      'UN PARTNER', 'SPS']

#Usefull Links
DC4_PROD_LINK = "http://dc4ui.p01.pro:7777/dc4custmanager/faces/home.jsp"
DC4_PREPROD_LINK = "http://dc4ui.p01.ppd:7777/dc4custmanager/faces/home.jsp"
JIRA_LINK = "https://atlassian.spscommerce.com/login.jsp"
LAUNCHPAD_LINK = "https://commerce.spscommerce.com/auth/login/"
I_AM_TOOL_LINK = "https://iam.spscommerce.com/login/login"
SALESFORCE_LINK = "https://spscommerce.my.salesforce.com/?ec=302&startURL=%2Fhome%2Fhome.jsp"
FTP_PREPROD_LINK= "https://commshare.spspreprod.in/#/ftp/inbound_edi/"


#Common Xpaths
#DC4 UI
DC4_TAB = '//*[@id="form1:menuTabs1:0:commandMenuItem1"]'
DC4_COMPANY_NAME_TEXT_FIELD = '//*[@id="inputText41"]'
DC4_COMPANY_NAME_SEARCH_CLICK = '//*[@id="commandButton12"]'
DC4_COMPANY_SEARCH_BY_EDI_INFO_TAB = 'showDetailItem2'
DC4_COMPANY_SEARCH_BY_ISA_ID_TEXT_FIELD = 'inputText49'
DC4_COMPANY_SEARCH_BY_ISA_ID_SEARCH_TAB = 'commandButton14'

DC4_COMPANY_SEARCH_BY_TPID_TAB = 'showDetailItem3'
DC4_COMPANY_SEARCH_BY_TPID_TEXT_FIELD = 'inputText66'
DC4_COMPANY_SEARCH_BY_TPID_SEARCH_TAB = 'commandButton16'


#Salsesforce
SAILPOINT_TAB = '//*[@id="idp_section_buttons"]/button'
SALESFORCE_TAB = '//*[@id="slpt-launchpad-launcher-salesforce-btnInnerEl"]'

#FTP_PREPROD
FTP_USERNAME= ".//input[@id='username']"
FTP_PASSWORD= ".//input[@id='password']"
FTP_LOGIN_BUTTON= ".//span[@id='LoginButtonText']"
FTP_ADD_FILES= ".//*[@id='browseFileButtonPanel']"
FTP_ADD_FILES_BTN= ".//*[@id='browseFileButtonPanel']"
FTP_UPLOAD_FILES_BTN= ".//*[@id='startUpload']"

TRANSACTION_TRACKER_PROD_LINK = 'https://commerce.spscommerce.com/transaction-tracker/prod/transactions/'
TRANSACTION_TRACKER_PREPROD_LINK= 'https://commerce.spscommerce.com/transaction-tracker/preprod/transactions/'
#T ransaction Tracker UI xpath
COMPANY_SEARCH_INPUTBOX=".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[2]/div[1]/div/companies-chosen-select/div/ul/li/input"
TRADING_SEARCH_INPUTBOX= ".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[2]/div[3]/div/trading-partner-chosen-select/div/ul/li/input"
START_DATE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/label[2]/input"
END_DATE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div/div[1]/label[2]/input"
DOCUMENT_TYPE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[3]/div[3]/div/input"
SERVICE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[3]/div[1]/div/sps-select/div/a/span[2]/span"
SEARCH_BTN=".//*[@id='advanced_search_dropdown']/div[2]/div/div/button[2]"
DC4ROUTER=".//*[contains(text(),'DC4Router')]"
STATUS= ".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[1]/div[3]/div/sps-select/div/a/span[2]/span"
ACCEPTED= ".//*[@id='ui-select-choices-row-5-1']/div/div"
LAST24HRS= ".//*[@id='advanced_search_dropdown']/div[1]/div/div[2]/div/div/div/div/div[1]/div/div/button[1]"

PARCEL_ID_SEARCH_BOX=".//*[@id='advanced_search_by_input']"
xpath=".//*[@id='ui-select-choices-row-2-"
PARCEL_COUNT="html/body/app-reporting/div/div/div/div/div/section/sps-search-results-bar/div/div/div/div/span/span[3]"
VIEW="html/body/app-reporting/div/div/div/div/div/section/div[3]/div[1]/span/sps-select/div/a"
# SELECT_100=".//*[contains(text(),'100')]"
SELECT_100=".//*[@id='ui-select-choices-row-11-3']/div/div"
NEXT_SEARCH_BTN="html/body/app-reporting/div/div/div/div/div/section/div[3]/form/div/button[2]"
DROP_DOWN_LIST=".//*[contains(@id,'ui-select-choices-row-')]"
CUSTOMER_FROM_TT_FOR_COMPANY_1=".//*[@id='ui-select-choices-row-1-"
CUSTOMER_FROM_TT_FOR_COMPANY_2="']/div/div"
CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_1=".//*[@id='ui-select-choices-row-2-"
CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_2="']/div/div"
#def get_CM_parcels(self,input_sheet,row)
PARCEL_ID_1=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr["
PARCEL_ID_2="]/td[2]"
STATUS_1=".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr["
STATUS_2="]/td[1]"
DOCUMENT_ID_1=".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr["
DOCUMENT_ID_2="]/td[5]"
LAST_PARCEL_ID=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[1]/td[2]"
#process test files
FIRST_FIVE_PARCELS_FILE_PATH="..\Applications\Workflows\ProcessTestFiles\AppResources\parcelIDsforSearch.txt"
FIRST_PARCEL_ID=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[1]/td[2]/a"
PARCEL_FIRST_STAGE="//h4[contains(text(),'Transformations ')]/following::i[4]"
PARCEL_FIRST_STAGE_ID="//h4[contains(text(),'Transformations ')]/following::span[3]"
DOWNLOAD_LOGO_BUTTON=".//*[@id='parcels_drop']/following::i"


#process()

PROCESS_PATH='D:\processtestfiles.txt'

#with open(path) as f


TRANSAFORMATION="//aside[text()='Transformations']/following::a[@title='View'][1]/div/div"
TRANSAFORMATION1="html/body/div[1]/section/section/div/div/section/div/div[3]/div[1]/div/div[1]/div/div/div/a/i"

