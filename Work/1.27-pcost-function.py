# pcost.py
#
# Exercise 1.27

import sys                                                  # Import sys module to check number of command line arguments passed - see line #22

def portfolio_cost(filename):                               # Define a function to calculate the total cost of the shares 
    totalcost = 0                                           # Initialise the totalcost variable
    with open(filename, 'rt') as file:                      # Open the file for reading
      header = next(file).split(',')                        # Get rid of the first header line 
      for line in file:                                     # Parse through the rest of the file, one line at a time
        line = line.rstrip('\n')                            # Strip out the new line chars 
        plist = line.split(',')                             # Split each line of text into a list 
        #print(plist)                                       # Debug print - initially had return within the for loop - doh!
        try:                                                # Adding error handling ... see line #15
          cost = int(plist[1]) * float(plist[2])            # Work out the cost the shares for each company (number of shares x's the cost per share)
        except ValueError:
          print('could not convert string to float:', line) # Report the exception, and carry on processing the file ... 
        totalcost = totalcost + cost                        # Increment the cost of each company's shares to a running total cost
    return(totalcost)                                       # Return the total cost of the shares 

if len(sys.argv) == 2:                                      # Check the number of arguments 
    filename = sys.argv[1]                                  # Allows users to pass the file to be parsed at the command line
else:
    filename = 'Data/portfolio.csv'                         # In case no alternative filename is passed, default 

share_cost = portfolio_cost(filename)
print(f'Total cost of all shares in the portfolio : {share_cost:0.2f}')      # Report the total cost
