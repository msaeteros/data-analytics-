#Assign variables 

a = 22
b = 3
c = 8

# find smallest number 
if a < 5 and a < c :
    smallest = a 
elif b < a and b < c:
    smallest = b 
else:
    smallest = c 

#find largest number

if a > b and a > c:
    largest = a

elif b > a and b > c:
    largest = b

else:
    largest = c

print(f'The samllest number is {smallest}')
print(f'The largest number is {largest}')