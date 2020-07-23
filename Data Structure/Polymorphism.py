class Bird:
	def fly(self, name):
		if name == "Parrot":
			print("Can Fly !!")
		if name == "Penguine":
			print("Can not Fly !!")
		if name is None:
			print("No input..")
obj = Bird()
obj.fly(None)
obj.fly("Parrot")
obj.fly("Penguine")