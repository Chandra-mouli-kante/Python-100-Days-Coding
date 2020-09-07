'''
CollatZ sequence:
Ex:
n=6
even n/2
odd n*3+1

6 3 10 5 16 8 4 2 1
(if 1 arrives stop the execution)
'''

#collatz sequence:
n=int(input("enetr n:"))
def collatz(n):
    while n>1:
        if(n%2==0):
            n=n//2
            print(n,end=" ")
        else:
            n=n*3+1
            print(n,end=" ")
collatz(n)
 
