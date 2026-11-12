# Given Variables 

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

# Convert names to .lower() case 
print("Names in lowercase:")

print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

#Use .title() to convert names to title case

print("\nNames in title case:")

print(name_1.title())
print(name_2.title())
print(name_3.title())

#Use .replace() to remove dollar signs

salary_1_clean = salary_1.replace("$", "")
salary_2_clean = salary_2.replace("$", "")

print("\nSalaries without dollar signs:")

print(salary_1_clean)
print(salary_2_clean)

# Check the data types

print(type(salary_1_clean))
print(type(salary_2_clean))

# They are still strings.
# To perform math, we need to convert them into integers.


# Remove dollar signs and commas,
# then convert salary_1 into an integer

salary_1_int = int(salary_1.replace("$", "").replace(",", ""))

print("\nSalary 1 as an integer:")
print(type(salary_1_int))