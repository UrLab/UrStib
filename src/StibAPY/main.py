from Query import Query
from ApiClient import ApiClient
from JSONStopConverter import JSONStopConverter
from StopRepository import StopRepository
from StopService import StopService
from EndpointRepository import EndpointRepository
from QueryBuilder import QueryBuilder

baseUrl = "https://data.stib-mivb.be/api/explore/v2.1"

def main(search):
	apiClient = ApiClient(EndpointRepository(), QueryDirector())
	stopConverter = JSONStopConverter()
	stopRepository = StopRepository([], stopConverter, apiClient)
	stopService = StopService(stopRepository)
	a = stopService.searchStops(search)
	print(a)

if __name__ == "__main__":
	from sys import argv
	main(argv[1])

