# def hello(name, age=21):
#     print (f'Hello, {name}, you are {age} years old!')
# def goodbye():
#     print ('Goodbye!')

# # Main Program
# x= 'John'
# hello(age=27, name=input('What is your name?'))
# goodbye()

TAX_RATE = 0.1
FLAT_SHIPPING = 10 
# ALLCAPS indicates this is a constant value

def add_tax(amount):
    return amount * (1 + TAX_RATE)

def add_shipping(amount):
    return amount + FLAT_SHIPPING

def calc_grand_total(amount):
    return add_tax(add_shipping(amount))
# function is calling two functions: function decopisition 

# Main program

subtotal = float(input('Subtotal: $'))
grand_total = calc_grand_total(subtotal)
print (f'Total:${grand_total: 10.2f}')

# 10 length, 2 decimal points and float 
