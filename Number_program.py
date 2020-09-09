#Armstrong Number:
'''
def length(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    return count    
def armstrong(n):
    arm=0
    n1=n
    l=length(n)
    while n>0:
        rem=n%10
        arm+=rem**l
        n//=10
    if n1==arm:
        return("armstrong")
    else:
        return("not armstrong")
n=int(input("enetr a number:"))
print(armstrong(n))
'''

'''
#PERFECT number:
Ex:
6
sum of 6 divisors
3+2+1=6
output: yes

10
sum of 10 divisors
5+2+1=8
output: No
'''

def perfect(n):
    c=0
    for i in range(1,n//2+1):
        if n%i==0:
            c+=i
    if c==n:
        return"True"
    else:
        return"False"
n=int(input("enter a number:"))
print(perfect(n))
