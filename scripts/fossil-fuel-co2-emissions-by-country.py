import csv
#import os
import urllib
#import dataconverters.xls
from operator import itemgetter
# first run the extract
# os.system('. scripts/constituents.sh')
source = "http://cdiac.ornl.gov/ftp/ndp030/CSV-FILES/nation.1751_2011.csv?force_download=true"
in_path = 'cache/fossil-fuel-co2-emissions-by-nation.csv'
out_path = 'data/fossil-fuel-co2-emissions-by-nation.csv'
def execute():
    urllib.urlretrieve(source, in_path)

    with open(in_path) as f:
        reader = csv.reader(f)
        records = list(reader)

    #header = records[0]
    #header[0], header[1] = header[1], header[0]
    header = ['Year', 'Country', 'Total', 'Solid Fuel', 'Liquid Fuel',
            'Gas Fuel', 'Cement', 'Gas Flaring', 'Per Capita', 'Bunker fuels (Not in Total)']
    records = records[3:]
    for i in records:
        i[0],i[1] = i[1],i[0]
    records = sorted(records, key=itemgetter(0))
    #header = ['Date', 'Price (Dollars per million btu)']
    # data begins on row 4
    #records = records[3:]

    #header = [ [ fixsymbol(x[1]) ] for x in header ]

    writer = csv.writer(open(out_path, 'w'), lineterminator='\n')
    writer.writerow(header)
    writer.writerows(records)


execute()
