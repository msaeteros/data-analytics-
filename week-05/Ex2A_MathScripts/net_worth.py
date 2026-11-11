# Net Woth Calculator 

#Assets 
checking_account = 3000
Savings_account = 6000
investments = 10000

#Debt 
Car_loan = 2000
Credit_Card_debt = 1000

#Calcuate Total Assets 
total_assets = checking_account + Savings_account + investments 

#Total Debts
Total_debts = Car_loan + Credit_Card_debt

# Net Worth 
net_worth = total_assets - Total_debts

print(f'Total assets: $ {total_assets:,.2f}')
print(f'Total debts: $ {Total_debts:,.2f}')
print(f'Net Worth: $ {net_worth:,.2f}')
