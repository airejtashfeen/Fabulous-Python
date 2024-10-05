a = int(input("Enter a number to reverse it:"))
num = 0
while a > 0:
    digit = a % 10       
    num = num * 10 + digit
    a = a // 10            
print(num)
