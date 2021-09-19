# waopp to get marks rno and name from user

class student:
	def __init__(self, rno, name, marks):
		self.rno = rno
		self.name = name
		self.marks = marks
	def info(self):
		print("rno = ", self.rno)
		print("name = ", self.name)
		print("marks = ", self.marks)

rno = int(input("enter rno "))
name = input("enter name ")
marks = int(input("enter marks "))

s1 = student(rno, name, marks)
s1.info()