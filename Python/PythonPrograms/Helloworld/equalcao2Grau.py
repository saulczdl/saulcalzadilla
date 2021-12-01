# Equacao de 2 grau:
print("Equacao de 2 grau:")
a = int(input("Primeiro item:"))
b = int(input("Segundo item:"))
c = int(input("Terceiro item:"))
# Delta
delta = b ** 2 - 4 * a * c
#equal = a ** 2 + 2 * b + c
if delta < 0:
    print("""Delta negativo: {0}
Nenhuma das duas raízes desta função é um número real.""". format(delta))
    exit()
else:
    x1 = (-b + (delta ** (1 / 2))) / (2 * a)
    x2 = (-b - (delta ** (1 / 2))) / (2 * a)
    print("Resultado de Delta:", delta)
    print("X1=", x1, "X2=", x2)
# pode ser feito tudo no print, ao invés de criar as variáveis X1 e X2, porém o codigo fica um pouco confuso.
    print("X1linha= {0} e X2linha= {1}.".format((-b + (delta ** (1 / 2))) / (2 * a), (-b - (delta ** (1 / 2))) / (2 * a)))
    exit()
