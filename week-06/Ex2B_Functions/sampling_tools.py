import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
            'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp',
            'Surge Protector']

# A. Products of the day 

product_of_the_day = random.choice(products)
print(f"Product of the Day: {product_of_the_day}")

# B: Usability survey

survey_products = random.sample(products, 3)
print(f"Survey Products: {survey_products}")

# c: Shuffle all products
random.shuffle(products)
print(f"Randomized Product List: {products}")

# D : Simulate daily transaction count 
transactions = random.randint(50, 300)
print(f"Daily Transactions: {transactions}")