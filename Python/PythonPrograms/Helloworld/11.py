for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

for i in range(0, 21):
    if i % 3 != 0 and i % 5 != 0: # que não são divisiveis por 3 e 5
        print(i)
for i in range(0, 21):
    if i % 3 == 0 or i % 5 == 0:
        continue# desconsidera, ppula o item que saisfaz a condição.
    print(i)