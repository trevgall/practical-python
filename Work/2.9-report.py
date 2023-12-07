# report.py
#
# Exercise 2.9 - report updated with formatted table output 

import csv 

def read_portfolio_list(filename): 
    '''Function to read in the contents of a portfolio file into a list of tuples.'''

    portfolio_list = []                                         # Initialize an empty list variable 

    with open(filename, 'rt') as file:                          # Open the file for reading
        rows = csv.reader(file)                                 # Use the csv module to read the file 
        header = next(rows)                                     # Get rid of the first header line 
        for row in rows:                                        # Parse through the rest of the file, one line at a time
            holding = (row[0], int(row[1]), float(row[2]))      # Each row becomes a tuple called holding 
            portfolio_list.append(holding)                      # And the holding tuple gets appended to the portfolio list

    return portfolio_list                                       # Return the list of tuples 

def read_portfolio_dict(filename): 
    '''Function to read in the contents of a portfolio file into a dictionary.'''

    portfolio_dict = []                                         # Initialize an empty list variable 

    with open(filename, 'rt') as file:
        rows = csv.reader(file)                                 # Use the csv module to read the file 
        header = next(rows)                                     # Get rid of the first header line 
        for row in rows:                                        # Parse through the rest of the file, one line at a time
            stock = {                                           # Create a holding dictionary data structure & assign values to keys
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio_dict.append(stock)                        # Append the dictionary to the list 

    return portfolio_dict                                       # Return the list of dictionary's 

def read_prices(filename):
    '''Function to read a file of key, value pairs and create a data dictionary.'''

    prices = {}                                                 # Initialize an empty dictionary variable 
    with open(filename) as file:                                # Open the file for reading 
        rows = csv.reader(file)                                 # Use the csv module to read the file 
        for row in rows:                                        # Parse through the file one line at a time
            try:
                prices[row[0]] = float(row[1])                  # Populate the dictionary with key value pairs 
            except IndexError:
                pass                                            # Catch any empty lines in the input file 

    return prices                                               # return the populated dictionary of names & price values  

def make_report(portfolio, prices): 
    '''Function to present portfolio stock, number of shares, current prices and loss/gain.'''

    report = []                                                 # Create the empty report list variable 
    print(f'\nPortfolio report : \n')                           # Give the report a title 
    headers = ('Name', 'Shares', 'Price $', 'Change $')         # Give the report table some headers 
    print('%10s %10s %10s %10s' % headers)                      # Print the headers out with formatting 
    print(('-' * 10 + ' ') * len(headers))                      # Print out a separator line 
    for stock in portfolio:                                     # Parse through the portfolio list 
        current_price = prices[stock['name']]                   # Get an update price for the stock from the latest prices dict
        change = current_price - stock['price']                 # Work out what the change in price is 
        # report_price = ('$' + str(current_price))             # Add a $ symbol to the output and convert the current_price to a string ... 
        # update = (stock['name'], stock['shares'], report_price, change)    # ... to allow the string concatination
        update = (stock['name'], stock['shares'], current_price, change)     # Build the report line for the stock 
        report.append(update)                                   # Append the line to the report 
    for row in report: 
        print('%10s %10d %10s %10.2f' % row)                    # Print out the report with formatting 
    return report                                               # Return the completed report 


# Run as list of tuples 
# print(f'\nRead portfolio file into list of tuples to calculate worth... \n')
# portfolio_l = read_portfolio_list('Data/portfolio.csv')
# #print(portfolio_l)
# total = 0.0
# for name, shares, prices in portfolio_l:
#     total += shares*prices
# #print('-- Actual list contents ... ', portfolio_l)
# #print('-- Portfolio total cost was £', total)


# Run as dictionary 
# print(f'\nRead portfolio file into list... \n')
portfolio_d = read_portfolio_dict('Data/portfolio.csv')
# print(portfolio_d)
# total = 0.0
# for stock in portfolio_d:
#     total += stock['shares']*stock['price']
# print('-- Actual list contents ... ', portfolio_d)
# print('-- Portfolio total cost was £', total)


# Read a list of prices into a dictionary 
# print(f'\nRead a csv file of latest price information into a dictionary... \n')
latest_prices = read_prices('Data/prices.csv')
# print('-- Actual dictionary contents ... ', latest_prices)

# Calculate the portfolio gain or loss and report 
# -- here we need a running total of the value of each stock, multiplying the number of shares by the latest_prices value 
# current_value = 0.0
# for stock in portfolio_d:
#     current_value += stock['shares']*latest_prices[stock['name']]

# print(f'\nReporting portfolio gain / loss :')
# print(f'-- Cost of portfolio at purchase £ {total:>10.2f}')
# print(f'-- Actual value of the portfolio today £ {current_value:>10.2f}')

# if current_value > total: 
#     print(f'-- Portfolio gain = £ {current_value - total:>10.2f}')
# else:
#     print(f'-- Portfolio loss = £ {current_value - total:>10.2f}')

# Generate report 
report_list = make_report(portfolio_d, latest_prices)
# print(report_list)