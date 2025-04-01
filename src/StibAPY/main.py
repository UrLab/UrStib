from Query import Query
from ApiClient import ApiClient
from JSONStopConverter import JSONStopConverter
from StopRepository import StopRepository
from StopService import StopService
from EndPointRepository import EndPointRepository
from QueryBuilder import QueryBuilder
from QueryDirector import QueryDirector

baseUrl = "https://data.stib-mivb.be/api/explore/v2.1"
enpointsFile = "endpoints.json"

def main(search):
	queryBuilder = QueryBuilder()
	apiClient = ApiClient(EndPointRepository(baseUrl, enpointsFile), QueryDirector(queryBuilder))
	stopConverter = JSONStopConverter()
	stopRepository = StopRepository([], stopConverter, apiClient)
	stopService = StopService(stopRepository)
	a = stopService.searchStopsByName(search)
	print(a)

if __name__ == "__main__":
	from sys import argv
	main(argv[1])

