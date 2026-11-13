# Create a list 

movies = ['Spider-Man 2','Avengers','Iron-Man 1','Spider-Man 1']

print(len(movies))

print(movies)

# Sort ASC Order 
print(sorted(movies)) # sorts the list from ASC order 
print(movies) # display original list 

#.sort()
movies.sort()# permanently sorts the list 
print(movies) # displays the updated list 

movies.append('Fast and Frious')
print(movies)