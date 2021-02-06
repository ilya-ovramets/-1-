def kvadrat(x1,y1,x2,y2,storona,vidp = "rrr"):
  iter_y = y1
  iter_y2 = y2
  if x1 == x2 and y1 == y2:
    vidp = "Квадрати співпадають"
  elif x1 != x2 and y1 != y2:
    while x1 < ( x1 + storona):
      while iter_y > (y1 - storona):
        if (x1 <= x2 + storona and x1 <= x2) and (iter_y >= y2 - storona   and iter_y >= y2):
          vidp = "Квадрати перетинаються"
    x1 +=1
      
  elif  x1 != x2 and y1 != y2:
    while x2 < ( x2 + storona):
      while iter_y2 > (y2 - storona):
        if (x2 <= x1 + storona and x2 <= x1) and (iter_y2 >= y1 - storona   and iter_y2 >= y1):
          vidp = "Квадрати перетинаються"
  elif  x1 != x2 and y1 != y2:
    while x1 < x1 + storona:
      if (y - storona-1) == y2 and x1 >= x2 or x1 == x2 

	
					



		
	
kvadrat(2,5,4,4,3)
