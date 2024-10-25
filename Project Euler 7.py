def findPrimes(n):
    if n < 2:
        return 0

    primes = [2]

    number = 2
    while len(primes) < n:

        prime = True
        for prime in primes:
            if number % prime == 0:
                prime = False
                break
        
        if prime:
            primes.append(number)

        number += 1
    
    return primes

print(findPrimes(10001))
