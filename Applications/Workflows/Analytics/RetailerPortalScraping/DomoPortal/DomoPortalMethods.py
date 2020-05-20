"""
@ Author - Krishnabhashkar jha
@ Creation date - 7/12/2019
@ Description - All methods .
"""
import os
import glob
import time
import shutil
import getpass
import openpyxl
import datetime
from self import self
from Applications.Workflows.Analytics.RetailerPortalScraping.DomoPortal import DomoElementLocators
from Applications.Workflows.Analytics.RetailerPortalScraping.Utilites.LogFileUtility import LogFileUtility
from Applications.Workflows.Analytics.RetailerPortalScraping.Utilites.SeleniumOperations import SeleniumOperations


def Login(self,v_Browser, supplier,lo):
    SeleniumOperation = SeleniumOperations(v_Browser, lo)
    v_Browser.get(DomoElementLocators.DomoPortal_URL)
    v_Browser.find_element_by_xpath(DomoElementLocators.Use_Direct_Sign_On).click()
    try:
        if supplier == "ColumbiaSportswear":
            # email = DomoElementLocators.Columbia_Sportswear_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Columbia_Sportswear_Username)
            # password = DomoElementLocators.Columbia_Sportswear_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Columbia_Sportswear_Password)
            # time.sleep(10)
        elif supplier == "VistaOutdoors":
            # email = DomoElementLocators.Vista_Outdoors_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Vista_Outdoors_Username)
            # password = DomoElementLocators.Vista_Outdoors_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Vista_Outdoors_Password)
        elif supplier == "KeenFootwear":
            # email = DomoElementLocators.Keen_Footwear_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Keen_Footwear_Username)
            # password = DomoElementLocators.Keen_Footwear_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Keen_Footwear_Password)
        elif supplier == "NorthFace":
            # email = DomoElementLocators.North_Face_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.North_Face_Username)
            # password = DomoElementLocators.North_Face_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.North_Face_Password)
        elif supplier == "Crocs":
            # email = DomoElementLocators.Crocs_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Crocs_Username)
            # password = DomoElementLocators.Crocs_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Crocs_Password)
        elif supplier == "Beretta":
            # email = DomoElementLocators.Beretta_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Beretta_Username)
            # password = DomoElementLocators.Beretta_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Beretta_Password)
        elif supplier == "PureFishing":
            # email = DomoElementLocators.Pure_Fishing_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Pure_Fishing_Username)
            # password = DomoElementLocators.Pure_Fishing_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Pure_Fishing_Password)
        elif supplier == "Saxx":
            # email = DomoElementLocators.Saxx_username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Saxx_username)
            # password = DomoElementLocators.Saxx_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Saxx_Password)
        elif supplier == "Yeti":
            # email = DomoElementLocators.Yeti_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Yeti_Username)
            # password = DomoElementLocators.Yeti_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Yeti_Password)
        elif supplier == "PelicanProducts":
            # email = DomoElementLocators.Pelican_Products_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Pelican_Products_Username)
            # password = DomoElementLocators.Pelican_Products_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Pelican_Products_Password)
        elif supplier == "GFiveOutdoors":
            # email = DomoElementLocators.G_Five_Outdoors_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.G_Five_Outdoors_Username)
            # password = DomoElementLocators.G_Five_Outdoors_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.G_Five_Outdoors_Password)
        elif supplier == "LacrosseFootwear":
            # email = DomoElementLocators.LacrosseFootwear_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.LacrosseFootwear_Username)
            # password = DomoElementLocators.LacrosseFootwear_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.LacrosseFootwear_Password)
        elif supplier == "UnderArmour":
            # email = DomoElementLocators.UnderArmour_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.UnderArmour_Username)
            # password = DomoElementLocators.UnderArmour_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.UnderArmour_Password)
        elif supplier == "GerberLegendaryBlades":
            # email = DomoElementLocators.GerberLegendaryBlades_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.GerberLegendaryBlades_Username)
            # password = DomoElementLocators.GerberLegendaryBlades_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.GerberLegendaryBlades_Password)
        elif supplier == "SITKAGear":
            # email = DomoElementLocators.SITKAGear_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.SITKAGear_Username)
            # password = DomoElementLocators.SITKAGear_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.SITKAGear_Password)
        elif supplier == "CarlZeiss":
            # email = DomoElementLocators.CarlZeiss_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.CarlZeiss_Username)
            # password = DomoElementLocators.Carlzeiss_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Carlzeiss_Password)
        elif supplier == "Kimber":
            # email = DomoElementLocators.Kimber_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Kimber_Username)
            # password = DomoElementLocators.Kimber_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Kimber_Password)
        elif supplier == "Wolverine":
            # email = DomoElementLocators.Wolverine_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Wolverine_Username)
            # password = DomoElementLocators.Wolverine_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Wolverine_Password)
        elif supplier == "GearAid":
            # email = DomoElementLocators.GearAid_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.GearAid_Username)
            # password = DomoElementLocators.GearAid_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.GearAid_Password)
        elif supplier == "GildanApparel":
            # email = DomoElementLocators.GildanApparel_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.GildanApparel_Username)
            # password = DomoElementLocators.GildanApparel_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.GildanApparel_Password)
        elif supplier == "MtnOps":
            # email = DomoElementLocators.MtnOps_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.MtnOps_Username)
            # password = DomoElementLocators.MtnOps_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.MtnOps_Password)
        elif supplier == "VistaOutdoor":
            # email = DomoElementLocators.VistaOutdoor_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.VistaOutdoor_Username)
            # password = DomoElementLocators.VistaOutdoor_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.VistaOutdoor_Password)
        elif supplier == "AmericanAccessoriesInc":
            # email = DomoElementLocators.AmericanAccessoriesInc_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.AmericanAccessoriesInc_Username)
            # password = DomoElementLocators.AmericanAccessoriesInc_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.AmericanAccessoriesInc_Password)
        elif supplier == "BenchmadeKnifeCo":
            # email = DomoElementLocators.BenchmadeKnifeCo_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.BenchmadeKnifeCo_Username)
            # password = DomoElementLocators.BenchmadeKnifeCo_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.BenchmadeKnifeCo_Password)
        elif supplier == "Chums":
            # email = DomoElementLocators.Chums_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Chums_Username)
            # password = DomoElementLocators.Chums_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Chums_Password)
        elif supplier == "DrewBradyCompanyInc":
            # email = DomoElementLocators.DrewBradyCompanyInc_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.DrewBradyCompanyInc_Username)
            # password = DomoElementLocators.DrewBradyCompanyInc_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.DrewBradyCompanyInc_Password)
        elif supplier == "TervisTumbler":
            # email = DomoElementLocators.TervisTumbler_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.TervisTumbler_Username)
            # password = DomoElementLocators.TervisTumbler_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.TervisTumbler_Password)
        elif supplier == "BuckGardnerCalls":
            # email = DomoElementLocators.BuckGardnerCalls_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.BuckGardnerCalls_Username)
            # password = DomoElementLocators.BuckGardnerCalls_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.BuckGardnerCalls_Password)
        elif supplier == "Energizer":
            # email = DomoElementLocators.Energizer_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Energizer_Username)
            # password = DomoElementLocators.Energizer_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Energizer_Password)
        elif supplier == "IndustrialRevolution":
            # email = DomoElementLocators.IndustrialRevolution_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.IndustrialRevolution_Username)
            # password = DomoElementLocators.IndustrialRevolution_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.IndustrialRevolution_Password)
        elif supplier == "Camelback":
            # email = DomoElementLocators.Camelback_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Camelback_Username)
            # password = DomoElementLocators.Camelback_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Camelback_Password)
        elif supplier == "Carhartt":
            # email = DomoElementLocators.Carhartt_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.Carhartt_Username)
            # password = DomoElementLocators.Carhartt_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.Carhartt_Password)
        elif supplier == "AriatInternational":
            # email = DomoElementLocators.AriatInternational_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.AriatInternational_Username)
            # password = DomoElementLocators.AriatInternational_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.AriatInternational_Password)
        elif supplier == "HydroFlask":
            # email = DomoElementLocators.HydroFlask_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.HydroFlask_Username)
            # password = DomoElementLocators.HydroFlask_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.HydroFlask_Password)
        elif supplier == "LifeIsGood":
            # email = DomoElementLocators.LifeIsGood_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.LifeIsGood_Username)
            # password = DomoElementLocators.LifeIsGood_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.LifeIsGood_Password)
        elif supplier == "TenderCorp":
            # email = DomoElementLocators.TenderCorp_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.TenderCorp_Username)
            # password = DomoElementLocators.TenderCorp_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.TenderCorp_Password)
        elif supplier == "LipseysInc":
            # email = DomoElementLocators.LipseysInc_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.LipseysInc_Username)
            # password = DomoElementLocators.LipseysInc_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.LipseysInc_Password)
        elif supplier == "StrikeKingLures":
            # email = DomoElementLocators.StrikeKingLures_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.StrikeKingLures_Username)
            # password = DomoElementLocators.StrikeKingLures_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.StrikeKingLures_Password)
        elif supplier == "LewsFishingTackle":
            # email = DomoElementLocators.LewsFishingTackle_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.LewsFishingTackle_Username)
            # password = DomoElementLocators.LewsFishingTackle_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.LewsFishingTackle_Password)
        elif supplier == "AllianceSportsGroup":
            # email = DomoElementLocators.AllianceSportsGroup_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.AllianceSportsGroup_Username)
            # password = DomoElementLocators.AllianceSportsGroup_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.AllianceSportsGroup_Password)
        elif supplier == "SmithandWesson":
            # email = DomoElementLocators.SmithandWesson_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.SmithandWesson_Username)
            # password = DomoElementLocators.SmithandWesson_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.SmithandWesson_Password)
        elif supplier == "MarolinaOutdoorInc":
            # email = DomoElementLocators.MarolinaOutdoorInc_Username
            # v_email = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Email_Xpath)
            # v_email.send_keys(email)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Email_Xpath,DomoElementLocators.MarolinaOutdoorInc_Username)
            # password = DomoElementLocators.MarolinaOutdoorInc_Password
            # v_password = v_Browser.find_element_by_xpath(DomoElementLocators.Login_Password_Xpath)
            # v_password.send_keys(password)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Supplier_Login).click()
            # time.sleep(10)
            SeleniumOperation.send_text_by_xpath(DomoElementLocators.Login_Password_Xpath,DomoElementLocators.MarolinaOutdoorInc_Password)
        SeleniumOperation.click_element_by_xpath(DomoElementLocators.Supplier_Login)
    except Exception as e:
        LogFileUtility.log_to_file(self, "ERROR", "Exception:" + str(e))

