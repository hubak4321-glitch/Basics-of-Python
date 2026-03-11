# Homework Question 
value= None
if value:
    print("Value is True: ")
else:
    print("Value is False: ") 


# Write a Simple Programme to determine if a given year is a "leap year" using  user input    

# sir solution
# leap year Condition :
# 4 divisible & 100 not divisible 
# 400 divisible

year=int(input("enter a year (e.g. 2024): "))

# Cheaking Leap Year 
if (year% 4==0 and year % 100 != 0) or (year% 400==0): # or condition (true + false = true) or condition lazmi hai isliye ka agar ek ka answer true or false means ka 4 se divide nhi horaha tou 400 sa tou hoga isliye
        print(f"{year} is  leap year")
else :
    print(f"{year} is not leap year") 

# Login Authentication usind Conditional Statement.Assume you have Predefined User_name and Password

# write a programe that prompt the user to enter a username and password and check whether 
# they match. provide appropriate message for the following cases
#  both username and password are correct

# predefine_username and password  
# login authentication
predefined_username= "Huba Khan"
predefined_password="huba131"

# prompt the user to enter a username and password 
username=input("enter your username: ")
password=input("enter your password: ")

# username and password are Match
if username==predefined_username:
    if password==predefined_password:                  # first line are incorrect then print invalid user name  
        print("Welcome! Login will successfully.")     # but first line is correct then nested if else condition are follow
    else:
        print("Incorrect Password!")    
else:
    print("Invalid Username.")        

# Addmission Eligiblity; A University has a following eligible criteria
# Marks in Mathematics>=65
# Marks in Physics>=55
# Marks in Chemistry>=50
# total marks in 3 subject>=180 OR total marks Mathematics and Physics >=140
    
print("enter your PCM Marks.") 
Physics_Marks=int(input("Enter your Pyhsics_Marks: "))
Chemistry_Marks=int(input("Enter your Chemistry_Marks: "))                                          
Maths_Marks=int(input("Enter your Math_Marks: "))

if (Physics_Marks and Chemistry_Marks and Maths_Marks and 
    (Physics_Marks+ Chemistry_Marks+Maths_Marks)>+180)or(Physics_Marks+Maths_Marks)>+140:
     print("you are eligible")
else:
     print("you are not Eligible")

