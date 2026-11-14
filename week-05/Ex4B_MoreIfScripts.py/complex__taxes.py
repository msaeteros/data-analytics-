pay_rate =eval(input('Enter your pay rate per hour : '))
hours_worked = eval(input('Enter the number of hours worked: '))

if hours_worked > 40 : 
    regular_pay = 40 * pay_rate
    overtime = hours_worked - 40 #Calcuate overtime hours 
    overtime_pay = overtime * (pay_rate * 1.5) # calcuate overtime pay 
    gross_pay = regular_pay + overtime_pay # gross pay 
else :
    gross_pay = hours_worked * pay_rate

annual_gross_pay = gross_pay * 52 

filing_status = input('Enter your filing status (single or joint)')

if filing_status == 'single':
    if annual_gross_pay < 12000:
        tax_rate = 0.05
    elif annual_gross_pay < 25000:
        tax_rate = 0.10
    elif annual_gross_pay < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filing_status == 'joint':
    if annual_gross_pay  < 12000:
        tax_rate = 0
    elif annual_gross_pay < 25000:
        tax_rate = 0.06
    elif annual_gross_pay < 75000:
        tax_rate = 0.11
    else:
        tax_rate =0.20


if tax_rate is not None:

    tax_withholding = gross_pay * tax_rate

    net_pay = gross_pay - tax_withholding


    print(f'You worked {hours_worked} hours this period.')
    print(f'Because you earn ${pay_rate:,.2f} per hour, your gross weekly pay is ${gross_pay:,.2f}')
    print(f'Your filing status is {filing_status}')
    print(f'Your tax withholding for the week is ${tax_withholding:,.2f}')
    print(f'Your net pay is ${net_pay:,.2f}')







