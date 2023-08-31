class Person:
	def __init__(self, name):
		self.name = name
	
	def greeting(self):
		print("Hi~")

class Teacher(Person):
	def __init__(self, name, subject):
		super().__init__(name)         # super()로 기반 클래스의 __init__ 호출
		self.subject = subject

	def show_info(self):
		print(f"""
			== teacher ==
			name: {self.name}, 
			subject: {self.subject}
		""")

class Student(Person):
	def show_info(self):
		print(f"student- name: {self.name} ")

Anna = Student('Anna')
Anna.greeting()
Anna.show_info()       

teacher1 = Teacher('Jane', 'Math')
teacher1.greeting()
teacher1.show_info()