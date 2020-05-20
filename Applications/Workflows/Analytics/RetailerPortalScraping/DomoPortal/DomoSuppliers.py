"""
@ Author - Krishnabhashkar jha
@ Creation date - 7/12/2019
@ Description - Domo suppliers.
"""
import os
import datetime
import shutil
from Applications.Workflows.Analytics.RetailerPortalScraping.DomoPortal import DownloadDomoReports
# from Applications.Workflows.Analytics.RetailerPortalScraping.Utilites.LogFileUtility import LogFileUtility
from Applications.Workflows.Analytics.RetailerPortalScraping.DomoPortal import DomoPortalMethods

def Execute_DomoSuppliers(self,v_Browser,lo):
        Days = datetime.datetime.now()
        var_foldername = Days.strftime("%d-%b-%Y")
        var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'DomoPortalSuppliers'
        if os.path.exists(var_pathName):
                shutil.rmtree(var_pathName)
        if not os.path.exists(var_pathName):
            try:
                DomoPortalMethods.copy_file()
            finally:
                # exception = DownloadDomoReports.ColumbiaSportswear(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH COLUMBIA SPORTWEAR."+str(exception))
                #
                # exception = DownloadDomoReports.VistaOutdoors(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH ATK."+str(exception))
                #
                # exception = DownloadDomoReports.KeenFootwear(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH KEEN FOOTWEAR."+str(exception))
                #
                # exception = DownloadDomoReports.NorthFace(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH NORTH FACE."+str(exception))
                #
                # exception = DownloadDomoReports.Crocs(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH CROCS."+str(exception))
                #
                # exception = DownloadDomoReports.Beretta(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH BERETTA."+str(exception))

                # exception = DownloadDomoReports.PureFishing(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH PUREFISHING."+str(exception))

                # exception = DownloadDomoReports.Yeti(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH YETI."+str(exception))
                #
                # exception = DownloadDomoReports.PelicanProducts(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH PELICANPRODUCTS."+str(exception))
                #
                # exception = DownloadDomoReports.GFiveOutdoors(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH GFIVEOUTDOORS."+str(exception))

                # exception = DownloadDomoReports.LacrosseFootwear(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH LACROSSEFOOTWEAR."+str(exception))

                # exception = DownloadDomoReports.UnderArmour(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH UNDERARMOUR."+str(exception))
                #
                # exception = DownloadDomoReports.GerLegendaryBlades(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH GERLEGENDARYBLADES."+str(exception))
                #
                # exception = DownloadDomoReports.SITKAGear(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH SITKAGEAR."+str(exception))
                #
                # exception = DownloadDomoReports.CarlZeiss(self, v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH CarlZeiss."+str(exception))

                # exception = DownloadDomoReports.Kimber(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH KIMBER."+str(exception))

                # exception = DownloadDomoReports.Wolverine(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH WOLVERINE."+str(exception))

                # exception = DownloadDomoReports.GearAid(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH GEARAIDINC."+str(exception))
                #
                # exception = DownloadDomoReports.GildanApparel(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH GILDANAPPAREL."+str(exception))
                #
                # exception = DownloadDomoReports.MtnOps(self,v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH MTNOPS."+str(exception))

                # exception = DownloadDomoReports.VistaOutdoor(self, v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH VISTAOUTDOOR."+str(exception))

                # exception = DownloadDomoReports.AmericanAccessoriesInc(self, v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH AMERICANACCESSORIESINC."+str(exception))

                # exception = DownloadDomoReports.BenchmadeKnifeCo(self, v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH BENCHMADEKNIFECO."+str(exception))
                #
                # exception = DownloadDomoReports.Chums(self, v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH CHUMS."+str(exception))

                exception = DownloadDomoReports.DrewBradyCompanyInc(self, v_Browser,lo)
                lo.log_to_file(self, "INFO", " DONE WITH DREWBRADYCOMPANYINC."+str(exception))

                exception = DownloadDomoReports.TervisTumbler(self, v_Browser,lo)
                lo.log_to_file(self, "INFO", " DONE WITH TERVISTUMBLER."+str(exception))

                exception = DownloadDomoReports.BuckGardnerCalls(self, v_Browser,lo)
                lo.log_to_file(self, "INFO", " DONE WITH BUCKGARDNERCALLS."+str(exception))

                exception = DownloadDomoReports.Energizer(self, v_Browser,lo)
                lo.log_to_file(self, "INFO", " DONE WITH ENERGIZER."+str(exception))

                exception = DownloadDomoReports.IndustrialRevolution(self, v_Browser,lo)
                lo.log_to_file(self, "INFO", " DONE WITH INDUSTRIALREVOLUTION."+str(exception))

                exception = DownloadDomoReports.Camelback(self, v_Browser,lo)
                lo.log_to_file(self, "INFO", " DONE WITH CAMELBACK."+str(exception))

                exception = DownloadDomoReports.Carhartt(self, v_Browser,lo)
                lo.log_to_file(self, "INFO", " DONE WITH Carhartt." + str(exception))

                exception = DownloadDomoReports.AriatInternational(self, v_Browser,lo)
                lo.log_to_file(self, "INFO", " DONE WITH AriatInternationalAriatInternational." + str(exception))

                exception = DownloadDomoReports.HydroFlask(self, v_Browser,lo)
                lo.log_to_file(self, "INFO", " DONE WITH HydroFlask." + str(exception))

                exception = DownloadDomoReports.LifeIsGood(self, v_Browser,lo)
                lo.log_to_file(self, "INFO", " DONE WITH LifeIsGood." + str(exception))

                # exception = DownloadDomoReports.TenderCorp(self, v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH TenderCorp." + str(exception))
                #
                # exception = DownloadDomoReports.LipseysInc(self, v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH LipseysInc." + str(exception))

                # exception = DownloadDomoReports.StrikeKingLures(self, v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH StrikeKingLures." + str(exception))
                #
                # exception = DownloadDomoReports.LewsFishingTackle(self, v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH LewsFishingTackle." + str(exception))

                # exception = DownloadDomoReports.AllianceSportsGroup(self, v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH AllianceSportsGroup." + str(exception))

                # exception = DownloadDomoReports.SmithandWesson(self, v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH SmithandWesson." + str(exception))
                #
                # exception = DownloadDomoReports.MarolinaOutdoorInc(self, v_Browser,lo)
                # lo.log_to_file(self, "INFO", " DONE WITH MarolinaOutdoorInc." + str(exception))
