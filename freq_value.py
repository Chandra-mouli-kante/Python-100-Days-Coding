a=[1,2,3,4]
l=[]
for i in range(0,len(a),2): #0,2
    l.extend([str(a[i+1])]*a[i]) #['1']*1=['1',]
print(l)
