print("What's your name?")
name = input()

print("How older is you?")
age = int(input())

if 18 <= age < 40:
    print("Welcome {0}, then to the holiday!!!".format(name))
else:
    print("Sorry, you are not allow to the holiday.")
