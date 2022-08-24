import os

# Global Variables
__company__ = ""
__weekly_close__ = ""
__stage__ = ""
__path_lc_duty_bv__ = "Seleccione el archivo que desea."
__path_lc_duty_bv_to_move__ = os.path.join("C:\\","Users","rpa.DECOWRAPS","Documents","BV","2. Input File for LC for Upload (USER)")
# __path_lc_duty_bv_to_move__ = os.path.join("C:\\","ROBOTS","decowraps","py_form","ouput","BV","2. Input File for LC for Upload (USER)")
__path_lc_duty_bv_to_move_close__ = os.path.join("C:\\","Users","rpa.DECOWRAPS","Documents","BV","3. Input File for Closing BV (USER)")
# __path_lc_duty_bv_to_move_close__ = os.path.join("C:\\","ROBOTS","decowraps","py_form","ouput","BV","3. Input File for Closing BV (USER)")
__path_apportionment__ = "Seleccione el archivo que desea."
__path_apportionment_to_move__ = os.path.join("C:\\","Users","rpa.DECOWRAPS","Documents","BV","4. Prorrateos and Duty (USER)")
# __path_apportionment_to_move__ = os.path.join("C:\\","ROBOTS","decowraps","py_form","ouput","BV","4. Prorrateos and Duty (USER)")
__path_duty_analysis__ = "Seleccione el archivo que desea."
__path_duty_analysis_to_move__ = os.path.join("C:\\","Users","rpa.DECOWRAPS","Documents","BV","4. Prorrateos and Duty (USER)")
# __path_duty_analysis_to_move__ = os.path.join("C:\\","ROBOTS","decowraps","py_form","ouput","BV","4. Prorrateos and Duty (USER)")
__path_tax_name__ = os.path.join("C:\\","Users","rpa.DECOWRAPS","Documents","BV","1. Bot Report Date and data (USER)", "Tax Name.txt")
# __path_tax_name__ = "Tax Name.txt"
# __path_tariff_rate__ = os.path.join("C:\\","Users","rpa.DECOWRAPS","Documents","BV","1. Bot Report Date and data (USER)", "Tax Name.txt")
__path_tariff_rate__ = "Tariff Rate.xlsx"
# __path_tariff_rate__ = os.path.join("C:\\", "ROBOTS", "decowraps", "py_form", "Tariff Rate.xlsx")
__path_bot_report_date__ = os.path.join("C:\\","Users","rpa.DECOWRAPS","Documents","BV","1. Bot Report Date and data (USER)", "Bot Report Date.xlsx")
# __path_bot_report_date__ = 'Bot Report Date.xlsx'
__upload_fire_cx__ = ""
__upload_acctivate__ = ""
__month__ = ""
__month_as_int__ = ""
__year__ = ""
__year_as_int__ = ""
__win_radio_button__ = 0        ##
__dict_radio_button__ = {}      ##
__col_lc_duty__ = {
    'ORIGINAL': ['Type', 'Date', 'Num', 'Name', 'Memo', 'Account', 'Debit', 'PO or transportations', 'Consolidates for PO', 'PO', 'RD', 'Change RD', 'Consolidates', 'Obs 1', 'LC For upload'], 
    'PO': ['Type', 'Date', 'Num', 'Name', 'Memo', 'Account', 'Class', 'Clr', 'Split', 'Debit', 'Credit', 'Balance'], 
    'RD': ['PONumber', 'Transaction Date', 'Change RD'], 
    'CHECK PO': ['Consolidates', 'POs RD this month', 'POs consolidates', '??', 'RD Last month', 'PO comercial samples', 'POs pending RD', 'Comentario 1', 'Comentario 2', 'LC UPLOAD', 'Duties'], 
    'Provisions Last month': ['Type', 'Date', 'Num', 'Name', 'Memo', 'Account', 'Debit', 'PO', 'RD', 
    'Consolidates', '?', 'Type.1', 'Date.1', 'Num.1', 'Name.1', 'Memo.1', 'Account.1', 'Debit.1', 'PO.1', 'RD.1', 'Consolidates.1'], 
    'Acctivate': ['PO', 'Vendor'], 
    'Consolidates': ['CONSOLIDATES 2022', 'PO', 'Only PO', 'CONSOLIDATES 2022.1', 'Vendor', 'RD']}
