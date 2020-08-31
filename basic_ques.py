'''
19= sum of2 primes
19=17+2

13=11+2
'''

'''
import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
       if n%i==0:
           break
   else:
       return n
def primesum(n):
    if(prime(n) and prime(n-2)):
        return(n-2,2)
n=int(input("enter a number:"))
print(primesum(n))
'''



'''
     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
'''


def Pattern(n): #5
    for i in range(n):  #0,1
        print(("* "*(i+1)).center(2*n)) #* ,
    for i in range(n-1,0,-1):
        print(("* "*(i)).center(2*n))
n = int(input("enter n:"))
Pattern(n)


