from Collection import Collection
from StopRecord import StopRecord
from re import sub
from json import loads

class StopFactory():
	def __init__(self):
		pass

	def createCollection(self, results):
		records = []
		knownIds = set()
		knownNames = set()
		for record in results:
			id_ = self.cleanId(record["id"])
			if id_ in knownIds:
				continue
			knownIds.add(id_)
			name = loads(record["name"])["fr"]
			knownNames.add(name)
			records.append(StopRecord(id_, loads(record["name"])["fr"]))
		return Collection(records)

	def cleanId(self, id_):
		return int(sub(r"\D", "", id_))

