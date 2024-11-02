def collatz(n):
    count = 0
    while True:
        count += 1
        if n == 1:
            break
        elif n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    
    return count

highest = [1, 1]
for i in range(1, 1000000):
    value = collatz(i)
    if value > highest[1]:
        highest[0] = i
        highest[1] = value

print(highest)