x = [1, 2, 3, 4 ,5]
print(x[3])

# Lists like above will rely on index and ordering whereas dictionaries will use keys (in python its typically a string)

my_dog = {}
# dictionary uses curly brackets. So we've opened an empty dictionary here


my_dog = {'name': 'Ted', 'age': 15, 'breed': 'Border Collie' }
# each element in a dictionary is a key/value pair. e.g name is key, ted is valu
# prints: {name: ted, age: 15 etc}

# As its not ordered like a list, theres no index so we dont use 0 for name, instead we call the key

print(my_dog['name'])
# will print out 'Ted'

my_dog['age'] = 16
# will update the age to 16


my_dog['owner'] - 'Matt'

# will add Matt and print: name: Ted, age: 16, breed: border collie, owner: Matt

print('age' in my_dog)
# will check for age keys and print TRUE !note it only checks keys not the values so searching 'Ted' will present FALSE]

# to look up value

print ('Ted' in my_dog.values())
# will print up TRUE

# likewise 
print(my_dog.values())
# will print a list of all values, if you replace .values with .keys a list of all the keys will print


print(my_dog.items())
# will print  a list with each key and value (tuples), 
# tuple is identical to list but immutable (so read only list)


for item in my_dog:
    print()
# prints each key
# 'for loops' will print keys by default, if you want values you can 

print(my_dog[item])


# but there is a nicer way to gey key and value which is using what we used to get the tuples above

for k, v in my_dog.items():

    print(f'The value of the "{k}" is {v}')


# k is key and v is value, in the loop, the tuple is being extracted into k and v. Its going into the tuple and taking the first element and storing into k and second element into v. 

print(my_dog['state'])
# gives a key error cause we dont have a state key



print(my_dog['state'])

# we want adefault value so if the key doesnt exists it will return a default value. 

# lets make the default "unkown"



print(my_dog.get('state'))
# using 'get' will now return 'none' 
# print will be 'none' but we can also provide an optoinal second parameter (anything) and that's what will be returned if key isnt found.

print(my_dog.get('state', 'Unknown'))







dogs = [
    {'name': 'Ted', 'age': 15, 'breed': 'Border Collie' }
    {'name': 'Loki', 'age': 3, 'breed': 'Border Collie' }
]

# Here is an example of a list of dictionaries 

print(dogs[1]['age'])
# will print 3

