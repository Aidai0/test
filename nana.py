'''
if True:
    print('hello')
''' 
'''
a = 10
b = 5
if a > b:
   print(True)
else:
   print(False)
'''
'''
a = input('Выберите язык: EN RU KG:')
if a == 'EN':
    print('Hello')
elif a == 'RU':
    print('Привет')
elif a =='KG':
    print('Салам')
else:
    print('Такого языка нет')
'''
'''
a = 40
b = 20 
c = 10
if a == b and a > c:
    print('True')
else:
    print('False')
'''
age = int(input('Ведите ваш возраст'))
if age < 18 and age > 12:
    print('Вы подросток')
elif age >= 18:
    print('Вы совершеннолетний,входите')
else:
    print('Вы ребенок')
