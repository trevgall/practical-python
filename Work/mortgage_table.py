# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
# extra_payment = 1000
# extra_payment_start_month = 1
# extra_payment_stop_month = 13

print('Welcome to the mortgage calculator... ')

extra_payment = input('What should your extra payment be set at? ')
extra_payment_start_month = input('Which month would you like to start paying extra? ')
extra_payment_stop_month = input('Which month would you like to stop paying extra? ')

while principal > 0:
    if month > int(extra_payment_start_month) and month < int(extra_payment_stop_month): 
        month = month + 1
        principal = principal * (1+rate/12) - (payment + int(extra_payment))
        total_paid = total_paid + payment + int(extra_payment)
        print(month, round(total_paid, 2), round(principal, 2))
    else: 
        month = month + 1
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        print(month, round(total_paid, 2), round(principal, 2))

#print('Total paid', round(total_paid, 2))
t_summary = f'Total paid : ${total_paid:0.2f}'
print(t_summary)
print('Total number of months : ', month)
