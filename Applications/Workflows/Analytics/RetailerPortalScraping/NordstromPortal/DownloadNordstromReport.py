"""
@ Author - Krishnabhashkar jha
@ Creation date - 03/02/2020
@ Description - Declares all the Suppliers to be used at the Process Level.
"""
import time
from Applications.Workflows.Analytics.RetailerPortalScraping.NordstromPortal.NordstromPortalMethods import NordstromPortalMethods

class DownloadNordstromReports():

    def __init__(self,v_Browser,lo,currentDate):
        self.v_Browser = v_Browser
        self.lo = lo
        self.currentDate = currentDate

    def NorthFace(self,supplier):
        NorthFace = NordstromPortalMethods(self.v_Browser,self.lo,self.currentDate)
        try:
            NorthFace.GetDate(supplier)
            NorthFace.Login(supplier)
            try:
                NorthFace.DownloadReport("938220761", "16")
                NorthFace.RenameReport("16")
                NorthFace.Move_File(supplier,"16")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 16 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "2")
                NorthFace.RenameReport("2")
                NorthFace.Move_File(supplier, "2")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 2 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "631")
                NorthFace.RenameReport("631")
                NorthFace.Move_File(supplier, "631")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 631 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "588")
                NorthFace.RenameReport("588")
                NorthFace.Move_File(supplier, "588")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 588 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "537")
                NorthFace.RenameReport("537")
                NorthFace.Move_File(supplier, "537")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 537 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "62")
                NorthFace.RenameReport("62")
                NorthFace.Move_File(supplier, "62")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 62 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "61")
                NorthFace.RenameReport("61")
                NorthFace.Move_File(supplier, "61")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 61 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "60")
                NorthFace.RenameReport("60")
                NorthFace.Move_File(supplier, "60")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 60 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "30")
                NorthFace.RenameReport("30")
                NorthFace.Move_File(supplier, "30")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 30 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "59")
                NorthFace.RenameReport("59")
                NorthFace.Move_File(supplier, "59")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 59 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "58")
                NorthFace.RenameReport("58")
                NorthFace.Move_File(supplier, "58")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 58 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "341")
                NorthFace.RenameReport("341")
                NorthFace.Move_File(supplier, "341")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 341 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "98")
                NorthFace.RenameReport("98")
                NorthFace.Move_File(supplier, "98")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 98 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "64")
                NorthFace.RenameReport("64")
                NorthFace.Move_File(supplier, "64")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 64 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "37")
                NorthFace.RenameReport("37")
                NorthFace.Move_File(supplier, "37")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 37 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "123")
                NorthFace.RenameReport("123")
                NorthFace.Move_File(supplier, "123")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 123 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "122")
                NorthFace.RenameReport("122")
                NorthFace.Move_File(supplier, "122")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 122 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "525")
                NorthFace.RenameReport("525")
                NorthFace.Move_File(supplier, "525")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 525 Exception: " + str(e))
                pass
            try:
                NorthFace.DownloadReport("938220761", "723 - MENS OUTERWEAR-NorthFace")
                NorthFace.RenameReport("723")
                NorthFace.Move_File(supplier, "723")
                time.sleep(3)
                NorthFace.Logout(supplier)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 723 Exception: " + str(e))
                pass
            try:
                time.sleep(8)
                NorthFace.Login(supplier)
                NorthFace.DownloadReport("5102324", "587")
                NorthFace.RenameReport("587")
                NorthFace.Move_File(supplier, "587")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Northface dept 587 Exception: " + str(e))
        except Exception as e:
            self.lo.log_to_file(self, "INFO", "" + str(e))
            if str(e) != " ":
                return str(e)
            else:
                return "No Exception"
        finally:
            NorthFace.Logout(supplier)

    def NuFace(self,supplier):
        NuFace = NordstromPortalMethods(self.v_Browser, self.lo, self.currentDate)
        try:
            NuFace.GetDate(supplier)
            NuFace.Login(supplier)
            try:
                NuFace.DownloadReport("5076122", "276")
                NuFace.RenameReport("276")
                NuFace.Move_File(supplier,"276")
                time.sleep(3)
                NuFace.Logout(supplier)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with NuFace dept 276 Exception: " + str(e))
                pass
            try:
                time.sleep(8)
                NuFace.Login(supplier)
                NuFace.DownloadReport("5070871", "32")
                NuFace.RenameReport("32")
                NuFace.Move_File(supplier, "32")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with NuFace dept 32 Exception: " + str(e))
        except Exception as e:
            self.lo.log_to_file(self, "INFO", "" + str(e))
            if str(e) != " ":
                return str(e)
            else:
                return "No Exception"
        finally:
            NuFace.Logout(supplier)

    def NewBalance(self,supplier):
        NewBalance = NordstromPortalMethods(self.v_Browser, self.lo, self.currentDate)
        try:
            NewBalance.GetDate(supplier)
            NewBalance.Login(supplier)
            try:
                NewBalance.DownloadReport("136864699", "37 - WOMENS ACTIVE SHOES-NewBalance")
                NewBalance.RenameReport("37")
                NewBalance.Move_File(supplier,"37")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with NewBalance dept 37 Exception: " + str(e))
                pass
            try:
                NewBalance.DownloadReport("136864699", "123 - MENS ACTIVE SHOES-NewBalance")
                NewBalance.RenameReport("123")
                NewBalance.Move_File(supplier,"123")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with NewBalance dept 123 Exception: " + str(e))
                pass
            try:
                NewBalance.DownloadReport("136864699", "54 - KIDS SHOES-NewBalance")
                NewBalance.RenameReport("54")
                NewBalance.Move_File(supplier,"54")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with NewBalance dept 54 Exception: " + str(e))
                pass
            try:
                NewBalance.DownloadReport("136864699", "16 - ACTIVEWEAR-NewBalance")
                NewBalance.RenameReport("16")
                NewBalance.Move_File(supplier,"16")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with NewBalance dept 16 Exception: " + str(e))
                pass
            try:
                NewBalance.DownloadReport("136864699", "588 - M ACTIVE/OUTERWER-NewBalance")
                NewBalance.RenameReport("588")
                NewBalance.Move_File(supplier,"588")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with NewBalance dept 588 Exception: " + str(e))
                pass
        except Exception as e:
            self.lo.log_to_file(self, "INFO", "" + str(e))
            if str(e) != " ":
                return str(e)
            else:
                return "No Exception"
        finally:
            NewBalance.Logout(supplier)

    def Vans(self,supplier):
        Vans = NordstromPortalMethods(self.v_Browser, self.lo, self.currentDate)
        try:
            Vans.GetDate(supplier)
            Vans.Login(supplier)
            try:
                Vans.DownloadReport("285090864", "37 - WOMENS ACTIVE SHOES")
                Vans.RenameReport("37")
                Vans.Move_File(supplier,"37")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Vans dept 37 Exception: " + str(e))
                pass
            try:
                Vans.DownloadReport("285090864", "127 - MENS TREND SHOES")
                Vans.RenameReport("127")
                Vans.Move_File(supplier,"127")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Vans dept 127 Exception: " + str(e))
                pass
            try:
                Vans.DownloadReport("285090864", "54 - KIDS SHOES")
                Vans.RenameReport("54")
                Vans.Move_File(supplier,"54")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Vans dept 54 Exception: " + str(e))
                pass
            try:
                Vans.DownloadReport("285090864", "75 - YOUNG MENS CONTEMPORARY")
                Vans.RenameReport("75")
                Vans.Move_File(supplier,"75")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Vans dept 75 Exception: " + str(e))
                pass
            try:
                Vans.DownloadReport("285090864", "59 - BOYS 8-20")
                Vans.RenameReport("59")
                Vans.Move_File(supplier,"59")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Vans dept 59 Exception: " + str(e))
                pass
            try:
                Vans.DownloadReport("285090864", "627 - YC DENIM & EMERGING BRANDS")
                Vans.RenameReport("627")
                Vans.Move_File(supplier,"627")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Vans dept 627 Exception: " + str(e))
                pass
            try:
                Vans.DownloadReport("285090864", "58 - LITTLE BOYS")
                Vans.RenameReport("58")
                Vans.Move_File(supplier, "58")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Vans dept 58 Exception: " + str(e))
                pass
            try:
                Vans.DownloadReport("285090864", "98 - BOYS ACC/SLP")
                Vans.RenameReport("98")
                Vans.Move_File(supplier, "98")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Vans dept 98 Exception: " + str(e))
                pass
            try:
                Vans.DownloadReport("285090864", "97 - BP ACCESSORIES")
                Vans.RenameReport("97")
                Vans.Move_File(supplier, "97")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Vans dept 97 Exception: " + str(e))
                pass
            try:
                Vans.DownloadReport("285090864", "537 - M ACCESSORIES")
                Vans.RenameReport("537")
                Vans.Move_File(supplier, "537")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Vans dept 537 Exception: " + str(e))
                pass
            try:
                Vans.DownloadReport("285090864", "122 - KIDS SHOES ACCESSORIES1")
                Vans.RenameReport("122")
                Vans.Move_File(supplier, "122")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Vans dept 122 Exception: " + str(e))
                pass
            try:
                Vans.DownloadReport("285090864", "608 - EMERGING DESIGNERS")
                Vans.RenameReport("608")
                Vans.Move_File(supplier, "608")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Vans dept 608 Exception: " + str(e))
        except Exception as e:
            self.lo.log_to_file(self, "INFO", "" + str(e))
            if str(e) != " ":
                return str(e)
            else:
                return "No Exception"
        finally:
            Vans.Logout(supplier)

    def Deckers(self,supplier):
        Deckers = NordstromPortalMethods(self.v_Browser, self.lo, self.currentDate)
        try:
            Deckers.GetDate(supplier)
            Deckers.Login(supplier)
            try:
                Deckers.DownloadReport("5088781", "3 - HOSIERY")
                Deckers.RenameReport("3")
                Deckers.Move_File(supplier,"3")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Deckers dept 3 Exception: " + str(e))
                pass
            try:
                Deckers.DownloadReport("5088781", "53 - SLEEPWEAR")
                Deckers.RenameReport("53")
                Deckers.Move_File(supplier,"53")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Deckers dept 53 Exception: " + str(e))
                pass
            try:
                Deckers.DownloadReport("5088781", "536 - M SPECIALIZED")
                Deckers.RenameReport("536")
                Deckers.Move_File(supplier,"536")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Deckers dept 536 Exception: " + str(e))
                pass
            try:
                Deckers.DownloadReport("5088781", "40 - SOFT GOODS/HOLIDAY")
                Deckers.RenameReport("40")
                Deckers.Move_File(supplier,"40")
                time.sleep(3)
                Deckers.Logout(supplier)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Deckers dept 40 Exception: " + str(e))
                pass
            try:
                time.sleep(8)
                Deckers.Login(supplier)
                Deckers.DownloadReport("114374778", "631 - PERFORMANCE OUTERWEAR")
                Deckers.RenameReport("631")
                Deckers.Move_File(supplier, "631")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with NuFace dept 631 Exception: " + str(e))
                pass
            try:
                Deckers.DownloadReport("114374778", "588 - M ACTIVE/OUTERWER")
                Deckers.RenameReport("588")
                Deckers.Move_File(supplier,"588")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Deckers dept 588 Exception: " + str(e))
                pass
            try:
                Deckers.DownloadReport("114374778", "24 - MENS UT/MODERN SHOES")
                Deckers.RenameReport("24")
                Deckers.Move_File(supplier,"24")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Deckers dept 24 Exception: " + str(e))
                pass
            try:
                Deckers.DownloadReport("114374778", "122 - KIDS SHOES ACCESSORIES2")
                Deckers.RenameReport("122")
                Deckers.Move_File(supplier,"122")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Deckers dept 122 Exception: " + str(e))
                pass
            try:
                Deckers.DownloadReport("114374778", "526 - WOMENS UGG SHOES")
                Deckers.RenameReport("526")
                Deckers.Move_File(supplier,"526")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Deckers dept 526 Exception: " + str(e))
        except Exception as e:
            self.lo.log_to_file(self, "INFO", "" + str(e))
            if str(e) != " ":
                return str(e)
            else:
                return "No Exception"
        finally:
            Deckers.Logout(supplier)

    def ColeHaan(self,supplier):
        ColeHaan = NordstromPortalMethods(self.v_Browser, self.lo, self.currentDate)
        try:
            ColeHaan.GetDate(supplier)
            ColeHaan.Login(supplier)
            try:
                ColeHaan.DownloadReport("136541105", "24 - MENS UT/MODERN SHOES2")
                ColeHaan.RenameReport("24")
                ColeHaan.Move_File(supplier,"24")
                time.sleep(6)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with ColeHaan dept 24 Exception: " + str(e))
                pass
            try:
                ColeHaan.DownloadReport("136541105", "109 - WOMENS CORE SHOES")
                ColeHaan.RenameReport("109")
                ColeHaan.Move_File(supplier,"109")
                time.sleep(10)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with ColeHaan dept 109 Exception: " + str(e))
                pass
            try:
                ColeHaan.DownloadReport("136541105", "191 - SP MENS UT/LUXURY SHOES")
                ColeHaan.RenameReport("191")
                ColeHaan.Move_File(supplier,"191")
                time.sleep(10)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with ColeHaan dept 191 Exception: " + str(e))
                pass
            try:
                ColeHaan.DownloadReport("136541105", "229 - SP SALON/PROGRESSV/BRIDGE SHOE")
                ColeHaan.RenameReport("229")
                ColeHaan.Move_File(supplier,"229")
                time.sleep(8)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with ColeHaan dept 229 Exception: " + str(e))
        except Exception as e:
            self.lo.log_to_file(self, "INFO", "" + str(e))
            if str(e) != " ":
                return str(e)
            else:
                return "No Exception"
        finally:
            ColeHaan.Logout(supplier)

    def LanaUnlimited(self,supplier):
        LanaUnlimited = NordstromPortalMethods(self.v_Browser, self.lo, self.currentDate)
        try:
            LanaUnlimited.GetDate(supplier)
            LanaUnlimited.Login(supplier)
            try:
                LanaUnlimited.DownloadReport("5085028", "574 - SP JEWELRY")
                LanaUnlimited.RenameReport("574")
                LanaUnlimited.Move_File(supplier,"574")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with LanaUnlimited dept 574 Exception: " + str(e))
                pass
            try:
                LanaUnlimited.DownloadReport("5085028", "696 - MODERN FINE JEWELRY")
                LanaUnlimited.RenameReport("696")
                LanaUnlimited.Move_File(supplier,"696")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with LanaUnlimited dept 696 Exception: " + str(e))
        except Exception as e:
            self.lo.log_to_file(self, "INFO", "" + str(e))
            if str(e) != " ":
                return str(e)
            else:
                return "No Exception"
        finally:
            LanaUnlimited.Logout(supplier)

    def Wolverine(self,supplier):
        Wolverine = NordstromPortalMethods(self.v_Browser, self.lo, self.currentDate)
        try:
            Wolverine.GetDate(supplier)
            Wolverine.Login(supplier)
            try:
                Wolverine.DownloadReport("163500919", "127 - MENS TREND SHOES-Wolverine")
                Wolverine.RenameReportForWolverine("Sperry Top-Sider Footwear","127")
                Wolverine.Move_File(supplier, "127")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 127 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("163500919", "191 - SP MENS UT/LUXURY SHOES2-Wolverine")
                Wolverine.RenameReportForWolverine("Sperry Top-Sider Footwear","191")
                Wolverine.Move_File(supplier, "191")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 191 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("163500919", "192 - SP WOMENS UT SHOES-Wolverine")
                Wolverine.RenameReportForWolverine("Sperry Top-Sider Footwear","192")
                Wolverine.Move_File(supplier, "192")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 192 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("163500919", "525 - COMFORT SHOES-Wolverine")
                Wolverine.RenameReportForWolverine("Sperry Top-Sider Footwear","525")
                Wolverine.Move_File(supplier, "525")
                time.sleep(3)
                Wolverine.Logout(supplier)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 525 Exception: " + str(e))
                pass
            try:
                time.sleep(8)
                Wolverine.Login(supplier)
                Wolverine.DownloadReport("116133218", "103 - SP WOMENS ACTIVE SHOES-Wolverine")
                Wolverine.RenameReportForWolverine("Merrell","103")
                Wolverine.Move_File(supplier, "103")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 103 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("116133218", "123 - MENS ACTIVE SHOES-Wolverine")
                Wolverine.RenameReportForWolverine("Merrell","123")
                Wolverine.Move_File(supplier, "123")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 123 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("116133218", "179 - SP MEN1-Wolverine")
                Wolverine.RenameReportForWolverine("Merrell","179")
                Wolverine.Move_File(supplier, "179")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 179 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("116133218", "525 - COMFORT SHOES2-Wolverine")
                Wolverine.RenameReportForWolverine("Merrell","525")
                Wolverine.Move_File(supplier, "525")
                time.sleep(3)
                Wolverine.Logout(supplier)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 525 Exception: " + str(e))
                pass
            try:
                time.sleep(8)
                Wolverine.Login(supplier)
                Wolverine.DownloadReport("422866488", "103 - SP WOMENS ACTIVE SHOES2-Wolverine")
                Wolverine.RenameReportForWolverine("Chaco","103")
                Wolverine.Move_File(supplier, "103")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 103 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("422866488", "123 - MENS ACTIVE SHOES2-Wolverine")
                Wolverine.RenameReportForWolverine("Chaco","123")
                Wolverine.Move_File(supplier, "123")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 123 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("422866488", "179 - SP MEN2-Wolverine")
                Wolverine.RenameReportForWolverine("Chaco","179")
                Wolverine.Move_File(supplier, "179")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 179 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("422866488", "525 - COMFORT SHOES3-Wolverine")
                Wolverine.RenameReportForWolverine("Chaco","525")
                Wolverine.Move_File(supplier, "525")
                time.sleep(3)
                Wolverine.Logout(supplier)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 525 Exception: " + str(e))
                pass
            try:
                time.sleep(8)
                Wolverine.Login(supplier)
                Wolverine.DownloadReport("5069454", "54 - KIDS SHOES-Wolverine")
                Wolverine.RenameReportForWolverine("Keds Kids","54")
                Wolverine.Move_File(supplier, "54")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 54 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("5069454", "178 - SP GIRLS SHOES-Wolverine")
                Wolverine.RenameReportForWolverine("Keds Kids","178")
                Wolverine.Move_File(supplier, "178")
                time.sleep(3)
                Wolverine.Logout(supplier)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 178 Exception: " + str(e))
                pass
            try:
                time.sleep(8)
                Wolverine.Login(supplier)
                Wolverine.DownloadReport("115437843", "54 - KIDS SHOES2-Wolverine")
                Wolverine.RenameReportForWolverine("Sperry Kids","54")
                Wolverine.Move_File(supplier, "54")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 54 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("115437843", "178 - SP GIRLS SHOES2-Wolverine")
                Wolverine.RenameReportForWolverine("Sperry Kids","178")
                Wolverine.Move_File(supplier, "178")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 178 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("115437843", "607 - SP BOYS SHOES-Wolverine")
                Wolverine.RenameReportForWolverine("Sperry Kids","607")
                Wolverine.Move_File(supplier, "607")
                time.sleep(3)
                Wolverine.Logout(supplier)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 607 Exception: " + str(e))
                pass
            try:
                time.sleep(8)
                Wolverine.Login(supplier)
                Wolverine.DownloadReport("706306622", "54 - KIDS SHOES3-Wolverine")
                Wolverine.RenameReportForWolverine("Saucony Childrens Footwear","54")
                Wolverine.Move_File(supplier, "54")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 54 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("706306622", "493 - SP BOYS ATHLETIC SHOES-Wolverine")
                Wolverine.RenameReportForWolverine("Saucony Childrens Footwear","493")
                Wolverine.Move_File(supplier, "493")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 493 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("706306622", "638 - SP GIRLS ATHLETIC SHOES-Wolverine")
                Wolverine.RenameReportForWolverine("Saucony Childrens Footwear","638")
                Wolverine.Move_File(supplier, "638")
                time.sleep(3)
                Wolverine.Logout(supplier)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 638 Exception: " + str(e))
                pass
            try:
                time.sleep(8)
                Wolverine.Login(supplier)
                Wolverine.DownloadReport("5117957", "122 - KIDS SHOES ACCESSORIES3-Wolverine")
                Wolverine.RenameReportForWolverine("Merrell Kids Footwear","122")
                Wolverine.Move_File(supplier, "122")
                time.sleep(3)
                Wolverine.Logout(supplier)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 122 Exception: " + str(e))
                pass
            try:
                time.sleep(8)
                Wolverine.Login(supplier)
                Wolverine.DownloadReport("153104053", "37 - WOMENS ACTIVE SHOES2-Wolverine")
                Wolverine.RenameReportForWolverine("Keds Womens-Mens","37")
                Wolverine.Move_File(supplier, "37")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 37 Exception: " + str(e))
                pass
            try:
                Wolverine.DownloadReport("153104053", "193 - SP JUNIOR/CONTEMPORARY SHOES-Wolverine")
                Wolverine.RenameReportForWolverine("Keds Womens-Mens","193")
                Wolverine.Move_File(supplier, "193")
                time.sleep(3)
                Wolverine.Logout(supplier)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 193 Exception: " + str(e))
                pass
            try:
                time.sleep(8)
                Wolverine.Login(supplier)
                Wolverine.DownloadReport("5097801", "37 - WOMENS ACTIVE SHOES3-Wolverine")
                Wolverine.RenameReportForWolverine("Keds for Kate Spade New York","37")
                Wolverine.Move_File(supplier, "37")
                time.sleep(3)
                Wolverine.Logout(supplier)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Wolverine dept 37 Exception: " + str(e))
        except Exception as e:
            self.lo.log_to_file(self, "INFO", "" + str(e))
            if str(e) != " ":
                return str(e)
            else:
                return "No Exception"
        finally:
            Wolverine.Logout(supplier)

    def BabyBiling(self,supplier):
        BabyBiling = NordstromPortalMethods(self.v_Browser, self.lo, self.currentDate)
        try:
            BabyBiling.GetDate(supplier)
            BabyBiling.Login(supplier)
            try:
                BabyBiling.DownloadReport("5073558", "64 - INFANT ACCESSORIES-BabyBiling")
                BabyBiling.RenameReport("64")
                BabyBiling.Move_File(supplier, "64")
                time.sleep(3)
                BabyBiling.Logout(supplier)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with BabyBiling dept 64 Exception: " + str(e))
        except Exception as e:
            self.lo.log_to_file(self, "INFO", "" + str(e))
            if str(e) != " ":
                return str(e)
            else:
                return "No Exception"
        finally:
            BabyBiling.Logout(supplier)

    def Reef(self,supplier):
        Reef = NordstromPortalMethods(self.v_Browser, self.lo, self.currentDate)
        try:
            Reef.GetDate(supplier)
            Reef.Login(supplier)
            try:
                Reef.DownloadReport("777311493", "37 - WOMENS ACTIVE SHOES-Reef")
                Reef.RenameReport("37")
                Reef.Move_File(supplier,"37")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Reef dept 37 Exception: " + str(e))
                pass
            try:
                Reef.DownloadReport("777311493", "122 - KIDS SHOES ACCESSORIES-Reef")
                Reef.RenameReport("122")
                Reef.Move_File(supplier,"122")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Reef dept 122 Exception: " + str(e))
                pass
            try:
                Reef.DownloadReport("777311493", "127 - MENS TREND SHOES-Reef")
                Reef.RenameReport("127")
                Reef.Move_File(supplier,"127")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Reef dept 127 Exception: " + str(e))
                pass
            try:
                Reef.DownloadReport("777311493", "178 - SP GIRLS SHOES-Reef")
                Reef.RenameReport("178")
                Reef.Move_File(supplier,"178")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Reef dept 178 Exception: " + str(e))
                pass
            try:
                Reef.DownloadReport("777311493", "193 - SP JUNIOR/CONTEMPORARY SHOES-Reef")
                Reef.RenameReport("193")
                Reef.Move_File(supplier,"193")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Reef dept 193 Exception: " + str(e))
                pass
            try:
                Reef.DownloadReport("777311493", "240 - SP MENS TREND SHOES-Reef")
                Reef.RenameReport("240")
                Reef.Move_File(supplier,"240")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Reef dept 240 Exception: " + str(e))
                pass
            try:
                Reef.DownloadReport("777311493", "607 - SP BOYS SHOES-Reef")
                Reef.RenameReport("607")
                Reef.Move_File(supplier,"607")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with Reef dept 607 Exception: " + str(e))
        except Exception as e:
            self.lo.log_to_file(self, "INFO", "" + str(e))
            if str(e) != " ":
                return str(e)
            else:
                return "No Exception"
        finally:
            Reef.Logout(supplier)

    def SmartWool(self,supplier):
        SmartWool = NordstromPortalMethods(self.v_Browser, self.lo, self.currentDate)
        try:
            SmartWool.GetDate(supplier)
            SmartWool.Login(supplier)
            try:
                SmartWool.DownloadReport("159643183", "3 - HOSIERY-SmartWool")
                SmartWool.RenameReport("3")
                SmartWool.Move_File(supplier, "3")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with SmartWool dept 3 Exception: " + str(e))
                pass
            try:
                SmartWool.DownloadReport("159643183", "536 - M SPECIALIZED-SmartWool")
                SmartWool.RenameReport("536")
                SmartWool.Move_File(supplier, "536")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with SmartWool dept 536 Exception: " + str(e))
                pass
            try:
                SmartWool.DownloadReport("159643183", "588 - M ACTIVE/OUTERWER-SmartWool")
                SmartWool.RenameReport("588")
                SmartWool.Move_File(supplier, "588")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with SmartWool dept 588 Exception: " + str(e))
                pass
            try:
                SmartWool.DownloadReport("159643183", "631 - PERFORMANCE OUTERWEAR-SmartWool")
                SmartWool.RenameReport("631")
                SmartWool.Move_File(supplier, "631")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with SmartWool dept 631 Exception: " + str(e))
                pass
            try:
                SmartWool.DownloadReport("159643183", "267 - SP MEN-SmartWool")
                SmartWool.RenameReport("267")
                SmartWool.Move_File(supplier, "267")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with SmartWool dept 267 Exception: " + str(e))
                pass
            try:
                SmartWool.DownloadReport("159643183", "67 - SP HOSIERY/SOCKS-SmartWool")
                SmartWool.RenameReport("67")
                SmartWool.Move_File(supplier, "67")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with SmartWool dept 67 Exception: " + str(e))
        except Exception as e:
            self.lo.log_to_file(self, "INFO", "" + str(e))
            if str(e) != " ":
                return str(e)
            else:
                return "No Exception"
        finally:
            SmartWool.Logout(supplier)

    def PopSockets(self,supplier):
        PopSockets = NordstromPortalMethods(self.v_Browser, self.lo, self.currentDate)
        try:
            PopSockets.GetDate(supplier)
            PopSockets.Login(supplier)
            try:
                PopSockets.DownloadReport("5144037", "44 - YC HANDBAGS-PopSockets")
                PopSockets.RenameReport("44")
                PopSockets.Move_File(supplier, "44")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with PopSockets dept 44 Exception: " + str(e))
                pass
            try:
                PopSockets.DownloadReport("5144037", "587 - POP IN SHOP-PopSockets")
                PopSockets.RenameReport("587")
                PopSockets.Move_File(supplier, "587")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with PopSockets dept 587 Exception: " + str(e))
        except Exception as e:
            self.lo.log_to_file(self, "INFO", "" + str(e))
            if str(e) != " ":
                return str(e)
            else:
                return "No Exception"
        finally:
            PopSockets.Logout(supplier)

    def SaxxUnderWear(self,supplier):
        SaxxUnderWear = NordstromPortalMethods(self.v_Browser, self.lo, self.currentDate)
        try:
            SaxxUnderWear.GetDate(supplier)
            SaxxUnderWear.Login(supplier)
            try:
                SaxxUnderWear.DownloadReport("5113558", "267 - SP MEN-SaxxUnderwear")
                SaxxUnderWear.RenameReport("267")
                SaxxUnderWear.Move_File(supplier, "267")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with SaxxUnderWear dept 267 Exception: " + str(e))
                pass
            try:
                SaxxUnderWear.DownloadReport("5113558", "536 - M SPECIALIZED-SaxxUnderwear")
                SaxxUnderWear.RenameReport("536")
                SaxxUnderWear.Move_File(supplier, "536")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with SaxxUnderWear dept 536 Exception: " + str(e))
                pass
            try:
                SaxxUnderWear.DownloadReport("5113558", "588 - M ACTIVE/OUTERWER-SaxxUnderwear")
                SaxxUnderWear.RenameReport("588")
                SaxxUnderWear.Move_File(supplier, "588")
                time.sleep(3)
            except Exception as e:
                self.lo.log_to_file(self, "ERROR", "Not Done with SaxxUnderWear dept 588 Exception: " + str(e))
        except Exception as e:
            self.lo.log_to_file(self, "INFO", "" + str(e))
            if str(e) != " ":
                return str(e)
            else:
                return "No Exception"
        finally:
            SaxxUnderWear.Logout(supplier)
