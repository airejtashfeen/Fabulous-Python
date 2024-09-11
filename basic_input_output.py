class Human:
  def __init__(self, name, age, weight, height):
    self.name= name
    self.age= age
    self.weight= weight
    self.height= height

  def showData(self):
    print("The name is:", self.name)
    print("The age is:", self.age)
    print("The height is:", self.height)
    print("The weight is:", self.weight)

name= input(str("Enter name:"))
age= int(input("Enter age:"))
weight= float(input("Enter weight:"))
height= float(input("Enter height:"))

human= Human(name, age,weight, height)
human.showData()
