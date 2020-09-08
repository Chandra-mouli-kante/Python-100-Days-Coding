'''
Beatty Sequence:
Ex:
n=5
n*sqrt(2)
1*sqrt(2)
2*sqrt(2)
3*sqrt(2)
4*sqrt(2)
5*sqrt(2)

1 2 4 5 7 -output
'''


import math
def beatty(n):
    for i in range(1,n+1):
        a=math.floor(i*math.sqrt(2))
        print(a)
n=int(input("enetr a number:"))
beatty(n)


