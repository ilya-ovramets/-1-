def intersection(quadro1, quadro2):
	# область локальных перменных
	x1b = quadro1["x"];
	x2b = quadro2["x"];
	y1b = quadro1["y"];
	y2b = quadro2["y"];
	# Область вычисляемых переменных
	x1e = x1b + quadro1['side'] - 1;
	y1e = y1b - quadro1['side'];
	x2e = x2b + quadro2['side'] - 1;
	y2e = y2b - quadro2['side'];
	# Проверяем, равны ли квадраты
	if (x1b == x2b and y1b == y2b and quadro1['side'] == quadro2['side']):
		return "Квадрати спiвпадають";
	# Определяем ОДЗ для работы с кубиками
	if ( 
	x1e - x2e >= -quadro1['side'] 
	and x1e - x2e <= quadro1['side']
	and y1e - y2e >= -quadro1['side'] 
	and y1e - y2e <= quadro1['side']
	and x1e - x2e <= quadro2['side']
	and x1e - x2e >= -quadro2['side']
	and y1e - y2e <= quadro2['side']
	and y1e - y2e >= -quadro2['side']
	):
	# Если второй квадрат входит в ОДЗ первого квадрата - вызываем функцию, для проверки координат, чтобы сверить условия воприкосновения
		if (x2e - x1e <= quadro2['side'] and x2b - x1b < quadro1['side']):
			return "Квадрати пертинаються";
		else:
			return "Квадрати торкаються";
		# добавить условия
	else:
		return "Квадрати не перетинаються";


# Вызываем функцию с необходимыми параметрами
print( intersection({"x": -5, "y": 4, "side": 4}, {"x": -8, "y": 5, "side": 4}) )