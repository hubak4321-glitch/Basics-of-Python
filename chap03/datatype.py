# data type in python
a=1
b=1
print(a+b)
print(type(b))      # checking data type :integer

a1="1"              # use only ("")
a2="1"
print(a1+a2)
print(type(a1))     # checking data type :string (variable)

# Basic data type in Python
# 1. Numeric
b1=1                 #1(a).integer
b2=1.5               #1(b).float    
b3=complex(3,4)      #1(c).comlex   3+5i (real,imagnary)     

# 2. Sequence
c1 ="hubakhan"                 #2(a).string using "" ''
print(type(c1))
c2=[1,3,6,9,78,67,'hubakhan']  #2(b).list   sq bracet []
print(type(c2))
c3=(1,3,6,9,78,67,'hubakhan')  #2(b).list   round bracet ()
print(type(c3))

#(3). Dictionary
#variable ("",'') value without "" (used :) used curlbracket {}
my_dictionary={'name':'huba','age':20,'city':'karachi'}    
print(type(my_dictionary))

#(4). Sets   (combination of elements or object)
# used curlybracket {}
my_sets={1,3,6,9,78,67,'hubakhan'} 
print(type(my_sets))
 
#(5). Boolean
# only two value used true and false 
bool1=True
bool2=False
print(type(bool1))

#(6). Binary
# byte, bytearray, memoryview
byte1 = b"hubakhan"
print(type(byte1))