shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = input("How item do you want to find? ")
found_at = None

# for index in range (6):
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
if found_at is not None:
    print("Item found in position {}.".format(found_at))
else:
    print("{} not found!".format(item_to_find))

print("________1________")
# or can be write this way to:
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("Item found in position {}.".format(found_at))
else:
    print("{} not found!".format(item_to_find))

print("________2________")
# ------ Make inside of the same if = extract after line 10
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
    else:
     break
     found_at = None
print("{} not found!".format(item_to_find))
