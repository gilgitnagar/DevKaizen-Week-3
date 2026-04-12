class Parrot:
    # class attribute
    name = ""
    age = 0
# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10
# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15
# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")

# define a class
class Bike:
    name = ""
    gear = 0
# create object of class
bike1 = Bike()
# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"
print(f"Name: {bike1.name}, Gears: {bike1.gear} ")

# Python Inheritanceclass Animal:
# attribute and method of the parent class
#name = ""
  #  def eat(self):
  #  print("I can eat")
# inherit from Animal
#class Dog(Animal):
     # new method in subclass
#def display(self):
# access name attribute of superclass using self print("My name is ", self.name)
# create an object of the subclass
#labrador = Dog()
# access superclass attribute and method

#labrador.name = "Rohu"
#labrador.eat()
# call subclass method
#labrador.display()


#Polymorphism

#class Polygon:
    # method to render a shape 
#def render(self):
 #print("Rendering Polygon...") 
#class Square(Polygon):
    # renders Square
# def render(self): print("Rendering Square...")
#class Circle(Polygon):
    # renders circle
 #def render(self): print("Rendering Circle...")
# create an object of Square
#s1 = Square()
#s1.render()
# create an object of Circle
#c1 = Circle()
#c1.render()
