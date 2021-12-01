answer = 5

print("Please guess a number between 1 and 10: ")
guess =int(input())

if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you heve not guessed correctly.")


# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # gess must be greater than answer
#         print(("Please guess lower"))
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you heve not guessed correctly.")
# else:
#     print("You got it first time")




# if guess < answer:
#     print("Please guess higher!")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not gessed")
# elif guess > answer:
#     print("Please guess lower!")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not gessed")
# else:
#     print("You got it first time!")


# x = 8
# y = 7
# if x == y:
#     print("x equals y")
# elif x > y:
#     print("x is greater the y")
# else:
#     print("x is smaller than y")