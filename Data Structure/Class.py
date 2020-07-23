#OOP Class Exmple
class Dog:
	def __init__ (self, name, colour):
		self.name = name
		self.colour = colour
		print(name)

	def bark(self):
		print (self.name + " Barks")
		print(self.colour)

	def Add(self, x):
		return x + 1
		
d3 = Dog("John", "Black")
#d2 = Dog("Tim")
d3.bark()
#d.bark()
#print(d.Add(4))