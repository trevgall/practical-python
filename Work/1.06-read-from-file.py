# 1.6-read-from-file.py

print('\nRead a file of configured ingresses and list the contents\n')

file = '/tmp/ingress.list'                                  # This a list of configured ingresses in the minikube cluster 
ingressNumber = 1                                           # Simple counter to use during the first iterative print block to number the ingresses 

print('\nFirst using a counter variable that increments as each line is read...')
with open(file, 'rt') as ingressfile:                       # Open the file to read
    for line in ingressfile:                                # Parse through the file one line at a time
        line = line.rstrip('\n')                            # Strip off the trailing (\n) new line chars
        print('Ingress', ingressNumber, '-', line)          # Print the ingress count and the line (here the whole line is just a text string)
        ingressNumber += 1                                  # Increment the counter 

# A quicker way to do the same line parsing but using enumerate to count the line numbers 
print('\n... and now using the enumerate function to increment a variable as each line is read...')
with open(file, 'rt') as ingressfile:                       # Open the file to read
    for lineno, line in enumerate(ingressfile, start=1):    # Parse through the file one line at a time, 
                                                            # and use the enumerate function to keep track of the line number, 
                                                            # assigning the line number to the variable lineno
        line = line.rstrip('\n')                            # Strip off the trailing (\n) new line chars
        print('Ingress', lineno, '-', line)                 # Print the lineno and the line (here the whole line is just a text string)
    
print('\nNow try to list the individual namespace and associated ingress... \n')
with open(file, 'rt') as ingressfile:                       # Open the file to read
    for line in ingressfile:                                # Parse through the file one line at a time
        line = line.rstrip('\n')                            # Strip off the trailing (\n) new line chars
        namespaceIngress = line.split(' ')                  # Split each line of text into a list 
        print(f'Namespace : {namespaceIngress[0]:25} Ingress : {namespaceIngress[1]:10}')       # Print each element of the list 
                                                                                                # (notice the f-string formatting to beautify the output)

