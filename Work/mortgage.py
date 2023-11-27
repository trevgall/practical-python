# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
additional = 1000

while principal > 0:
    if month < 13: 
        month = month + 1
        principal = principal * (1+rate/12) - (payment + additional)
        total_paid = total_paid + payment + additional
    else: 
        month = month + 1
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

print('Total paid', round(total_paid, 2))
print('Total number of months: ', month)
