# Задание (Вариант 1): последовательность их 5-ти чисел x1-x5, необходимо найти два наибольших и два наименьших значения
# [12, 44, 46, 78, 99]
x1 = int(input('Введите x1: '));
x2 = int(input('Введите x2: '));
x3 = int(input('Введите x3: '));
x4 = int(input('Введите x4: '));
x5 = int(input('Введите x5: '));

z = min(x1,x2,x3,x4,x5)
y = max(x1,x2,x3,x4,x5)
print("Мінімальное 1",z)
if z <= x1 and x1 < x2 and x1 < x3 and x1 < x4 and x1 < x5:
  print("Мінімальное 2",x1)
if z <= x2  and x2 < x3 and x2 < x4 and x2 < x5:
  print("Мінімальное 2",x2)
if z <= x3 and x3 < x1 and x3 < x4 and x3 < x5:
  print("Мінімальное 2",x3)
if z <= x4 and x4 < x1 and x4 < x2 and x4 < x5:
  print("Мінімальное 2",x4)  
if z <= x5 and x5 < x1 and x5 < x2 and x5 < x3 and x5 < x4:
  print("Мінімальное 2",x5)  
"""  
print("Максимальне 1",y)
if y > x1 and x1 > x2 and x1 > x3 and x1 > x4 and x1 > x5:
  print("Максимальне 2",x1)
if y > x2 and x2 > x3 and x2 > x4 and x2 > x5:
  print("Максимальне 2",x2)
if y > x3 and x3 > x1 and x3 > x4 and x3 > x5:
  print("Максимальне 2",x3)
if y > x4 and x4 > x1 and x4 > x2 and x4 > x5:
  print("Максимальне 2",x4)  
if y > x5 and x5 > x1 and x5 > x2 and x5 > x3:
  print("Максимальне 2",x5) 
"""     