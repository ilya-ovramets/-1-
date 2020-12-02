#1) Знайти голоснілітери, які не містяться у рядку.
text = "Прамичгс раг рррррррр нннннннннннн гггггг шшшш щ ззззззщ   щщщщщщщ шшшшшшшш шгггг ннн "
i = 0
lenght = len(text)
word_dict = " аоеуєюіїяи";
response = "аоеуєюіїяи";
while i < lenght:
	letter = text[i];
	if (word_dict.find(letter) > 0):
		response = response.replace(letter, "");
	i = i + 1;
print(f"Відповідь: {response}"); 