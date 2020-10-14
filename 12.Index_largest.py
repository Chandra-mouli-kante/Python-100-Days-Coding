a=[3,6,1,0]
m=max(a)
b=a.copy()
b.pop(a.index(m))
c=0
for i in b:
    if m>=2*i:
        c+=1
if c==len(b):
    print(a.index(m))
else:
    print(-1)
