import math

sequence = [1, 3]

for i in range(100000):
    sequence.append(sequence[-1] + len(sequence) + 1)

print(sequence)

def numDivisors(n): # doesn't work for numbers less than 4
    numbers = [False] * int(math.sqrt(n))

    for i in range(1, len(numbers)):
        if n % i == 0:
            numbers[i - 1] = True

    count = 0

    if math.sqrt(n) == math.sqrt(n) // 1:
        count = 1
    
    for num in numbers:
        if num == True:
            count += 2
    
    return count


for num in sequence:
    if numDivisors(num) > 500:
        print(num)
        break
