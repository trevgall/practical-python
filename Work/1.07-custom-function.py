# 1.7-customo-function.py 

def sumcount(n): 
    '''
    Returns the sum of the first n integers
    '''
    total = 0 
    while n > 0:
        total += n
        n -= 1
    return total 

value = input('Which integer would you like to sum? ')
a = sumcount(int(value))
print(a)