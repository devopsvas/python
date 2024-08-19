#!/usr/bin/python3

#Simple dictionary
my_dict = {'key1':'value1','key2':'value2'}

# Calling dictionary
print (my_dict['key1'])

#Example dictionary 

prices_lookup = {'apple':200.00,'oranges':60.00,'milk':5.80  }

print (prices_lookup['apple'])

#Complex Dict with list and another dict

d = {'k1': 123, 'k2':[0,1,2],'k3':{'insidKey':100}}

print (d['k2'])

print (d['k2'])

# calling Dict with in Dict 

print (d['k3']['insidKey'])

#Grabibing a key form list inside a dict and make to upper 
c =  {'key': ['a', 'b', 'c']}
print (c['key'][2].upper())

# Assigning a new key in the already existing dict 

d = {'k1': 100, 'k2': 200}

print (d)

d['k3'] = 300

print (d)

# to list down all the keys 

print (d.keys())

# to print all the values 

print (d.values())

# 1. Do dictionaries keep an order? How do I print the values of the dictionary in order?

# Dictionaries are mappings and do not retain order! If you do want the capabilities of a dictionary but you would like ordering as well, check out the ordereddict object lecture later on in the course!