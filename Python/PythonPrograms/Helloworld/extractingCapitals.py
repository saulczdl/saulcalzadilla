quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
letters = ""
for capitals in quote:
    if capitals.isupper():
        letters = letters + capitals
print(letters)
letters2 = str.upper(quote)
print(letters2)
letters3 = str.lower(letters2)
print(letters3)
letters4 = str.capitalize(letters3)
print(letters4)
# -----------------------------------------
print("-" * 80)

for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char)
        
quote2 = """
alright, but apart from the sanitation, the medicine, education, wine,
public order, irrigation, roads, the fresh-water system,
and public health, what have the romans ever done for us?
"""
print(quote2.capitalize())