def Download(self, report, v_Browser, retailer,lo):
        SeleniumOperation = SeleniumOperations(v_Browser,lo)
        if report == "SALES":
            v_Browser.get(DomoElementLocators.Ten_VND_Sales)
            v_Browser.get(DomoElementLocators.BC_SALES_DETAIL_SKU_STORE_DAY)
            time.sleep(15)#20
            # assert 'B/C SALES DETAIL SKU STORE DAY' in v_Browser.title
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.Previous_Week)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Previous_Week).click()
            time.sleep(3)#5
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.Previous_Week_Button)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Previous_Week_Button).click()
            # time.sleep(2)
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.Previous_Week_Between)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Previous_Week_Between).click()
            # put wait till full page not loaded after between click.
            # put date method here after each date click wait till page not loaded.
            getSunSatDate(v_Browser)
            # time.sleep(10)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Filter).click()
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.Add_Filter)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Add_Filter).click()
            # time.sleep(2)#3
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.Banner)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Banner).click()
            # Banner(v_Browser)
            if retailer == "BPS":
                # time.sleep(7)#10
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.BPS)
                # v_Browser.find_element_by_xpath(DomoElementLocators.BPS).click()
                # time.sleep(3)
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.Apply)
                # v_Browser.find_element_by_xpath(DomoElementLocators.Apply).click()
                time.sleep(15)
                # put wait till full page not loaded after Apply click.
            elif retailer == "CAB":
                # time.sleep(15)
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.CAB)
                # v_Browser.find_element_by_xpath(DomoElementLocators.CAB).click()
                # time.sleep(5)
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.Apply)
                # v_Browser.find_element_by_xpath(DomoElementLocators.Apply).click()
                # put wait till full page not loaded after Apply click.
                time.sleep(15)
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.share)
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.send_Export)
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.csv_Download)
            # v_Browser.find_element_by_xpath(DomoElementLocators.share).click()
            # v_Browser.find_element_by_xpath(DomoElementLocators.send_Export).click()
            # v_Browser.find_element_by_xpath(DomoElementLocators.csv_Download).click()
            # put the wait till sales file Downloded
            time.sleep(55)
        elif report == "INVENTORY":
            v_Browser.get(DomoElementLocators.Seven_Vnd_Inventory)
            # put wait
            v_Browser.get(DomoElementLocators.Bc_Total_Inventpry)
            # put wait
            time.sleep(20)#30
            if retailer == "BPS":
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.BPS_Retail)
                # v_Browser.find_element_by_xpath(DomoElementLocators.BPS_Retail).click()
                # time.sleep(5)#15
                # put wait page loaded
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.BPS_Whse)
                # v_Browser.find_element_by_xpath(DomoElementLocators.BPS_Whse).click()
                time.sleep(15)#15
                # put wait page loded.
            elif retailer == "CAB":
                # time.sleep(10)#10
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.CAB_US_Retail)
                # v_Browser.find_element_by_xpath(DomoElementLocators.CAB_US_Retail).click()
                # time.sleep(15)#15
                # put wait
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.CAB_US_Whse)
                # v_Browser.find_element_by_xpath(DomoElementLocators.CAB_US_Whse).click()
                time.sleep(15)#15

            v_Browser.find_element_by_xpath(DomoElementLocators.share).click()
            v_Browser.find_element_by_xpath(DomoElementLocators.send_Export).click()
            v_Browser.find_element_by_xpath(DomoElementLocators.csv_Download).click()
            time.sleep(90)#150
            # put the wait till sales file Downloded
            for file in [doc for doc in os.listdir("C:\\Users\\krishnabhashkar.jha\\Downloads") if doc.endswith(".crdownload")]:
                file_name = file
                file_name_with_extension = os.path.splitext(file_name)
                file_extension = file_name_with_extension[1]
            try:
                while (file_extension == '.crdownload'):
                    if file in [doc for doc in os.listdir("C:\\Users\\krishnabhashkar.jha\\Downloads") if doc.endswith(".crdownload")]:
                        file_name = file
                        file_name_with_extension = os.path.splitext(file_name)
                        file_extension = file_name_with_extension[1]
                        if (file_extension == '.crdownload'):
                            LogFileUtility.log_to_file(self, "INFO", "partial file download.")
                            if os.path.exists("C:\\Users\\krishnabhashkar.jha\\Downloads"):
                                shutil.rmtree("C:\\Users\\krishnabhashkar.jha\\Downloads")
                            else:
                                LogFileUtility.log_to_file(self, "ERROR", "The File Does not Exists.")
                            v_Browser.find_element_by_xpath(DomoElementLocators.share).click()
                            v_Browser.find_element_by_xpath(DomoElementLocators.send_Export).click()
                            v_Browser.find_element_by_xpath(DomoElementLocators.csv_Download).click()
                            time.sleep(145)  # 150
                        continue
                    else:
                        break
            except:
                pass

