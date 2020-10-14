a=[2,3,5,1,3]
x=3
l=[]
for i in a:
    if i+x>=max(a):
        l.append(True)
    else:
        l.append(False)
print(l)


#Method 2:
a=[2,3,5,1,3]
x=3
m=max(a)
l=[True if i+x>=m else False for i in a]
