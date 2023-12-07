# pcost-gzip.py
#
# Exercise 1.27 - modified to work with a gzip compressed archive file 

import gzip 

totalcost = 0

with gzip.open('Data/portfolio.csv.gz', 'rt') as file:      # Open the gzip file for reading
    header = next(file).split(',')                          # Get rid of the first header line 
    for line in file:                                       # Parse through the rest of the file, one line at a time
        line = line.rstrip('\n')                            # Strip out the new line chars 
        plist = line.split(',')                             # Split each line of text into a list 
        cost = float(plist[1]) * float(plist[2])            # Work out the cost the shares for each company (number of shares x's the cost per share)
        totalcost = totalcost + cost                        # Increment the cost of each company's shares to a running total cost
    #    print(f'{cost:0.2f}')
    #    print(f'{totalcost:0.2f}')

print(f'Total cost of all shares in the portfolio : {totalcost:0.2f}')      # Report the total cost
