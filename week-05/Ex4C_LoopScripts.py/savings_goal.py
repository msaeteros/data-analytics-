bank_balance = 100
savings_goal = 1000
weekly_savings = 100

while bank_balance < savings_goal:
    bank_balance += weekly_savings

    if bank_balance >= savings_goal * 0.75:
        treat = 20
        bank_balance -= treat
        print(f"So close! After treating myself, my balance is up to ${bank_balance}.")

    elif bank_balance > savings_goal * 0.50:
        print(f"Almost there! This week my balance is up to ${bank_balance}.")

    else:
        print(f"This week my balance increased to ${bank_balance}.")

print(f"Goal met! My current balance is ${bank_balance}.")