# spam = 0 
# while spam <5:
#     print('Hello')
#     spam += 1    
#     #spam = spam + 1

# print ('Done')




# for spam in range(5):   
#     print(f'Hello {spam}')

# spam take on value 0-4 and prints 5 times Hello 0 , Hello 1, Hello 2 etc

# FOR LOOPS


# for spam in range(1, 11, 2):   
#     print(f'Hello {spam}')

# The third value here: Take 2 steps instead of 1, taking every 2nd value after the one, can do 3, taking every 3rd value after the one etc

# EXTENDED FOR LOOPS

import random 

count = int(input('How many random integers?'))
for i in range (count):
    print(random.randint(1,100))
