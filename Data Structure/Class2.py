class Student:
	def __init__ (self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade
	
	def get_grade(self):
		return self.grade

class course:
	def __init__ (self, name, max_students):
		self.name = name
		self.max_students = max_students
		self.students = []

	def add_student(self , student):
		if len(self.students) < self.max_students:
			self.students.append(student)
			return True
		return False

	def get_avg_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()


		return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Jay", 23, 88)
course = course ("Science",2)
course.add_student(s1)
course.add_student(s2)
print(course.get_avg_grade())
s3 = Student("Josh", 19, 56)
print(course.add_student(s3))