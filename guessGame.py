# Guess game 
# finding name
import random 
count=1
x=' '
while x!='no':
    number=random.randint(0,10)
    print('I`m computer and I thought one number:')
    n=int(input(print('you may enter [0:10] numbers that I thought>>>')))    
    while n!=number:
        if number>n:
            print('Sorry! you can`t fint it ')
            n=int(input('you must enter bigger number>>>'))
            count+=1
        elif number <n:
            print('you can`t find it')
            n=int(input('you must enter lower number'))
            count+=1
    print(f'Congralations you find  hiding number {count} times')
    c=count
    count=1
    print(f'I`m turn and I must think one number and computer find it')
    my_number=int(input(' My number>>> '))
    second_count=1
    while my_number!=number:
        if my_number>number:
            print(f'Sorry! computer can`t fint it,'
            f'/ncomputer enter bigger number')
            second_count+=1
            number=random.randint(my_number,10)
        else:
            print(f'Sorry! computer can`t fint it '
            f'computer enter lower number')
            second_count+=1
            number=random.randint(0,my_number)
    print(f'Congralations computer find  hiding number {second_count} times')
    sc=second_count
    second_count=1
    x=input('Do you want to continue game (yes/no)>')
if c<sc:
    print(f'congralations!!! you win game -{c} times'
        f'computer -{sc}')
elif sc<c:
      print(f'Sorry!!! computer win game -{sc} times'
        f'you -{c}')
else:print(f' you two win -{c}')

            
            

