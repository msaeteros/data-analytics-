# Example values
current_savings = 1000
interest_rate = 6

# Calculate the number of years
years = 72 / interest_rate

# Calculate doubled savings
doubled_balance = current_savings * 2

# Display the results
print(f"Your current savings is {format(current_savings, '.2f')}.")

print(f"At a {format(interest_rate / 100, '.0%')} interest rate, your savings account will be worth {format(doubled_balance, '.2f')} in {format(years, '.1f')} years")
