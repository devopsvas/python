#! /usr/bin/python3

current_movies = {'The Test Movie': '11.00am',
                  'Kilukkam': '12.00pm',
                  'Devsuram': '13.00 am',
                  'Devdoodan': '2.00'}

print('we are showing the following movies')
for key in current_movies:
    print(key)
movie = input('What movie would you like to watch\n')

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, 'is playing at', showtime)
