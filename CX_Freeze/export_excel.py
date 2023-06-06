import os
import pandas as pd
from subprocess import call

def export_to_excel(dataframes):
    writer = pd.ExcelWriter('temp.xlsx', engine='openpyxl')
    for i, df in enumerate(dataframes):
        # Add the stakeout ID as the first column


        # Write the DataFrame to the Excel file, including the index
        df.to_excel(writer, sheet_name=f'Sheet {i+1}', index=True, startrow=1)

        # Write the column headers to the worksheet
        workbook = writer.book
        worksheet = writer.sheets[f'Sheet {i+1}']
        worksheet.cell(row=1, column=1, value='Point')
        worksheet.cell(row=1, column=2, value='X')
        worksheet.cell(row=1, column=3, value='Y')
        worksheet.cell(row=1, column=4, value='Z')

    writer.save()

    # Open Excel file
    if os.name == 'nt':  # Windows
        os.startfile('temp.xlsx')
    elif os.name == 'posix':  # Linux, macOS
        subprocess.call(('open', 'temp.xlsx'))
