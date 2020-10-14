#a=list(map(int,input().split()))
a=[1,1,4,2,1,3]
b=sorted(a)
c=0
for i in range(len(a)):
    if a[i]!=b[i]:
        c+=1
print(c)
