'''
5
2 3 5
1 2 3  - super prime


7
2 3 5 7
1 2 3 4 - not a super prime
'''


def prime(n):
   for i in range(2,n):
       if(n%i==0):
           break
   else:
       return(1)
n=int(input("enter number:")) #5
cnt=0
if(prime(n)==1): #True
   print(n,"is prime")
   for i in range(2,n+1): #(2,3,4,5) 2
       if(prime(i)==1):
            cnt+=1#1,2,3
   if(prime(cnt)==1 and n>2):
       print(n,"is super prime")
   else:
       print(n,"is not super prime")
else:
       print(n,"is not prime")
