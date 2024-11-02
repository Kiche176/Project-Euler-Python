import math



nums = []

factorial = str(math.factorial(100))

for i in range(len(factorial)):
    nums.append(int(factorial[i]))

print(sum(nums))