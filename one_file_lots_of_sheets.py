import re 
import pandas as pd

def excel_sheet_based_on_column_values(dataframe: pd.DataFrame, column: str, filename: str):
    ### First create a dictionary with values as keys and subdataframes as values
    dizionario_df = dict((i, dataframe[dataframe[column] == i]) for i in list(dataframe[column].unique()))
    ### Then open the ExcelWriter
    with pd.ExcelWriter(filename) as file:
        # Then iterate over items, sheet will be the sheet name and df will be the sheet content
        for (sheet, df) in dizionario_df.items():
            df.to_excel(file, index = False, sheet_name = re.sub(r"[^a-zA-Z0-9'\s\-]",r'',sheet)[0:30])
        file.close()

comuni_italiani = pd.read_excel("C://Users//Utente//Downloads//Elenco-comuni-italiani (1).xls")   

excel_sheet_based_on_column_values(comuni_italiani, 'Denominazione regione', "C://Users//Utente//Desktop//regions_sheets.xlsx")
