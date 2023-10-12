import dog

# dog1 =dog.create('Ted', 15, 'Border Collie')
# dog2 = dog.create('Loki', 3, 'Border Collie')

# dog.walk(dog1)
# dog.walk(dog2)
# dog.walk(dog2)

# print(dog1)
# print(dog2)



# We call it like we call a funtion, to create a new instance of this class dog
dog1 =dog.Dog() #creates new instance of dog
dog1.name ='Ted' #creates new attribute
# builds/contructs an instance of a class (contructor)



dog2 =dog.Dog()

# print(dir(dog1))
# print(dir(dog2))

# self parameter
print(f'dog1:{dog1.__dict__}')

# __dict__ shows all thevalues of object and the attributes of the object
dog1.greet()
