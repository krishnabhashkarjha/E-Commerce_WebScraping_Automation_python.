"""
@ Author - Krishnabhashkar jha
@ Creation date - 17/01/2020
@ Description - Declares all the Methods to be used at the Process Level.
"""

import time
import shutil
import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Applications.Workflows.Analytics.RetailerPortalScraping.AmazonPortal.AmazonSuppliers import AmazonSuppliers
from Applications.Workflows.Analytics.RetailerPortalScraping.Utilites.LogFileUtility import LogFileUtility as lo

class AmazonPortalMain():

    def __init__(self):
        chrome_option = Options()
        chrome_option.add_argument("--user-data-dir=C:/Users/Krishnabhashkar.Jha/AppData/Local/Google/Chrome/User Data")
        self.v_Browser = webdriver.Chrome(executable_path='C:/driver/chromedriver', chrome_options=chrome_option)
        self.v_Browser.maximize_window()
        self.lo = lo

    def Execute_Main(self):
        try:
            var_pathName = "C:\Automation\Amazon"
            shutil.rmtree(var_pathName)
            os.makedirs("C:\Automation" + "\\" + 'Amazon')
            Days = datetime.datetime.now()
            var_foldername = Days.strftime("%d-%b-%Y")
            var_pathName = "C:\Automation\Amazon" + "\\" + var_foldername
            if os.path.exists(var_pathName):
                shutil.rmtree(var_pathName)
            if not os.path.exists(var_pathName):
                try:
                    os.makedirs("C:\Automation\Amazon" + "\\" + var_foldername)
                    os.makedirs(r'C:\\Automation\Amazon' + "\\" + var_foldername + "\\" + 'AmazonPortal')
                    self.lo.log_to_file(self, "INFO", "Folder created For AmazonPortal.")
                finally:
                    Main_Methods = AmazonSuppliers(self.v_Browser, self.lo)
                    Main_Methods.Execute_AmazonSuppliers()
                    self.lo.log_to_file(self, "INFO", "Download Complete for AmazonPortal")
                    shutil.make_archive(r'C:\Automation\BackUp\Reports' + var_foldername, 'zip', 'C:/Automation/Amazon')

        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception:" + str(e))








