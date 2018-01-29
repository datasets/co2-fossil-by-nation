import csv
import urllib
from operator import itemgetter

source = "http://cdiac.ornl.gov/ftp/ndp030/CSV-FILES/nation.1751_2014.csv?force_download=true"
in_path = 'cache/fossil-fuel-co2-emissions-by-nation.csv'
out_path = 'data/fossil-fuel-co2-emissions-by-nation.csv'

# get data
urllib.urlretrieve(source, in_path)
with open(in_path) as f:
    reader = csv.reader(f)
    records = list(reader)

# process data
header = ['Year', 'Country', 'Total', 'Solid Fuel', 'Liquid Fuel',
          'Gas Fuel', 'Cement', 'Gas Flaring', 'Per Capita', 'Bunker fuels (Not in Total)']
records = records[4:]
for i in records:
    i[0], i[1] = i[1], i[0]
records = sorted(records, key=itemgetter(0))

# save data
writer = csv.writer(open(out_path, 'w'), lineterminator='\n')
writer.writerow(header)
writer.writerows(records)
