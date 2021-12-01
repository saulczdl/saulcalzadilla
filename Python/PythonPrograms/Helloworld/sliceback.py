letters = "abcdefghijklmnopqrstuvwxyz"
#          01234567890123456789012345
backwards = letters[25:0:-1]
print(backwards)

backwards = letters[25::-1]
print(backwards)

print(letters[-10:13:-1]) # or [16:13::-1]

print(letters[-22::-1]) # or [4::-1]

backwards2 = letters[:17:-1] # or [:-9:-1]
print(backwards2)

print(letters[-4:])