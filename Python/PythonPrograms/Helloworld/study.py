print("Hello World", (int(2)))
print("This string \nis split\n in \nseveral \nlines")
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)
print("a\tb\tc\td\te\tf")
age = 22
# age = str(age)
name = "Saul"
print(name + " " + str(age) + " anos.")
print(f"name {37}")
# Teste de Print
# Positions
print("\n \n \n \n")
# print(input("Digite Ok"))
stringTest = "O Pergaminho Secreto dos Kouga"
print(stringTest[0] + stringTest[-5])
print(stringTest[2:5] + stringTest[18:-10])
print(stringTest[13:15] + stringTest[16] + " " + stringTest[-5:])
print(stringTest[0::2])  # Slice o começo ao final de 3 em 3.| [0: ->começo | : : -> até o final
# ou poderia colocar 29 | :3
print(stringTest[29:-6:-1])  # Inverso imprimindo Kouga ao inverso.
print(stringTest[-1:-4:-1] + stringTest[-1])  # Inverso imprimindo Kouga ao inverso.
# Fazendo operações matemáticas e substituições.
print(stringTest[5 * 3 - 15] + stringTest[20 - (5 ** 2)])
print("""
Em pleno Período Edo, Ieyasu Tokugawa precisava nomear seu sucessor. Diante da
indecisão entre dois herdeiros, o poderoso xogum resolveu promover um duelo entre entre
duas grandes familias de ninjas, "Kouga" e "Iga".""")
# clan = input("Qual o nome do Clã?")
# print(clan in stringTest) # Verifiacar forma de evitar que aceite espaco ou não digitar nada.
# print("Kouga" in clan)
# print(input("Digite Ok"))
print(r"\c:\Windows \home\saul http://www.hardnet.com.br" + r'teste barra teste entre "barras" pronto')
# print(f" O nome do Clã é: {clan} mais R${100 / 25:12.50f} pontos")
# INTERPOILATION
weigh = int(input("How much do you weigh?"))
tall = int(input("How tall are you?"))
icm = weigh / tall
print("My ICM is %f, my age is %d end my name is %s." % (weigh / tall, age, name))
computer = ["monitor", "mouse", "teclado"]
print(computer[0], computer[2])
print(name * 3)
print(
    "Os dias da semana são: {0}, {1}, {2}, {3}, {4}, {5}. {6}".format("Domingo", "Segunda", "Terça", "Quarta", "Quinta",
                                                                      "Sexta", "Sabado"))
print()

a = 2
b = 1
primeiroGrau = (-b) / a
print(primeiroGrau)


import numpy

for x in numpy.arange(-5, 5, 0.1):
    print("f(x): 2X+1 = 0 ({1:5.1f}) -> {0:5.1f}".format(a * x + b, x))
    print('{0:.1f}'.format(x))
    c = a * x + b
    print("{0:.1f}".format(c))

for j in range(100):
    print(j, end="\t")


exit()
