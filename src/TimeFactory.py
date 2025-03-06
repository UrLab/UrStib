from Collection import Collection
from TimeRecord import TimeRecord
from re import sub
from json import loads

class TimeFactory():
	def __init__(self):
		pass

	def createCollection(self, results):
		records = []
		for record in results:
			records.append(TimeRecord(id_, loads(record["name"])["fr"]))
		return Collection(records)

	def cleanId(self, id_):
		return int(sub(r"\D", "", id_))

