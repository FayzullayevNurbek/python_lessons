
import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if (a+b)>c and (a+c)>b and (c+b)>a:
   if a==b and b==c:
       print(3)
   elif (a==b and a!=c) or (a==c and b!=a):
        print(2)   
   else:print(1)
else: print(0)
print('stop')    