__col_apportionment__ = {'ORIGINAL': ['Type', 'Date', 'Num', 'Name', 'Memo', 'Account', 'Debit', 'PO or transportations', 'Consolidates for PO', 'PO', 'RD', 'Change RD', 'Consolidates', 'Obs 1', 'LC For upload']}
__col_duty_analysis__ = {'ORIGINAL': ['Type', 'Date', 'Num', 'Name', 'Memo', 'Account', 'Debit', 'PO or transportations', 'Consolidates for PO', 'PO', 'RD', 'Change RD', 'Consolidates', 'Obs 1', 'LC For upload']}




# import os
# import pandas as pd
# __path_lc_duty_bv_to_move__ = os.path.join("C:\\","ROBOTS","decowraps","py_form","input","backups","9. LC DUTY BV 020822.xlsx")
# # __path_lc_duty_bv_to_move__ = os.path.join("C:\\","ROBOTS","decowraps","py_form","ouput","BV","4. Prorrateos and Duty (USER)")
# # path = __path_lc_duty_bv_to_move__+"\\BV prorrateo April 2022.xlsx"
# xl = pd.ExcelFile(__path_lc_duty_bv_to_move__)
# sheetnames = xl.sheet_names
# print(sheetnames)
# dict_columns = {}
# for item in sheetnames:
#     df = pd.read_excel(xl, sheet_name=item)
#     column_list = list(df.columns)
#     # column_list = list(df.iloc[2])
#     # column_list = list(df.iloc[2].values)
#     dict_columns[item] = column_list
# print(dict_columns) 



# __col_lc_duty__ = {
#     'ORIGINAL': ['Unnamed: 0', 1, 3, 2, '7 (despues de la coma y sin el fee)', 8, 6, 'Unnamed: 7', 'Unnamed: 8', 13, '1.1', 'Unnamed: 11', '14 y 7 20 caracteres', 'LCFD_ORIGINAL', 'Unnamed: 14'], 
#     'PO': ['Type', 'Date', 'Num', 'Name', 'Memo', 'Account', 'Class', 'Clr', 'Split', 'Debit', 'Credit', 'Balance', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15'], 
#     'QBooks': ['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15'], 
#     'RD': ['PONumber', 'Transaction Date', 'Change RD', 'Unnamed: 3', 'LCFD_RD'], 
#     'CHECK PO': ['Consolidates', 'POs RD this month', 'POs consolidates', '??', 'RD Last month', 'PO comercial samples', 'POs pending RD', 'Comentario 1', 'Comentario 2', 'LC UPLOAD', 'Duties'], 
#     'Provisions Last month': ['Type', 'Date', 'Num', 'Name', 'Memo', 'Account', 'Debit', 'PO', 'RD', 'Consolidates', '?', 'Type.1', 'Date.1', 'Num.1', 'Name.1', 'Memo.1', 'Account.1', 'Debit.1', 'PO.1', 'RD.1', 'Consolidates.1'], 
#     'Acctivate': ['PO', 'Vendor'], 
#     'Consolidates': ['CONSOLIDATES 2022', 'PO', 'Only PO', 'CONSOLIDATES 2022.1', 'Vendor', 'RD', 'Se tiene  que ordenar por fecha de RD de mayor a menos y despues por consolidado', 'Unnamed: 7', 'LCFD_CONS '], 
#     'Consolidado 2': ['S:', 'Digital Files Decowraps SA', 'Import Records', 'Purchase Orders', 'CONSOLIDATION 2022', '01042022_AIR_AMS', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'LCFD_CONSTranspo ', 'Unnamed: 10', 'Unnamed: 11', '01042022_AIR_AMS.1', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'S:\\Digital Files Decowraps SA\\Import Records\\Purchase Orders\\CONSOLIDATION 2022\\01042022_AIR_AMS']}

