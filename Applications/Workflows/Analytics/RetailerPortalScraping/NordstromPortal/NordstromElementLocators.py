"""
@ Author - Krishnabhashkar jha
@ Creation date - 28/01/2020
@ Description - Declares all the constants to be used at the Process Level.
"""

# Xpath of DownloadNordstromReport.
Nordstrom_Login = ".//*[contains(text(),'Log In')]"
Login_Email_Xpath = "//input[@type='text' and @name = 'username']" #".//*[contains(text(),'Sign In')]/following::input[1]"
Login_Password_Xpath = "//input[@type='password' and @name = 'password']"#".//*[contains(text(),'Sign In')]/following::input[2]"
Supplier_Login_click = "//button[@type='submit']"
DepartmentNumber_click = ".//*[contains(@id,'rw_1_input')]"
Sales_and_Inventory_by_DeptVPN_click = '//*[contains(@id,"root")]/div/div/div[2]/div/div/div/div/ul/div[2]'
Generate_CSV_Report_click = '//*[@id="root"]/div/div/div[2]/div/div/div/div/ul/div[2]/div[2]/div/div/div/div/div[2]/button[2]'
SPS_Commerce_click = "//button[@type='button']/span[1]/span"
# Logout_click = ".//*[contains(@id,'profile-menu')]/div[2]/ul/li[contains(text(),'Logout')]"
Logout_click = ".//*[contains(text(),'Logout')]"

