x = input("Enter Grade: ")
if x >= 90:
	print("%d is A" %x)
elif x < 90 and x >= 80:
	print("%d is B" %x)
elif x < 80 and x >= 70:
	print("%d is C" %x)
elif x < 70 and x >= 60:
	print("%d is D" %x)
else:
	print("%d is E" %x)