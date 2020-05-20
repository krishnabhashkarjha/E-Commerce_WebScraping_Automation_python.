'''
@ Author - Karan Pandya
@ Creation date - 08/29/2018
@ Description - Selection of script as per user request
'''
from Applications.Workflows.ProcessTestFiles.Scripts.Process_Test_Files_Main import Process_Test_Files
from Utilites.LogFileUtility import LogFileUtility
from Applications.Workflows.ProductionDataMonitoring.Scripts.ProductionDataMonitoring import ProductionDataMonitoring
from Applications.Workflows.ErrorHospital.Scripts.ErrorHospital import ErrorHospital
from Applications.Workflows.Netsuite_FI_850_PPD_Setup.Scripts.Netsuite_FI_850_PPD_Setup import Netsuite_FI_850_PPD_Setup
from Applications.Workflows.Requeue.Scripts.Requeue import Requeue
#from Applications.Workflows.ProcessTestFiles.Scripts.Process_Test_Files_Main import Process_Test_Files
from Applications.Workflows.Normal_Web_Fulfillment.Scripts.Web_Fulfillment_main import Normal_Web_Fulfillment_main
from Applications.Workflows.Covalent_Web_Fulfillment.Scripts.Web_Fulfillment_main import Covalent_Web_Fulfillment_main
class Execution:
    def __init__(self, username, team, task_type, log_file_object):
        self.v_username = username
        self.v_task_type = task_type
        self.v_team = team
        self.log_file_object = log_file_object
    def main_execution(self):
        if self.v_task_type == "Production Data Monitoring":
            self.log_file_object.log_to_file("INFO", "Executing Script Prodution Data Monitoring")
            pdm = ProductionDataMonitoring(self.v_task_type, self.log_file_object, self.v_username)
            pdm.execute_main()
        elif self.v_task_type == "Error Hospital - Setup Fix":
            self.log_file_object.log_to_file("INFO", "Executing Script Error Hospital - Setup Fix")
            error_hospital_object = ErrorHospital(self.v_task_type, self.log_file_object, self.v_username)
            error_hospital_object.execute_main()
        elif self.v_task_type == "Netsuite 850 Pre-PROD Setup":
            self.log_file_object.log_to_file("INFO", "Executing Script Netsuite Review 850")
            nr = Netsuite_FI_850_PPD_Setup(self.v_task_type, self.log_file_object, self.v_username)
            nr.execute_main()
        elif self.v_task_type == "Requeue":
            self.log_file_object.log_to_file("INFO", "Executing Script Reueue")
            rq = Requeue(self.v_task_type, self.log_file_object, self.v_username)
            rq.execute_main()
        elif self.v_task_type == "Process Test Files":
            self.log_file_object.log_to_file("INFO", "Executing Script Process Test Files")
            ptf = Process_Test_Files(self.v_task_type, self.log_file_object, self.v_username)
            ptf.execute_main()
        elif self.v_task_type == "Normal Web Fulfillment Setup":
            self.log_file_object.log_to_file("INFO", "Executing Script Normal Web Fulfillment Setup")
            wf = Normal_Web_Fulfillment_main(self.v_task_type, self.log_file_object, self.v_username)
            wf.execute_main()
        elif self.v_task_type == "Covalent Web Fulfillment Setup":
            self.log_file_object.log_to_file("INFO", "Executing Script Covalent Web Fulfillment Setup")
            wf = Covalent_Web_Fulfillment_main(self.v_task_type, self.log_file_object, self.v_username)
            wf.execute_main()
        else:
            self.log_file_object.log_to_file('ERROR','Invalid Task Type')
