# lottery_player_dict = {
# 	"name": "Rolf",
# 	"numbers": (5, 6, 7, 8, 1)
# }

# class LotteryPlayer:
# 	def __init__(self, name):
# 		self.name = name
# 		self.numbers = (5, 6, 7, 8, 1)

# 	def total(self):
# 		return sum(self.numbers)



##

class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len(self.marks)

	@staticmethod
	def go_to_school():
		print("I'm going to school.")


anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(71)

print(anna.go_to_school())