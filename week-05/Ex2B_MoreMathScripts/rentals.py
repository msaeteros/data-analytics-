import math 

people = int(input('How many people are going on tour? '))

total_vans = math.ceil(people/ 15) 

van_cost = total_vans * 250 

totalcost_per_person = van_cost / people 

print(f'Vans need {total_vans}.')
print(f'The total cost to rent the is $ {van_cost:.2f}')
print(f'Total cost per person is $ {totalcost_per_person:.2f}')
