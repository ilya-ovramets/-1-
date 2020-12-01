#1) Знайти голоснілітери, які не містяться у рядку.
s=("Сивочолий чернець Нестор, схилившись над столом, пише історію свого народу.\r Цей епізод, увічнений у мармурі, – красномовне свідчення того, що люди здавна\r прагнули зберегти інформацію для своїх нащадків.")
i = 0
l = len(s)
tab=[]
gol=["а","о","е","у","є","ю","і","ї","я","и"]

while i < l:
  c = s[i]
  if c == "а" or c == "A":
    tab.append(c)
  if c == "о" or c == "О":
    tab.append(c)  
  if c == "е" or c == "E":
    tab.append(c) 
  if c == "у" or c == "У":
    tab.append(c)
  if c == "є" or c == "Є":
    tab.append(c)
  if c == "ю" or c == "Ю":
    tab.append(c)
  if c == "і" or c == "І":
    tab.append(c)
  if c == "ї" or c == "Ї":
    tab.append(c)
  if c == "я" or c == "Я":
    tab.append(c)  
  if c == "и":
    tab.append(c)  
  i=i+1
golos=gol.intersection[tab]
print("Відповідь:",golos)  