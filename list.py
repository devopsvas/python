#!/usr/bin/python3

# List can holds Variety pf data type.


# List concatination

my_list = ["one", "two", "three"]
my_new_list = ["four", "five", "Six"]

final_list = my_list + my_new_list

print (final_list)

#Mutate elements in a list, Mutate "one" with "hundred"

my_list[0] = "hundred"

print(my_list)

#Adding element at the end of the list 

my_list.append("Nine")

print(my_list)

#Removing Items form the list 

my_list.pop()

print(my_list)

# To remove a sepcific item form the list 

my_list.pop(2)
print(my_list)

# Sorting the list example 

myvaslist = ['a', 'f', 'b', 'e', 'c', 'd', 'j', 'k', 't', 'y']

sortedmyvaslist = myvaslist.sort()

print(myvaslist)

test = type(myvaslist)

print(test)

# Reversing the list 

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num_list1 = num_list.reverse()

print(num_list)