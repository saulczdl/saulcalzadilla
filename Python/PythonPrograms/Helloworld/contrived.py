numbers = [1, 48, 32, 12, 60, 21]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine")
