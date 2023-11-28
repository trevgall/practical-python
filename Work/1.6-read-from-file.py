# 1.6-read-from-file.py

print('Read a file of configured ingresses and list the contents')

file = '/tmp/ingress.list'                                  # This a list of configured ingresses in the minikube cluster 
ingressNumber = 1                                           # Simple counter to use during the first iterative print block to number the ingresses 

with open(file, 'rt') as ingressfile:                       # Open the file to read
    for line in ingressfile:                                # Parse through the file one line at a time
        print('Ingress', ingressNumber, '-', line)          # Print the ingress count and the line (here the whole line is just a text string)
        ingressNumber += 1                                  # Increment the counter 
    
print('\nNow try to list the individual namespace and associated ingress... \n')
with open(file, 'rt') as ingressfile:                       # Open the file to read
    for line in ingressfile:                                # Parse through the file one line at a time
        line = line.rstrip('\n')                            # Strip off the trailing (\n) new line chars
        namespaceIngress = line.split(' ')                  # Split the text into a list 
        print(f'Namespace : {namespaceIngress[0]:25} Ingress : {namespaceIngress[1]:10}')       # Print each element of the list 
                                                                                                # (notice the f-string formatting to beautify the output)

