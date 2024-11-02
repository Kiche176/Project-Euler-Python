def primesBelow(n):
    numbers = []
    for i in range(2, n + 1):
        numbers.append(i)
    
    marked = []

    for number in numbers:
        if number not in marked:
            for i in range(number ** 2, len(numbers) + 2, number): # len numbers + 2 bc numbers starts at 2, not 0
                marked.append(i)


    marked = set(marked)
    for number in marked:
            numbers.remove(number)
    
    return numbers

def primesBelowEX(n):
    numbers = []
    for i in range(2, n + 1):
        numbers.append(i)
    
    for number in numbers:
        for i in range(number ** 2, n + 1, number): 
            if i in numbers:
                numbers.remove(i)
    
    return numbers


thing = primesBelowEX(100000)
print(thing)

print(sum(thing))