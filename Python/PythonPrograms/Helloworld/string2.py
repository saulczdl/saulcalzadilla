parrot = "Norwegian Blue"

print(parrot)
    # print positinons
print(parrot[3])
print(parrot[0])
print()
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print()
    # print negatives positions
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()
    # print operation
print(parrot[3 - 14])
print(parrot[2 + 3])
print(parrot[2 * 3])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])
    # Slicing
print(parrot[0:6])
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])
print(parrot[10:])
print(parrot[:6] + parrot[6:])
print(parrot[:])
    # inverse
print(parrot[-4:-2])    #Bl
print(parrot[-4:12])    #Bl

print(parrot[0:6])
print(parrot[-14:-8])

print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223;373:036 854,775;807"
print(number[1::4])
seperators = number[1::4]
print(seperators)
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])