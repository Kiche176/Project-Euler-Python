import math

triplet = []

# a + b = 1000 - c  This is how we will use pointers

for c in range(1000, 0, -1):
    for b in range(1000 - c, 0, -1):
        for a in range(1000 - c - b, 0, -1):
            if (a**2 + b**2 == c**2) and (a + b + c == 1000):
                triplet = [a, b, c]

print(triplet)
print(triplet[0] * triplet[1] * triplet[2])