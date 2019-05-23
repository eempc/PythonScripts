##Install pip install openpyxl==2.3.3
import openpyxl

print("---- Start ----")
#Load workbook wb
wb = openpyxl.load_workbook('readtest.xlsx')
print(type(wb))

sheetNamesArray = wb.get_sheet_names() #deprecated
sheetNamesArray2 = wb.sheetnames

print(sheetNamesArray2)

sheet1 = wb.get_sheet_by_name('Sheet1')
print(type(sheet1))
print(sheet1.title)

lastActiveSheet = wb.active
print(lastActiveSheet)

targetSheetString = sheetNamesArray2[0]
print(targetSheetString) # No need for .title, it returns the name only, not a sheet object, this is string

s = wb.get_sheet_by_name(sheetNamesArray2[0])

print(s['B2'].value)
print(s['C2'].value)
print(s['B2'].column)
print(s['B2'].row)
print(s['B2'].coordinate)

print(s.cell(row=1, column=2).value)

for i in range(1,4,1):
    print(i, s.cell(row=1, column=i).value)

print(s.max_row)
print(s.max_column)