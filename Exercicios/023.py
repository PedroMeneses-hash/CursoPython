numero = int(input("Digite um número:"))
numeroString = str(numero)
print('Milhar:', numeroString[0])
print('Centena:', numeroString[1])
print('Dezena:', numeroString[2])
print('Unidade:', numeroString[3])

unidade = numero // 1 % 10
print(unidade)
dezena = numero // 10 % 10
print(dezena*10)
centena = numero // 100 % 10
print(centena*100)
milhar = numero // 1000 % 10
print(milhar*1000)
