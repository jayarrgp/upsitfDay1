firstAddend = []
secondAddend = []
fibonacciNumber = []

firstAddend.append(0)
secondAddend.append(1)
fibonacciNumber.append(firstAddend [0]+ secondAddend[0])
x = int(input("Please input how many Fibonacci numbers: "))

for x in range(x-3):
	fibonacciNumber.append(fibonacciNumber[x] + secondAddend [x])
	secondAddend.append(fibonacciNumber[x])

fibonacciNumber.insert(0,firstAddend[0])
fibonacciNumber.insert(1,secondAddend[0])
print (fibonacciNumber)
