a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a>=b and b>=c:
    w=c
    c=a
    a=w
    print(f'{a}<{b}<{c}')
elif a>=b and a<=c:
     w=b
     b=a
     a=w
     print(f'{a}<{b}<{c}')
elif b>=a and a>=c:
     w=c
     c=b
     b=a
     a=w
     print(f'{a}<{b}<{c}')
elif b<=c and c<=a:
     w=a
     a=b
     b=c
     c=w
     print(f'{a}<{b}<{c}')
else :
     print(f'{a}<{b}<{c}')
