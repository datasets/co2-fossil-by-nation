import csv
import requests
import openpyxl

from operator import itemgetter

source = "https://rieee.appstate.edu/wp-content/uploads/2024/07/nation.1751_2020.xlsx"
in_path = 'cache/fossil-fuel-co2-emissions-by-nation.xlsx'
out_path = 'data/fossil-fuel-co2-emissions-by-nation.csv'

header = ['Year', 'Country', 'Total', 'Solid Fuel', 'Liquid Fuel',
            'Gas Fuel', 'Cement', 'Gas Flaring', 'Per Capita', 'Bunker fuels (Not in Total)']

def process():
    # get data
    response = requests.get(source)
    open(in_path, 'wb').write(response.content)

    wb = openpyxl.load_workbook(in_path)
    wb = wb.active
    
    records = []

    for index, row in enumerate(wb.iter_rows(values_only=True)):
        if index == 0:  
            continue
        if row[0] is None: 
            continue
        records.append([row[1], row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])
        
    records = sorted(records, key=itemgetter(0))

    # save data
    writer = csv.writer(open(out_path, 'w'), lineterminator='\n')
    writer.writerow(header)
    writer.writerows(records)

if __name__ == '__main__':
    process()