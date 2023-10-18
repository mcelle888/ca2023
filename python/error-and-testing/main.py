class NegativeNumberError(Exception):
    pass

try:
    n = int(input('Enter a numerator: '))
    d = int(input('Enter a denominator: '))

    if n < 0 or d < 0:
        raise NegativeNumberError()

    q = n / d  # Exception was raised when trying to divide by zero

    print(q)

    # lets attempt 5 / 0 :
    # 'ZeroDivisionError' at line 4 so above ^
    # we can use a try/except block so that if any code tries to raise an exception or throw an exception, execution of try block will stop and immediately jump to the except block: 

# ___CODE___

# except Exception as e: 
#     print(e)
#     print('Caught an exception')


# if we have an except block and it executes, it will override default behavior of python so we wont get that 'ZeroDivisionError' 

# ___PART 2___
# What if we want to customise like what if we want to restrict the answers to positive integer? We use if and raise methods


except ZeroDivisionError: 
    print('Denominator cannot be zero')

except ValueError:
    print("Inputs must be integers")

except NegativeNumberError:
    print('Inputs cannot be negative numbers')

except Exception as e:
    print('Something went wrong')
    print(e)
    # Log debug information (including traceback) to an error log file 
    # So we show one thing to user but we show the debugging in a seperate file 


# we want to only wrap things that might call an exception in the try block. So the print funciton wouldnt call the exception so you wouldnt have to wrap that. Next time we would only wrap where a possible error could occur (just this example most of the code could cause an exception to appear) 