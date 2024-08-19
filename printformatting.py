#! /usr/bin/python3

# .format() method f-strings() method 

# .format() method

print ('This is a string {}'.format('INSERTED'))

print ('The {} {} {}'.format('fox', 'brown', 'quick'))

# to Print only "The Fox Fox Fox" Index prostion 0 

print ('The {0} {0} {0}'.format('fox', 'brown', 'quick'))


# Index Variables method 

print ('The {f} {b} {q}'.format(f ='fox',b='brown', q='quick'))

# Float formatting follows Format is "{value.width.precision f}"


result = 100/777 # Answer of this is 0.1287001287001287

# To format the 0.1287001287001287 3 postions

print("The Result is{r:10.3f}".format(r=result))


#f strings examples 
name = "Vasanth" 
age = 38
print(f'{name} is {age} years old')


