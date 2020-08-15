'''
n=int(input("enter the value of n:"))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if count==2:
    print(n,"is prime number")
else:
    print(n,"is  not a prime number")
'''

'''
n=int(input("enter the value of n:"))
count=0
for i in range(2,n):
    if(n%i==0):
        count+=1
if count>0:
    print(n,"is not a prime number")
else:
    print(n,"is a prime number")
'''

'''
n=int(input("enter the value of n:"))
for i in range(2,n):
    if(n%i==0):
        print(n,"is not a prime number")
        break
else:
    print(n,"is a prime number")
'''        

'''
n=int(input("enter the value of n:"))
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print("enter value more than 1")
'''

'''
import math
n=int(input("Enter  Value of n:"))
for i in range(2,abs(int(math.sqrt(n)))+1):
    if n%i == 0:
        print(n,"Is not a prime")
        break
else:
    print(n,"Is a Prime")
'''





