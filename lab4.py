A, B = 2.1, 7.4              #Значення А,В

dx = 0.0005                  #Крок числа
y = 0;
x = A;
result = [];
while x <= B:
	y = 3 * (x**3) - 2 * x + 1;       #Функція
	#print(y, "|", x)                  #Усі значення у при змінній х
	x += dx                           #Збільшення числа х на установлений крок
  if x == A:
	  print("Мінімальне:",y)
  if x == B:
	  print("Максимальне",y)	
	#result.append(y);                 #Записування усіх результатів
# print(result)
#print("Максимальное: %.6f\r\nМинимальное: %.6f" % (max(result), min(result)));                  #Результат
