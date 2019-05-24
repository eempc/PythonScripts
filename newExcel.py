import openpyxl
import datetime
import os

#Creating
wb = openpyxl.Workbook()
wb.get_sheet_names()
sheet = wb.active

sheet.title = "Spam Bacon Eggs"







# Saving
file_name = str(datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')) + "-CreationTest.xlsx"
print(os.getcwd())
full_path = os.path.join(os.getcwd(), "XLSX", file_name)
print(full_path)
folders_only = os.path.dirname(full_path)
print(folders_only)

if (not os.path.exists(folders_only)):
    os.makedirs(folders_only)

wb.save(full_path)
