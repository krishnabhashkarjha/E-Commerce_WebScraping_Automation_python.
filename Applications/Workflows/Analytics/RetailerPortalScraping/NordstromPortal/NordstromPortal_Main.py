"""
@ Author - Krishnabhashkar jha
@ Creation date - 29/01/2020
@ Description - Declares all the Methods to be used at the Process Level.
"""
import os
import datetime
import shutil
from selenium import webdriver
from Applications.Workflows.Analytics.RetailerPortalScraping.Utilites.LogFileUtility import LogFileUtility as lo
from Applications.Workflows.Analytics.RetailerPortalScraping.NordstromPortal.NordstromSuppliers import NordstromSuppliers

class NordstromPortal_Main():

    def __init__(self):
        self.currentDate = datetime.datetime.today().strftime("%d-%m-%Y")
        self.v_Browser = webdriver.Chrome('C:/driver/chromedriver')
        self.v_Browser.maximize_window()
        self.lo = lo

    def Execute_Main(self):
        try:
            try:
                var_pathName = r"C:\Automation\Nordstrom"
                shutil.rmtree(var_pathName)
            finally:
                os.makedirs(r"C:\Automation" + "\\" + 'Nordstrom')
                var_pathName = r"C:\Automation\Nordstrom" + "\\" + self.currentDate
            if os.path.exists(var_pathName):
                shutil.rmtree(var_pathName)
            if not os.path.exists(var_pathName):
                try:
                    os.makedirs(r"C:\Automation\Nordstrom" + "\\" + self.currentDate)
                    self.lo.log_to_file(self, "INFO", "Folder created For NordstromPortal.")
                finally:
                    Main_Methods = NordstromSuppliers(self.v_Browser, self.lo, self.currentDate)
                    Main_Methods.Execute_NordstromSuppliers()
                    self.lo.log_to_file(self, "INFO", "Download Complete for NordstromPortal")
                    shutil.make_archive(r'C:\Automation\BackUp\Reports' + self.currentDate, 'zip', 'C:/Automation/Nordstrom')
        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception:" + str(e))