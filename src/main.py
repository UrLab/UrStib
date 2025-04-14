from core import Query, ApiClient, JSONStopConverter, StopRepository, StopService, EndPointRepository, QueryBuilder, QueryDirector, JSONPassingTimeConverter, PassingTimeRepository, PassingTimesService

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
	for waitingTime in waitingTimes:
		print(waitingTime.getLineId(), waitingTime.getDestination(), waitingTime.getRemainingTime(), waitingTime.getMessage())

if __name__ == "__main__":
	from sys import argv
	main(argv[1])

