"""
@ Author - Krishnabhashkar jha
@ Creation date - 03/02/2020
@ Description - Declares all the Methods to be used at the Process Level.
"""
from Applications.Workflows.Analytics.RetailerPortalScraping.NordstromPortal.DownloadNordstromReport import DownloadNordstromReports

class NordstromSuppliers():

    def __init__(self,v_Browser,lo,currentDate):
        self.currentDate = currentDate
        self.v_Browser = v_Browser
        self.lo = lo

    def Execute_NordstromSuppliers(self):
        Suppliers = DownloadNordstromReports(self.v_Browser, self.lo, self.currentDate)
        try:
            # exception = Suppliers.NorthFace("NorthFace")
            # self.lo.log_to_file(self, "INFO", " Done With NorthFace. " + str(exception))
            # exception = Suppliers.NuFace("NuFace")
            # self.lo.log_to_file(self, "INFO", " Done With NuFace. " + str(exception))
            # exception = Suppliers.NewBalance("NewBalanceAthleticShoe")
            # self.lo.log_to_file(self, "INFO", " Done With NewBalance. " + str(exception))
            # exception = Suppliers.Vans("Vans")
            # self.lo.log_to_file(self, "INFO", " Done With Vans. " + str(exception))
            # exception = Suppliers.Deckers("DECKERS")
            # self.lo.log_to_file(self, "INFO", " Done With Deckers. " + str(exception))
            # exception = Suppliers.ColeHaan("COLEHAAN")
            # self.lo.log_to_file(self, "INFO", " Done With ColeHaan. " + str(exception))
            # exception = Suppliers.LanaUnlimited("LANAUNLIMITED")
            # self.lo.log_to_file(self, "INFO", " Done With LanaUnlimited. " + str(exception))
            exception = Suppliers.Wolverine("WOLVERINE")
            self.lo.log_to_file(self, "INFO", " Done With Wolverine. " + str(exception))
            exception = Suppliers.BabyBiling("BabyBiling")
            self.lo.log_to_file(self, "INFO", " Done With BabyBiling. " + str(exception))
            exception = Suppliers.Reef("Reef")
            self.lo.log_to_file(self, "INFO", " Done With Reef. " + str(exception))
            exception = Suppliers.SmartWool("SmartWool")
            self.lo.log_to_file(self, "INFO", " Done With SmartWool. " + str(exception))
            exception = Suppliers.PopSockets("POPSOCKETS")
            self.lo.log_to_file(self, "INFO", " Done With PopSockets. " + str(exception))
            exception = Suppliers.SaxxUnderWear("SAXXUNDERWAER")
            self.lo.log_to_file(self, "INFO", " Done With PopSockets. " + str(exception))

        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception:" + str(e))
