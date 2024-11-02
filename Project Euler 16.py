num = str(2 ** 1000)

total = 0
for i in range(len(num)):
    total += int(num[i])

print(total)