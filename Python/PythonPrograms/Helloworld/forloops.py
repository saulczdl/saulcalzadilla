# parrot = "Norwegian Blue"
#
# for character in parrot:
#     print(character)

number = input("Plese enter a series of numbers, using any separators you like: ")
# print(number[1::4])
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char
print(seperators)

print("*" * 80)

values = "".join(char if char not in seperators else " " for char in number).split()
print(sum([int(val) for val in values]))
#     soma os numeros, sem o "sum", os números aparencem em intervalos separados por vírgula.