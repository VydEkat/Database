import os
import pandas as pd

excel_input = pd.ExcelFile("data/Full.xlsx")

table_n1 = pd.read_excel(excel_input, 'Main')   #Нормализированная таблица 1
table_n2 = pd.read_excel(excel_input, 'Sports') #Нормализированная таблица 2
table_n3 = pd.read_excel(excel_input, 'Gender') #Нормализированная таблица 3
