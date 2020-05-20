"""
@ Author - Krishnabhashkar jha
@ Creation date - 17/01/2020
@ Description - Declares all the Methods to be used at the Process Level.
"""
from Applications.Workflows.Analytics.RetailerPortalScraping.AmazonPortal.DownloadAmazonReports import DownloadAmazonReports

class AmazonSuppliers():

    def __init__(self,v_Browser,lo):
        self.v_Browser = v_Browser
        self.lo = lo

    def Execute_AmazonSuppliers(self):
        try:
            Suppliers = DownloadAmazonReports(self.v_Browser,self.lo)
            exception = Suppliers.Gildan()
            self.lo.log_to_file(self, "INFO", " Done With Gildan. "+str(exception))

        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception:" + str(e))
