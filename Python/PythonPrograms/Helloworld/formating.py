for raiz in range(1, 13):
    print("No.  {0:2} squared is {1:3} and cube is {2:4}".format(raiz, raiz ** 2, raiz ** 3))
print()
for raiz in range(1, 13):
    print("No.  {0:2} squared is {1:<3} and cube is {2:<4}".format(raiz, raiz ** 2, raiz ** 3))

print()
for raiz in range(1, 13):
    print("No.  {0:2} squared is {1:<3} and cube is {2:^4}".format(raiz, raiz ** 2, raiz ** 3))

print()

print("Pi is approximately {0:<12}".format(22 / 7))
print("Pi is approximately {0:<12f}".format(22 / 7))
print("Pi is approximately {0:<12.50f}".format(22 / 7))
print("Pi is approximately {0:<52.50f}".format(22 / 7))
print("Pi is approximately {0:<62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))
