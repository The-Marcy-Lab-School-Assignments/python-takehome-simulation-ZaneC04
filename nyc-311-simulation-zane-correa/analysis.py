import csv

rows = []

with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

open_requests = 0
complaint_counter = {}
borough_counter = {}
sorted_complaints = {}
borough_complaints = {}
closure_rates = {}

for row in rows: # count how many times "Open" shows up
    if row['resolution_status'] == 'Open':
        open_requests += 1


for row in rows: # frequency counter for complaint type and number of complaints
    if row['complaint_type'] in complaint_counter:  
        complaint_counter[row['complaint_type']] += 1
    else:
        complaint_counter[row['complaint_type']] = 1

for key in sorted(complaint_counter, key=complaint_counter.get, reverse=True): # sorts complaint types by value descending
    sorted_complaints[key] = complaint_counter[key]



common_complaint = max(complaint_counter, key=complaint_counter.get) # key of highest frequency

for row in rows: # frequency counter for borough and amount of complaints (times it shows up in rows)
    if row['borough'] in borough_counter:
        borough_counter[row['borough']] += 1
    else:
        borough_counter[row['borough']] = 1

for row in rows: # frequency counter, increments if resolution status is open 
    if row['borough'] in borough_complaints and row['resolution_status'] == 'Open':
        borough_complaints[row['borough']] += 1 
    elif row['borough'] not in borough_complaints and row['resolution_status'] == 'Open':
        borough_complaints[row['borough']] = 1

max_complaints_borough = max(borough_complaints, key=borough_complaints.get) # gets borough with most open requests

for key in borough_counter: # calculates percentage from total of complaints from borough_counter and amount of open complaints from borough_complaints
    closure_rates[key] = round((borough_counter[key] - borough_complaints[key]) / borough_counter[key] * 100, 1)

closure_rates = dict(sorted(closure_rates.items())) # sorts percentages alphabetically

borough_counter = dict(sorted(borough_counter.items())) # sorts total requests alphabetically

sorted_borough_counter = {} # sorts total requests by amount descending
for key in sorted(borough_counter, key=borough_counter.get, reverse=True):
    sorted_borough_counter[key] = borough_counter[key]



with open('output.txt', 'w') as f:
    f.write(f'Open requests: {open_requests}\n\n')
    f.write(f'Most common complaint type: {common_complaint} ({complaint_counter[common_complaint]} requests)\n\n')
    f.write(f'Requests per borough:\n- Bronx: {borough_counter['Bronx']}\n- Brooklyn: {borough_counter['Brooklyn']}\n- Manhattan: {borough_counter['Manhattan']}\n- Queens: {borough_counter['Queens']}\n- Staten Island: {borough_counter['Staten Island']}\n\n')
    f.write('Requests by complaint type:\n')
    for key in sorted_complaints:
        f.write(f'- {key}: {sorted_complaints[key]}\n')
    f.write(f'\nBorough with most open requests: {max_complaints_borough} ({borough_complaints[max_complaints_borough]} open)\n\n')
    f.write(f'Closure rate by borough:\n')
    for key in closure_rates:
        f.write(f'- {key}: {closure_rates[key]}%\n')
    f.write(f'\nTop 3 boroughs by total requests:\n')
    for i, key in enumerate(sorted_borough_counter):
        if i == 3:
            break
        f.write(f'{i+1}. {key} ({sorted_borough_counter[key]} requests)\n')



print('Output saved to output.txt')