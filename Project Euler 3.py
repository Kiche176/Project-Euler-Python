
def findPrimeFactors(num):

    factors = []
    lowestFactor = 2

    while True:
        if lowestFactor < num:
            for i in range(lowestFactor, num + 1):
                if num % i == 0:
                    factors.append(i)
                    num = num // i
                    lowestFactor = i
                    break
        
        else:
            break
    
    return factors
    

    
    
print(findPrimeFactors(600851475143))