import csv

rows = []

with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

open_requests = 0
complaint_counter = {}
borough_counter = {}

for row in rows: # count how many times "Open" shows up
    if row['resolution_status'] == 'Open':
        open_requests += 1


for row in rows: # frequency counter for complaint type and number of complaints
    if row['complaint_type'] in complaint_counter:  
        complaint_counter[row['complaint_type']] += 1
    else:
        complaint_counter[row['complaint_type']] = 1

common_complaint = max(complaint_counter, key=complaint_counter.get) # key of highest frequency

for row in rows: # frequency counter for borough and amount of complaints (times it shows up in rows)
    if row['borough'] in borough_counter:
        borough_counter[row['borough']] += 1
    else:
        borough_counter[row['borough']] = 1



with open('output.txt', 'w') as f:
    f.write(f'Open requests: {open_requests}\n\n')
    f.write(f'Most common complaint type: {common_complaint} ({complaint_counter[common_complaint]} requests)\n\n')
    f.write(f'Requests per borough:\n- Bronx: {borough_counter['Bronx']}\n- Brooklyn: {borough_counter['Brooklyn']}\n- Manhattan: {borough_counter['Manhattan']}\n- Queens: {borough_counter['Queens']}\n- Staten Island: {borough_counter['Staten Island']}')

print('Output saved to output.txt')