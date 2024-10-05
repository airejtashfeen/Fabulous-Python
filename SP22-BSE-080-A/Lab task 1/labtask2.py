num = 0
even = 0
odd = 0
while(True):
    num = int(input("Enter any number or press 0 to exit "))
    if(num == 0):
        break
    elif(num%2==0):
        even+=num
    else :
        odd=odd+num
print("Odd Sum :",odd)
print("Even Sum : ",even)        
