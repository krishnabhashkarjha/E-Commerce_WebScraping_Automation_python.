"""
@ Author - Krishnabhashkar jha
@ Creation date - 17/01/2020
@ Description - Declares all the Suppliers to be used at the Process Level.
"""
from Applications.Workflows.Analytics.RetailerPortalScraping.AmazonPortal.AmazonPortalMethods import AmazonPortalMethods

class DownloadAmazonReports():

    def __init__(self,v_Browser,lo):
        self.v_Browser = v_Browser
        self.lo = lo

    def Gildan(self):
        Gildan = AmazonPortalMethods(self.v_Browser, self.lo)
        try:
            Gildan.Login("GILDAN")
            Gildan.Download("SALES", "GILDAN")
            Gildan.Rename_File("SALES","GILDAN","US")
            Gildan.Move_File()
            Gildan.Download("INVENTORY", "GILDAN")
            Gildan.Rename_File("INVENTORY", "GILDAN", "US")
            Gildan.Move_File()

        except Exception as e:
            self.lo.log_to_file(self, "INFO", "" + str(e))
            if str(e) != " ":
                return str(e)
            else:
                return "No Exception"
        finally:
            Gildan.SignOut("GILDAN")

