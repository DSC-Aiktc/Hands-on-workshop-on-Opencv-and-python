#EXPLAIN CLASS

#EXPLAIN __INIT__ FUNCTION

class car:
	def __init__(self,model,color):
		self.model = model
		self.color = color

honda = car("CITY","RED")
jeep = car("WRANGLER","BLACK")

print(honda.model)

print(jeep.color)