# __col_apportionment__ = {
#     'PRORRATEO MAIN': ['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 0.16935124674527505, 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26', 'Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29', 'Unnamed: 30', 'Unnamed: 31', 'Unnamed: 32', 'Unnamed: 33', 'Unnamed: 34', 'Unnamed: 35', 'Unnamed: 36', 'Unnamed: 37', 'Unnamed: 38', 'Unnamed: 39', 'Unnamed: 40', 'Unnamed: 41', 'Unnamed: 42', 'Unnamed: 43', 'Unnamed: 44', 'Unnamed: 45', 'Unnamed: 46', 'Unnamed: 47', 'Unnamed: 48', 'Unnamed: 49', 'Unnamed: 50', 'Unnamed: 51', 'Unnamed: 52', 'Unnamed: 53', 'Unnamed: 54', 'Unnamed: 55', 'Unnamed: 56', 'Unnamed: 57', 'Unnamed: 58', 'Unnamed: 59', 'Unnamed: 60', 'Unnamed: 61', 'Unnamed: 62', 'Unnamed: 63', 'Unnamed: 64', 'Unnamed: 65', 'Unnamed: 66', 'Unnamed: 67', 'Unnamed: 68'], 
#     'ORIGINAL': ['Type', 'Date', 'new Num', 'Name', 'Memo', 'Account', 'Debit', 'PO or transportations', 'Consolidates for PO', 'PO', 'RD', 'Change RD', 'Consolidates', 'Obs 1', 'LC For upload'], 
#     'PENDINGS': ['Unnamed: 0', 'Unnamed: 1', 'Type', 'Date', 'Num', 'Name', 'Memo', 'Account', 'Debit', 'PO or transportations', 'Consolidates for PO', 'PO', 'RD', 'Change RD', 'Consolidates', 'Obs 1', 'LC For upload', 'PO Pending', 'total amount', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24'], 
#     'QB': ['Unnamed: 0', 'QB', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14'], 
#     'Tarif_Code': ['PONumber', 'Product ID', 'Description', 'Ordered', 'Volume per Item', 'Volume Total', 'CONSOLIDATES', 'Prorratear', 'MIX and CONSOLIDATES', 'Date RD', 'Se usa la descarga del tarif. Sepegan las columnas en azul. Se buscan los consolidados. Se verifica si se tiene que prorratear. Y se eliminan los que no. Despues se hace el calculo de los amarillos', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'], 
#     'PO': ['Type', 'Date', 'Num', 'Name', 'Memo', 'Account', 'Class', 'Clr', 'Split', 'Debit', 'Credit', 'Balance'], 
#     'Consolidates': ['CONSOLIDATES 2022', 'PO', 'Only PO', 'CONSOLIDATES 2022.1', 'Vendor', 'RD', 'Se tiene  que ordenar por fecha de RD de mayor a menos y despues por consolidado', 'Unnamed: 7', 'LCFD_CONS ', 'Se usa el del LC DUTY'], 
#     'ORIGINALOLD': ['Type', 'Date', 'Num', 'OLD Name', 'Memo', 'Account', 'Debit', 'PO or transportations', 'Consolidates for PO', 'PO', 'RD', 'Change RD', 'Consolidates', 'Obs 1', 'LC For upload', 'Unnamed: 15', 'new', 'Total amount', 'Ordenar por MEMO y despues por NUM'], 
#     'CHECK PO': ['Consolidates', 'POs RD this month', 'POs consolidates', '??', 'RD Last month', 'PO comercial samples', 'POs pending RD', 'Comentario 1', 'Comentario 2', 'LC UPLOAD', 'Duties'], 
#     'ReportProductDimensionsEU': ['UPC', 'Product ID', 'Description', 'Item Type', 'Status', 'Unit', 'Package Unit', 'Alternate Unit', 'Alternate Unit Conversion Factor', 'Weight', 'Length', 'Height', 'Width', 'Volume', 'Alt Weight', 'Alt Length', 'Alt Height', 'Alt Width', 'Alt Volume', 'Unnamed: 19', 'EA LEN', 'EA HEI', 'EA WID', 'EA VOL', 'EA WGT', 'PRODUCT CLASS', 'Unnamed: 26', 'Unnamed: 27', 'Se descarga en crudo', 'Unnamed: 29', 'Unnamed: 30', 'Unnamed: 31', 'Unnamed: 32', 'Product Dimensions', 'PRORR_RPD'], 
#     'RD': ['PONumber', 'Transaction Date', 'Change RD', 'Unnamed: 3', 'LCFD_RD'], 
#     'Provisions Last month': ['Type', 'Date', 'Num', 'Name', 'Memo', 'Account', 'Debit', 'PO', 'RD', 'Consolidates', '?', 'Type.1', 'Date.1', 'Num.1', 'Name.1', 'Memo.1', 'Account.1', 'Debit.1', 'PO.1', 'RD.1', 'Consolidates.1'], 
#     'Consolidado 2': []}


