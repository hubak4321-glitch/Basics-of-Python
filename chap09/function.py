# User defined function
# without parameter
# create function 
def Greeting ():
    print("Welcome to the python tutorial by huba ")
# call function use function use ()
Greeting ()   

# With paramater
# create function 
def add2number (a,b):    # parameters
    result =a+b
    print("the sum is:", result)
# call funtion 
add2number(5,8)       # argument (5,8)

add2number(a=10,b=100)
add2number(b=2,a=5)

def add3number(a,b,c):
    results=a+b+c
    print("the sum of 3 numbers is:", results)
    
 # call function
add3number(1,7,5)
add3number(c=6,b=9,a=3)
add3number(7,8,3)
# return result the function is stop running
# function with return statement

def add2num (a,b):
    return a+b
    # return a-b after return statement function 
sum2num = add2num(2,8)    
print(sum2num)
 
# function convert celsius to fahrenheit used return statement
def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit

# used function 
temp_f=celsius_to_fahrenheit (25)
print(temp_f)
print("with return",type(temp_f))
    
# function convert celsius to fahrenheit without return statement
def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    print(fahrenheit)

# used function 
temp_f2=celsius_to_fahrenheit (50)
print("without return",type(temp_f2))
# pass statement  code to update later
def kuchbhi ():  
    pass  # this does nothing
print("hello")

        


 