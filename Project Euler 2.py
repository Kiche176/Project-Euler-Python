sequence = [1, 2]

while sequence[-1] < 4000000:
    sequence.append(sequence[-2] + sequence[-1])

del sequence[-1]

total = 0
for num in sequence:
    if num % 2 == 0:
        total += num

print(total)