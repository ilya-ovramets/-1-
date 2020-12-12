"""
s = int(input('Введіть кількість студентів-->'))
y=1
nemes = []
manis = []
while y <= s:
	neme = input('Введіть Прізвище студента-->')
	nemes.append(neme)
	mani = input('Введіть річний бал-->')
	manis.append(mani)
	y += 1
for i in range(len(nemes)):
	print(f'{nemes[i]} - {manis[i]}')


#text=input("Введіть текст--//")
#
#print(text[::-1])
"""
s = int(input('Виберіть пункт'))

if s == 1:
	