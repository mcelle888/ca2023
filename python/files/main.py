
# __________TO OPEN A FILE____________
f = open ('shopping.txt') 

# to get items out of file, call the read method: 

data = f.read(10)
data2 = f.read(10)

f.close()
# need to close after working with the file

print(data)
# will print the string
print(data2)

print(repr(data))
# will return the raw string (e.g. the new line characters)

# **************OR************

# opening file without having to close later: we are using the with method. Here f is an object that represents the file so f = file

with open('shopping.txt') as f:
    data = f.readline()
    print(repr(data))


# this will loop / iterate through a file
with open('shopping.txt') as f:
    for line in f:
        print(line.strip())

# making a list from data 
shopping_list = []
with open('shopping.txt') as f:
    for line in f:
        shopping_list.append(line.strip())

print(shopping_list)

# 2nd way to create the list whereby you split the whole thing (suitable for small files)
shopping_list = []
with open('shopping.txt') as f:
    data= f.read()
    shopping_list = data.split('\n')

print(shopping_list)



# ______________________WRITING A FILE______________________
# for writing we need to pass second paramenter string 'w' in with method and this should create a new file if it doesn't exist and overwrite if it does exist. 

with open('tv-shows.txt', 'w') as f:
    f.write('The X Files\n')
    f.write('The Witcher\n')

    # or this will produce the same result too

    f.write('The X Files\nThe Witcher\n')

# _______ to add list into new file
shows = [
    'The Mandalorian'
    'The Witcher'
    'The X Files'
]

with open('tv-shows.txt', 'w') as f:
    f.write('\n'.join(shows))

# __________another method is using a for loop
with open('tv-shows.txt', 'w') as f:
    for s in shows:
        f.write(f'{s}\n')

# ______appending: we set parameter as 'a' and not a 'w'
# go back to shopping list that takes input from user and adds to shopping list

item = input('What do you need to buy? ')

with open('shopping.txt', 'a') as f:
    f.write(f'\n{item}')