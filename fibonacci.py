num = int(input("Digite o número: "))

firstValue = 0
secondValue = 1
value = 0
belong = False
while value <= num:
	if value == num:
		belong = True
	value = firstValue + secondValue
	firstValue = secondValue
	secondValue = value

if belong:
	print("O número pertence a sequencia!")
else:
	print("O número nao pertence a sequencia...")