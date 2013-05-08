from person import Person 

class Manager(Person):
	def __init__(self, name, age, pay, job):
		Person.__init__(self, name, age, pay, 'Manager')

	def giveRaise(self, percent, bonus=0.1):
		self.pay *= (1.0 + percent + bonus)