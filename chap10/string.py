# Strings charcter in single double triple quotes
name="Nurulhuda"               # creating string
print(name)
print(type(name))              # checking data type

print('Hello world')
print("Hello worrld")

print("it's easy")
# print(""kw-double quotes"")    # show error
print('''"Quotes"''')
print("\"Quotes\"")           # escape sequence

# Formating String

# old style formatting-% operator
name="Huba"
age=22
print("My name is %s and i am %d"%(name,age))
# %s,%d are placeholder for the integer

# Formate String
# index no. position
Name="Alina"
Age=23
print("My name is {} and I'm {}".format(Name,Age))
# you can reference  variable by index and keyword  index=position
print("My name is {0} and I'm {1}".format(Name,Age))
print("My name is {1} and I'm {0}".format(Name,Age))

print("My name is {name} and I'm {age}".format(name="Umer", age=24))

# f string
Subject ="Math"
Marks=90
print(f"Result of {Subject} on my last semester is {Marks}")

# Escape character-back slash with character 
print("\"kw-double qoutes\"")  # double quotes using

print("\'kw-single qoute\'")
print("Hello\nworld")    # \n new line
print("Hello\tWorld")     # \t tab = space
# STRING OPERATOR 
a="Hello"
b="Python"
print(a + b)    #concatenate=add string
print(a*2)      # muliple copies
print(b*3)      # 3 time copies
 
if "H" in a:
    print("yes") 
else:                # case sensitive
    print("no")      

print(r"hello\n huba")    # raw string surpass the escape
# string index  index=position no.
# string[index_value]  positive starting 0  ending position -1
my_name="Hamia"
print(my_name[0])     # 1st character of str
print(my_name[1])     # 2nd character of str
print(my_name[2])     # 3rd character of str
print(my_name[3])     # 4th character of str
print(my_name[4])     # 5th character of str

# index : 12345678
name3="Huba Khan"
print(name3[4])
# - index start -1,-2,-3
# last character of my string
print(name3[-1])    # 1st last
print(name3[-2])    # 2nd last
print(name3[-5])    # blank space is also cahracter

# STRING SLICING
# syntex
#  string[start:end:step]
name="Hubakhan"
print(name[0:3])      # last cahr4acter is  exclusive
print(name[0:8:2])
print(name[1:8:2])
print(name[2:5])       # 3rd to 5th character
print(name[1:4])        # second to forth
print(name[-2:])        # last 2 character
print(name [-3:])      # last 3 character
print(name[1::2])     # every second character
print(name[::])       #  all character 
print(name [:])        # all character
print(name[::-1])      #reverse order

# String method
word="Hello, Huba"
# 1.len()
print(len(word))

# 2.upper()
print(word.upper())

# 3.lower
print(word.lower())

# 4. count
print(word.count('a'))

# 5. find method         position value
print(word.find('b'))

# 6. split           
print(word.split())
print(word.split(','))

# 7.  replace 
print(word.replace("Huba","Hamia"))

word2="hello, HUba is great"
# 8 . title
print(word2.title())

# 9 . strip
word3="   Hello Huba  "
print(len(word3))
print(word3.strip()) 

# 10. join()
zwords=("Huba","is","Great")
print(" ".join(zwords))
print("-".join(zwords))

