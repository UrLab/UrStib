class Name():
	def __init__(self, frenchName, dutchName):
		self.frenchName = frenchName
		self.dutchName = dutchName

	def getFrenchName(self):
		return self.frenchName

	def getDutchName(self):
		return self.dutchName

	def __repr__(self):
		return str((self.frenchName, self.dutchName))

