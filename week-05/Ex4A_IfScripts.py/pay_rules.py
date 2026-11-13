# Variables 

pay_rate =eval(input('Enter your pay rate per hour : '))
hours_worked = eval(input('Enter the number of hours worked: '))

if hours_worked > 40 : 
    regular_pay = 40 * pay_rate
    overtime = hours_worked - 40 #Calcuate overtime hours 
    overtime_pay = overtime * (pay_rate * 1.5) # calcuate overtime pay 
    gross_pay = regular_pay + overtime_pay # gross pay 
else :
    gross_pay = hours_worked * pay_rate

print (f'Gross pay: $ {gross_pay:,.2f}')