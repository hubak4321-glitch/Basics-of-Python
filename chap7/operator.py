# Operator

#1. Arithematic Operator
a=5
b=2
print(a+b)                   # Addition Operator
print(a-b)                   # Subtarction Operator
print(a*b)                   # Multiplicaton Operator
print(a%b)                   # Modulus Operator          (Remainder value)

#2. Camparison Operator
a=5 
b=3
print(a > b)                # Greater than Operator 
print(a < b)                # less than Operator 
print(a == b)               # equal Operator 
print(a != b)               # not equal Operator 

#3. Assignment Operator
a=5                      # assign operator

#4. Logical operator
# Rule for and operator
# 1. True _+ True = True
# 2. True + False = False 
# 3. False + False = False
c=10
d=20
print(c>10 and d<10)
print(c==10 and d==20)

# Rule for or operator
# 1. True _+ True = True
# 2. True + False = True
# 3. False + False = False
print(c==10 or d>10)

# Rule for not operator
print(not(c==10 and d==20))      # villan 

# 5. Identity Operator
# is , is not
x=[1,2,3]
y=x
z=[1,2,3]
print(x is y)             # is Operatror
print(x is z)             # location bases not value (z data store another place in python)

print(x is not z)         # villan

#6. Membership  Operator 
# in , in not
my_list=['apple','orange','mango']
print('apple' in my_list)
print('banana'in my_list)
print('apple' not in my_list)

#7. Bitwise Operator
# AND (&), OR (!) , XOR (^) , NOT (~) etc
a1=5                                # 5 in binary-0101
a2=3                                # 3 in Binary-0011      0=F,1=T
print(a&b)                          # 1 in Binary-0001
# Rule for AND (&) operator
# 1. True _+ True = True
# 2. True + False = False 
# 3. False + False = False

b1=5                                
b2=8                               # 8 in Binary-1000
print(b1 & b2)
