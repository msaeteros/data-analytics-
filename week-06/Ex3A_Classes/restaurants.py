class Restaurant:
    def __init__(self,rest_name, food_type):
        """Store restaurant name and the food type"""
        self.res_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}.')
        

    def rest_open(self):
        print(f'{self.rest_name} is open')

restaurant1 = Restaurant('Duck', 'dounts' )
restaurant2 = Restaurant('Dondald Farm', 'burgers')
restaurant3 = Restaurant('Terminal','Pasta')

restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()



    
