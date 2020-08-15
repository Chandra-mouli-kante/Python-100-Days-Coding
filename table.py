'''
n=int(input("Enter a number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)
'''


'''
n=int(input("Enter a number:"))
r=int(input("Enter the range:"))
for i in range(1,r+1):
    print(n,"*",i,"=",n*i)
'''

'''
n=int(input("Enter a number:"))
r1=int(input("Enter the starting range:"))
r2=int(input("Enter the ending range:"))
for i in range(r1,r2+1):
    print(n,"*",i,"=",n*i)
'''



n=int(input("Enter a number:"))
r1=int(input("Enter the starting range:"))
r2=int(input("Enter the ending range:"))
if(r1<r2):
    for i in range(r1,r2+1):
        print(n,"*",i,"=",n*i)
else:
    for i in range(r1,r2-1,-1):
        print(n,"*",i,"=",n*i)
