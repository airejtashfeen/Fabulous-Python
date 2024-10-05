num = int(input("Enter a number to calculate its factorial: "))

fact = 1
while num > 0:
    fact *= num
    num -= 1

print("Factorial is:", fact)
