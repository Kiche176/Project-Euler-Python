numbers = {1: 3,
           2: 3,
           3: 5,
           4: 4,
           5: 4,
           6: 3,
           7: 5,
           8: 5,
           9: 4,
           10: 3,
           11: 6,
           12: 6,
           13: 8,
           14: 8,
           15: 7,
           16: 7,
           17: 9,
           18: 8,
           19: 8,
           20: 6,
           30: 6,
           40: 5,
           50: 5,
           60: 5,
           70: 7,
           80: 6,
           90: 6,
           "hundred": 7,
           "thousand": 8,
           "and": 3}

first9 = numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5] + numbers[6] + numbers[7] + numbers[8] + numbers[9]

teens = numbers[11] + numbers[12] + numbers[13] + numbers[14] + numbers[15] + numbers[16] + numbers[17] + numbers[18] + numbers[19]

preHundred = (first9 * 9) + numbers[10] + teens + 10 * (numbers[20] + numbers[30] + numbers[40] + numbers[50] + numbers[60] + numbers[70] + numbers[80] + numbers[90]) # 1-99

preThousand = preHundred

for i in range (1, 10):
    preThousand += (100 * (numbers[i] + numbers["hundred"]) + 99 * numbers["and"] + preHundred)

print(preThousand + numbers[1] + numbers["thousand"])