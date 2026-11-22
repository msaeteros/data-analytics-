f = open('about_me.txt', 'r')

#print(f.read(50))
#print(f.read(50))

#for i in range(1, 5):
#    print(f.readline())

#print(f.readlines(1))
#print(f.readlines(1))
#print(f.readlines(10))
#print(f.readlines(10))

first_50 = f.read(50)

next_four = []

for i in range(1, 5):
    next_four.append(f.readline())

next_100 = f.readlines(100)

print(f'First 50 characters: {first_50}')

print(f'Next four lines, as list by line: {next_four}')

print(f'Next 100 characters, as list by line, rounded up to complete lines: {next_100}')


f.close()


