import xlrd
import datetime


# RUTA DEL ARCHIVO
# filePath = "C:\\Users\\Aaron\\Desktop\\xlrd\\1Read\\Libro.xls"
filePath = "C:\\Users\\Aaron\\Desktop\\xlrd\\miModulo\\ECOGUARDAS_ene_2020.xls"

# ABIR UN ARCHIVO
openFile = xlrd.open_workbook(filePath)

# LA HOJA DEL ARCHIVO A ABRIR

# sheet = openFile.sheet_by_name("Hoja1")
sheet = openFile.sheet_by_index(0)


## MOSTRAR SOLO UN CAMPO (FILA, COLUMNA)
# print(sheet.cell_value(6,0))

# # RECORRER TODAS LAS FILAS

#FORMA 1
# for i in range(sheet.nrows):
#         print(sheet.cell_value(i,0), "         ", sheet.cell_value(i,1))


# FORMA 2
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        print(sheet.cell_value(row, col), end='   ')
        print('\t', end='   ')
    print()

#FORMA 2: ARREGLAR FORMATO DE FECHA
# for row in range(sheet.nrows):
#     for col in range(sheet.ncols):
#         if col == 0 and row != 0:
#             #Formato de fecha
#             raw_value = sheet.cell_value(row, col)
#             converted_date = xlrd.xldate_as_tuple(raw_value, openFile.datemode)
#             # print(converted_date) #Regresara una tupla
#             to_print_date = datetime.datetime(*converted_date).strftime("%m/%d/%y") #*converted_date = pasara cada valor de la tupla a la vez
#             # to_print_date = datetime.datetime(converted_date[0], converted_date[1],converted_date[2],converted_date[3]).strftime("%m/%d/%y")
#             print(to_print_date, end=' ')
#         else:
#             print(sheet.cell_value(row, col), end='   ')
#         print('\t', end='   ')
#     print()






# Mostrar numero de filas y de columnas
# print("Your Worksheet has " + str(sheet.ncols)+ " columns")
# print("Your Workshhet has " + str(sheet.nrows)+ " rows")


