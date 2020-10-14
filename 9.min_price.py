#a=list(map(int,input().split()))
p=[8,4,6,2,3]
l=[]
for i in range(len(p)):
    for j in range(i+1,len(p)):
        if p[i]>p[j]:
            l.append(p[i]-p[j])
            break
    else:
        l.append(p[i])
print(l)
    
