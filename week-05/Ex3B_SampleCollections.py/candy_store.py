candy_types = ('Lollipops', 'Gum', 'Gummies')

fruit_flavors = ('Mango', 'Apple', 'Orange',)

candy_combinations = set()

candy_combinations.add(candy_types[0] + " - " + fruit_flavors[2])
candy_combinations.add(candy_types[1] + " - " + fruit_flavors[0])
candy_combinations.add(candy_types[2] + " - " + fruit_flavors[1])

print("Candy options include:")
print(candy_combinations)