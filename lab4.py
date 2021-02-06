"""
def diap(minis, maxis, condition):
  maxd = max(a1, a2, a3, a4, a5, b1, b2, b3, b4, b5);
  mind = min(a1, a2, a3, a4, a5, b1, b2, b3, b4, b5);
  if (maxd >= minis and maxd <= maxis) and (mind >= minis and mind <= maxis):
    print(f'Все значения подходят под параметр {condition}');
  else:
    print(f'Условие не подходят под параметр {condition}');
while True:
  a1 = int(input('Введіть значення a1:'))
  a2 = int(input('Введіть значення a2:'))
  a3 = int(input('Введіть значення a3:'))
  a4 = int(input('Введіть значення a4:'))
  a5 = int(input('Введіть значення a5:'))
  b1 = int(input('Введіть значення b1:'))
  b2 = int(input('Введіть значення b2:'))
  b3 = int(input('Введіть значення b3:'))
  b4 = int(input('Введіть значення b4:'))
  b5 = int(input('Введіть значення b5:'))


#Параметры
diap(0, 122, 'возраст');
diap(0, 768, 'давление');
diap(45, 210, 'рост');
diap(2800, 200000, 'вес человека в граммах');
diap(31, 49, 'размер обуви');
diap(21021, 21021, 'почтовый индекс Винницы');
diap(1, 118, 'таблиця Мінділєєва');
"""
# while True:
#   a1 = int(input('Введіть значення a1:'))
#   a2 = int(input('Введіть значення a2:'))
#   a3 = int(input('Введіть значення a3:'))
#   a4 = int(input('Введіть значення a4:'))
#   a5 = int(input('Введіть значення a5:'))
  
#   b1 = int(input('Введіть значення b1:'))
#   b2 = int(input('Введіть значення b2:'))
#   b3 = int(input('Введіть значення b3:'))
#   b4 = int(input('Введіть значення b4:'))
#   b5 = int(input('Введіть значення b5:'))

#   maxd = max(a1, a2, a3, a4, a5, b1, b2, b3, b4, b5);
#   mind = min(a1, a2, a3, a4, a5, b1, b2, b3, b4, b5);

#   if (maxd >= 0 and maxd <= 122) and (mind >= 0 and mind <= 122):
#     print(f'Все значения подходят под параметр возраст');
#   else:
#     print(f'Условие не подходят под параметр возраст');
#   if (maxd >= 0 and maxd <= 768) and (mind >= 0 and mind <= 768):
#     print(f'Все значения подходят под параметр давление');
#   else:
#     print(f'Условие не подходят под параметр давление');
#   if (maxd >= 45 and maxd <= 210) and (mind >= 45 and mind <= 210):
#     print(f'Все значения подходят под параметр рост');
#   else:
#     print(f'Условие не подходят под параметр рост');
#   if (maxd >= 2800 and maxd <= 200000) and (mind >= 2800 and mind <= 200000):
#     print(f'Все значения подходят под параметр вес человека в граммах');
#   else:
#     print(f'Условие не подходят под параметр вес человека в граммах');
#   if (maxd >= 31 and maxd <= 49) and (mind >= 31 and mind <= 49):
#     print(f'Все значения подходят под параметр размер обуви');
#   else:
#     print(f'Условие не подходят под параметр размер обуви')
#   if (maxd >= 21021 and maxd <= 21021) and (mind >= 21021 and mind <= 21021):
#     print(f'Все значения подходят под параметр почтовый индекс Винницы');
#   else:
#     print(f'Условие не подходят под параметр почтовый индекс Винницы')    
#   if (maxd >= 1 and maxd <= 118) and (mind >= 1 and mind <= 118):
#     print(f'Все значения подходят под параметр таблиця Мінділєєва');
#   else:
#     print(f'Условие не подходят под параметр таблиця Мінділєєва')
  

def obmen(a,b,vidp = "Щось"):         
  dol=a*28.18                             
  evr=b*1.18*28.18                     #Розрахунки
  grn=a*b
  if dol>evr and dol>grn:                    #Порівняння долара
    vidp = "A-доларів більше:"
  elif evr>dol and evr>grn:                  #Порівняння євро
    vidp = "B-євро більше:"
  else:
    vidp = "A*B гривень більше:"
  print(vidp);
  return vidp;

def poriv(a,b,c,d,e):
  sum_al = a+b+c+d+e
  dob_al = a*b*c*d*e
  list_caunt = [a,b,c,d,e]
  sum_h = 0
  dob_h = 0
  i = 0
  for i in range(len(list_caunt)):
    if list_caunt[i] == sum_al - list_caunt[i]:
      sum_h += 1
    if list_caunt[i] == (dob_al / list_caunt[i]):
      dob_h += 1
  print(f"""Чисел шо рівні сумі ={sum_h}
  Чисел шо рівні добутку ={dob_h} """)

poriv(2,2,2,2,8)
