# NYC 311 Service Requests Analysis

## How to Run

1. Make sure you have Python 3 installed.
2. Navigate to this folder in your terminal.
3. Run the script:

python3 analysis.py

Output will be saved to `output.txt`. The console will confirm when the file has been written.

## What This Script Does

This script reads NYC 311 request data and writes a statistic summary through the `output.txt` file. The list is as follows:

- Amount of open requests through all boroughs
- Most common complaint type through all boroughs
- Amount of total requests per borough
- Amount of requests per complaint type
- Borough with most open requests and amount of requests
- Closure rate of requests by borough, sorted alphabetically
- Top 3 boroughs by total requests, sorted alphabetically

This script utilizes dictionaries as frequency counters for counting complaint types, amount of open requests, etc. Some data is written to the `output.txt` file through a loop from previous dictionaries.

## Dependencies

This script uses only Python's built-in libraries: `csv`.

## Notes

[Optional: anything you want to flag about your approach or assumptions.]
