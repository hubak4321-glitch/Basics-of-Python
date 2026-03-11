# Assigment no. 4
#  limit the decimal places to digit using formate method n\
    # and print result , for the variable pi= 3.14159265359
pi=3.14159265359
print(round(pi,2))
# . formate method
print("Value of pi is {}".format (pi))
# using f value flot no.
print("Value of pi is {:.1f}".format (pi))
print("Value of pi is {:.2f}".format (pi))
print(f"{pi:.2f}")


# Q2 extract character form index 2 to 8 with a syep of 
# 2:Given my_string ="Python Course",slice characters
# from index 2 to 8 skipping every other char

my_string="Python course"
# string[start:stop:step]
print(my_string[2:8:2])


# slice to the middle character(s):for my string="Hubakhan" ,use slicing 
# to extract the middle character
string = "Hubakhan"    # 8 character even
string2= "Hubia"       # 5 character odd
# index : 01234567
def mid_str(words):                
    middle=int(len(words)/2)             # 4     even char
    if len(words)%2==0:
        return words [middle-1:middle+1]   # 3:5    
    else:
        return words[middle]             # odd char \
        
print(mid_str(string))
print(mid_str(string2))

# Q4 remove first and last 3 character :Given my_string ="Regression Ananlysis" ,
# remove first 3 and last 3 character 

my_string="Regression Analysis"
print(my_string[3:-3])

# Q5  Get subracting start 4 character from the end to the 
# last character : for my_string =" Classification ",
# slice the string start from thr 4th character from the end to the last character
 
my_string="Classification"
print(my_string[-4:])

# Q6b how to reverse a string using python string method
word="Python"
print(word[::-1])         #step value -1 


# Q7 write a python function to check if a string is a palindraome using string method 

word2="madam"
word3="apple"
def palindrome (s):
    if s==s[::-1]:
        print (f"{s} is a palidrome")
    else:
        print(f"{s} is not a palidrome")
        
palindrome (word2)
        
palindrome (word3)