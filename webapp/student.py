students = []


class Student:

	school_name = "Springfield Elementary"

	def __init__(self, email, password):
		self.email = email
		self.password = password
		students.append(self)

	def __str__(self):
		return "Student "

	def get_name_capitalize(self):
		return self.name.capitalize()

	def get_school_name(self):
		return self.school_name