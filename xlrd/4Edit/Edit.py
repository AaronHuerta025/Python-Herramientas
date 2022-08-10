import xlrd 
import xlsxwriter

# Abrir un archivo
old_path = "C:\\Users\\Aaron\\Desktop\\xlrd\\4Edit\\nuevo.xls"
old_workbook = xlrd.open_workbook(old_path)
old_worksheet = old_workbook.sheet_by_index(0)

#Copy Data
all_rows = []
for row in range(old_worksheet.nrows):
    curr_row =  []
    for col in range(old_worksheet.ncols):
        curr_row.append(old_worksheet.cell_value(row,col))
    all_rows.append(curr_row)

#Modify data
all_rows[3][1] = 1000000

#Create new file
new_path="C:\\Users\\Aaron\\Desktop\\xlrd\\4Edit\\copia\\nuevoModificado.xls"
new_workbook = xlsxwriter.Workbook(new_path)
new_worksheet = new_workbook.add_worksheet()


#Populate the new file
for row in range(len(all_rows)):
    for col in range(len(all_rows[0])):
        new_worksheet.write(row, col, all_rows[row][col])
new_workbook.close()