class Stop():
	def __init__(self, id_, name, coordinates):
		self.id = id_
		self.name = name
		self.coordinates = coordinates

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def getGPSCoordinates(self):
		return self.coordinates

	def __eq__(self, other):
		return self.id == other.getId()

	def __hash__(self):
		return hash(self.id)

	def __str__(self):
		return str((self.id, self.name))

