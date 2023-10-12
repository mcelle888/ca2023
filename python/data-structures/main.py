import my_module, #random
# can import multiple modules in a single statement

print(my_module.s)
# module . 'anything in the module' here is s '


my_module.foo(my_module.person)
my_module.foo({'name':'Michelle', 'age' : 27})


print(my_module) 
# will just say that its a module and where its located

print(dir() )

# dir is directory of your current scope youre in so in this case it will be a list of symbols that will print out with my module included

print(dir(my_module))
# will give the directory of the module itself so it will print out a, foo, s (so i can use this see what is inside the module, can be handy for debugging when youre trying to call something in the module or look for something)




# if we want to use only one or two things in a module, we don't want to import the whole module (takes memory and time)


# thers another form of import statement:

from my_module import foo, person

# list out symbols you want to import, in this case foo and person

my_module.foo(my_module.person)
my_module.foo({'name':'Michelle', 'age' : 27})

# this imports the individual elements into this main.py file so we no longer need: 
my_module.foo(my_module.person)
my_module.foo({'name':'Michelle', 'age' : 27})
# becomes

foo(my_module.person)
foo({'name':'Michelle', 'age' : 27})

# imported symbols into the local namespace, meaning we can access them directly without prefixing with module names, making code more dry. 





def foo(x): 
    print (x)

foo(my_module.person)
foo({'name':'Michelle', 'age' : 27})

# There is conflict here as we are defining foo again as x . Where tgers a name conflict, we can suffex name import with an 'as' :

from my_module import foo as bar, person

def foo(x): 
    print (x)

foo(my_module.person)
bar({'name':'Michelle', 'age' : 27})

# no conflict now so foo refers to local foo and bar now refers to imported foo.
# if you have a name conflict, you 'as' to rename an import to fix 

#  PACKAGES in python is a group of modules 




# importing package

from colort import colorize, ForegroundColor as fc, Style, BackgroundColor as bc

colored_text = colorize('Hello World!', fc.GREEN, Style.BOLD, bc.YELLOW)
print("colored text: ", colored_text)


# pip freeze in the terminal will show us all the packages/dependencies that are in use 