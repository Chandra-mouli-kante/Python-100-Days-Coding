'''
1)
a=[2,3,5,6]
b=[7,6]

Output: 
a=[2,3,5,6,7]
'''
#Code:
'''
a=[2,3,5,6]
b=[7,6]
for i in b:
    if i not in a:
        a.append(i)
print(a)
'''


'''
2)
[2,0,5,0,4,5]
output:
[2,5,4,5,0,0]
'''
#Code:
'''
a=[2,0,5,0,4,5]
for i in range(len(a)):
    if a[i]==0:
        a.pop(i)
        a.append(0)
print(a)
'''

#3)Code:
'''
a={1:5,2:6,3:7}
for i in a.keys():
    print(i)

a={1:5,2:6,3:7}
for i in a.keys():
    print(i,a[i])

a={1:5,2:6,3:7}
for i in a.values():
    print(i)

a={1:5,2:6,3:7}
for i,j in a.items():
    print(i,j)
'''

#4)Code:
a=[i for i in range(5)]
print(a)

a=[i for i in range(5) if i!=2]
print(a)

a=[]
for i in range(5):
    if i!=2:
        a.append(i)
print(a)
    
