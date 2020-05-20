"""
@ Author - Krishnabhashkar jha
@ Creation date - 7/12/2019
@ Description - Main Scripts of Analytics Automation.
"""
import datetime
import os
from selenium import webdriver
import shutil
from Applications.Workflows.Analytics.RetailerPortalScraping.DomoPortal.DomoSuppliers import Execute_DomoSuppliers
from Utilites.LogFileUtility import LogFileUtility as lo


class RetailerPortalScraping_Main():
    def __init__(self):
        self.v_Browser = webdriver.Chrome('C:/driver/chromedriver')
        self.v_Browser.maximize_window()
        self.lo = lo

    def execute_Main(self):
        var_pathName = r"C:\Automation\Reports"
        shutil.rmtree(var_pathName)
        os.makedirs("C:\Automation" + "\\" + 'Reports')
        Days = datetime.datetime.now()
        var_foldername = Days.strftime("%d-%b-%Y")
        var_pathName = r"C:\Automation\Reports" + "\\" + var_foldername
        if os.path.exists(var_pathName):
            shutil.rmtree(var_pathName)
        if not os.path.exists(var_pathName):
            try:
                os.makedirs(r"C:\Automation\Reports" + "\\" + var_foldername)
                os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal')
                lo.log_to_file(self, "INFO", "Folder created For DomoPortal.")

            finally:
                Execute_DomoSuppliers(self, self.v_Browser,self.lo)
                lo.log_to_file(self, "INFO", "Download Complete for Domo Portal")
                shutil.make_archive(r'C:\Automation\BackUp\Reports' + var_foldername, 'zip', 'C:/Automation/Reports')
                # self.v_Browser.quit()
