import random 
import math 
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

# Displays statistics for the 75 values

print(f'Sum of 75 sample values from 1 to 100: {sum(vals_sample)}')
print(f'Average of 75 sample values: {statistics.mean(vals_sample):,.2f}')
print(f'Median of 75 samples values: {statistics.median(vals_sample)}')

# Display statisitcs for 200 values 

print(f'Average of 200 values: {statistics.mean(vals_choices)}')
print(f'Median of 200 values: {statistics.median(vals_choices)}')
print(f'Mode of 200 values: {statistics.mode(vals_choices)}')
print(f'Standard deviation of 200 values: {statistics.stdev(vals_choices):,.2f}')
print(f'Variance of 200 values: {statistics.variance(vals_choices):,.2f}')

# Modeling a random circle
area = pi * radius **2 

area_up = math.ceil(area)
area_down = math.floor(area)

# Display are calcualtions 
print(f'Radius = {radius}, area = {area_up}')
print(f'Radius = {radius}, area = {area_down}')