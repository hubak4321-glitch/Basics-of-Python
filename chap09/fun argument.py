# types of argument
# Required argument
# keywords argument
# Arbitary argument
def greeting (name):
    print("Hello,",name,"!")
    
greeting  ("Huba")
# greeting  ("Huba") Huba is argument
# greeting  () required an arrgument to run code
def intro(course_name,instructor_name):
    print("Welcome to",course_name,"course by",instructor_name)
    
intro("statistics","huba")   
# DEFAULT ARRGUMENT
def dear (name="khan"):      # default function (khan)
    print("Hello,",name,"!")
    
dear()       # run without error using default value

def dear (name="khan"):      # default function (khan)
    print("Hello,",name,"!")
dear("world")          # default value nhi lega

# keyword arrgument

def divide (a,b):
    return a/b
division=divide(4,2)              
print(division)

# arbitrary argument
# arbitrary positional arrgument
def add_number(*args):
    return sum (args)
sum=add_number(1,2,3,4,5)        # variable no. of argument
print(sum)
# argument as tuple
def mam (*names):
    for name in names:
        print(f"Hello,{name}","!")
mam("huba","kissa","esha")

 # arbitrary keyword argument (**kwargs)
# argument stored as a dictionary
def print_detail(**kwargs) :
    for key ,value in kwargs.items():    #used for loop
        print(f"{key}:{value}")
        
# print_detail(name="sidra", age= 24,city="karachi")        
print_detail(name="sidra",age=20)        
