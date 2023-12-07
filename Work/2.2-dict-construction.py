# 2.2-dict-construction.py

prices = {}                                                   # Initialize an empty dictionary

print('Populate a dictionary from the contents of a file. \n')
with open('Data/prices.csv', 'rt') as f:                       # Open the file for reading 
    for line in f: 
        #print(line)                                           # Debug - so we can see the line before it's split
        row = line.split(',')                                  # Split each line of text into a list
        #print(row)                                            # Debug print 
        try:
            prices[row[0]] = float(row[1])              
        except IndexError: 
            print('List index out of range... encountered an empty line.')

    print('Printing the contents of the dictionary...')
    print(prices)