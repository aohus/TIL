class Person:
	def __init__(self):
		print("Person 생성자")

	def person_method(self):
		print("person method")

class School:
	def __init__(self):
		print("School 생성자")

	def school_method(self):
		print("school method")

class Teacher(Person, School):
	def __init__(self):
		super().__init__()

teacher = Teacher() # Person 생성자
teacher.person_method()
teacher.school_method()

class Teacher(School, Person):
	def __init__(self):
		super().__init__()

teacher = Teacher() # School 생성자


class Teacher(School, Person):
	def __init__(self):
		School.__init__(self)
		Person.__init__(self)

teacher = Teacher() # School 생성자