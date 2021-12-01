age = 38
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec") + ".")

print("Jan: {2}, Feb: {0} {3}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {1}, Sep: {2}"
      " Oct: {1}, Nov: {2}, Dec: {1}"
      .format(29, 30, 31, "days"))

print("""Jan: {2}
Feb: {0} {3}
Mar: {2} {3}
Apr: {1} {3}
May: {2} {3}
Jun: {1} {3}
Jul: {2} {3}
Aug: {1} {3}
Sep: {2} {3}
Oct: {1} {3}
Nov: {2} {3}
Dec: {1} {3}"""
      .format(29, 30, 31, "days"))
