'''
import math
n=int(input("enter a number:"))
for i in range(2,abs(int(math.sqrt(n)))+1):
    if n%i==0:
        break
else:
    print(n,end=" ")
'''

'''
import math
def prime(n):
    for i in range(2,abs(int(math.sqrt(n)))+1):
        if n%i==0:
            break
    else:
        return(n)
n=int(input("enter a number:"))
print(prime(n))
'''

'''
import math
def prime(n):
    for i in range(2,abs(int(math.sqrt(n)))+1):
        if n%i==0:
            break
    else:
        return(1)
n=int(input("enter a number:"))
a=n
cnt=0
if (prime(n)==1):
    print("prime")
    while n:
        r=n%10
        n//=10
        if(prime(r)==1):
            cnt+=1
else:
    print("not prime")
if cnt==len(str(a)):
    print("mega prime")
else:
    print("not a mega prime")
'''


import math
def prime(n):
    for i in range(2,abs(int(math.sqrt(n)))+1):
        if n%i==0:
            break
    else:
        return(1)
n=int(input("enter a number:"))
for i in range(n-1,0,-1):
    if prime(i)==1:
        a=i
        break
print(a)
i=n+1
while n:
    if prime(i)==1:
        b=i
        break
    i+=1
print(b)
if abs(n-a)>abs(n-b):
    print(b,"is near")
elif abs(n-a)==abs(n-b):
    print(a,b,"both are equal")
else:
    print(a,"is near")

