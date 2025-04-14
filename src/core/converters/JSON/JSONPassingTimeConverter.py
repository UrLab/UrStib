from json import loads
from core.models import Name, Time, Id, Message, PassingTime

class JSONPassingTimeConverter:
	def __init__(self):
		pass

	def convertPassingTimes(self, passingTimesJSON):
		results = passingTimesJSON["results"]
		passingTimes = []
		for passingTimeJSON in results:
			passingTimes.extend(self.convertPassingTimePair(passingTimeJSON))
		return passingTimes

	def convertPassingTimePair(self, passingTimeJSON):
		passingTimes = loads(passingTimeJSON["passingtimes"])
		return [self.convertPassingTime(passingTime) for passingTime in passingTimes]

	def convertPassingTime(self, passingTimeJSON):
		try:
			destination = Name(passingTimeJSON["destination"]["fr"], passingTimeJSON["destination"]["nl"])
		except KeyError:
			destination = Name("", "")
		arrivalTime = Time(passingTimeJSON["expectedArrivalTime"])
		lineId = Id(passingTimeJSON["lineId"])
		try:
			message = Message(passingTimeJSON["message"]["fr"], passingTimeJSON["message"]["nl"], passingTimeJSON["message"]["en"])
		except KeyError:
			message = Message("", "", "")
		return PassingTime(destination, arrivalTime, lineId, message)

