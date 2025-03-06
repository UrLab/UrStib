from json import loads
from StopRecord import StopRecord
from Collection import Collection
from re import sub

class StopCollection(Collection):
	def __init__(self, records):
		self.records = []
		knownIds = set()
		knownNames = set()
		for record in records:
			id_ = self.cleanId(record["id"])
			if id_ in knownIds:
				continue
			knownIds.add(id_)
			name = loads(record["name"])["fr"]
			knownNames.add(name)
			self.records.append(StopRecord(id_, loads(record["name"])["fr"]))
		super().__init__(self.records)

	def cleanId(self, id_):
		return int(sub(r"\D", "", id_))

