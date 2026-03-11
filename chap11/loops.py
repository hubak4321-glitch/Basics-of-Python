# # loops and its type 
# # 1.while loop        (repeating excutes a block of code condition true)  (condition false stop the code run)
# # 2.for loop        
# # 3.nested loop 
# # WHILE LOOP
# #  check condition to avoid infinte loop
# count = 0
# while count < 4:            # condition true
#     print(count)
#     count+=1               # or count=count+1  condition one by print in terminal
 
# # print no 1 to 5 using while loop      
# count = 1
# while count < 6:            # condition true
#     print(count)
#     count= count + 1
    
# count = 6
# while count > 0:            # condition true  
#     print(count)
#     count= count -1  
# else:
#     print("While loop is ended")
    
# #  check condition to avoid infinte loop

# # FOR LOOPS 
# # iterate on sequence bar bar chaley (tuple dictionary set )

# Language="Python"           # sequence
# for x in Language:
#     print(x)
# # Range function
# # range(stop)    
# # range[start,stop,step]    
# for i in range(5):           # stop argument
#     print(i)
# for z in range(5,10):        # start stop argument
#     print(z)   
# for y in range(1,10,3):       # start stop and step argument
#     print(y)    
    
# for i in range(5):           # stop argument
#     print(i)  
# else:
#     print("For loop is ended")      
    
# LOOP CONTROL STATEMENT  (allow you alter the normal flow of the loop)
# (3 clause)
# pass statement    [placeholder(doing nothing) future code (run entire code without error)] 
# break statement
# continue statement 

# for i in range(5):
#     # not in the mood 
#     pass

count=5
while count > 0:
    if count  == 3:
        pass
    else :
        print(count)
    count -= 1   
    