
###########################################################
# import xlrd
# import openpyxl
# from functools import reduce
# import math
#
# # workbook = xlrd.open_workbook("C:/Users/Krishnabhashkar.Jha/Desktop/Book1.xlsx")
# # sheet = workbook.sheet_by_index(0)
# # #
# # # col_a = sheet.col_values(0, 1)
# # # col_b = sheet.col_values(1, 1)
# # #
# # # print(col_a)
# # sheet = workbook.sheet_by_index(0)
# # sheet.cell_value(0,0)
# # max_row=sheet.utter_max_rows
# # # for i in range(sheet.ncols):
# # #     print(sheet.cell_value(i,0))
# # #     for j in range(sheet.nrows):
# # #         print(sheet.cell_value(0,i))
# # print(max_row)
# # for i in range()


# ###########################################################
# v_input_wb = openpyxl.load_workbook("C:/Users/Krishnabhashkar.Jha/Desktop/Book1.xlsx")
# v_input_sheet = v_input_wb.get_sheet_by_name("Sheet2")
# total_rows_input=v_input_sheet.max_row
# arr = []
# for i in range(2,int(total_rows_input)+1):
#     j = 5
#     while True:
#         arr.append(v_input_sheet.cell(row=(i),column=j).value)
#         j += 1
#         if type(v_input_sheet.cell(row=(i),column=j).value)!=int:
#             break
#     print(arr)
#     sum = reduce(lambda a, b: a + b, arr)
#     w_bar = int(sum)/int(len(arr))
#     w_bar_arr = list(map(lambda w:w-w_bar,arr))
#     square_arr = list(map(lambda g:g*g,w_bar_arr))
#     addition_arr = reduce(lambda k,l:k+l,square_arr)
#     sd = addition_arr/(int(len(arr))-1)
#     Final_SD = math.sqrt(sd)
#     upper_limit = (w_bar + (3*Final_SD))
#     lower_limit = (w_bar - (3*Final_SD))
#     # Final_SD = math.sqrt(addi_arr)
#     # print(w_bar_arr)
#     # print(square_arr)
#     # print("w_bar = "+str(w_bar))
#     # print("SD is : "+str(sd))
#     print("Final SD is : "+str(Final_SD))
#     print("Upper Limit of File is : "+str(upper_limit))
#     print("Lower Limit of File is : "+str(lower_limit))
#     v_input_sheet.cell(row=i,column=2).value=lower_limit
#     v_input_sheet.cell(row=i,column=3).value=upper_limit
#     v_input_sheet.cell(row=i,column=4).value=Final_SD
#     v_input_wb.save("C:/Users/Krishnabhashkar.Jha/Desktop/Book1.xlsx")
#     arr.clear()
#     w_bar_arr.clear()
#     square_arr.clear()

##########################################################
# import csv
# import getpass
# import glob
# list_of_files = glob.glob("C:\\Users\\" + getpass.getuser() + "\\Downloads\\*")
# latest_file_In_Download = max(list_of_files, key=os.path.getctime)
# print(latest_file_In_Download)
# with open(latest_file_In_Download) as latest_file_In_Download:
#     wb = csv.reader(latest_file_In_Download)
#     i = 1
#     for row in wb:
#         if i == 2:
#             a = row[12]
#             break
#         i += 1
#     if a == "BPS":
#         print("This is BPS File")
#     elif a == "CAB":
#         print("This is CAB File")
#     else:
#         print("No file is there")

####################### NumPy ##########################
# import numpy as np
# arr = ([[1,2,3,4],[2,3,4,5]])
# a = np.zeros((2,3),dtype=np.int16,order='F')
# # print(np.ones((2,3),dtype=np.int64,order='C'))
# print(np.ones_like((a)))
# # print(np.arange(15))
# print(np.linspace(1,10,10))
# print(np.ravel)
# print(np.empty((2,3),dtype=np.int16,order='C'))
# print(np.empty_like(a))
# # print(np.reshape(3,3))
# # print(np.ravel)
# print(np.argmax(arr))
# print(np.argsort(arr))

############################ UI ###################################
# import tkinter
# from tkinter import *
# Tkinter = tkinter.Tk()
# # Tkinter.attributes('-fullscreen',True)
# # Tkinter.attributes('-zoomed',True)
# m = Tkinter.maxsize()
# Tkinter.geometry('{}x{}+0+0'.format(*m))
# background_image=tkinter.PhotoImage(r"C:/Users/Krishnabhashkar.Jha/Desktop/CV/bhaskii")
# background_label = tkinter.Label(image=tkinter.PhotoImage(r"C:/Users/Krishnabhashkar.Jha/Desktop/CV/bhaskii"))
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# Tkinter.title('Happy to Help you')
# Happy = tkinter.Button(text = "HAPPY" , width = 20).pack()
# Sad = tkinter.Button(text = "SAD" , width = 20).pack()
# Tkinter.mainloop()
