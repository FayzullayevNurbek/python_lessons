def users(name,surname,tug_joyi,email="",phone_nomer=None,age=None):
   users_information={'name':name,
        'surname':surname,
        'tug_joyi':tug_joyi,
        'email':email,
        'phone_nomer':phone_nomer,
        'age':age}
   return  users_information
   
   
customers=[]
print('list customer`s base:')
while True:
        print('\n enter costumer`s information:')
        name=input('enter costumer`s name:')
        surname=input('enter costumer`s surname:')
        tug_joyi=input('enter costumer`s born village:')
        email=input('enter costumer`s email:')
        phone_nomer=int(input('enter costumer`s phone nomer:'))
        age=int(input('enter costumer`s age:'))
        customers.append(users(name,surname,tug_joyi,email,phone_nomer,age))
        w=input('Do you want to add again costumers:"yes/no"')
        if w.lower()=='no':
            break

print("Costumers:")
for x in customers:
   print(f'{x["name"]} {x["surname"]}, '
   f'{x["tug_joyi"]} da tu`gilgan ,'
   f'\nEmail:{x["email"]} \nPhone nomer: {x["phone_nomer"]}')

