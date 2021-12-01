for i in range(10, 21):
    print(" i é now {}!".format(i))

for i in range(0, 10, 2):
    print(" i é now {}!".format(i))

for i in range(10, 0, -2):
    print(" i é now {}!".format(i))

age = int(input("How older is you? "))
# if age >=  16 and age <= 60: # True and True
# if 16 <= age <= 65:
if age in range(16, 66):
    print("Have a good day at work!")
else:
    print("Enjoy your free time!")
exit()