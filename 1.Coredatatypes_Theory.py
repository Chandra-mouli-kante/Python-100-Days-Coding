
#Core data types:
'''
List:
    mutable
    declare: a=[1,2,3]
    access:  a[1],a[1:4]
    modify:  a[1]=100
           a.append(8),a.extend([45,65]),a.insert(1,45)
    delete:  del a[2],del a[2:5]
           a.pop(),a.pop(2),del a
           a.clear()
           
Tuple:
    immutable- cannot be changed
    declare: a=(1,2,3,4)
    access:  a[1]
    modify: not possible
    deletion not possible
    del a - entire deletion is possible

set:
    mutable
    Unorderd lists without duplicates
    a={1,2,3,4}
    index accessing is not possible
    adding ele: a.add(ele)
                a.update({2,3,99})
    delete:  del a - entire set is deleted
    
dictionary:
    key&value pair
    a={1:23,2:34,3:45}    
    access: a[key]
    modify: a[key]=new value,a[key]=update value, a.update({key:value,key:value})
    deletion: del a, del a[key]
'''

#Adding elements into dict:
#METHOD-1:
'''
a={}
for i in range(2): #keys
    k=input("enter a key:") #s1
    v=[]
    for j in range(2): #values
        m=int(input("enter marks: "))
        v.append(m) #[34,54]
    a[k]=v #a['s1']=[34,54],a['s2']=[65,54]
print(a)
'''

#METHOD-2:
'''
a={}
n=int(input("enter key count:"))
for i in range(1,n+1): #keys
    k=input("enter a key:") 
    v=[]
    p=int(input("enter a value count:"))
    for j in range(p): #values
        m=int(input("enter marks: "))
        v.append(m)
    a[k]=v 
print(a)
'''

#METHOD-3:
a={}
n=int(input("enter key count:"))
for i in range(1,n+1):
    k=input("enter a key:")
    a[k]=list(map(int,input().split()))
print(a)
