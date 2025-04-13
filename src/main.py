from Query import Query
from ApiClient import ApiClient
from JSONStopConverter import JSONStopConverter
from StopRepository import StopRepository
from StopService import StopService
from EndPointRepository import EndPointRepository
from QueryBuilder import QueryBuilder
from QueryDirector import QueryDirector
from JSONPassingTimeConverter import JSONPassingTimeConverter
from PassingTimesRepository import PassingTimesRepository
from PassingTimesService import PassingTimesService
from Time import Time

baseUrl = "https://data.stib-mivb.be/api/explore/v2.1"
enpointsFile = "endpoints.json"

def main(search):
	queryBuilder = QueryBuilder()
	apiClient = ApiClient(EndPointRepository(baseUrl, enpointsFile), QueryDirector(queryBuilder))
	stopConverter = JSONStopConverter()
	stopRepository = StopRepository(set(), stopConverter, apiClient)
	stopService = StopService(stopRepository)
	stops = stopService.searchStopsByName(search)
	passingTimesConverter = JSONPassingTimeConverter()
	passingTimesRepository = PassingTimesRepository(set(), passingTimesConverter, apiClient)
	passingTimesService = PassingTimesService(passingTimesRepository)
	waitingTimes = []
	for stop in stops:
		waitingTimes.extend(passingTimesService.getPassingTimesByStop(stop))
	now = Time.now()
	for waitingTime in waitingTimes:
		if (waitingTime.getDestination().getFrenchName() == ""):
			continue
		print(waitingTime.getLineId(), waitingTime.getDestination(), waitingTime.getRemainingTime(now), waitingTime.getMessage())

if __name__ == "__main__":
	from sys import argv
	main(argv[1])

