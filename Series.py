'''
n=int(input("enter a range:"))
a=0
b=1
for i in range(2,n+1):
    c=a+b
    a=b
    b=c
    print(b, end=" ")
'''

'''
n=int(input("enter a number:"))
m=int(input("enter a number:"))
if n>m:
    small=m
else:
    small=n
for i in range(1,small+1):
    if(n%i==0 and m%i==0):
        gcd=i
print(gcd)
'''

'''
n=int(input("enter a number:"))
m=int(input("enter a number:"))
if n>m:
    small=m
else:
    small=n
for i in range(1,small+1):
    if(n%i==0 and m%i==0):
        gcd=i
        print("multiplicants",i)
print("gcd is",gcd)
'''

'''
a = int(input("First Number :"))
b = int(input("Second Number :"))
i = 1
gcd = 1
while i<=min(a,b):
 if a%i==0 and b%i==0 :
    gcd = i
 i+=1
print(gcd)
'''


n=int(input("enter a number:"))
m=int(input("enter a number:"))


