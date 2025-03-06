from StopCollection import StopCollection

class StopFactory():
	def __init__(self):
		pass

	def createCollection(self, getResult):
		data = getResult.json()
		return StopCollection(data["results"])

