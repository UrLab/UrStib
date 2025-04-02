class Name():
	def __init__(self, frenchName, dutchName):
		self.frenchName = frenchName
		self.dutchName = dutchName

	def getFrenchName(self):
		return self.frenchName

	def getDutchName(self):
		return self.dutchName

	def __str__(self):
		return self.frenchName

	def __repr__(self):
		return str(self)

