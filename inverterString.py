string = "ola, mundo!"

#transforma em uma lista
string = list(string)


for c in range(len(string) -1, -1, -1):
	print(string[c], end="")