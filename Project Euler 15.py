# the answer is 40 choose 20

import math

def choose(n, r):
    return (math.factorial(n) / (math.factorial(n-r) * math.factorial(r)))

print(choose(40, 20))