def getSunSatDate(v_Browser):
    today = datetime.date.today()
    datetime.date(2013,8,13)
    idx = (today.weekday() +1) %7  # MON = 0, SUN = 6 -> SUN = 0 .. SAT = 6
    sun = (today - datetime.timedelta(7 + idx))
    sat = (today - datetime.timedelta(7 + idx - 6))
    # return sun, sat
    v_sun = v_Browser.find_element_by_xpath(DomoElementLocators.StartDate)
    time.sleep(2)
    v_sun.clear()
    time.sleep(1)
    v_sun.send_keys(str(sun.strftime('%m/%d/%y')))
    v_sat = v_Browser.find_element_by_xpath(DomoElementLocators.EndDate)
    time.sleep(2)
    v_sat.clear()
    time.sleep(1)
    v_sat.send_keys(str(sat.strftime('%m/%d/%y')))
    v_Browser.find_element_by_xpath(DomoElementLocators.Filter).click()
    time.sleep(10)#10

def Rename_File(report, retailer, supplier):
    try:
        # global report_shortcut
        home = os.path.expanduser('~')  # print(home)  C:\Users\krishnabhashkar.jha
        location1 = os.path.join(home, "Downloads")  # print(location)  C:\Users\krishnabhashkar.jha\Downloads
        today = datetime.date.today()
        Days = datetime.datetime.now()
        offset = (today.weekday() - 5) % 7
        last_saturday = today - datetime.timedelta(days=offset)
        if report == "SALES":
            sales = os.path.join(location1, "B_C+" + report + "+" + "DETAIL+" + "SKU+" + "STORE+" + "DAY"+ ".csv")
            if retailer == "BASSPRO":
                basspro = os.path.join(location1, retailer + "_"+ supplier + "_" + report + "_" + str(last_saturday.strftime('%Y%m%d')) + ".csv")
                os.rename(sales, basspro)
            elif retailer =="BASSPRODOMO":
                basspro = os.path.join(location1, retailer + "_"+ supplier + "_" + report + "_" + str(last_saturday.strftime('%Y%m%d')) + ".csv")
                os.rename(sales, basspro)
            elif retailer == "CABELAS":
                cabelas = os.path.join(location1, retailer + "_"+ supplier + "_" + report + "_" + str(last_saturday.strftime('%Y%m%d')) + ".csv")
                os.rename(sales, cabelas)
            elif retailer == "CABELASDOMO":
                cabelas = os.path.join(location1, retailer + "_"+ supplier + "_" + report + "_" + str(last_saturday.strftime('%Y%m%d')) + ".csv")
                os.rename(sales, cabelas)
        elif report == "INVENTORY":
            inventory = os.path.join(location1, "B_C+" + "TOTAL" + "+" + report + "+" + "BY" + "+" + "STORE+" + "DETAIL" + ".csv")
            if retailer == "BASSPRO":
                basspro = os.path.join(location1, retailer + "_"+ supplier + "_" + report + "_" + str(last_saturday.strftime('%Y%m%d')) +".csv")
                os.rename(inventory, basspro)
            elif retailer == "BASSPRODOMO":
                basspro = os.path.join(location1, retailer + "_"+ supplier + "_" + report + "_" + str(last_saturday.strftime('%Y%m%d')) +".csv")
                os.rename(inventory, basspro)
            elif retailer == "CABELAS":
                cabelas = os.path.join(location1, retailer + "_"+ supplier + "_" + report + "_" + str(last_saturday.strftime('%Y%m%d')) +".csv")
                os.rename(inventory, cabelas)
            elif retailer == "CABELASDOMO":
                cabelas = os.path.join(location1, retailer + "_"+ supplier + "_" + report + "_" + str(last_saturday.strftime('%Y%m%d')) +".csv")
                os.rename(inventory, cabelas)
    except Exception as e:
        LogFileUtility.log_to_file(self, "ERROR", "Exception:" + str(e))

