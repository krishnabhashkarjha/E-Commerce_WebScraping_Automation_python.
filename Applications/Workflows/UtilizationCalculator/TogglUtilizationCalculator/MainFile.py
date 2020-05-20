
"""
@ Author - Krishnabhashkar jha
@ Creation date - 28/03/2020
@ Description - Declares all the Methods to be used at the Process Level.
"""

from selenium import webdriver
from Applications.Workflows.UtilizationCalculator.Utilites.LogFileUtility import LogFileUtility as lo
from Applications.Workflows.UtilizationCalculator.TogglUtilizationCalculator.UtilizationMethods import UtilizationMethod

class Execute_Main():

    def __init__(self):
        self.v_Browser = webdriver.Chrome('C:/driver/chromedriver')
        self.v_Browser.maximize_window()
        self.lo = lo

    def Execute_Main(self):
        try:
            Main_Method = UtilizationMethod(self.v_Browser,self.lo)
            Main_Method.Login()
            Time = Main_Method.get_value(1,3)
            Main_Method.Set_Week(str(Time))
            T = Main_Method.Get_Utilization("adatar")
            Main_Method.Excel_Update(4,3,T)
            T = Main_Method.Get_Utilization("sadake")
            Main_Method.Excel_Update(5, 3, T)
            T = Main_Method.Get_Utilization("apawar2")
            Main_Method.Excel_Update(6, 3, T)
            T = Main_Method.Get_Utilization("ainamdar")
            Main_Method.Excel_Update(7, 3, T)
            T = Main_Method.Get_Utilization("Ajay Choudhary")
            Main_Method.Excel_Update(8, 3, T)
            T = Main_Method.Get_Utilization("mkamble")
            Main_Method.Excel_Update(9, 3, T)
            T = Main_Method.Get_Utilization("averma")
            Main_Method.Excel_Update(10, 3, T)
            T = Main_Method.Get_Utilization("amane")
            Main_Method.Excel_Update(11, 3, T)
            T = Main_Method.Get_Utilization("srathore")
            Main_Method.Excel_Update(12, 3, T)
            T = Main_Method.Get_Utilization("nmahala")
            Main_Method.Excel_Update(13, 3, T)
            T = Main_Method.Get_Utilization("sswami")
            Main_Method.Excel_Update(14, 3, T)
            T = Main_Method.Get_Utilization("rchoudhari")
            Main_Method.Excel_Update(15, 3, T)
            T = Main_Method.Get_Utilization("vtemkar")
            Main_Method.Excel_Update(16, 3, T)
            T = Main_Method.Get_Utilization("asarode")
            Main_Method.Excel_Update(17, 3, T)
            T = Main_Method.Get_Utilization("rkute")
            Main_Method.Excel_Update(18, 3, T)
            T = Main_Method.Get_Utilization("pshende")
            Main_Method.Excel_Update(19, 3, T)
            T = Main_Method.Get_Utilization("njalkote")
            Main_Method.Excel_Update(20, 3, T)
            T = Main_Method.Get_Utilization("syadav")
            Main_Method.Excel_Update(21, 3, T)
            T = Main_Method.Get_Utilization("ssharma")
            Main_Method.Excel_Update(22, 3, T)
            T = Main_Method.Get_Utilization("rsingh")
            Main_Method.Excel_Update(23, 3, T)
            T = Main_Method.Get_Utilization("praut")
            Main_Method.Excel_Update(24, 3, T)
            T = Main_Method.Get_Utilization("sjakkanawar")
            Main_Method.Excel_Update(25, 3, T)
            T = Main_Method.Get_Utilization("smishra2")
            Main_Method.Excel_Update(26, 3, T)
            T = Main_Method.Get_Utilization("vsingh")
            Main_Method.Excel_Update(27, 3, T)
            T = Main_Method.Get_Utilization("ymaurya")
            Main_Method.Excel_Update(28, 3, T)
            T = Main_Method.Get_Utilization("skumari2")
            Main_Method.Excel_Update(29, 3, T)
            T = Main_Method.Get_Utilization("ktiwari")
            Main_Method.Excel_Update(30, 3, T)
            T = Main_Method.Get_Utilization("agurav")
            Main_Method.Excel_Update(31, 3, T)
            T = Main_Method.Get_Utilization("sshetty")
            Main_Method.Excel_Update(32, 3, T)
            T = Main_Method.Get_Utilization("gpawar3")
            Main_Method.Excel_Update(33, 3, T)
            T = Main_Method.Get_Utilization("udhotre")
            Main_Method.Excel_Update(34, 3, T)
            T = Main_Method.Get_Utilization("asalunkhe")
            Main_Method.Excel_Update(35, 3, T)
            T = Main_Method.Get_Utilization("ashinde")
            Main_Method.Excel_Update(36, 3, T)
            Main_Method.Logout()
            Main_Method.Utilization_calculator()
            self.v_Browser.close()
        except Exception as e:
            self.lo.log_to_file(self, "ERROR", "Exception is : " + str(e))