# Department Select click
# NorthFace Dept
NorthFace_DepartmentNumber_16_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'16 - ACTIVEWEAR')]"
NorthFace_DepartmentNumber_2_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'2 - COATS')]"
NorthFace_DepartmentNumber_631_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'631 ')]"
NorthFace_DepartmentNumber_588_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'588 ')]"
NorthFace_DepartmentNumber_537_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'537 ')]"
NorthFace_DepartmentNumber_62_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'62 ')]"
NorthFace_DepartmentNumber_61_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'61 - LITTLE GIRLS')]"
NorthFace_DepartmentNumber_60_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'60 - INFANT GIRLS')]"
NorthFace_DepartmentNumber_30_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'30 - GIRLS ACC/SLP')]"
NorthFace_DepartmentNumber_59_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'59 - BOYS 8-20')]"
NorthFace_DepartmentNumber_58_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'58 - LITTLE BOYS')]"
NorthFace_DepartmentNumber_341_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'341 - INFANT BOYS')]"
NorthFace_DepartmentNumber_98_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'98 - BOYS ACC/SLP')]"
NorthFace_DepartmentNumber_64_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'64 - INFANT ACCESSORIES')]"
NorthFace_DepartmentNumber_37_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'37 - WOMENS ACTIVE SHOES')]"
NorthFace_DepartmentNumber_123_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'123 - MENS ACTIVE SHOES')]"
NorthFace_DepartmentNumber_122_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'122 - KIDS SHOES ACCESSORIES')]"
NorthFace_DepartmentNumber_525_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'525 - COMFORT SHOES')]"
NorthFace_DepartmentNumber_723_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'723 - MENS OUTERWEAR')]"
NorthFace_DepartmentNumber_587_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'587 - POP IN SHOP')]"
NuFace_DepartmentNumber_276_click = "//*[contains(text(),'Department Number')]/following::li[contains(text(),'276 - TR ADVANCED TECH/TOOLS')]"
NuFace_DepartmentNumber_32_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'32 - SPA NORDSTROM')]"
vans_DepartmentNumber_37_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'37 - WOMENS ACTIVE SHOES')]"
vans_DepartmentNumber_127_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'127 - MENS TREND SHOES')]"
vans_DepartmentNumber_54_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'54 - KIDS SHOES')][1]"
vans_DepartmentNumber_75_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'75 - YOUNG MENS CONTEMPORARY')]"
vans_DepartmentNumber_59_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'59 - BOYS 8-20')]"
vans_DepartmentNumber_627_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'627 - YC DENIM & EMERGING BRANDS')]"
vans_DepartmentNumber_58_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'58 - LITTLE BOYS')]"
vans_DepartmentNumber_98_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'98 - BOYS ACC/SLP')]"
vans_DepartmentNumber_97_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'97 - BP ACCESSORIES')]"
vans_DepartmentNumber_537_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'537 - M ACCESSORIES')]"
vans_DepartmentNumber_122_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'122 - KIDS SHOES ACCESSORIES')]"
vans_DepartmentNumber_608_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'608 - EMERGING DESIGNERS')]"
Deckers_DepartmentNumber_3_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'3 - HOSIERY')]"
Deckers_DepartmentNumber_53_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'53 - SLEEPWEAR')]"
Deckers_DepartmentNumber_536_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'536 - M SPECIALIZED')]"
Deckers_DepartmentNumber_40_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'40 - SOFT GOODS/HOLIDAY')]"
Deckers_DepartmentNumber_631_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'631 - PERFORMANCE OUTERWEAR')]"
Deckers_DepartmentNumber_588_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'588 - M ACTIVE/OUTERWER')]"
Deckers_DepartmentNumber_24_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'24 - MENS UT/MODERN SHOES')]"
Deckers_DepartmentNumber_122_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'122 - KIDS SHOES ACCESSORIES')]"
Deckers_DepartmentNumber_526_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'526 - WOMENS UGG SHOES')]"
ColeHaan_DepartmentNumber_24_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'24 - MENS UT/MODERN SHOES')][1]"
ColeHaan_DepartmentNumber_109_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'109 - WOMENS CORE SHOES')]"
ColeHaan_DepartmentNumber_191_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'191 - SP MENS UT/LUXURY SHOES')]"
ColeHaan_DepartmentNumber_229_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'229 - SP SALON/PROGRESSV/BRIDGE SHOE')]"
LanaUnlimited_DepartmentNumber_574_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'574 - SP JEWELRY')]"
LanaUnlimited_DepartmentNumber_696_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'696 - MODERN FINE JEWELRY')]"
Wolverine_DepartmentNumber_127_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'127 - MENS TREND SHOES')]"
Wolverine_DepartmentNumber_191_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'191 - SP MENS UT/LUXURY SHOES')]"
Wolverine_DepartmentNumber_192_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'192 - SP WOMENS UT SHOES')]"
Wolverine_DepartmentNumber_525_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'525 - COMFORT SHOES')]"
Wolverine_DepartmentNumber_103_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'103 - SP WOMENS ACTIVE SHOES')]"
Wolverine_DepartmentNumber_123_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'123 - MENS ACTIVE SHOES')]"
Wolverine_DepartmentNumber_179_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'179 - SP MEN')]"
Wolverine_DepartmentNumber_525_Merrell_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'525 - COMFORT SHOES')]"
Wolverine_DepartmentNumber_103_charco_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'103 - SP WOMENS ACTIVE SHOES')]"
Wolverine_DepartmentNumber_123_charco_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'123 - MENS ACTIVE SHOES')]"
Wolverine_DepartmentNumber_179_charco_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'179 - SP MEN')]"
Wolverine_DepartmentNumber_525_charco_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'525 - COMFORT SHOES')]"
Wolverine_DepartmentNumber_54_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'54 - KIDS SHOES')]"
Wolverine_DepartmentNumber_178_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'178 - SP GIRLS SHOES')]"
Wolverine_DepartmentNumber_54_SperryKids_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'54 - KIDS SHOES')]"
Wolverine_DepartmentNumber_178_SperryKids_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'178 - SP GIRLS SHOES')]"
Wolverine_DepartmentNumber_607_SperryKids_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'607 - SP BOYS SHOES')]"
Wolverine_DepartmentNumber_54_SauconyFootwear_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'54 - KIDS SHOES')]"
Wolverine_DepartmentNumber_493_SauconyFootwear_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'493 - SP BOYS ATHLETIC SHOES')]"
Wolverine_DepartmentNumber_638_SauconyFootwear_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'638 - SP GIRLS ATHLETIC SHOES')]"
Wolverine_DepartmentNumber_122_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'122 - KIDS SHOES ACCESSORIES')]"
Wolverine_DepartmentNumber_37_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'37 - WOMENS ACTIVE SHOES')]"
Wolverine_DepartmentNumber_193_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'193 - SP JUNIOR/CONTEMPORARY SHOES')]"
Wolverine_DepartmentNumber_37_Kfork_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'37 - WOMENS ACTIVE SHOES')]"
BabyBling_department_64_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'64 - INFANT ACCESSORIES')]"
Reef_DepartmentNumber_37_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'37 - WOMENS ACTIVE SHOES')]"
Reef_DepartmentNumber_122_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'122 - KIDS SHOES ACCESSORIES')]"
Reef_DepartmentNumber_127_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'127 - MENS TREND SHOES')]"
Reef_DepartmentNumber_178_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'178 - SP GIRLS SHOES')]"
Reef_DepartmentNumber_193_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'193 - SP JUNIOR/CONTEMPORARY SHOES')]"
Reef_DepartmentNumber_240_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'240 - SP MENS TREND SHOES')]"
Reef_DepartmentNumber_607_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'607 - SP BOYS SHOES')]"
SmartWool_DepartmentNumber_3_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'3 - HOSIERY')]"
SmartWool_DepartmentNumber_536_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'536 - M SPECIALIZED')]"
SmartWool_DepartmentNumber_588_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'588 - M ACTIVE/OUTERWER')]"
SmartWool_DepartmentNumber_631_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'631 - PERFORMANCE OUTERWEAR')]"
SmartWool_DepartmentNumber_267_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'267 - SP MEN')]"
SmartWool_DepartmentNumber_67_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'67 - SP HOSIERY/SOCKS')]"
PopSockets_DepartmentNumber_44_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'44 - YC HANDBAGS')]"
PopSockets_DepartmentNumber_587_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'587 - POP IN SHOP')]"
SaxxUnderwear_DepartmentNumber_267_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'267 - SP MEN')]"
SaxxUnderwear_DepartmentNumber_536_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'536 - M SPECIALIZED')]"
SaxxUnderwear_DepartmentNumber_588_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'588 - M ACTIVE/OUTERWER')]"
NewBalance_DepartmentNumber_37_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'37 - WOMENS ACTIVE SHOES')]"
NewBalance_DepartmentNumber_123_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'123 - MENS ACTIVE SHOES')]"
NewBalance_DepartmentNumber_54_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'54 - KIDS SHOES')]"
NewBalance_DepartmentNumber_16_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'16 - ACTIVEWEAR')]"
NewBalance_DepartmentNumber_588_click = ".//*[contains(text(),'Department Number')]/following::li[contains(text(),'588 - M ACTIVE/OUTERWER')]"
# Portal URL of Suppliers.
NordstromPortal_URL = "https://partner.nordstrom.com"
SupplierReport = 'https://partner.nordstrom.com/#/'
NorthFace_click = 'https://partner.nordstrom.com/#/reports/938220761'
Cp_NorthFace_click = 'https://partner.nordstrom.com/#/reports/5102324'
Beauty_NuFace_click = 'https://partner.nordstrom.com/#/reports/5076122'
SPA_NuFace_click = 'https://partner.nordstrom.com/#/reports/5070871'
NewBalance_click = 'https://partner.nordstrom.com/#/reports/136864699'
Vans_click = 'https://partner.nordstrom.com/#/reports/285090864'
Deckers_UGGAL_click = 'https://partner.nordstrom.com/#/reports/5088781'
Deckers_UGG_click = 'https://partner.nordstrom.com/#/reports/114374778'
ColeHaan_click = 'https://partner.nordstrom.com/#/reports/136541105'
LanaUnlimited_click = 'https://partner.nordstrom.com/#/reports/5085028'
Wolverine_SperryTopSiderFootwear_click = 'https://partner.nordstrom.com/#/reports/163500919'
Wolverine_Merrell_click = 'https://partner.nordstrom.com/#/reports/116133218'
Wolverine_Chaco_click = 'https://partner.nordstrom.com/#/reports/422866488'
Wolverine_KedsKids_click = 'https://partner.nordstrom.com/#/reports/5069454'
Wolverine_SperryKids_click = 'https://partner.nordstrom.com/#/reports/115437843'
Wolverine_SauconyChildrensFootwear_click = 'https://partner.nordstrom.com/#/reports/706306622'
Wolverine_MerrellKidsFootwear_click = 'https://partner.nordstrom.com/#/reports/5117957'
Wolverine_KedsWomensMens_click = 'https://partner.nordstrom.com/#/reports/153104053'
Wolverine_KedsforKateSpadeNewYork_click = 'https://partner.nordstrom.com/#/reports/5097801'
BabyBling_click = 'https://partner.nordstrom.com/#/reports/5073558'
Reef_click = 'https://partner.nordstrom.com/#/reports/777311493'
SmartWool_click = 'https://partner.nordstrom.com/#/reports/159643183'
PopSockets_click = 'https://partner.nordstrom.com/#/reports/5144037'
SaxxUnderwear_click = 'https://partner.nordstrom.com/#/reports/5113558'

