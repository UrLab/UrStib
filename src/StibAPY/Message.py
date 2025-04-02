class Message():
	def __init__(self, french, dutch, english):
		self.french = french
		self.dutch = dutch
		self.english = english

	def getFrench(self):
		return self.french

	def getDutch(self):
		return self.dutch

	def getEnglish(self):
		return self.english

	def __str__(self):
		return self.french

	def __repr__(self):
		return str(self)

