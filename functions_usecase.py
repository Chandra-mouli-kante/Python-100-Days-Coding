'''
a=10
print(a,'1')    #10
def ex():
    a=10
    a+=1
    print(a,'2')    #11
ex()
print(a,'3')    #10
'''

'''
a=10
print(a,'1')    #10
def ex():
    global a
    a=10
    a+=1
    print(a,'2')    #11
ex()
print(a,'3')    #10
'''


'''
def sum_digits(n):
    s=0
    while n>0:
        rem=n%10
        s+=rem
        n//=10
    return s
n=int(input("enter n:"))
print(sum_digits(n))
'''

'''
n=input("enter n:")
s=0
for i in n:
    s+=int(i)
print(s)
'''


def is_armstrong(n):
    arm=0
    n1=n
    while n>0:
        rem=n%10
        arm+=rem*rem*rem
        n//=10
    if n1==arm:
        return("Armstrong number")
    else:
        return("Not a armstrong number")aa
n=int(input("enter n:"))
print(is_armstrong(n))

