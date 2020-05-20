"""
@ Author - Krishnabhashkar jha
@ Creation date - 17/01/2020
@ Description - Declares all the Methods to be used at the Process Level.
"""
import getpass
import glob
import os
import shutil
import time
import datetime
from Applications.Workflows.Analytics.RetailerPortalScraping.AmazonPortal import AmazonElementLocators as Element
from Applications.Workflows.Analytics.RetailerPortalScraping.Utilites.SeleniumOperations import SeleniumOperations


class AmazonPortalMethods():

    def __init__(self,v_Browser,lo):
        self.v_Browser = v_Browser
        self.lo = lo

    def Login(self,supplier):
        try:
            SeleniumOperation = SeleniumOperations(self.v_Browser, self.lo)
            if supplier == "GILDAN":
                self.v_Browser.get(Element.Gildan_URL)
                SeleniumOperation.click_element_by_xpath(Element.vendor_central_click)
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,Element.Gildan_Username)
                # username = self.v_Browser.find_element_by_xpath(Element.Login_Email_Xpath)
                # username.send_keys('amazonportal-gildan@spscommerce.com')
                # password = self.v_Browser.find_element_by_xpath(Element.Login_Password_Xpath)
                # password.send_keys('SPSap2*')
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,Element.Gildan_Password)
                SeleniumOperation.click_element_by_xpath(Element.Supplier_Login)
                self.lo.log_to_file(self, "INFO", "Successfully Login to Gildan")

            elif supplier == "LacrosseFootwearInclacrosse":
                self.v_Browser.get(Element.LacrosseFootwearInc_URL)
                SeleniumOperation.click_element_by_xpath(Element.vendor_central_click)
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,
                                                     Element.LacrosseFootwearInc_lacrosse_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,
                                                     Element.LacrosseFootwearInc_lacrosse_Password)
                SeleniumOperation.click_element_by_xpath(Element.Supplier_Login)
                self.lo.log_to_file(self, "INFO", "Successfully Login to LacrosseFootwearInclacrosse")

            elif supplier == "LacrosseFootwearIncdanner":
                self.v_Browser.get(Element.LacrosseFootwearInc_URL)
                SeleniumOperation.click_element_by_xpath(Element.vendor_central_click)
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath,
                                                     Element.LacrosseFootwearInc_danner_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath,
                                                     Element.LacrosseFootwearInc_danner_Password)
                SeleniumOperation.click_element_by_xpath(Element.Supplier_Login)
                self.lo.log_to_file(self, "INFO", "Successfully Login to LacrosseFootwearIncdanner")

            elif supplier == "UnderArmourIndia":
                self.v_Browser.get(Element.UnderArmourIndia_URL)
                SeleniumOperation.click_element_by_xpath(Element.vendor_central_click)
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath, Element.UnderArmourIndia_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath, Element.UnderArmourIndia_Password)
                SeleniumOperation.click_element_by_xpath(Element.Supplier_Login)
                self.lo.log_to_file(self, "INFO", "Successfully Login to UnderArmourIndia")

            elif supplier == "UnderArmourEurope":
                self.v_Browser.get(Element.UnderArmourEurope_URL)
                SeleniumOperation.click_element_by_xpath(Element.vendor_central_click)
                SeleniumOperation.send_text_by_xpath(Element.Login_Email_Xpath, Element.UnderArmourEurope_Username)
                SeleniumOperation.send_text_by_xpath(Element.Login_Password_Xpath, Element.UnderArmourEurope_Password)
                SeleniumOperation.click_element_by_xpath(Element.Supplier_Login)
                self.lo.log_to_file(self, "INFO", "Successfully Login to UnderArmourEurope")

        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception:" + str(e))


    def Download(self,report,supplier):
        SeleniumOperation = SeleniumOperations(self.v_Browser, self.lo)
        try:
            if report == "SALES":
                self.open_URL(report, supplier)
                SeleniumOperation.click_element_by_xpath(Element.Distributor_View)
                SeleniumOperation.click_element_by_xpath(Element.Distributor_View_Sourcing)
                SeleniumOperation.click_element_by_xpath(Element.Sales_View)
                if(SeleniumOperation.check_exists_by_xpath(Element.Sales_View_By_Country_Region) ==True):
                    SeleniumOperation.click_element_by_xpath(Element.Sales_View_By_Country_Region)
                else:
                    self.lo.log_to_file(self, "INFO", "Xpath is not there")
                SeleniumOperation.click_element_by_xpath(Element.Viewing)
                SeleniumOperation.click_element_by_xpath(Element.Viewing_Last_Report)
                if(SeleniumOperation.check_exists_by_xpath(Element.Apply_Change) ==True):
                    SeleniumOperation.click_element_by_xpath(Element.Apply_Change)
                else:
                    self.lo.log_to_file(self, "INFO", "Xpath is not there")
                SeleniumOperation.click_element_by_xpath(Element.Detail_View_Add)
                SeleniumOperation.click_element_by_xpath(Element.Add_UPC)
                SeleniumOperation.click_element_by_xpath(Element.Download_Click)
                SeleniumOperation.click_element_by_xpath(Element.Download_DetailView_Excel_Sales)
                time.sleep(15)
                self.v_Browser.switchTo().alert().accept()
                time.sleep(15)
                self.lo.log_to_file(self, "INFO", "Successfully Download Sales Report for " +str(supplier))
            elif report == "INVENTORY":
                self.open_URL(report,supplier)
                SeleniumOperation.click_element_by_xpath(Element.Distributor_View)
                SeleniumOperation.click_element_by_xpath(Element.Distributor_View_Sourcing)
                SeleniumOperation.click_element_by_xpath(Element.Viewing)
                SeleniumOperation.click_element_by_xpath(Element.Viewing_Last_Report)
                SeleniumOperation.click_element_by_xpath(Element.Detail_View_Add)
                SeleniumOperation.click_element_by_xpath(Element.Add_UPC)
                SeleniumOperation.click_element_by_xpath(Element.Download_Click)
                SeleniumOperation.click_element_by_xpath(Element.Download_DetailView_Excel_Inventory)
                time.sleep(40)
                self.v_Browser.switchTo().alert().accept()
                time.sleep(20)
                self.lo.log_to_file(self, "INFO", "Successfully Download Inventory Report for " + str(supplier))
        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception: " + str(e))


    def open_URL(self,report,supplier):
        if report == "SALES":
            if supplier == "GILDAN":
                print("GILDAN")
                self.v_Browser.get(Element.SalesDiagnostic_Gildan)
        elif report == "INVENTORY":
            if supplier == "GILDAN":
                self.v_Browser.get(Element.InventoryHealth_Gildan)


    def SignOut(self,supplier):
        try:
            SeleniumOperation = SeleniumOperations(self.v_Browser, self.lo)
            SeleniumOperation.click_element_by_xpath(Element.SignOut)
            self.lo.log_to_file(self, "INFO", "Successfully SignOut from "+str(supplier))
        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception: " + str(e))


    def Rename_File(self,report,supplier,country):
        try:
            global report_shortcut
            home = os.path.expanduser('~')  # print(home)  C:\Users\krishnabhashkar.jha
            location1 = os.path.join(home, "Downloads")  # print(location)  C:\Users\krishnabhashkar.jha\Downloads
            today = datetime.date.today()
            Days = datetime.datetime.now()
            offset = (today.weekday() - 5) % 7
            last_saturday = today - datetime.timedelta(days=offset)
            if report == "SALES":
                sales = os.path.join(location1, "Sales Diagnostic" + "_" + "Detail View" + "_" + country + ".xlsx")
                Sales = os.path.join(location1, "AMAZONPORTAL" + "_" + supplier + "_" + report + "_" + str(last_saturday.strftime('%Y%m%d')) + ".xlsx")
                os.rename(sales, Sales)
                self.lo.log_to_file(self, "INFO", "Successfully Rename Sales Report for " + str(supplier))
            elif report == "INVENTORY":
                inventory = os.path.join(location1,"Inventory Health"+ "_" + country + ".xlsx")
                inventorys = os.path.join(location1, "AMAZONPORTAL" + "_" + supplier + "_" + report + "_" + str(last_saturday.strftime('%Y%m%d')) + ".xlsx")
                os.rename(inventory, inventorys)
                self.lo.log_to_file(self, "INFO", "Successfully Rename Inventory Report for " + str(supplier))
        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception: " + str(e))


    def Move_File(self):
        try:
            today = datetime.date.today()
            Days = datetime.datetime.now()
            var_foldername = Days.strftime("%d-%b-%Y")
            offset = (today.weekday() - 5) % 7
            list_of_files =glob.glob("C:\\Users\\" + getpass.getuser() + "\\Downloads\\*")
            latest_file_In_Download = max(list_of_files, key=os.path.getctime)
            print(latest_file_In_Download)
            move_location = 'C:\\Automation\Amazon' + "\\" + var_foldername + "\\" + 'AmazonPortal'
            time.sleep(3)
            shutil.move(latest_file_In_Download, move_location)

        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception:" + str(e))

