class Id:
	def __init__(self, identifier):
		self.identifier = identifier

	def getIdentifier(self):
		return self.identifier

	def __str__(self):
		return str(self.identifier)

	def __eq__(self, other):
		return self.identifier == other.getIdentifier()

	def __hash__(self):
		return hash(self.identifier)

