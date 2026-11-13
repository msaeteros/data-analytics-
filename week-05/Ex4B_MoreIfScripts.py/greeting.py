Current_hour= int(input('Enter the current hour (0-23): '))

if Current_hour < 4 or Current_hour >= 23:
    print('What are you doing up so late??')
elif Current_hour <= 10 :
    print('Good morning!')
elif Current_hour < 17:
    print("Good day!")
else:
    print("Good evening!")