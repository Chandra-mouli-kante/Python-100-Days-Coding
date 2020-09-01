'''
def fib(n):
    a=0
    b=1
    i=2
    while i<n:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        i+=1
fib(5)
'''

'''
#sum of fibnocci series
def fib(n):
    a=0
    b=1
    s=a+b
    i=2
    while i<n:
        c=a+b
        s+=c
        print(c,end=" ")
        a=b
        b=c
        i+=1
    else:
        print(s)
fib(5)
'''

'''
#nth element of fib series
def fib(n):
    a=0
    b=1
    i=2
    while i<n:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        i+=1
    print(b)
    
fib(5)
'''

'''
#recursion
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
print(fib(10))
'''


#factorial with recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return(n*fact(n-1))
print(fact(5))
