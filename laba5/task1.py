#Знайти  максимум  і  мінімум  функції y=3x**3–2x+1для  аргументу,  що #змінюється в діапазоні [A; B]з кроком 0,0005.

A, B = 2.1, 7.4              #Значення А,В

dx = 0.0005                  #Крок числа
y = 0;
x = A;
mins = None;
maxs = None;
while x <= B:
	y = 3 * (x**3) - 2 * x + 1;       #Функція
	if (mins is None or maxs is None):
		mins = y; maxs = y
	#print(y, "|", x)                 #Усі значення у при змінній х
	if (y >= maxs):
		maxs = y;
	if (y <= mins):
		mins = y;
	x += dx                           #Збільшення числа х на установлений крок

# print(result)

print("Максимальное: %.6f\r\nМинимальное: %.6f" % (mins, maxs));