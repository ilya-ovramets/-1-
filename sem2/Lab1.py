def kvadrat(x1,y1,x2,y2,storona,vidp = "rrr"):
	if x1 == x2 and y1 == x2:
		vidp = "Квадрати співпадають"
	while: x1 < x2:
		
	elif x1 + storona + 1 == x2 or y1 - storona - 1 == y2:
		vidp = "Квадрати торкаються"
	else:
		vidp = "Квадрати не співпадають"
	print(vidp)
	return vidp
kvadrat(2,5,4,4,3)
