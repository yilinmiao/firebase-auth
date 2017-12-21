students = []


def get_students_titlecase():
	students_titlecase = []
	for student in students:
		students_titlecase.append(student["email"].title())
	return students_titlecase


def print_students_titlecase():
	students_titlecase = get_students_titlecase()
	print(students_titlecase)


def add_student(email, password):
	student = {"email": email, "password": password}
	students.append(student)


def save_file(student):
	try:
		f = open("students.txt", "a")
		f.write(student + "\n")
		f.close()
	except Exception:
		print("Could not save file")


def read_file():
	try:
		f = open("students.txt", "r")
		for student in f.readlines():
			add_student(student)
		f.close()
	except Exception:
		print("Could not read file")


read_file()
print_students_titlecase()

email = input("Enter email: ")
password = input("Enter password: ")

add_student(email, password)
save_file(email)


