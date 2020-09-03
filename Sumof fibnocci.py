'''
fib series: 0 1 1 2 3 5 8 13 21 34 55 89
Ex: 30         
  21+8+1
Ex: 10
  8+2
algo approach:
Ex:30
21
30-21=9
8
9-8=1
1
'''

'''
def nearfib(n):   #30,9
    a,b=0,1
    while n>=b:
        if n==b:
            return b
        a,b=b,a+b
    print(a)   #21,8,1
    return nearfib(n-a)   #9,1
n=int(input())    #10
print(nearfib(n))
'''





