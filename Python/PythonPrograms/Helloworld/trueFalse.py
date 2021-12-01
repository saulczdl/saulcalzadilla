day = "Monday"
temperature = 30
raining = False

if day == "Saturday" and temperature > 27 and not raining:
    print("Go swimming")
else:
    print("Learn Python")

print("=*" * 70)

if (day == "Monday" and temperature > 31) or not raining:
    print("Go swimming")
else:
    print("Learn Python")

print("=*" * 70)

#       True                True           False + False = True
if day == "Monday" and (temperature > 31 or not raining):
    print("Go swimming")
else:
    print("Learn Python")

if 0:
    print("True")
else:
    print("False")

print("Please enter your name: ")
name = input()
#if name:
if name != "":
    print("Hello, {}!".format(name))
else:
    print("Are you the man with no name?")