def Move_File(supplier,retailer):
    try:
        today = datetime.date.today()
        Days = datetime.datetime.now()
        var_foldername = Days.strftime("%d-%b-%Y")
        offset = (today.weekday() - 5) % 7
        list_of_files = glob.glob("C:\\Users\\" + getpass.getuser() + "\\Downloads\\*")
        latest_file_In_Download = max(list_of_files, key=os.path.getctime)
        print(latest_file_In_Download)
        move_location = 'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + supplier + "\\" + retailer
        time.sleep(3)
        shutil.move(latest_file_In_Download, move_location)
    except Exception as e:
        LogFileUtility.log_to_file(self, "ERROR", "Exception:" + str(e))

def copy_file():
    try:
        Days = datetime.datetime.now()
        var_foldername = Days.strftime("%d-%b-%Y")
        source = "C:\Automation\Templates\DomoPortalSuppliers.xlsx"
        Destination = 'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal'
        shutil.copy(source, Destination)
    except Exception as e:
        LogFileUtility.log_to_file(self, "ERROR", "Exception:" + str(e))

def set_value_to_cell(file_name, row_index, column_index, key):
    try:
        wb = openpyxl.load_workbook(file_name)
        sheet = wb.active
        sheet.cell(row_index, column_index, key)
        wb.save(filename=file_name)
    except Exception as e:
        LogFileUtility.log_to_file(self, "ERROR", "Exception:" + str(e))

