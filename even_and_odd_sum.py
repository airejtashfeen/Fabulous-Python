val= int(input("Enter any value or press 0 to exit:"))
evenSum=0
oddSum=0
while val!=0:
    if val%2==0:
        evenSum+=val
    else:
        oddSum+=val
    val= int(input("Enter any value or press 0 to exit:"))

print("The even sum is:",evenSum)
print("The odd sum is:",oddSum)