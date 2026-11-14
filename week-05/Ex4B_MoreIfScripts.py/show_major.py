#Assign Variables

student_name = input('Enter your name : ')
student_major = input('Enter your major code: ')

if student_major == 'BIOL' :
    major_name ='Biology' 
    Department_Office =' Science Bldge, Room 310 '
    print (f'{student_name} majors in {major_name} located in {Department_Office}')
elif student_major == 'CSCI':
    major_name = 'Computer Science'
    Department_Office = 'Sheppard Hall, Room 314'
    print (f'{student_name} majors in {major_name} located in {Department_Office}')
elif student_major == 'ENG':
    major_name = 'English'
    Department_Office = 'Kerr Hall, Room 201'
    print (f'{student_name} majors in {major_name} located in {Department_Office}')
elif student_major == 'HIST':
    major_name = 'History' 
    Department_Office = 'Kerr Hall, Room 114'
    print (f'{student_name} majors in {major_name} located in {Department_Office}')
elif student_major =='MKT':
    major_name = 'Marketing'
    Department_Office = 'Westly Hall, Room 310'
    print (f'{student_name} majors in {major_name} located in {Department_Office}')
else :
    print('Invaild major code')

