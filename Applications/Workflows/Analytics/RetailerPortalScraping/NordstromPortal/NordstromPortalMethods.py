"""
@ Author - Krishnabhashkar jha
@ Creation date - 30/01/2020
@ Description - Declares all the Methods to be used at the Process Level.
"""

import getpass
import glob
import os
import shutil
import time
import datetime

from Applications.Workflows.Analytics.RetailerPortalScraping.NordstromPortal import NordstromElementLocators as Element
from Applications.Workflows.Analytics.RetailerPortalScraping.Utilites.SeleniumOperations import SeleniumOperations

class NordstromPortalMethods():

    def __init__(self,v_Browser,lo,currentDate):
        self.v_Browser = v_Browser
        self.lo = lo
        self.currentDate = currentDate

    def Login(self,supplier):
        try:
            SeleniumOperation = SeleniumOperations(self.v_Browser, self.lo)
            self.v_Browser.get(Element.NordstromPortal_URL)
            SeleniumOperation.click_element_by_xpath(Element.Nordstrom_Login)
            if supplier == "NorthFace":
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,Element.NorthFace_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,Element.NorthFace_Password)
            elif supplier == "NuFace":
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,Element.NuFace_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,Element.NuFace_Password)
            elif supplier == "NewBalanceAthleticShoe":
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,Element.NewBalance_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,Element.NewBalance_Password)
            elif supplier == "Vans":
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,Element.Vans_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,Element.Vans_Password)
            elif supplier == "DECKERS":
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,Element.Deckers_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,Element.Deckers_Password)
            elif supplier == "COLEHAAN":
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,Element.ColeHaan_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,Element.ColeHaan_Password)
            elif supplier == "LANAUNLIMITED":
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,Element.LanaUnlimited_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,Element.LanaUnlimited_Password)
            elif supplier == "WOLVERINE":
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,Element.Wolverine_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,Element.Wolverine_Password)
            elif supplier == "BabyBiling":
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,Element.BabyBling_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,Element.BabyBling_Password)
            elif supplier == "Reef":
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,Element.Reef_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,Element.Reef_Password)
            elif supplier == "SmartWool":
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,Element.SmartWool_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,Element.SmartWool_Password)
            elif supplier == "POPSOCKETS":
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,Element.PopSockets_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,Element.PopSockets_Password)
            elif supplier == "HerbivoreBotanicals":
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,Element.HerbivoreBotanicals_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,Element.HerbivoreBotanicals_Password)
            elif supplier == "SAXXUNDERWAER":
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath, Element.SaxxUnderwear_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath, Element.SaxxUnderwear_Password)
            SeleniumOperation.click_element_by_xpath(Element.Supplier_Login_click)
            time.sleep(10)
            self.lo.log_to_file(self, "INFO", "Successfully Login to " + str(supplier))
        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception:" + str(e))

    def DownloadReport(self,code,dept):
        SeleniumOperation = SeleniumOperations(self.v_Browser, self.lo)
        try:
            if code == "938220761":
                self.v_Browser.get(Element.NorthFace_click)
            elif code == "5102324":
                self.v_Browser.get(Element.Cp_NorthFace_click)
            elif code == "5076122":
                self.v_Browser.get(Element.Beauty_NuFace_click)
            elif code == "5070871":
                self.v_Browser.get(Element.SPA_NuFace_click)
            elif code == "136864699":
                self.v_Browser.get(Element.NewBalance_click)
            elif code == "285090864":
                self.v_Browser.get(Element.Vans_click)
            elif code == "5088781":
                self.v_Browser.get(Element.Deckers_UGGAL_click)
            elif code == "114374778":
                self.v_Browser.get(Element.Deckers_UGG_click)
            elif code == "136541105":
                self.v_Browser.get(Element.ColeHaan_click)
            elif code == "5085028":
                self.v_Browser.get(Element.LanaUnlimited_click)
            elif code == "163500919":
                self.v_Browser.get(Element.Wolverine_SperryTopSiderFootwear_click)
            elif code == "116133218":
                self.v_Browser.get(Element.Wolverine_Merrell_click)
            elif code == "422866488":
                self.v_Browser.get(Element.Wolverine_Chaco_click)
            elif code == "5069454":
                self.v_Browser.get(Element.Wolverine_KedsKids_click)
            elif code == "115437843":
                self.v_Browser.get(Element.Wolverine_SperryKids_click)
            elif code == "706306622":
                self.v_Browser.get(Element.Wolverine_SauconyChildrensFootwear_click)
            elif code == "5117957":
                self.v_Browser.get(Element.Wolverine_MerrellKidsFootwear_click)
            elif code == "153104053":
                self.v_Browser.get(Element.Wolverine_KedsWomensMens_click)
            elif code == "5097801":
                self.v_Browser.get(Element.Wolverine_KedsforKateSpadeNewYork_click)
            elif code == "5073558":
                self.v_Browser.get(Element.BabyBling_click)
            elif code == "777311493":
                self.v_Browser.get(Element.Reef_click)
            elif code == "159643183":
                self.v_Browser.get(Element.SmartWool_click)
            elif code == "5144037":
                self.v_Browser.get(Element.PopSockets_click)
            elif code == "5113558":
                self.v_Browser.get(Element.SaxxUnderwear_click)
            SeleniumOperation.click_element_by_xpath(Element.DepartmentNumber_click)
            time.sleep(5)
            self.Select_Dept(dept)
            SeleniumOperation.click_element_by_xpath(Element.Sales_and_Inventory_by_DeptVPN_click)
            time.sleep(5)
            SeleniumOperation.click_element_by_xpath(Element.Generate_CSV_Report_click)
            time.sleep(18)
            self.lo.log_to_file(self, "INFO", "Successfully Report Downloaded for dept " + str(dept))
        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception: " + str(e))

    def Select_Dept(self,dept):
        try:
            SeleniumOperation = SeleniumOperations(self.v_Browser, self.lo)
            if dept == "16":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_16_click)
            elif dept == "2":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_2_click)
            elif dept == "631":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_631_click)
            elif dept =="588":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_588_click)
            elif dept == "537":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_537_click)
            elif dept == "62":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_62_click)
            elif dept == "61":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_61_click)
            elif dept == "60":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_60_click)
            elif dept == "30":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_30_click)
            elif dept == "59":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_59_click)
            elif dept == "58":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_58_click)
            elif dept == "341":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_341_click)
            elif dept == "98":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_98_click)
            elif dept == "64":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_64_click)
            elif dept == "37":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_37_click)
            elif dept == "123":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_123_click)
            elif dept == "122":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_122_click)
            elif dept == "525":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_525_click)
            elif dept == "723 - MENS OUTERWEAR-NorthFace":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_723_click)
            elif dept == "587":
                SeleniumOperation.click_element_by_xpath(Element.NorthFace_DepartmentNumber_587_click)
            elif dept == "276":
                SeleniumOperation.click_element_by_xpath(Element.NuFace_DepartmentNumber_276_click)
            elif dept == "32":
                SeleniumOperation.click_element_by_xpath(Element.NuFace_DepartmentNumber_32_click)
            elif dept == "37 - WOMENS ACTIVE SHOES-NewBalance":
                SeleniumOperation.click_element_by_xpath(Element.NewBalance_DepartmentNumber_37_click)
            elif dept == "123 - MENS ACTIVE SHOES-NewBalance":
                SeleniumOperation.click_element_by_xpath(Element.NewBalance_DepartmentNumber_123_click)
            elif dept == "54 - KIDS SHOES-NewBalance":
                SeleniumOperation.click_element_by_xpath(Element.NewBalance_DepartmentNumber_54_click)
            elif dept == "16 - ACTIVEWEAR-NewBalance":
                SeleniumOperation.click_element_by_xpath(Element.NewBalance_DepartmentNumber_16_click)
            elif dept == "588 - M ACTIVE/OUTERWER-NewBalance":
                SeleniumOperation.click_element_by_xpath(Element.NewBalance_DepartmentNumber_588_click)
            elif dept == "37 - WOMENS ACTIVE SHOES":
                SeleniumOperation.click_element_by_xpath(Element.vans_DepartmentNumber_37_click)
            elif dept == "127 - MENS TREND SHOES":
                SeleniumOperation.click_element_by_xpath(Element.vans_DepartmentNumber_127_click)
            elif dept == "54 - KIDS SHOES":
                SeleniumOperation.click_element_by_xpath(Element.vans_DepartmentNumber_54_click)
            elif dept == "75 - YOUNG MENS CONTEMPORARY":
                SeleniumOperation.click_element_by_xpath(Element.vans_DepartmentNumber_75_click)
            elif dept == "59 - BOYS 8-20":
                SeleniumOperation.click_element_by_xpath(Element.vans_DepartmentNumber_59_click)
            elif dept == "627 - YC DENIM & EMERGING BRANDS":
                SeleniumOperation.click_element_by_xpath(Element.vans_DepartmentNumber_627_click)
            elif dept == "58 - LITTLE BOYS":
                SeleniumOperation.click_element_by_xpath(Element.vans_DepartmentNumber_58_click)
            elif dept == "98 - BOYS ACC/SLP":
                SeleniumOperation.click_element_by_xpath(Element.vans_DepartmentNumber_98_click)
            elif dept == "97 - BP ACCESSORIES":
                SeleniumOperation.click_element_by_xpath(Element.vans_DepartmentNumber_97_click)
            elif dept == "537 - M ACCESSORIES":
                SeleniumOperation.click_element_by_xpath(Element.vans_DepartmentNumber_537_click)
            elif dept == "122 - KIDS SHOES ACCESSORIES1":
                SeleniumOperation.click_element_by_xpath(Element.vans_DepartmentNumber_122_click)
            elif dept == "608 - EMERGING DESIGNERS":
                SeleniumOperation.click_element_by_xpath(Element.vans_DepartmentNumber_608_click)
            elif dept == "3 - HOSIERY":
                SeleniumOperation.click_element_by_xpath(Element.Deckers_DepartmentNumber_3_click)
            elif dept == "53 - SLEEPWEAR":
                SeleniumOperation.click_element_by_xpath(Element.Deckers_DepartmentNumber_53_click)
            elif dept == "536 - M SPECIALIZED":
                SeleniumOperation.click_element_by_xpath(Element.Deckers_DepartmentNumber_536_click)
            elif dept == "40 - SOFT GOODS/HOLIDAY":
                SeleniumOperation.click_element_by_xpath(Element.Deckers_DepartmentNumber_40_click)
            elif dept == "631 - PERFORMANCE OUTERWEAR":
                SeleniumOperation.click_element_by_xpath(Element.Deckers_DepartmentNumber_631_click)
            elif dept == "588 - M ACTIVE/OUTERWER":
                SeleniumOperation.click_element_by_xpath(Element.Deckers_DepartmentNumber_588_click)
            elif dept == "24 - MENS UT/MODERN SHOES":
                SeleniumOperation.click_element_by_xpath(Element.Deckers_DepartmentNumber_24_click)
            elif dept == "122 - KIDS SHOES ACCESSORIES2":
                SeleniumOperation.click_element_by_xpath(Element.Deckers_DepartmentNumber_122_click)
            elif dept == "526 - WOMENS UGG SHOES":
                SeleniumOperation.click_element_by_xpath(Element.Deckers_DepartmentNumber_526_click)
            elif dept == "24 - MENS UT/MODERN SHOES2":
                SeleniumOperation.click_element_by_xpath(Element.ColeHaan_DepartmentNumber_24_click)
            elif dept == "109 - WOMENS CORE SHOES":
                SeleniumOperation.click_element_by_xpath(Element.ColeHaan_DepartmentNumber_109_click)
            elif dept == "191 - SP MENS UT/LUXURY SHOES":
                SeleniumOperation.click_element_by_xpath(Element.ColeHaan_DepartmentNumber_191_click)
            elif dept == "229 - SP SALON/PROGRESSV/BRIDGE SHOE":
                SeleniumOperation.click_element_by_xpath(Element.ColeHaan_DepartmentNumber_229_click)
            elif dept == "574 - SP JEWELRY":
                SeleniumOperation.click_element_by_xpath(Element.LanaUnlimited_DepartmentNumber_574_click)
            elif dept == "696 - MODERN FINE JEWELRY":
                SeleniumOperation.click_element_by_xpath(Element.LanaUnlimited_DepartmentNumber_696_click)
            elif dept == "127 - MENS TREND SHOES-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_127_click)
            elif dept == "191 - SP MENS UT/LUXURY SHOES2-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_191_click)
            elif dept == "192 - SP WOMENS UT SHOES-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_192_click)
            elif dept == "525 - COMFORT SHOES-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_525_click)
            elif dept == "103 - SP WOMENS ACTIVE SHOES-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_103_click)
            elif dept == "123 - MENS ACTIVE SHOES-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_123_click)
            elif dept == "179 - SP MEN1-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_179_click)
            elif dept == "525 - COMFORT SHOES2-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_525_Merrell_click)
            elif dept == "103 - SP WOMENS ACTIVE SHOES2-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_103_charco_click)
            elif dept == "123 - MENS ACTIVE SHOES2-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_123_charco_click)
            elif dept == "179 - SP MEN2-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_179_charco_click)
            elif dept == "525 - COMFORT SHOES3-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_525_charco_click)
            elif dept == "54 - KIDS SHOES-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_54_click)
            elif dept == "178 - SP GIRLS SHOES-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_178_click)
            elif dept == "54 - KIDS SHOES2-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_54_SperryKids_click)
            elif dept == "178 - SP GIRLS SHOES2-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_178_SperryKids_click)
            elif dept == "607 - SP BOYS SHOES-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_607_SperryKids_click)
            elif dept == "54 - KIDS SHOES3-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_54_SauconyFootwear_click)
            elif dept == "493 - SP BOYS ATHLETIC SHOES-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_493_SauconyFootwear_click)
            elif dept == "638 - SP GIRLS ATHLETIC SHOES-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_638_SauconyFootwear_click)
            elif dept == "122 - KIDS SHOES ACCESSORIES3-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_122_click)
            elif dept == "37 - WOMENS ACTIVE SHOES2-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_37_click)
            elif dept == "193 - SP JUNIOR/CONTEMPORARY SHOES-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_193_click)
            elif dept == "37 - WOMENS ACTIVE SHOES3-Wolverine":
                SeleniumOperation.click_element_by_xpath(Element.Wolverine_DepartmentNumber_37_Kfork_click)
            elif dept == "64 - INFANT ACCESSORIES-BabyBiling":
                SeleniumOperation.click_element_by_xpath(Element.BabyBling_department_64_click)
            elif dept == "37 - WOMENS ACTIVE SHOES-Reef":
                SeleniumOperation.click_element_by_xpath(Element.Reef_DepartmentNumber_37_click)
            elif dept == "122 - KIDS SHOES ACCESSORIES-Reef":
                SeleniumOperation.click_element_by_xpath(Element.Reef_DepartmentNumber_122_click)
            elif dept == "127 - MENS TREND SHOES-Reef":
                SeleniumOperation.click_element_by_xpath(Element.Reef_DepartmentNumber_127_click)
            elif dept == "178 - SP GIRLS SHOES-Reef":
                SeleniumOperation.click_element_by_xpath(Element.Reef_DepartmentNumber_178_click)
            elif dept == "193 - SP JUNIOR/CONTEMPORARY SHOES-Reef":
                SeleniumOperation.click_element_by_xpath(Element.Reef_DepartmentNumber_193_click)
            elif dept == "240 - SP MENS TREND SHOES-Reef":
                SeleniumOperation.click_element_by_xpath(Element.Reef_DepartmentNumber_240_click)
            elif dept == "607 - SP BOYS SHOES-Reef":
                SeleniumOperation.click_element_by_xpath(Element.Reef_DepartmentNumber_607_click)
            elif dept == "3 - HOSIERY-SmartWool":
                SeleniumOperation.click_element_by_xpath(Element.SmartWool_DepartmentNumber_3_click)
            elif dept == "536 - M SPECIALIZED-SmartWool":
                SeleniumOperation.click_element_by_xpath(Element.SmartWool_DepartmentNumber_536_click)
            elif dept == "588 - M ACTIVE/OUTERWER-SmartWool":
                SeleniumOperation.click_element_by_xpath(Element.SmartWool_DepartmentNumber_588_click)
            elif dept == "631 - PERFORMANCE OUTERWEAR-SmartWool":
                SeleniumOperation.click_element_by_xpath(Element.SmartWool_DepartmentNumber_631_click)
            elif dept == "267 - SP MEN-SmartWool":
                SeleniumOperation.click_element_by_xpath(Element.SmartWool_DepartmentNumber_267_click)
            elif dept == "67 - SP HOSIERY/SOCKS-SmartWool":
                SeleniumOperation.click_element_by_xpath(Element.SmartWool_DepartmentNumber_67_click)
            elif dept == "44 - YC HANDBAGS-PopSockets":
                SeleniumOperation.click_element_by_xpath(Element.PopSockets_DepartmentNumber_44_click)
            elif dept == "587 - POP IN SHOP-PopSockets":
                SeleniumOperation.click_element_by_xpath(Element.PopSockets_DepartmentNumber_587_click)
            elif dept == "267 - SP MEN-SaxxUnderwear":
                SeleniumOperation.click_element_by_xpath(Element.SaxxUnderwear_DepartmentNumber_267_click)
            elif dept == "536 - M SPECIALIZED-SaxxUnderwear":
                SeleniumOperation.click_element_by_xpath(Element.SaxxUnderwear_DepartmentNumber_536_click)
            elif dept == "588 - M ACTIVE/OUTERWER-SaxxUnderwear":
                SeleniumOperation.click_element_by_xpath(Element.SaxxUnderwear_DepartmentNumber_588_click)
        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception: " + str(e) +str(dept))

    def Logout(self,supplier):
        try:
            SeleniumOperation = SeleniumOperations(self.v_Browser, self.lo)
            SeleniumOperation.click_element_by_xpath(Element.SPS_Commerce_click)
            time.sleep(3)
            SeleniumOperation.click_element_by_xpath(Element.Logout_click)
            self.lo.log_to_file(self, "INFO", "Successfully Logout from "+str(supplier))
        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception: " + str(e))


    def RenameReport(self,dept):
        try:
            home = os.path.expanduser('~')  # print(home)  C:\Users\krishnabhashkar.jha
            location = os.path.join(home, "Downloads")
            file = os.path.join(location,str(dept) + ".csv")
            path = "C:\\Users\\Krishnabhashkar.Jha\\Downloads\\" + str(os.listdir(r'C:\Users\Krishnabhashkar.Jha\Downloads')[0])
            os.rename(path, file)
            time.sleep(3)
            self.lo.log_to_file(self, "INFO", "Successfully Report Rename for dept " + str(dept))
        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception: " + str(e))

    def RenameReportForWolverine(self,AccountName,dept):
        try:
            home = os.path.expanduser('~')  # print(home)  C:\Users\krishnabhashkar.jha
            location = os.path.join(home, "Downloads")
            file = os.path.join(location,str(AccountName)+"_"+str(dept) + ".csv")
            path = "C:\\Users\\Krishnabhashkar.Jha\\Downloads\\" + str(os.listdir(r'C:\Users\Krishnabhashkar.Jha\Downloads')[0])
            os.rename(path, file)
            time.sleep(3)
            self.lo.log_to_file(self, "INFO", "Successfully Report Rename for dept " + str(dept))
        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception: " + str(e))

    def Move_File(self,supplier,dept):
        try:
            today = datetime.date.today()
            offset = (today.weekday() - 5) % 7
            last_saturday = today - datetime.timedelta(days=offset)
            # today = datetime.date.today()
            # currentDate = datetime.datetime.today().strftime("%d-%b-%Y")
            # Days = datetime.datetime.now()
            # var_foldername = Days.strftime("%d-%b-%Y")
            # # offset = (today.weekday() - 5) % 7
            list_of_files = glob.glob("C:\\Users\\" + getpass.getuser() + "\\Downloads\\*")
            latest_file_In_Download = max(list_of_files, key=os.path.getctime)
            move_location = 'C:\\Automation\\Nordstrom' + "\\" + self.currentDate + "\\" + supplier + "_" + "NordstromPortal" + "_" + str(last_saturday)
            shutil.move(latest_file_In_Download, move_location)
            self.lo.log_to_file(self, "INFO", "Successfully Report Move in there Respective dept  " + str(dept))
        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception:" + str(e))

    def GetDate(self,supplier):
        today = datetime.date.today()
        offset = (today.weekday() - 5) % 7
        last_saturday = today - datetime.timedelta(days=offset)
        # currentDate = datetime.datetime.today().strftime("%d-%m-%Y")
        os.makedirs('C:\\Automation\\Nordstrom' + "\\" + self.currentDate + "\\" + supplier + "_" + "NordstromPortal" + "_" + str(last_saturday))


