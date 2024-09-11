class Rectangle:
  def __init__(self,length,width):
    self.length= float(length)
    self.width= float(width)
  
  def areaCalculate(self):
    return self.length*self.width

length= input("Enter length:")
width= input("Enter width:")

rectangle= Rectangle(length, width)
print("The area of the rectangle is:", rectangle.areaCalculate())