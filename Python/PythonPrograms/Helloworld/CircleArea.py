print("Área do Círculo")
r = float(input("Qual é o diâmetro do cilindro em centímetros?  "))
# r = int(.... declara número inteiro (sem virgula)
area = (r/2) ** 2 * 3.1415
print("A área do base do cirulo é: ", area)
print("Litros do cilindro")
a = float(input("Qual é a altura do cilindro?"))
print("O Cilindor possui em litros: ", (area * a / 1000), "litros")
exit()
