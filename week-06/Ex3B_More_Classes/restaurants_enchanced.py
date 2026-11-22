class Restaurant:
    def __init__(self,rest_name, food_type):
        """Store restaurant name and the food type"""
        self.rest_name = rest_name
        self.food_type = food_type
        self.num_served  = 0
        self.customer_rating = []

    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}.')
        

    def rest_open(self):
        print(f'{self.rest_name} is open')

def add_num_served(self):
    served = int(input('How many customers served today? '))
    self.number_served += served  

def print_num_served(self):
    print(f'{self.rest_name} has served {self.number_served}')

def customer_rating(self):
    while True:
        rating = input(
            "How would you rate your experience today on a scale of 1-5 (5 being excellent)"
        )
       
        try: 
            rating = int(rating)

            if 1 <= rating <= 5:
                self.customer_ratings.append(rating)

                average = sum(self.customer_ratings) / len(self.customer_ratings)

                print(f'Your rating was {rating}. The average rating for this restaurant is {average:.2f}')
                break

            else:
                print('Please enter a rating between 1 and 5.')

        except ValueError:
                print('Invalid input. Please enter a whole number from 1-5.')



restaurant1 = Restaurant('Duck', 'dounts' )
restaurant2 = Restaurant('Dondald Farm', 'burgers')
restaurant3 = Restaurant('Terminal','Pasta')

restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()

# Test number of customers served

restaurant1.print_num_served()
restaurant1.add_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()

restaurant2.print_num_served()
restaurant2.add_num_served()
restaurant2.print_num_served()

restaurant3.print_num_served()
restaurant3.add_num_served()
restaurant3.print_num_served()


# Test customer ratings

restaurant1.customer_rating()
restaurant1.customer_rating()
restaurant1.customer_rating()

restaurant2.customer_rating()
restaurant2.customer_rating()
restaurant2.customer_rating()

restaurant3.customer_rating()
restaurant3.customer_rating()
restaurant3.customer_rating()