# loginId and loginCode of Suppliers
NorthFace_Username = 'nordstromportal-northface@spscommerce.com'
NorthFace_Password = 'SPSnp123*****'
NuFace_Username = 'nordstromportal-nuface@spscommerce.com'
NuFace_Password = 'SPSnp123*****'
NewBalance_Username = 'nordstromportal-NEWBALANCEATHLETICSHOE@spscommerce.com'
NewBalance_Password = 'SPSnp123******'
Vans_Username = 'nordstromportal-vans@spscommerce.com'
Vans_Password = 'SPSnp123*****'
Deckers_Username = 'nordstromportal-ugg@spscommerce.com'
Deckers_Password = 'SPSnp123*****'
ColeHaan_Username = 'nordstromportal-colehaan@spscommerce.com'
ColeHaan_Password = 'SPSnp123***'
LanaUnlimited_Username = 'nordstromportal-lana@spscommerce.com'
LanaUnlimited_Password = 'SPSnp123*****'
Wolverine_Username = 'nordstromportal-wolverine@spscommerce.com'
Wolverine_Password = 'SPSnp123*****'
BabyBling_Username = 'nordstromportal-babybling@spscommerce.com'
BabyBling_Password = 'SPSnp123****'
Reef_Username = 'nordstromportal-Reef@spscommerce.com'
Reef_Password = 'SPSnp123***'
SmartWool_Username = 'nordstromportal-smartwool@spscommerce.com'
SmartWool_Password = 'SPSnp123***'
PopSockets_Username = 'nordstromportal-popsockets@spscommerce.com'
PopSockets_Password = 'SPSnp123***'
HerbivoreBotanicals_Username = 'Nordstromportal-HerbivoreBotanicals@spscommerce.com'
HerbivoreBotanicals_Password = 'SPSnp123*'
SaxxUnderwear_Username = 'kiersten.jirik@saxxunderwear.com'
SaxxUnderwear_Password = 'Something123!'
