#def diap(minis, maxis, condition):
#  maxd = max(a1, a2, a3, a4, a5, b1, b2, b3, b4, b5);
#  mind = min(a1, a2, a3, a4, a5, b1, b2, b3, b4, b5);
#  if (maxd >= minis and maxd <= maxis) and (mind >= minis and mind <= maxis):
#    print(f'Все значения подходят под параметр {condition}');
#  else:
#    print(f'Условие не подходят под параметр {condition}');

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

  maxd = max(a1, a2, a3, a4, a5, b1, b2, b3, b4, b5);
  mind = min(a1, a2, a3, a4, a5, b1, b2, b3, b4, b5);

  if (maxd >= 0 and maxd <= 122) and (mind >= 0 and mind <= 122):
    print(f'Все значения подходят под параметр возраст');
  else:
    print(f'Условие не подходят под параметр возраст');
  if (maxd >= 0 and maxd <= 768) and (mind >= 0 and mind <= 768):
    print(f'Все значения подходят под параметр давление');
  else:
    print(f'Условие не подходят под параметр давление');
  if (maxd >= 0 and maxd <= 45) and (mind >= 0 and mind <= 210):
    print(f'Все значения подходят под параметр рост');
  else:
    print(f'Условие не подходят под параметр рост');    
  # Параметры
  #diap(0, 122, 'возраст');
  #diap(0, 768, 'давление');
  #diap(45, 210, 'рост');
  #diap(2800, 200000, 'вес человека в грамма');
  #diap(31, 49, 'размер обуви');
  #diap(21021, 21021, 'почтовый индекс Винницы');
  #diap(1, 118, 'таблиця Мінділєєва');

