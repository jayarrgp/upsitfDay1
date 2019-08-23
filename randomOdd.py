import random
randomNumbers = []
randomNumbersOdd = []
for x in range(20):
	randomNumbers.append(random.randint(1,100))
	if randomNumbers[x]%2 == 0:
		randomNumbersOdd.append(randomNumbers[x]+1)
	else:
		randomNumbersOdd.append(randomNumbers[x])
print ("Random Numbers = " +str(randomNumbers))
print ("Odd-ed Numbers = " +str(randomNumbersOdd))