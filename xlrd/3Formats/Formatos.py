import xlsxwriter 

# Directorio donde creara el archivo
path = "C:\\Users\\Aaron\\Desktop\\xlrd\\3Formats\\nuevo.xls"

# Busca el directorio donde creara el documento
excel_workbook = xlsxwriter.Workbook(path)

# Crear las hojas
excel_sheet = excel_workbook.add_worksheet()
excel1_sheet = excel_workbook.add_worksheet()


#Create formats 
header_format = excel_workbook.add_format()
header_format.set_font_color('orange')
header_format.set_bg_color('#0000AA')
header_format.set_underline(True)
header_format.set_center_across(True)
header_format.set_font_size(14)

money_format = excel_workbook.add_format({'num_format': '$#,#'})
bold_money_format = excel_workbook.add_format({'num_format': '$#,#', 'bold': True})


#Escribir en el archivo
excel_sheet.write("A1", "Date", header_format)
excel_sheet.write("B1", "Revenue", header_format)
excel_sheet.write(0,2, "Cost", header_format)
excel_sheet.write(0,3, "Profit", header_format)

header_format.set_underline(False)

#Prepare
dates = ["06/02/2020", "06/03/2020", "06/04/2020"]
revenues = [100, 200, 500]
cost = [50, 100, 150]

for i in range(len(dates)):
    excel_sheet.write(i+1, 0, dates[i])
    excel_sheet.write(i+1, 1, revenues[i], money_format)
    excel_sheet.write(i+1, 2, cost[i], money_format)
    excel_sheet.write(i+1, 3, '=B' +str(i+2) + '-C' + str(i+2), bold_money_format)  #=Bn-Cn E.g. = B2-C2


# Cerrar e archivo
excel_workbook.close()
