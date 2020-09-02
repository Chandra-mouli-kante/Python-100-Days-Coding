'''
#nth element of fibnocci series
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
print(fib(5))
#fib(4)+fib(3)= 2+1=3
#fib(4)=fib(3)+fib(2)=1+1
#fib(3)=fib(2)+fib(1)=1+0
'''

'''
#before element
def beforefib(n):
    a,b = 0,1
   while b<=n:
         c=a+b
         a=b
         b=c
    return a
n=int(input())
print(beforefib(n))
'''


'''
#before fIBONACCI
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
num=int(input())
for i in range(1,num):
    k=fib(i)
    if k==num:
        print(num)
        break
    if k>num:
        print(fib(i-1))
        break
'''

'''
#After element in fibnocci
def afterfib(n):
    a,b = 0,1
   while b<=n:
         c=a+b
         a=b
         b=c
    return b
n=int(input())
print(afterfib(n))
'''


#Nearest fibnocci element to given number
def nearestfib(n):
    a,b = 0,1
   while b<=n:
         c=a+b
         a=b
         b=c
    if abs(a-n)<=abs(b-n):
        return a
    else:
        return b
n=int(input())
print(nearestfib(n))
