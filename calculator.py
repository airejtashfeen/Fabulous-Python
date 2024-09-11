class Calculator:
  def sum(self, num1, num2):
    return num1+num2

  def subtract(self, num1, num2):
    return num1-num2

  def multiply(self, num1, num2):
    return num1*num2

  def divide(self, num1, num2):
    return num1/num2

calculator= Calculator()
num1= int(input("Enter number 1:"))
num2= int(input("Enter number 2:"))

sum= calculator.sum(num1,num2)
mult= calculator.multiply(num1,num2)
div= calculator.divide(num1,num2)
subt= calculator.subtract(num1,num2)

print("The sum of the two numbers is:", sum)
print("The subtraction of the two numbers is:", subt)
print("The multiplication of the two numbers is:", mult)
print("The division of the two numbers is:", div)
  