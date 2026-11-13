# Descritption : This script tests various numeric 
#                Conversion techniques 
# Author : Sam Q. Newprogrammer 

a = "   101.1 "
b= '55'
c = "402 Stevens"
d = 'Number 5  '

# Convery to float
a_float =float(a)
#print(a_float)

# Variable b
b_int = int(b)
b_float = float(b)
#print(b_int)

#Variable c 
#c_int = int(c)
# Error: ValueError because c contains letters

#Variable d 
# d_float = float(d)
# Error: ValueError because d contains letters.

# Using Slicing 

a_number = float(a[1:6])
b_number = int(b[0:2])
c_number = int(c[0:3])
d_number = int(d[7:8])

# Use strip() to remove extra spaces 
print("Removing spaces using strip():")
print(a.strip())
print(d.strip())


# Print original variables and their data types
print("\nOriginal variables and their types:")

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))


# Print the new variables and their types
print("\nNew variables and their types:")

print(a_float, type(a_float))
print(b_int, type(b_int))
print(b_float, type(b_float))
print(a_new, type(a_new))

print(a_number, type(a_number))
print(b_number, type(b_number))
print(c_number, type(c_number))
print(d_number, type(d_number))