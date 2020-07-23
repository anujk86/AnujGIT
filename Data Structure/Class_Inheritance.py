class Pet:
	def __init__ (self, name, colour):
		self.name = name
		self.colour = colour

	def show(self):
		print(f"I am {self.name} and I am of the clour {self.colour} ")

class Dog(Pet):
		
	def speak (self):
		print("Bark")

class Cat(Pet):
	
	def speak (self):
		print("Meow")

p = Pet("John", "Black")
p.show()
c = Cat("Bunty", "Black")
c.show()
c.speak()
d = Dog("Mohan", "White")
d.show()
d.speak()