#CLASS TO BE IMPORTED

class car:
	def __init__(self,model,color):
		self.model = model
		self.color = color

	def printdetails(self):
		print(self.model)
		print(self.color)