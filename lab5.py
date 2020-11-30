#В  діапазоні [A;  B)  знайти  кількість  цілих  чисел,  які  можуть  #вважатися високосними роками.
#Знайти  максимум  і  мінімум  функції y=3x**3–2x+1для  аргументу,  що #змінюється в діапазоні [A; B]з кроком 0,0005.

import math;
A, B = 2.1, 7.4              #Значення А,В

dx = 0.0005                  #Крок числа
y = 0;
x = A;
result = [];
while x <= B:
	y = 3 * (x**3) - 2 * x + 1;       #Функція
	#print(y, "|", x)                  #Усі значення у при змінній х
	x += dx                           #Збільшення числа х на установлений крок
	result.append(y);                 #Записування усіх результатів
# print(result)
print("Максимальное: %.6f\r\nМинимальное: %.6f" % (max(result), min(result)));                  #Результат

#13Серед усіх чисел діапазону [0; A]знайти кількість чисел, сума цифр яких є квадратом цілого числа. Також знайти середнєарифметичне таких чисел.
#14Серед  усіх  чисел  діапазону [0; A]знайти  кількість  чисел,  із  цифр  яких можна скласти непарне число, що є дільником числа A**2. 
# 0; A
# 1) X = A**(1/2)
# 2) X % 1 == 0 - корень
# 3) X % 1 != 0 - просто число
#14Серед  усіх  чисел  діапазону [0; A]знайти  кількість  чисел,  із  цифр  яких можна скласти непарне число, що є дільником числа A**2. 
'''
A = 987;                         #Значення А
i = 0;
cnt = 0;
while(i <= A):
	_temp = list(str(i));               #Створення змінної _temp
	_summ = 0;
	for j in _temp:
		_summ += int(j);
	if(_summ % 2 == 1):                  #Условіє що відкидає всі непарні числа
		if( A*A % (_summ % 2 == 1) == 0): #Виконує перевірку умови задачі
			cnt += 1;                        #Розрахунок кінцевої кількості чисел
		
	i += 1;
print("Число А:",A)
print("Кількість  чисел,  із  цифр  яких можна скласти непарне число, що є дільником числа A**2:",cnt)
'''