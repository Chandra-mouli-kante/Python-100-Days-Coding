'''
Bitwise xor operator: Returns 1 if one of the bit is 1 and other
                        is 0 else returns false.
a = 10 = 1010 (Binary)
b = 4 =  0100 (Binary)

a ^ b = 1010
         ^
        0100
      = 1110
      = 14 (Decimal)
'''
#Code:
n=5
s=0
x=0
for i in range(n):
    x^=s+(2*i)
print(x)


