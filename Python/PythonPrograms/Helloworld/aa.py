greeting = "Good "
print(greeting)
greeting += "Morning"
print(greeting)
greeting *= 5
print(greeting)

number = 5
multiplier = 8
answer = 0

# add your loop after this comment
times = 0
while times < multiplier:
    answer += number
    times += 1

print(answer)
print(times)

for i in range(multiplier):
    answer += number
print(answer)