def Excel_Update(self,row,col):
    try:
        Days = datetime.datetime.now()
        var_foldername = Days.strftime("%d-%b-%Y")
        v_filePath = 'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'DomoPortalSuppliers.xlsx'
        v_row = row
        v_col = col
        status = 'Successfull'
        set_value_to_cell(v_filePath, v_row, v_col, status)
    except Exception as e:
        LogFileUtility.log_to_file(self, "ERROR", "Exception:" + str(e))

def SignOut(v_Browser):
    try:
        v_Browser.find_element_by_xpath(DomoElementLocators.SignOutClick).click()
        v_Browser.find_element_by_xpath(DomoElementLocators.SignOut).click()
        LogFileUtility.log_to_file(self, "INFO", "Successfully Signout.")
    except Exception as e:
        LogFileUtility.log_to_file(self,"ERROR","Exception:"+str(e))

def DownloadForColumbia(self, report, v_Browser, retailer, lo):
        SeleniumOperation = SeleniumOperations(v_Browser, lo)
        if report == "SALES":
            v_Browser.get(DomoElementLocators.Ten_VND_Sales)
            v_Browser.get(DomoElementLocators.BC_SALES_DETAIL_SKU_STORE_DAY)
            time.sleep(15)  # 20
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.Previous_Week)
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.Previous_Week_Button)
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.Previous_Week_Between)
            getSunSatDate(v_Browser)
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.Add_Filter)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Add_Filter).click()
            # time.sleep(2)#3
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.Banner)
            # v_Browser.find_element_by_xpath(DomoElementLocators.Banner).click()
            # Banner(v_Browser)
            if retailer == "BPS":
                # time.sleep(7)#10
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.BPS)
                # v_Browser.find_element_by_xpath(DomoElementLocators.BPS).click()
                # time.sleep(3)
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.Apply)
                # v_Browser.find_element_by_xpath(DomoElementLocators.Apply).click()
                time.sleep(15)
                # put wait till full page not loaded after Apply click.
            elif retailer == "CAB":
                # time.sleep(15)
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.CAB)
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.Apply)
                time.sleep(15)
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.share)
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.send_Export)
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.csv_Download)
            time.sleep(40)
        elif report == "INVENTORY":
            v_Browser.get(DomoElementLocators.Seven_Vnd_Inventory)
            # put wait
            v_Browser.get(DomoElementLocators.Bc_Total_Inventpry)
            # put wait
            time.sleep(20)  # 30
            if retailer == "BPS":
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.BPS_Retail)
                # v_Browser.find_element_by_xpath(DomoElementLocators.BPS_Retail).click()
                # time.sleep(5)#15
                # put wait page loaded
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.BPS_Whse)
                # v_Browser.find_element_by_xpath(DomoElementLocators.BPS_Whse).click()
                time.sleep(15)  # 15
                # put wait page loded.
            elif retailer == "CAB":
                # time.sleep(10)#10
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.CAB_US_Retail)
                # v_Browser.find_element_by_xpath(DomoElementLocators.CAB_US_Retail).click()
                # time.sleep(15)#15
                # put wait
                SeleniumOperation.click_element_by_xpath(DomoElementLocators.CAB_US_Whse)
                # v_Browser.find_element_by_xpath(DomoElementLocators.CAB_US_Whse).click()
                time.sleep(15)  # 15
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.share)
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.send_Export)
            SeleniumOperation.click_element_by_xpath(DomoElementLocators.csv_Download)
            # v_Browser.find_element_by_xpath(DomoElementLocators.share).click()
            # v_Browser.find_element_by_xpath(DomoElementLocators.send_Export).click()
            # v_Browser.find_element_by_xpath(DomoElementLocators.csv_Download).click()
            time.sleep(160)  # 150
            # put the wait till sales file Downloded
            for file in [doc for doc in os.listdir("C:\\Users\\krishnabhashkar.jha\\Downloads") if
                         doc.endswith(".crdownload")]:
                file_name = file
                file_name_with_extension = os.path.splitext(file_name)
                file_extension = file_name_with_extension[1]
            try:
                while (file_extension == '.crdownload'):
                    if file in [doc for doc in os.listdir("C:\\Users\\krishnabhashkar.jha\\Downloads") if
                                doc.endswith(".crdownload")]:
                        file_name = file
                        file_name_with_extension = os.path.splitext(file_name)
                        file_extension = file_name_with_extension[1]
                        if (file_extension == '.crdownload'):
                            LogFileUtility.log_to_file(self, "INFO", "partial file download.")
                            if os.path.exists("C:\\Users\\krishnabhashkar.jha\\Downloads"):
                                shutil.rmtree("C:\\Users\\krishnabhashkar.jha\\Downloads")
                            else:
                                LogFileUtility.log_to_file(self, "ERROR", "The File Does not Exists.")
                            v_Browser.find_element_by_xpath(DomoElementLocators.share).click()
                            v_Browser.find_element_by_xpath(DomoElementLocators.send_Export).click()
                            v_Browser.find_element_by_xpath(DomoElementLocators.csv_Download).click()
                            time.sleep(155)  # 150
                        continue
                    else:
                        break
            except:
                pass