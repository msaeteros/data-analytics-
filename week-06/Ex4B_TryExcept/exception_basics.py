# Marilyn Saeteros
# 11/20/2026
# Expections Handling


# ValueError
try:
    age = int("banana")

except ValueError:
    print("ValueError: You entered an invalid value.")

else:
    print(age)

finally:
    print("Let's try another one...")


# NameError
try:
    m = banana

except NameError:
    print("NameError: Oops, looks like you tried to assign an undefined object to a variable.")

else:
    print(m)

finally:
    print("Let's try another one...")

# TypeError 
try:
    result = "Hello" + 5

except TypeError:
    print("TypeError: You cannot combine a string and an integer.")

else:
    print(result)

finally:
    print("Let's try another one...")

#SynatxError 

try:
    compile("print('Hello'", "<string>", "exec")

except SyntaxError:
    print("SyntaxError: You have an error in your Python syntax.")

else:
    print("Your code has correct syntax.")

finally:
    print("Let's try another one...")