"""
@ Author - Krishnabhashkar jha
@ Creation date - 7/12/2019
@ Description - Main Scripts of Analytics Automation.
"""
import os
import shutil
import time
import datetime
from Applications.Workflows.Analytics.RetailerPortalScraping.DomoPortal import DomoPortalMethods
from Applications.Workflows.Analytics.RetailerPortalScraping.Utilites.LogFileUtility import LogFileUtility

Days = datetime.datetime.now()
var_foldername = Days.strftime("%d-%b-%Y")


def ColumbiaSportswear(self,v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'ColumbiaSportswear'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'ColumbiaSportswear')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'ColumbiaSportswear' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'ColumbiaSportswear' + "\\" + 'CAB')
        finally:
            try:
                # Login to ColumbiaSportswear
                DomoPortalMethods.Login(self,self.v_Browser, "ColumbiaSportswear",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To ColumbiaSportswear.")
                # SALES -> BASSPRO
                DomoPortalMethods.DownloadForColumbia(self, "SALES", v_Browser,"BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 2, 2)
                DomoPortalMethods.Rename_File("SALES","BASSPRO","COLUMBIA")
                DomoPortalMethods.Move_File('ColumbiaSportswear','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.DownloadForColumbia(self, "SALES", v_Browser,"CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 2, 3)
                DomoPortalMethods.Rename_File("SALES","CABELAS","COLUMBIA")
                DomoPortalMethods.Move_File('ColumbiaSportswear','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.DownloadForColumbia(self, "INVENTORY", v_Browser,"BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 2, 4)
                DomoPortalMethods.Rename_File("INVENTORY","BASSPRO","COLUMBIA")
                DomoPortalMethods.Move_File('ColumbiaSportswear','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.DownloadForColumbia(self, "INVENTORY", v_Browser,"CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 2, 5)
                DomoPortalMethods.Rename_File("INVENTORY","CABELAS","COLUMBIA")
                DomoPortalMethods.Move_File('ColumbiaSportswear','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)



def VistaOutdoors(self,v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'ATK'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'ATK')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'ATK' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'ATK' + "\\" + 'CAB')
        finally:
            try:
                # Login to VistaOutdoors
                DomoPortalMethods.Login(self, self.v_Browser, "VistaOutdoors",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To VistaOutdoors.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser,"BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 3, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRO", "VISTA")
                DomoPortalMethods.Move_File('ATK','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser,"CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 3, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELAS", "VISTA")
                DomoPortalMethods.Move_File('ATK','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser,"BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 3, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRO", "VISTA")
                DomoPortalMethods.Move_File('ATK','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser,"CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 3, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELAS", "VISTA")
                DomoPortalMethods.Move_File('ATK','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)


def KeenFootwear(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'KeenFootwear'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'KeenFootwear')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'KeenFootwear' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'KeenFootwear' + "\\" + 'CAB')
        finally:
            try:
                # Login to KeenFootwear
                DomoPortalMethods.Login(self, self.v_Browser, "KeenFootwear",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To KeenFootwear.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 4, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRO", "KEEN")
                DomoPortalMethods.Move_File('KeenFootwear','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 4, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELAS", "KEEN")
                DomoPortalMethods.Move_File('KeenFootwear','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 4, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRO", "KEEN")
                DomoPortalMethods.Move_File('KeenFootwear','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 4, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELAS", "KEEN")
                DomoPortalMethods.Move_File('KeenFootwear','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def NorthFace(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'NorthFace'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'NorthFace')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'NorthFace' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'NorthFace' + "\\" + 'CAB')
        finally:
            try:
                # Login to NorthFace
                DomoPortalMethods.Login(self, self.v_Browser, "NorthFace",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To NorthFace.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 5, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "NORTHFACE")
                DomoPortalMethods.Move_File('NorthFace','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 5, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "NORTHFACE")
                DomoPortalMethods.Move_File('NorthFace','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 5, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "NORTHFACE")
                DomoPortalMethods.Move_File('NorthFace','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 5, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "NORTHFACE")
                DomoPortalMethods.Move_File('NorthFace','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def Crocs(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Crocs'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Crocs')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Crocs' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Crocs' + "\\" + 'CAB')
        finally:
            try:
                # Login to Crocs
                DomoPortalMethods.Login(self, self.v_Browser, "Crocs",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To Crocs.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 6, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "CROCS")
                DomoPortalMethods.Move_File('Crocs','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 6, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "CROCS")
                DomoPortalMethods.Move_File('Crocs','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 6, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "CROCS")
                DomoPortalMethods.Move_File('Crocs','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 6, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "CROCS")
                DomoPortalMethods.Move_File('Crocs','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def Beretta(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Beretta'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Beretta')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Beretta' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Beretta' + "\\" + 'CAB')
        finally:
            try:
                # Login to Beretta
                DomoPortalMethods.Login(self, self.v_Browser, "Beretta",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To Beretta.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 7, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "BERETTA")
                DomoPortalMethods.Move_File('Beretta','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 7, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "BERETTA")
                DomoPortalMethods.Move_File('Beretta','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 7, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "BERETTA")
                DomoPortalMethods.Move_File('Beretta','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 7, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "BERETTA")
                DomoPortalMethods.Move_File('Beretta','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def PureFishing(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'PureFishing'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'PureFishing')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'PureFishing' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'PureFishing' + "\\" + 'CAB')
        finally:
            try:
                # Login to PureFishing
                DomoPortalMethods.Login(self, self.v_Browser, "PureFishing",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To PureFishing.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 8, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "PUREFISHING")
                DomoPortalMethods.Move_File('PureFishing','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 8, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "PUREFISHING")
                DomoPortalMethods.Move_File('PureFishing','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 8, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "PUREFISHING")
                DomoPortalMethods.Move_File('PureFishing','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 8, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "PUREFISHING")
                DomoPortalMethods.Move_File('PureFishing','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def Yeti(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Yeti'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Yeti')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Yeti' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Yeti' + "\\" + 'CAB')
        finally:
            try:
                # Login to Yeti
                DomoPortalMethods.Login(self, self.v_Browser, "Yeti",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To Yeti.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 9, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "YETI")
                DomoPortalMethods.Move_File('Yeti','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 9, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "YETI")
                DomoPortalMethods.Move_File('Yeti','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 9, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "YETI")
                DomoPortalMethods.Move_File('Yeti','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 9, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "YETI")
                DomoPortalMethods.Move_File('Yeti','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def PelicanProducts(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'PelicanProducts'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'PelicanProducts')
            os.makedirs(
                r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'PelicanProducts' + "\\" + 'BPS')
            os.makedirs(
                r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'PelicanProducts' + "\\" + 'CAB')
        finally:
            try:
                # Login to PelicanProducts
                DomoPortalMethods.Login(self, self.v_Browser, "PelicanProducts",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To PelicanProducts.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 10, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "PELICANPRODUCTS")
                DomoPortalMethods.Move_File('PelicanProducts','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 10, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "PELICANPRODUCTS")
                DomoPortalMethods.Move_File('PelicanProducts','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 10, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "PELICANPRODUCTS")
                DomoPortalMethods.Move_File('PelicanProducts','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 10, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "PELICANPRODUCTS")
                DomoPortalMethods.Move_File('PelicanProducts','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def GFiveOutdoors(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GFiveOutdoors'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GFiveOutdoors')
            os.makedirs(
                r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GFiveOutdoors' + "\\" + 'BPS')
            os.makedirs(
                r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GFiveOutdoors' + "\\" + 'CAB')
        finally:
            try:
                # Login to GFiveOutdoors
                DomoPortalMethods.Login(self, self.v_Browser, "GFiveOutdoors",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To GFiveOutdoors.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 11, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "G5OUTDOORS")
                DomoPortalMethods.Move_File('GFiveOutdoors','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 11, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "G5OUTDOORS")
                DomoPortalMethods.Move_File('GFiveOutdoors','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 11, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "G5OUTDOORS")
                DomoPortalMethods.Move_File('GFiveOutdoors','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 11, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "G5OUTDOORS")
                DomoPortalMethods.Move_File('GFiveOutdoors','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def LacrosseFootwear(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LacrosseFootwear'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LacrosseFootwear')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LacrosseFootwear' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LacrosseFootwear' + "\\" + 'CAB')
        finally:
            try:
                # Login to LacrosseFootwear
                DomoPortalMethods.Login(self, self.v_Browser, "LacrosseFootwear",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To LacrosseFootwear.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 12, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "LACROSSE")
                DomoPortalMethods.Move_File('LacrosseFootwear','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 12, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "LACROSSE")
                DomoPortalMethods.Move_File('LacrosseFootwear','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 12, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "LACROSSE")
                DomoPortalMethods.Move_File('LacrosseFootwear','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 12, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "LACROSSE")
                DomoPortalMethods.Move_File('LacrosseFootwear','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def UnderArmour(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'UnderArmour'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'UnderArmour')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'UnderArmour' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'UnderArmour' + "\\" + 'CAB')
        finally:
            try:
                # Login to UnderArmour
                DomoPortalMethods.Login(self, self.v_Browser, "UnderArmour",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To UnderArmour.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 13, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "UNDERARMOUR")
                DomoPortalMethods.Move_File('UnderArmour','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 13, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "UNDERARMOUR")
                DomoPortalMethods.Move_File('UnderArmour','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 13, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "UNDERARMOUR")
                DomoPortalMethods.Move_File('UnderArmour','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 13, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "UNDERARMOUR")
                DomoPortalMethods.Move_File('UnderArmour','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def GerLegendaryBlades(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GerberLegendaryBlades'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GerberLegendaryBlades')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GerberLegendaryBlades' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GerberLegendaryBlades' + "\\" + 'CAB')
        finally:
            try:
                # Login to GerberLegendaryBlades
                DomoPortalMethods.Login(self, self.v_Browser, "GerberLegendaryBlades",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To GerberLegendaryBlades.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 14, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "GERBER")
                DomoPortalMethods.Move_File('GerberLegendaryBlades','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 14, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "GERBER")
                DomoPortalMethods.Move_File('GerberLegendaryBlades','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 14, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "GERBER")
                DomoPortalMethods.Move_File('GerberLegendaryBlades','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 14, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "GERBER")
                DomoPortalMethods.Move_File('GerberLegendaryBlades','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def SITKAGear(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'SITKAGear'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'SITKAGear')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'SITKAGear' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'SITKAGear' + "\\" + 'CAB')
        finally:
            try:
                # Login to SITKAGear
                DomoPortalMethods.Login(self, self.v_Browser, "SITKAGear",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To SITKAGear.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 15, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "SITKA")
                DomoPortalMethods.Move_File('SITKAGear','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 15, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "SITKA")
                DomoPortalMethods.Move_File('SITKAGear','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 15, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "SITKA")
                DomoPortalMethods.Move_File('SITKAGear','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 15, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "SITKA")
                DomoPortalMethods.Move_File('SITKAGear','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def CarlZeiss(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'CarlZeiss'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'CarlZeiss')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'CarlZeiss' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'CarlZeiss' + "\\" + 'CAB')
        finally:
            try:
                # Login to CarlZeiss
                DomoPortalMethods.Login(self, self.v_Browser, "CarlZeiss",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To CarlZeiss.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 16, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "CARLZEISS")
                DomoPortalMethods.Move_File('CarlZeiss','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 16, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "CARLZEISS")
                DomoPortalMethods.Move_File('CarlZeiss','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 16, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "CARLZEISS")
                DomoPortalMethods.Move_File('CarlZeiss','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 16, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "CARLZEISS")
                DomoPortalMethods.Move_File('CarlZeiss','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def Kimber(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Kimber'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Kimber')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Kimber' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Kimber' + "\\" + 'CAB')
        finally:
            try:
                # Login to Kimber
                DomoPortalMethods.Login(self, self.v_Browser, "Kimber",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To Kimber.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 17, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "KIMBER")
                DomoPortalMethods.Move_File('Kimber','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 17, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "KIMBER")
                DomoPortalMethods.Move_File('Kimber','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 17, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "KIMBER")
                DomoPortalMethods.Move_File('Kimber','BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 17, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "KIMBER")
                DomoPortalMethods.Move_File('Kimber','CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def Wolverine(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Wolverine'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Wolverine')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Wolverine' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Wolverine' + "\\" + 'CAB')
        finally:
            try:
                # Login to Wolverine
                DomoPortalMethods.Login(self, self.v_Browser, "Wolverine",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To Wolverine.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 18, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "WOLVERINE")
                DomoPortalMethods.Move_File('Wolverine', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 18, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "WOLVERINE")
                DomoPortalMethods.Move_File('Wolverine', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 18, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "WOLVERINE")
                DomoPortalMethods.Move_File('Wolverine', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 18, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "WOLVERINE")
                DomoPortalMethods.Move_File('Wolverine', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def GearAid(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GearAid'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GearAid')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GearAid' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GearAid' + "\\" + 'CAB')
        finally:
            try:
                # Login to GearAid
                DomoPortalMethods.Login(self, self.v_Browser, "GearAid",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To GearAid.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 19, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "GEARAIDINC")
                DomoPortalMethods.Move_File('GearAid', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 19, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "GEARAIDINC")
                DomoPortalMethods.Move_File('GearAid', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 19, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "GEARAIDINC")
                DomoPortalMethods.Move_File('GearAid', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 19, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "GEARAIDINC")
                DomoPortalMethods.Move_File('GearAid', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def GildanApparel(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GildanApparel'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GildanApparel')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GildanApparel' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'GildanApparel' + "\\" + 'CAB')
        finally:
            try:
                # Login to GildanApparel
                DomoPortalMethods.Login(self, self.v_Browser, "GildanApparel",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To GildanApparel.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 20, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "GILDANAPPAREL")
                DomoPortalMethods.Move_File('GildanApparel', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 20, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "GILDANAPPAREL")
                DomoPortalMethods.Move_File('GildanApparel', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 20, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "GILDANAPPAREL")
                DomoPortalMethods.Move_File('GildanApparel', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 20, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "GILDANAPPAREL")
                DomoPortalMethods.Move_File('GildanApparel', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def MtnOps(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'MtnOps'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(
                r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'MtnOps')
            os.makedirs(
                r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'MtnOps' + "\\" + 'BPS')
            os.makedirs(
                r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'MtnOps' + "\\" + 'CAB')
        finally:
            try:
                # Login to MtnOps
                DomoPortalMethods.Login(self, self.v_Browser, "MtnOps",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To MtnOps.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 21, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "MTNOPS")
                DomoPortalMethods.Move_File('MtnOps', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 21, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "MTNOPS")
                DomoPortalMethods.Move_File('MtnOps', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 21, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "MTNOPS")
                DomoPortalMethods.Move_File('MtnOps', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 21, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "MTNOPS")
                DomoPortalMethods.Move_File('MtnOps', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def VistaOutdoor(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'VistaOutdoor'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'VistaOutdoor')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'VistaOutdoor' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'VistaOutdoor' + "\\" + 'CAB')
        finally:
            try:
                # Login to VistaOutdoor
                DomoPortalMethods.Login(self, self.v_Browser, "VistaOutdoor",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To VistaOutdoor.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 22, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "VISTAOUTDOOR")
                DomoPortalMethods.Move_File('VistaOutdoor', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 22, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "VISTAOUTDOOR")
                DomoPortalMethods.Move_File('VistaOutdoor', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 22, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "VISTAOUTDOOR")
                DomoPortalMethods.Move_File('VistaOutdoor', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 22, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "VISTAOUTDOOR")
                DomoPortalMethods.Move_File('VistaOutdoor', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def AmericanAccessoriesInc(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'AmericanAccessoriesInc'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'AmericanAccessoriesInc')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'AmericanAccessoriesInc' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'AmericanAccessoriesInc' + "\\" + 'CAB')
        finally:
            try:
                # Login to AmericanAccessoriesInc
                DomoPortalMethods.Login(self, self.v_Browser, "AmericanAccessoriesInc",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To AmericanAccessoriesInc.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 23, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "AMERICANACCESSORIESINC")
                DomoPortalMethods.Move_File('AmericanAccessoriesInc', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 23, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "AMERICANACCESSORIESINC")
                DomoPortalMethods.Move_File('AmericanAccessoriesInc', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 23, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "AMERICANACCESSORIESINC")
                DomoPortalMethods.Move_File('AmericanAccessoriesInc', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 23, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "AMERICANACCESSORIESINC")
                DomoPortalMethods.Move_File('AmericanAccessoriesInc', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def BenchmadeKnifeCo(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'BenchmadeKnifeCo'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'BenchmadeKnifeCo')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'BenchmadeKnifeCo' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'BenchmadeKnifeCo' + "\\" + 'CAB')
        finally:
            try:
                # Login to BenchmadeKnifeCo
                DomoPortalMethods.Login(self, self.v_Browser, "BenchmadeKnifeCo",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To BenchmadeKnifeCo.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 24, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "BENCHMADEKNIFECO")
                DomoPortalMethods.Move_File('BenchmadeKnifeCo', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 24, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "BENCHMADEKNIFECO")
                DomoPortalMethods.Move_File('BenchmadeKnifeCo', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 24, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "BENCHMADEKNIFECO")
                DomoPortalMethods.Move_File('BenchmadeKnifeCo', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 24, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "BENCHMADEKNIFECO")
                DomoPortalMethods.Move_File('BenchmadeKnifeCo', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def Chums(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Chums'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Chums')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Chums' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Chums' + "\\" + 'CAB')
        finally:
            try:
                # Login to Chums
                DomoPortalMethods.Login(self, self.v_Browser, "Chums",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To Chums.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 25, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "CHUMS")
                DomoPortalMethods.Move_File('Chums', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 25, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "CHUMS")
                DomoPortalMethods.Move_File('Chums', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 25, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "CHUMS")
                DomoPortalMethods.Move_File('Chums', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 25, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "CHUMS")
                DomoPortalMethods.Move_File('Chums', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def DrewBradyCompanyInc(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'DrewBradyCompanyInc'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'DrewBradyCompanyInc')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'DrewBradyCompanyInc' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'DrewBradyCompanyInc' + "\\" + 'CAB')
        finally:
            try:
                # Login to DrewBradyCompanyInc
                DomoPortalMethods.Login(self, self.v_Browser, "DrewBradyCompanyInc",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To DrewBradyCompanyInc.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 26, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "DREWBRADYCOMPANYINC")
                DomoPortalMethods.Move_File('DrewBradyCompanyInc', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 26, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "DREWBRADYCOMPANYINC")
                DomoPortalMethods.Move_File('DrewBradyCompanyInc', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 26, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "DREWBRADYCOMPANYINC")
                DomoPortalMethods.Move_File('DrewBradyCompanyInc', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 26, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "DREWBRADYCOMPANYINC")
                DomoPortalMethods.Move_File('DrewBradyCompanyInc', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def TervisTumbler(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'TervisTumbler'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'TervisTumbler')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'TervisTumbler' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'TervisTumbler' + "\\" + 'CAB')
        finally:
            try:
                # Login to TervisTumbler
                DomoPortalMethods.Login(self, self.v_Browser, "TervisTumbler",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To TervisTumbler.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 27, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "TERVISTUMBLER")
                DomoPortalMethods.Move_File('TervisTumbler', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 27, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "TERVISTUMBLER")
                DomoPortalMethods.Move_File('TervisTumbler', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 27, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "TERVISTUMBLER")
                DomoPortalMethods.Move_File('TervisTumbler', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 27, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "TERVISTUMBLER")
                DomoPortalMethods.Move_File('TervisTumbler', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def BuckGardnerCalls(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'BuckGardnerCalls'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'BuckGardnerCalls')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'BuckGardnerCalls' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'BuckGardnerCalls' + "\\" + 'CAB')
        finally:
            try:
                # Login to BuckGardnerCalls
                DomoPortalMethods.Login(self, self.v_Browser, "BuckGardnerCalls",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To BuckGardnerCalls.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 28, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "BUCKGARDNERCALLS")
                DomoPortalMethods.Move_File('BuckGardnerCalls', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 28, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "BUCKGARDNERCALLS")
                DomoPortalMethods.Move_File('BuckGardnerCalls', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 28, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "BUCKGARDNERCALLS")
                DomoPortalMethods.Move_File('BuckGardnerCalls', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 28, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "BUCKGARDNERCALLS")
                DomoPortalMethods.Move_File('BuckGardnerCalls', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)


def Energizer(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Energizer'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Energizer')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Energizer' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Energizer' + "\\" + 'CAB')
        finally:
            try:
                # Login to Energizer
                DomoPortalMethods.Login(self, self.v_Browser, "Energizer",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To Energizer.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 29, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "ENERGIZER")
                DomoPortalMethods.Move_File('Energizer', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 29, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "ENERGIZER")
                DomoPortalMethods.Move_File('Energizer', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 29, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "ENERGIZER")
                DomoPortalMethods.Move_File('Energizer', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 29, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "ENERGIZER")
                DomoPortalMethods.Move_File('Energizer', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)


def IndustrialRevolution(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'IndustrialRevolution'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'IndustrialRevolution')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'IndustrialRevolution' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'IndustrialRevolution' + "\\" + 'CAB')
        finally:
            try:
                # Login to IndustrialRevolution
                DomoPortalMethods.Login(self, self.v_Browser, "IndustrialRevolution",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To IndustrialRevolution.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 30, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "INDUSTRIALREVOLUTION")
                DomoPortalMethods.Move_File('IndustrialRevolution', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 30, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "INDUSTRIALREVOLUTION")
                DomoPortalMethods.Move_File('IndustrialRevolution', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 30, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "INDUSTRIALREVOLUTION")
                DomoPortalMethods.Move_File('IndustrialRevolution', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 30, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "INDUSTRIALREVOLUTION")
                DomoPortalMethods.Move_File('IndustrialRevolution', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)


def Camelback(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Camelback'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Camelback')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Camelback' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Camelback' + "\\" + 'CAB')
        finally:
            try:
                # Login to Camelback
                DomoPortalMethods.Login(self, self.v_Browser, "Camelback",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To Camelback.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 31, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "CAMELBACK")
                DomoPortalMethods.Move_File('Camelback', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 31, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "CAMELBACK")
                DomoPortalMethods.Move_File('Camelback', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 31, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "CAMELBACK")
                DomoPortalMethods.Move_File('Camelback', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 31, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "CAMELBACK")
                DomoPortalMethods.Move_File('Camelback', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)


def Carhartt(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Carhartt'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Carhartt')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Carhartt' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'Carhartt' + "\\" + 'CAB')
        finally:
            try:
                # Login to Camelback
                DomoPortalMethods.Login(self, self.v_Browser, "Carhartt",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To Carhartt.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 32, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "CARHARTT")
                DomoPortalMethods.Move_File('Carhartt', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 32, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "CARHARTT")
                DomoPortalMethods.Move_File('Carhartt', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 32, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "CARHARTT")
                DomoPortalMethods.Move_File('Carhartt', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 32, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "CARHARTT")
                DomoPortalMethods.Move_File('Carhartt', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def AriatInternational(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'AriatInternational'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'AriatInternational')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'AriatInternational' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'AriatInternational' + "\\" + 'CAB')
        finally:
            try:
                # Login to Camelback
                DomoPortalMethods.Login(self, self.v_Browser, "AriatInternational",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To AriatInternational.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 33, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "ARIATINTERNATIONAL")
                DomoPortalMethods.Move_File('AriatInternational', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 33, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "ARIATINTERNATIONAL")
                DomoPortalMethods.Move_File('AriatInternational', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 33, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "ARIATINTERNATIONAL")
                DomoPortalMethods.Move_File('AriatInternational', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 33, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "ARIATINTERNATIONAL")
                DomoPortalMethods.Move_File('AriatInternational', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def HydroFlask(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'HydroFlask'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'HydroFlask')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'HydroFlask' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'HydroFlask' + "\\" + 'CAB')
        finally:
            try:
                # Login to Camelback
                DomoPortalMethods.Login(self, self.v_Browser, "HydroFlask",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To HydroFlask.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 34, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "HYDROFLASK")
                DomoPortalMethods.Move_File('HydroFlask', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 34, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "HYDROFLASK")
                DomoPortalMethods.Move_File('HydroFlask', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 34, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "HYDROFLASK")
                DomoPortalMethods.Move_File('HydroFlask', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 34, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "HYDROFLASK")
                DomoPortalMethods.Move_File('HydroFlask', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def LifeIsGood(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LifeIsGood'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LifeIsGood')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LifeIsGood' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LifeIsGood' + "\\" + 'CAB')
        finally:
            try:
                # Login to Camelback
                DomoPortalMethods.Login(self, self.v_Browser, "LifeIsGood",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To LifeIsGood.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 35, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "LIFEISGOOD")
                DomoPortalMethods.Move_File('LifeIsGood', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 35, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "LIFEISGOOD")
                DomoPortalMethods.Move_File('LifeIsGood', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 35, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "LIFEISGOOD")
                DomoPortalMethods.Move_File('LifeIsGood', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 35, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "LIFEISGOOD")
                DomoPortalMethods.Move_File('LifeIsGood', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def TenderCorp(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'TenderCorp'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'TenderCorp')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'TenderCorp' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'TenderCorp' + "\\" + 'CAB')
        finally:
            try:
                # Login to Camelback
                DomoPortalMethods.Login(self, self.v_Browser, "TenderCorp",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To TenderCorp.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 36, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "TENDERCORP")
                DomoPortalMethods.Move_File('TenderCorp', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 36, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "TENDERCORP")
                DomoPortalMethods.Move_File('TenderCorp', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 36, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "TENDERCORP")
                DomoPortalMethods.Move_File('TenderCorp', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 36, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "TENDERCORP")
                DomoPortalMethods.Move_File('TenderCorp', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def LipseysInc(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LipseysInc'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LipseysInc')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LipseysInc' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LipseysInc' + "\\" + 'CAB')
        finally:
            try:
                # Login to Camelback
                DomoPortalMethods.Login(self, self.v_Browser, "LipseysInc",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To LipseysInc.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 37, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "LIPSEYSINC")
                DomoPortalMethods.Move_File('LipseysInc', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 37, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "LIPSEYSINC")
                DomoPortalMethods.Move_File('LipseysInc', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 37, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "LIPSEYSINC")
                DomoPortalMethods.Move_File('LipseysInc', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 37, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "LIPSEYSINC")
                DomoPortalMethods.Move_File('LipseysInc', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def StrikeKingLures(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'StrikeKingLures'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'StrikeKingLures')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'StrikeKingLures' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'StrikeKingLures' + "\\" + 'CAB')
        finally:
            try:
                # Login to Camelback
                DomoPortalMethods.Login(self, self.v_Browser, "StrikeKingLures",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To StrikeKingLures.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 38, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "STRIKEKINGLURES")
                DomoPortalMethods.Move_File('StrikeKingLures', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 38, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "STRIKEKINGLURES")
                DomoPortalMethods.Move_File('StrikeKingLures', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 38, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "STRIKEKINGLURES")
                DomoPortalMethods.Move_File('StrikeKingLures', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 38, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "STRIKEKINGLURES")
                DomoPortalMethods.Move_File('StrikeKingLures', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def LewsFishingTackle(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LewsFishingTackle'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LewsFishingTackle')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LewsFishingTackle' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'LewsFishingTackle' + "\\" + 'CAB')
        finally:
            try:
                # Login to Camelback
                DomoPortalMethods.Login(self, self.v_Browser, "LewsFishingTackle",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To LewsFishingTackle.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 39, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "LEWSFISHINGTACKLE")
                DomoPortalMethods.Move_File('LewsFishingTackle', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 39, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "LEWSFISHINGTACKLE")
                DomoPortalMethods.Move_File('LewsFishingTackle', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 39, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "LEWSFISHINGTACKLE")
                DomoPortalMethods.Move_File('LewsFishingTackle', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 39, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "LEWSFISHINGTACKLE")
                DomoPortalMethods.Move_File('LewsFishingTackle', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def AllianceSportsGroup(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'AllianceSportsGroup'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'AllianceSportsGroup')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'AllianceSportsGroup' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'AllianceSportsGroup' + "\\" + 'CAB')
        finally:
            try:
                # Login to Camelback
                DomoPortalMethods.Login(self, self.v_Browser, "AllianceSportsGroup",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To AllianceSportsGroup.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 40, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "ALLIANCESPORTSGROUP")
                DomoPortalMethods.Move_File('AllianceSportsGroup', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 40, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "ALLIANCESPORTSGROUP")
                DomoPortalMethods.Move_File('AllianceSportsGroup', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 40, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "ALLIANCESPORTSGROUP")
                DomoPortalMethods.Move_File('AllianceSportsGroup', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 40, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "ALLIANCESPORTSGROUP")
                DomoPortalMethods.Move_File('AllianceSportsGroup', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def SmithandWesson(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'SmithandWesson'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'SmithandWesson')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'SmithandWesson' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'SmithandWesson' + "\\" + 'CAB')
        finally:
            try:
                # Login to Camelback
                DomoPortalMethods.Login(self, self.v_Browser, "SmithandWesson",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To SmithandWesson.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 41, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "SMITHANDWESSON")
                DomoPortalMethods.Move_File('SmithandWesson', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 41, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "SMITHANDWESSON")
                DomoPortalMethods.Move_File('SmithandWesson', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 41, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "SMITHANDWESSON")
                DomoPortalMethods.Move_File('SmithandWesson', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 41, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "SMITHANDWESSON")
                DomoPortalMethods.Move_File('SmithandWesson', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)

def MarolinaOutdoorInc(self, v_Browser,lo):
    var_pathName = "C:\Automation\Reports" + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'MarolinaOutdoorInc'
    if os.path.exists(var_pathName):
        shutil.rmtree(var_pathName)
    if not os.path.exists(var_pathName):
        try:
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'MarolinaOutdoorInc')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'MarolinaOutdoorInc' + "\\" + 'BPS')
            os.makedirs(r'C:\\Automation\Reports' + "\\" + var_foldername + "\\" + 'DomoPortal' + "\\" + 'MarolinaOutdoorInc' + "\\" + 'CAB')
        finally:
            try:
                # Login to Camelback
                DomoPortalMethods.Login(self, self.v_Browser, "MarolinaOutdoorInc",lo)
                LogFileUtility.log_to_file(self, "INFO", "Successfully SignIN To MarolinaOutdoorInc.")
                # SALES -> BASSPRO
                DomoPortalMethods.Download(self, "SALES", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 42, 2)
                DomoPortalMethods.Rename_File("SALES", "BASSPRODOMO", "MAROLINAOUTDOORINC")
                DomoPortalMethods.Move_File('MarolinaOutdoorInc', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Basspro.")
                # SALES -> CABELAS
                DomoPortalMethods.Download(self, "SALES", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download sales Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 42, 3)
                DomoPortalMethods.Rename_File("SALES", "CABELASDOMO", "MAROLINAOUTDOORINC")
                DomoPortalMethods.Move_File('MarolinaOutdoorInc', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move sales Report for Cabelas.")
                # INVENTORY -> BASSPRO
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "BPS",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Basspro.")
                DomoPortalMethods.Excel_Update(self, 42, 4)
                DomoPortalMethods.Rename_File("INVENTORY", "BASSPRODOMO", "MAROLINAOUTDOORINC")
                DomoPortalMethods.Move_File('MarolinaOutdoorInc', 'BPS')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move Inventory Report for Basspro.")
                # INVENTORY -> CABELAS
                DomoPortalMethods.Download(self, "INVENTORY", v_Browser, "CAB",lo)
                LogFileUtility.log_to_file(self, "INFO", "Download Inventory Report Successfully for Cabelas.")
                DomoPortalMethods.Excel_Update(self, 42, 5)
                DomoPortalMethods.Rename_File("INVENTORY", "CABELASDOMO", "MAROLINAOUTDOORINC")
                DomoPortalMethods.Move_File('MarolinaOutdoorInc', 'CAB')
                LogFileUtility.log_to_file(self, "INFO", "Successfully Rename and Move inventory Report for Cabelas.")
            except Exception as e:
                LogFileUtility.log_to_file(self, "INFO", ""+str(e))
                if str(e) != " ":
                    return str(e)
                else:
                    return "No Exception"
            finally:
                DomoPortalMethods.SignOut(v_Browser)
