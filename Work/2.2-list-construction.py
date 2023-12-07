# 2.2-list-construction.py

records = []                                                   # Initialize an empty list

print('A list of tuples : ')
with open('Data/portfolio.csv', 'rt') as f:                    # Open the file for reading 
    next(f)                                                    # Skip the header 
    for line in f: 
        #print(line)                                           # Debug - so we can see the line before it's split
        row = line.split(',')                                  # Split each line of text into a list
        records.append((row[0], int(row[1]), float(row[2])))   # Append each tuple to the empty list 
    
    print(records)