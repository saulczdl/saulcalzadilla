for i in range(11):
    for j in range(11):
        for k in range(11):
            print("{1} times {0} times {2} is {3}".format(j, i, k, i * j * k))
        print("------------------------------")
