'''
Right truncated prime
Ex:239
239 -prime
23 -prime
2 -prime
Then it is truncated prime.
'''


def prime(n):





n=int(input("enter a number:")) #239
a=n #239
cnt=0
while(prime(n) and n>0):
    n=n//10 #23
    if prime(n):
        cnt=1
    else:
        cnt=0
if cnt==1:
    print(a,"right truncated prime")
else:
    print(a,"not a right truncated prime")
    