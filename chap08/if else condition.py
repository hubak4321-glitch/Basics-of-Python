# Conditional statement in Python 

# 1. if statement
# if statement work only for true condition
a = 26
b = 108
if b > a:
   print(" b is greater than a")

age = 20
if age > 19:
    print ("you are an adult")


age = int(input("enter your age"))
if age > 19:
    print ("you are an adult")

# 2.If-else statement
# else handle false condition
Temperature = 30
if Temperature > 25:
    print("it's a hot day.")
else:
    print(" it's a cool day")    

age = int(input("enter your age"))
if age > 19:
    print ("you are an adult")
else:
    print("you are not an adult")

# 3. If-elif-else 
name=input("enter student name")
score=int (input("enter student score"))
if score >= 90:
    print("Grade_A+")
elif score >= 80:
    print("Grade_A") 
elif score >= 70:
    print("Grade_B+")
elif score >= 60:
    print("Grade_B")
elif score >= 50:
    print("Grade_C")
else:
    print("fail")

# Nested If else statement
# If-else inside if-else
# Multiple condition depend on each other
# Q: Positive'Negative and zero . Positive - even/odd
number=int(input("Enter a number: "))

if number > 0:                               # Checking Positive NUmber
    if number % 2 == 0:                      # divide by 2 == remainder 0
        print("This is the even number")
    else:
        print("This is odd number")  
else:           
    if number==0:                           # Number =0
        print("This is zero")
    else:                                   # negative number
        print("This is the negative number: ")

# 5. Conditional Expression (Ternary Operator)

age=int(input(" enter your age: "))
status= "Adult"  if age > 18  else "Child"
print(status)
