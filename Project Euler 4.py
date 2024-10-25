palindromes = []

for i in range(10000, 1000000):
    if str(i) == str(i)[::-1]:
        palindromes.append(i)


ThreeDigitFactorPalindromes = []

for palindrome in palindromes:
    for i in range(100, 1000):
        if palindrome % i == 0:
            if len(str(palindrome // i)) == 3:
                ThreeDigitFactorPalindromes.append({
                    "Palindrome": palindrome,
                    "Factor 1": i,         
                    "Factor 2": palindrome // i
                })

print(ThreeDigitFactorPalindromes)