# __col_duty_analysis__ = {
#     'DATA': ['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2'], 
#     'Duty1': ['Consolidates', 'PO', 'Key', 'Unnamed: 3'], 
#     'TARIFF CODE': ['PONumber', 'Vendors', 'Arrival', 'Product ID', 'Description', 'Amount', 'Tarif Code', 'Concatenar "A" "C" "D" "V"', 'Mover todo de la pestaña Tarif_Code_SA del archivo check RD pero no debe pasar los local purchase, DW german, CURRIER. Descartar todos los CONSOLIDADOS que no son DUTY col U. Ordenar monto de menor a mayor, por fecha, despues por product ID y despues por PO', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 330.16730000000007, 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26', 'Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29', 'Unnamed: 30', 'Unnamed: 31', 'Unnamed: 32', 'Unnamed: 33'], 
#     'Summary Duty': ['Consolidates', 'Amount USD', 'Amount \nin Euros', 'Amount Euros to Allocate', 'Exact Duty Amount per Item', 'Missing Duty from Invoice', 'Amount per Ítem allocated for Difference', 'Total Duty allocated Per Item', 'Status', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12'], 
#     'Duty': ['Type', 'Date', 'Num', 'Name', 'Memo', 'Account', 'Debit', 'PO or transportations', 'Consolidates for PO', 'PO', 'RD', 'Change RD', 'Consolidates', 'Obs 1', 'LC For upload', 'Consolidado', 'Nro consolidados'], 
#     'By Product': ['CONSOLIDATES', '(Todas)', 'Unnamed: 2'], 
#     'Dutymain': ['Key consolidates PO', 'Consolidates', 'PODuty', 'Rate', 'Amount', 'Duty N°', 'Type', 'Date', 'Num', 'Name', 'Memo', 'Account', 'Debit', 'PO or transportations', 'Consolidates for PO', 'PO', 'RD', 'Change RD', 'Consolidates.1', 'Obs 1', 'LC For upload', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24'], 
#     'ORIGINAL (DUTY)': ['Unnamed: 0', 'Traer todos los DUTIEs que aparecen en "ORIGINAL" COL OBS1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'De prorrateos traer todos los DUTies que en la columna "MEMO" aparece "DUTY"', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20'], 
#     'TARIFF RATE': ['Tarrif Code', 'Rate', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8'], 
#     'RD': ['Product ID', 'Journal', 'Session', 'PONumber', 'Transaction Date', 'Warehouse', 'Key', 'Debit Amount', 'Consolidates', 'Unnamed: 9', 'Line number', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15'], 
#     'Product id': ['CONSOLIDATES', 'PONumber', 'Product ID', 'Duty \nRate', 'Tax', 'Num', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'DutyAn_ TariffCode ', 'DutyAn_ ProductId'], 
#     'PT SLC': ['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3'], 
#     'SLC': ['Memo', 'Amount', 'Consolidate', 'Unnamed: 3', 'Valores y consolidados de Archivo 2 LC Duty hoja Original']}