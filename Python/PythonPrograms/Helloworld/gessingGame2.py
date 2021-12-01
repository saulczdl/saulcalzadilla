import random

highest = 10
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess =int(input())

if guess != answer:
    while guess != answer:
#        if guess == answer:
#            print("Well done, you guessed it!")
        if guess == 0:
            print("You give up")
            break
        elif guess > answer:
            print("Please guess lower")
            guess = int(input())
        elif guess < answer:
            print("Please guess higher")
            guess = int(input())
    else:
        print("Well done, you guessed it!")
elif guess == 0:
    print("You give up!")
else:
    print("You got it first time")


# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly.")

# answer = 5
#
# print("Please guess a number between 1 and 10: ")
# guess =int(input())
#
# while guess != answer:
#     if guess > answer:
#         print("Please guess lower")
#         guess = int(input())
#     elif guess < answer:
#         print("Please guess higher")
#         guess = int(input())
# print("Well done, you guessed it!")
