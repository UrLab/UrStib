class Collection():
	def __init__(self, recordsList):
		self.recordsList = recordsList

	def getRecordsList(self):
		return self.recordsList

	def discard(self, record):
		try:
			return self.recordsList.remove(record)
		except ValueError:
			raise ValueError("Record not in collection")

	def __iter__(self):
		return iter(self.recordsList)


