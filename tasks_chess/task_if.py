k=int(input('[1;8]_k=>>>'))
l=int(input('[1;8]_l=>>>'))
m=int(input('[1;8]_m=>>>'))
n=int(input('[1;8]_n=>>>'))
if k%m==0 or l%n==0:
   print('ruh can jump firs time at the given point')
else: print(f"first option {m,l}, second option {k,n}")

