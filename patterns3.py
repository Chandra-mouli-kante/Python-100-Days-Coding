'''
a='ABCDE'
for i in range(len(a)):
    print(a)
'''

'''
for i in range(5):
    for j in range(5):
        print(chr(j+65),end="")
    print()
'''

'''
for i in range(5):
    for j in range(65,70):
        print(chr(j),end="")
    print()
'''

'''
a='MOULI'
for i in range(len(a)):
    print(a[i],end="")
'''

'''
a='MOULI'
for i in a:
    print(i,end="")
'''

'''
for i in 'ABCDE':
        print(i,end="")
'''


'''
for i in range(65,70):
    for j in range(5):
        print(chr(i),end="")
    print() 
'''

'''
for i in range(5):
        print(chr(i+65)*5)
'''

'''
import math
n=int(input("enter a number:"))
for i in range(2,abs(int(math.sqrt(n)))+1):
    if n%i==0:
        print(n,"is not a prime")
        break
else:
    print(n,"is a prime")
'''


import math
a=int(input("enter a starting point:"))
b=int(input("enter the end point:"))
for n in range(a,b+1):
    for i in range(2,abs(int(math.sqrt(n)))+1):
        if n%i==0:
            break
    else:
        print(n,end=" ")
