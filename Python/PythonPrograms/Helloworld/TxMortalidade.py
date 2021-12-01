print("Cálculo de Taxa de Mortalidade do Vírus Corona:")
deads = float(input("Qual a quantidade de mortos pelo Corona Vírus?"))
infected = float(input("Quantos foram infectados pelo corona vírus?"))
print("A quantidade de mortos é de:", deads, "\n", "Equivalente a uma taxa de: %", deads / infected * 100)
print(f"A quantidade de mortos é de: {deads} \n Equivalente a uma taxa de: % {deads / infected * 100:12.50}")
tx = deads / infected * 100
print(f"A quantidade de mortos é de: {deads} \n Equivalente a uma taxa de:  {tx:12.50} %")
exit()