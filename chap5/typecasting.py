# casting in python 
# cast means change data type     
a=1            #integer
b="1"          #string
c=int(b)       #converting data type
print(a+c)
print(a+int(b))
# all string didn't cast into numeric
name = "huba"
# newname = int(name)   #ValueError:
# all numeric cast into str
myage =20
myage2=str(myage)
print(type(myage2))

f1=22.56
f2=int(f1)
print(type(f2))
print(f2)

in1=26
print(type(float(in1)))
print(float(in1))

# Implict type casting   (coercion)
# automatic change data type no instruction give data 
var1=10           #int type
var2=15.5         #float type
var3=var1+var2
print(var3)
print(type(var3))  # python give correct answer  automatic in float 

# Explicit type casting
int_num=101
str_num=str(int_num)
print(type(str_num))
print(str_num)

h=bool(0)
print(h)
print(type(h))

g=bool(1)
print(g)
print(type(g))