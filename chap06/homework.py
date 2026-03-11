# HW write a program to input student name and marks of 3 subject and print name percentage 
name=input("enter your name:")

# subject marks
sub_eng=input("enter english mark: " )
sub_urdu=input("enter urdu mark: ")
sub_math=input("enter math mark: ")

# calculating percentage
percentage=((int(sub_eng)+int(sub_math)+int(sub_urdu))/300)*100
print((int(percentage)),'%')
# print result
print(f"The result of {name} is {int(percentage)}% .weldone")


# optimize solution
name=input("enter your name:")
print("percentage calculator")
# subject marks
sub_eng=int(input("enter english mark: " ))
sub_urdu=int(input("enter urdu mark: "))
sub_math=int(input("enter math mark: "))

# calculating percentage
percentage=(((sub_eng)+(sub_math)+(sub_urdu))/300)*100
print((int(percentage)),'%')
# print result
print(f"The result of {name} is {int(percentage)}% .weldone")

#Q2:Write a program that collects multiple types of data to store in a dictionary and print output
#intializing a dictionary
user_data={}

# input from user
user_data['name']=input("enter your name: ")
user_data['age']= int(input("enter your age: "))
user_data['height']=float(input("enter your height: "))   #height in float 
user_data['student']=input("are you a student (yes/no): ")

# print the input from user
print(user_data)
#{'name': 'Huba khan', 'age': 20, 'height': 5.4, 'student': 'yes'} ans in dictionary 
# form fill kartay hai