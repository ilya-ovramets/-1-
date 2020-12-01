#1) Знайти голоснілітери, які не містяться у рядку.
text = "Сивочолий чернець Нестор, схилившись над столом, пише історію свого народу.\r Цей епізод, увічнений у мармурі, – красномовне свідчення того, що люди здавна\r прагнули зберегти інформацію для своїх нащадків."
i = 0
lenght = len(text)
word_dict = " аоеуєюіїяи";
response = "аоеуєюіїяи";
while i < lenght:
	letter = text[i];
	if (word_dict.find(letter) > 0):
		response = response.replace(letter, "");
	i = i + 1;
# golos=gol.intersection[tab]
print(f"Відповідь: {response}"); 