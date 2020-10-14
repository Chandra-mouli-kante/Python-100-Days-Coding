'''
1)
2 3 1 5 4
inc-dec-inc-dec-inc
output:
True
'''
#Code:
'''
a=[2,3,1,5,3]
status=True
for i in range(len(a)-1):
    if a[i]<a[i+1] and i%2==0:
        status=True
    elif a[i]>a[i+1] and i%2==1:
        status=True
    else:
        status=False
        break
print(status)
'''


'''
2)
input:
[2,3,4,1,6,7,8,0]
if n=len(a)/2
   n=4
Output:
[2,6,3,7,4,8,1,0]
'''
#Code:
'''
a=[2,3,4,1,6,7,8,0]
#a= list(map(int,input().split()))
n=len(a)//2
l=[]
for i in range(n):
    l.extend([a[i],a[i+n]])
print(l)
'''

'''
3)
input:
[8,1,2,2,3]
we need to print no.of ele less than n(consider) in an order
Output:
[4,0,1,1,3]
'''
#Code:
a=[8,1,2,2,3]
print(a)
#a=list(map(int,input().split()))
l=[]
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[j]<a[i]:
            c+=1
    l.append(c)
print(l)
