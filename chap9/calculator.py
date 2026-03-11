# PYTHON PROGRME TO CALCULATOR
# function for operator
# user input 
# print function

def addition (a,b):
    return a+b
def subtraction (a,b):
    return a-b 
def multiplication(a,b):
    return a*b
def dividsion (a,b):
    return a/b 
def average (a,b):
    return (a+b)/2

# user input 
print(" please select operation:\n "\
    "1.Addition\n"\
    "2.Subtract\n"\
    "3.Multiply\n"\
    "4.Division\n"\
    "5.Average")
# print function
select=int(input("select the operaqtion 1,2,3,4,5: "))
number1=int(input("enter your First number: "))
number2=int(input("enter your second number: "))

# print the result
if select ==1 :
    print(number1,"+",number2,"=",\
        addition(number1,number2))
elif select==2:
    print(number1,"-",number2,"=",\
        subtraction(number1,number2))
    
elif select==3:
    print(number1,"*",number2,"=",\
        multiplication(number1, number2))
elif select==4:
    print(number1,"/",number2,"=",\
        dividsion(number1,number2))
elif select==5:
    print("(",number1,"+",number2,")","/","2","=",\
        average(number1,number2))
    
else:
    print("Invalid Operation please select again")     
       
        