import xlsxwriter 

# Directorio donde creara el archivo
path = "C:\\Users\\Aaron\\Desktop\\xlrd\\2Create\\nuevo.xls"

# Busca el directorio donde creara el documento
excel_workbook = xlsxwriter.Workbook(path)

# Crear las hojas
excel_sheet = excel_workbook.add_worksheet()
excel1_sheet = excel_workbook.add_worksheet()

#Escribir en el archivo
excel_sheet.write("A1", "Date")
excel_sheet.write("B1", "Revenue")
excel_sheet.write(0,2, "Cost")
excel_sheet.write(0,3, "Profit")

#Prepare
dates = ["06/02/2020", "06/03/2020", "06/04/2020"]
revenues = [100, 200, 500]
cost = [50, 100, 150]

for i in range(len(dates)):
    excel_sheet.write(i+1, 0, dates[i])
    excel_sheet.write(i+1, 1, revenues[i])
    excel_sheet.write(i+1, 2, cost[i])
    excel_sheet.write(i+1, 3, '=B' +str(i+2) + '-C' + str(i+2))  #=Bn-Cn E.g. = B2-C2


# Cerrar e archivo
excel_workbook.close()
