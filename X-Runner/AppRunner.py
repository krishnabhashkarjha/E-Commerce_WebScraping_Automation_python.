'''

@ Author - Karan Pandya
@ Creation date - 08/27/2018
@ Description - Take the inputs from input GUI and run the script accordingly
'''

from Utilites.InputGUI import InputGUI
from Utilites.Execution import Execution
from Utilites.LogFileUtility import LogFileUtility

class AppRunner:

    input_gui_object = InputGUI()
    input_gui_object.window_creation()
    input_gui_object.validation(input_gui_object.username_flag, input_gui_object.team_flag, input_gui_object.task_type_flag)
    v_user_name = input_gui_object.username
    v_team = input_gui_object.team
    v_task_type = input_gui_object.task_type
    log_file_object = LogFileUtility(v_task_type)
    execution_file_object = Execution(v_user_name, v_team, v_task_type, log_file_object)
    execution_file_object.main_execution()
