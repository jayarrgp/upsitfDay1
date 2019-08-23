x = input("Enter a number : ")
if x%400 == 0 and x > 0:
	print('%d is a LEAP year!' %x)
elif x%100 == 0:
	print('%d is NOT a leap year.' %x)
elif x%4 == 0:
	print('%d is a leap year!' %x)
else:
	print('%d is NOT leap year.' %x)