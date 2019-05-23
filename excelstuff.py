##Install pip install openpyxl==2.3.3
import openpyxl
from openpyxl.cell import get_column_letter, column_index_from_string

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

# Get a cell value

print(s['B2'].value)
print(s['C2'].value)
print(s['B2'].column)
print(s['B2'].row)
print(s['B2'].coordinate)

print(s.cell(row=1, column=2).value)

# Iterating through a row
for i in range(1,4,1):
    print(i, s.cell(row=1, column=i).value)

# Get last used row and column
print(s.max_row)
print(s.max_column)

# Converting between the Excel letters and integer

print(get_column_letter(27)) # Expect AA
print(column_index_from_string('C')) # Expect 3

# Slice a sheet section and iterate through each cell

tupleSlice = tuple(s['A1':'C3'])

i = 0
for row in tupleSlice:
    print("*Row " + str(i))
    for cellObj in row:
        print(cellObj.coordinate, cellObj.value)
    print ("--End Row--")
    i = i + 1

# Print all of column B's values (auto stops after reaching bounds), it's a tuple

print(s.columns[1])
for cell in s.columns[1]:
    print(cell.value)
