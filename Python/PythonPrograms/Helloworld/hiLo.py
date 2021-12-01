low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press Enter to start!")

guesses = 1
while low != high:
#    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h ou l,  or c if my guess was correct"
                     .format(guess)).casefold()

    if high_low == "h":
        # Ghess Higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess Lower. The high end of the range becomes one less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got in in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c:")
    #    guesses = guesses + 1
    guesses += 1
#completed:
#nobreak:
else:
    print("You through of the number {}".format(low))
    print("I got it in {} guesses.".format(guesses))
exit()




#
# while True:
#     print("\tGuessing in the range of {} to {}".format(low, high))
#     guess = low + (high - low) // 2
#     high_low = input("My guess is {}. Should I guess higher or lower? "
#                      "Enter h ou l,  or c if my guess was correct"
#                      .format(guess)).casefold()
#
#     if high_low == "h":
#         # Ghess Higher. The low end of the range becomes 1 greater than the guess.
#         low = guess + 1
#     elif high_low == "l":
#         # Guess Lower. The high end of the range becomes one less than the guess.
#         high = guess - 1
#     elif high_low == "c":
#         print("I got in in {} guesses!".format(guesses))
#         break
#     else:
#         print("Please enter h, l or c:")
#
#     #    guesses = guesses + 1
#     guesses += 1