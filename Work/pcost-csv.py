# pcost.py
#
# Exercise 1.27

import csv

totalcost = 0

with open('Data/portfolio.csv', 'rt') as file:              # Open the file for reading
    rows = csv.reader(file)                                 # Use the csv module to read the file 
    header = next(rows)                                     # Get rid of the first header line 
    for row in rows:                                        # Parse through the rest of the file, one line at a time
        #line = line.rstrip('\n')                           # Strip out the new line chars - NO LONGER REQUIRED - csv module takes care of this 
        #plist = line.split(',')                            # Split each line of text into a list - NO LONGER REQUIRED - csv module takes care of this
        cost = int(row[1]) * float(row[2])                  # Work out the cost the shares for each company (number of shares x's the cost per share)
        totalcost = totalcost + cost                        # Increment the cost of each company's shares to a running total cost
        #print(f'{cost:0.2f}')
        #print(f'{totalcost:0.2f}')

print(f'Total cost of all shares in the portfolio : {totalcost:0.2f}')      # Report the total cost
