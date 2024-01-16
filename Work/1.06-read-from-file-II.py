# 1.6-read-from-file-II.py

# Format of the input file changed! 
# Original version of this script was working kubectl describe output ... 
# Latest version of /tmp/ingress.list is dump of `kubectl get ingress -A`
# So we need to strip out the empty space chars and convert to csv

import csv 
import re

print('\nRead a file of configured ingresses and list the contents\n')

file = '/tmp/ingress.list'                                  # This a list of configured ingresses in the minikube cluster 
ingressNumber = 1                                           # Simple counter to use during the first iterative print block to number the ingresses 

print('\nFirstly as a dump of all the information provided from a \'kubectl get ingress -A\'...\n')
with open(file, 'rt') as ingressfile:                       # Open the file to read
    #next(ingressfile)                                      # Skip the file header line 
    for line in ingressfile:                                # Parse through the file one line at a time
        line = line.rstrip('\n')                            # Strip off the trailing (\n) new line chars
        print(line)                                         # Print

print()
print('\nSecondly as a csv file containing all the information provided from a \'kubectl get ingress -A\'...\n')
with open(file, 'rt') as ingressfile:                       # Open the file to read
    #next(ingressfile)                                      # Skip the file header line 
    for line in ingressfile:                                # Parse through the file one line at a time
        line = line.rstrip('\n')                            # Strip off the trailing (\n) new line chars
        line = re.sub(r'\s{2,}', ',', line)                 # Use the re.sub function to replace each occurance of 2 or more
                                                            # empty chars with a comma thus creating a csv 
        print(line)                                         # Print

print()
print('\nAnd finally just print out the namespace and the name of the ingress ...\n')
with open(file, 'rt') as ingressfile:                       # Open the file to read
    #next(ingressfile)                                      # Skip the file header line 
    for line in ingressfile:                                # Parse through the file one line at a time
        line = line.rstrip('\n')                            # Strip off the trailing (\n) new line chars
        line = re.sub(r'\s{2,}', ',', line)                 # Use the re.sub function to replace each occurance of 2 or more
                                                            # empty chars with a comma thus creating a csv 
        namespaceIngress = line.split(',')                  # Split each line of text into a list so we can extract particula fields 
        print(f'Namespace : {namespaceIngress[0]:25} Ingress : {namespaceIngress[1]:10}')       # Print each element of the list 


 