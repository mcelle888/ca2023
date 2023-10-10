spam = []
# list are created using square brackets and the list is stored in a variable called spam
print(spam)


spam = ['cat', 'dog', 'bird']
eggs = [12, 78, 100, 54, 42]
foo = ['Michelle', 27]

print(len(spam)) #tells us number of elements so here it would be 3

print(spam[2]) # prints bird, indexing starts at 0
# can also slice:  
print(eggs[1:3]) #prints [27, 100]

tic_tac_toe = [
    ['', '0', ''], 
    ['X', '', '' ],
    ['', 'X', '']
]

# shows the results of tictactoe game



# MODIFY LIST
spam[1]= 'hello'
print(spam) 
# will now print cat hello bird [ADDING]

print(spam + eggs)
# will print both lists in one big list [COMBINING]

del spam[1]
# will delete dog and bird will move up to fill up space and index will change [DELETING]



for animal in spam:
    print(animal)
# visits each element until reach the last element so will prints:
# print(cat): cat
# print(dog): dog
# print(bird): bird
# list has ended so loop ends. 

# vists the element, stores the value into 'animal' (sentinal variable that can be any name) and prints then moves to the next until the end of the list

# An analogy may be having a row on boxes on a table (the row of boxes being a list), and the loop is going through and opening each of the boxes one by one and looking at the contents



index = 1
for animal in spam:
    print(f'{index}. {animal}')
    index +=1 
# to print out numbered list so:
# 1. cat
# 2. dog 
# 3. bird


# EASIER METHOD : ENUMERATION
# PAIRS EACH ELEMENT WITH ITS INDEX

for index, animal in enumerate(spam):
    print(f'{index + 1}. {animal}')

# this for will give me a pair of values, first: the numbers and second: the elements 
# plus one cause index starts at 0
# dont need to index function here because enumeration function is already generating two values 


# APPEND  will add a new element to the end of the list
spam.append('kangaroo')
print (spam)
# will print: cat, dog, bird, kangaroo

spam.append(foo)
print(spam)
# will print foo list INSIDE spam list as a single element so will print: [cat, dog, bird, [Michelle, 27]]


# TO APPEND EACH INDIVIDUAL ELEMENT OF ANOTHER LIST 
spam.extend(foo)
print(spam)
# will take elements from foo list and add them into spam list so will print: [cat, dog, bird, Michelle, 27]

# ALTTERNATELY
spam += foo
print(spam)

# add to original and extend





x = spam.index('dog')
print(x)
# like a search will return the index which is 1 


x = 'dog' in spam
print(x)
# prints: TRUE to determine if something exists in a list, if it is a said element of specified list



def display_person(person):
    print(f'{person[0]} is {person[1]} years old and {person[2]} is cm tall')

display_person(foo)

# person doesnt really describe so we can pull them out into variables first: 

def display_person(person):
    name = person[0]
    age = person[1]
    height = person[2]
    print(f'{person[0]} is {person[1]} years old and {person[2]} is cm tall')

display_person(foo)

# but this isnt very dry so lets repalce 3 lines with: 

def display_person(person):
    # name = person[0]
    # age = person[1]
    # height = person[2]
    name, age, height = person 
    print(f'{person[0]} is {person[1]} years old and {person[2]} is cm tall')

display_person(foo)

# this says get the 0 element and store in element called name, get 1 element and store in age, get 2nd element and sotre in height. this is also known as 'DE-STRUCTURING(JAVASCRIPT)/UNPACKING(PYTHON):breaking up a data structure to get values without destroying original data'


# append will always add data to the end but if we want to add somewhere else we use INSERT

spam.insert(1, 'kangaroo')
print(spam)

# prints: cat, kangaroo, dog, bird




# POP FUNCTION: removes last item off the list and returns it (incase you want to use it) 
x=spam.pop()
print(x)
# prints:
# cat, kangaroo, dog
# bird



# SORTING LIST: alphabetical/numerical order ascending 

spam.sort
spam.sort(reverse=True) 
# for descending order
print(spam)

