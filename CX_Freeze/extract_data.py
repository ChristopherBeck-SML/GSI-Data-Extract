import os
import pandas as pd

def export_to_excel(dataframes, filenames):
    writer = pd.ExcelWriter('temp.xlsx', engine='openpyxl')
    for i, (df, filename) in enumerate(zip(dataframes, filenames)):
        # Write the DataFrame to the Excel file, including the index
        df.to_excel(writer, sheet_name=f'{filename}', index=True, startrow=1)

        # Write the column headers to the worksheet
        workbook = writer.book
        worksheet = writer.sheets[f'{filename}']

    writer.save()

    # Open Excel file
    if os.name == 'nt':  # Windows
        os.startfile('temp.xlsx')
    elif os.name == 'posix':  # Linux, macOS
        os.system('open temp.xlsx')

folder_path = "GSI Data"
output_folder = "Extracted Data"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

dataframes = []
filenames = []
for filename in os.listdir(folder_path):
    if filename.endswith('.GSI'):
        input_file = os.path.join(folder_path, filename)
        output_file = os.path.join(output_folder, filename[:-4] + '.txt')

        with open(input_file, 'r') as file:
            data = {}
            for line in file:
                if line.startswith('Stakeout:'):
                    stakeout_id = line.split()[1]
                    if stakeout_id not in data:
                        data[stakeout_id] = {'x': [], 'y': [], 'z': []}
                elif line.startswith('STAKED STKER') and stakeout_id and stakeout_id.startswith('R'):
                    values = line.split()
                    x, y, z = float(values[2][2:]), float(values[3][2:]), float(values[4][2:])
                    data[stakeout_id]['x'].append(x)
                    data[stakeout_id]['y'].append(y)
                    data[stakeout_id]['z'].append(z)

        data_avg = []
        for stakeout_id, values in data.items():
            x_list, y_list, z_list = values['x'], values['y'], values['z']
            if x_list and y_list and z_list:
                x_avg = round(sum(x_list) / len(x_list), 3)
                y_avg = round(sum(y_list) / len(y_list), 3)
                z_avg = round(sum(z_list) / len(z_list), 3)
                # Convert stakeout ID to integer for sorting
                if stakeout_id.startswith('R'):
                    stakeout_id = int(stakeout_id[1:])
                data_avg.append({'Point': stakeout_id, 'X': x_avg, 'Y': y_avg, 'Z': z_avg})

        data_avg.sort(key=lambda x: x['Point'])  # Sort the data_avg list based on 'Point' key
        df = pd.DataFrame(data_avg).set_index('Point')
        dataframes.append(df)
        filenames.append(filename[:-4])

if dataframes:
    # Call export_to_excel function to export the dataframes to Excel
    export_to_excel(dataframes, filenames)
