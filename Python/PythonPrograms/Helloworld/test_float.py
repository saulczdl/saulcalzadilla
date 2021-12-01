"""
Desc : This function generates a float range of numbers w/o using any library.

Params :
A (int/float) : First number in the range
L (int/float) : Last number in the range
D (int/float) : Step or the common difference
"""
def float_range(A, L=None, D=None):
    #Use float number in range() function
    # if L and D argument is null set A=0.0 and D = 1.0
    if L == None:
        L = A + 0.0
        A = 0.0
    if D == None:
        D = 1.0
    while True:
        if D > 0 and A >= L:
            break
        elif D < 0 and A <= L:
            break
        yield ("%g" % A) # return float number
        A = A + D
#end of function float_range()

"""
Desc: This section calls the above function with different test data.
"""
print ("\nPrinting float range")
print ("\nTest 1: ", end = " ")
for i in float_range(0.1, 5.0, 0.5):
    print (i, end=", ")

print ("\nTest 2: ", end = " ")
for i in float_range(-5.0, 5.0, 1.5):
    print (i, end=", ")

print ("\nTest 3: ", end = " ")
for num in float_range(5.5):
    print (num, end=", ")

print ("\nTest 4: ", end = " ")
for num in float_range(10.1, 20.1):
    print (num, end=", ")