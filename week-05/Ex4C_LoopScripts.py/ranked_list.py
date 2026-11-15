favorite_foods = ["pizza", "sushi", "pasta", "ramen", "chicken wings"]

print("My Favorite Foods:")

for index, food in enumerate(favorite_foods, start=1):
    if index == 1:
        print(f"{index}. {food} <- top pick!")
    else:
        print(f"{index}. {food}")