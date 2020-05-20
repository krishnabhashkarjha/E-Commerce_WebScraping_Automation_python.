"""
@ Author - Krishnabhashkar jha
@ Creation date - 16/01/2020
@ Description - Declares all the constants to be used at the Process Level.
"""

# Xpath of DownloadAmazonReport.
vendor_central_click = ".//*[contains(@id,'login-button-container')]"
Login_Email_Xpath = ".//*[contains(@id,'ap_email')]"
Login_Password_Xpath = ".//*[contains(@id,'ap_password')]"
Supplier_Login = ".//*[contains(@id,'signInSubmit')]"
Distributor_View = ".//*[contains(text(),'Distributor View')]"
Distributor_View_Sourcing = ".//*[contains(text(),'• Sourcing')]"
Sales_View = ".//*[contains(text(),'Sales View')]"
Sales_View_By_Country_Region = ".//*[contains(text(),'By Country/Region')]"
Viewing = ".//*[@id='dashboard-filter-basicViewingRange']"
Viewing_Last_Report = ".//*[contains(text(),'Last reported')]"
Apply_Change = ".//*[contains(text(),'FAQ')]/following::button[contains(.,'Apply')]"
Detail_View_Add = ".//*[contains(text(),'FAQ')]/following::button[contains(.,'Select')]"
Add_UPC = ".//*[contains(text(),'FAQ')]/following::button[contains(.,'Select')]/following::a[contains(text(),'UPC')]"
Download_Click = ".//*[contains(@id,'downloadButton')]"
Download_DetailView_Excel_Sales = ".//p[contains(text(),'Detail View')]/following::a[1]"
Download_DetailView_Excel_Inventory = ".//p[contains(text(),'Inventory Health')]/following::a[1]"
SwitchAccountTo = ".//*[contains(@id,'vendor-group-switch-modal')]"
SwitchTo_FR = ".//*[contains(text(),'Switch regional accounts')]/following::input[2]"
SwitchTo_DE = ".//*[contains(text(),'Switch regional accounts')]/following::input[3]"
SwitchTo_ES = ".//*[contains(text(),'Switch regional accounts')]/following::input[4]"
SwitchTo_IT = ".//*[contains(text(),'Switch regional accounts')]/following::input[5]"
SwitchTo_GB = ".//*[contains(text(),'Switch regional accounts')]/following::input[6]"
SwitchAccount = ".//*[contains(@id,'vendor-group-switch-confirm-button')]/span/input"
SignOut = ".//*[contains(@id,'logout_topRightNav')]"

# Portal URL of Suppliers.
# Glidan
Gildan_URL = "https://vendorcentral.amazon.com/gp/vendor/sign-in"
SalesDiagnostic_Gildan = "https://vendorcentral.amazon.com/analytics/dashboard/salesDiagnostic"
InventoryHealth_Gildan = "https://vendorcentral.amazon.com/analytics/dashboard/inventoryHealth"
# LacrosseFootwearInc
LacrosseFootwearInc_URL = "https://vendorcentral.amazon.com/gp/vendor/sign-in"
SalesDiagnostic_lacrosse = "https://vendorcentral.amazon.com/analytics/dashboard/salesDiagnostic"
InventoryHealth_lacrosse = "https://vendorcentral.amazon.com/analytics/dashboard/inventoryHealth"
SalesDiagnostic_Danner = "https://vendorcentral.amazon.com/analytics/dashboard/salesDiagnostic"
InventoryHealth_Danner = "https://vendorcentral.amazon.com/analytics/dashboard/inventoryHealth"
#UnderArmourIndia
UnderArmourIndia_URL = "https://www.vendorcentral.in/gp/vendor/sign-in"
SalesDiagnostic_India = "https://www.vendorcentral.in/analytics/dashboard/salesDiagnostic"
InventoryHealth_India = "https://www.vendorcentral.in/analytics/dashboard/inventoryHealth"
#UnderArmourEurope
UnderArmourEurope_URL = "http://vendorcentral.amazon.it/gp/vendor/sign-in"
SalesDiagnostic_Europe = "https://vendorcentral.amazon.it/analytics/dashboard/salesDiagnostic"
InventoryHealth_Europe = "https://vendorcentral.amazon.it/analytics/dashboard/inventoryHealth"



# loginId and loginCode of Suppliers.
Gildan_Username = 'amazonportal-gildan@spscommerce.com'
Gildan_Password = 'SPSap2*'
LacrosseFootwearInc_lacrosse_Username = "amazonportal-lacrosse@spscommerce.com"
LacrosseFootwearInc_lacrosse_Password = "SPSap2*"
LacrosseFootwearInc_danner_Username = "amazonportal-danner@spscommerce.com"
LacrosseFootwearInc_danner_Password = "SPSap2**"
UnderArmourIndia_Username = "amazonportal-uaindia@spscommerce.com"
UnderArmourIndia_Password = "SPSap2*"
UnderArmourEurope_Username = "amazonportal-uaeurope@spscommerce.com"
UnderArmourEurope_Password = "SPSap2*"

