from Query import Query
from ApiClient import ApiClient
from JSONStopConverter import JSONStopConverter
from StopRepository import StopRepository
from StopService import StopService
from EndpointUrlRepository import EndpointUrlRepository
from EndPointFactory import EndPointFactory
from QueryBuilder import QueryBuilder

baseUrl = "https://data.stib-mivb.be/api/explore/v2.1"
queryUrlFormat = "?select={}&where={}&group_by={}&order_by={}&limit={}&offset={}&refine={}&exclude={}&lang={}&timezone={}&include_links={}&include_app_metas={}"
q = Query(queryUrlFormat)

print(baseUrl+ "/catalog/datasets/stop-details-production/records" + str(q))

def main(search):
	apiClient = ApiClient(baseUrl, EndpointUrlRepository(), EndPointFactory(), QueryBuilder())
	stopConverter = JSONStopConverter()
	stopRepository = StopRepository([], stopConverter, apiClient)
	stopService = StopService(stopRepository)
	a = stopService.searchStops(search)
	print(a)

if __name__ == "__main__":
	from sys import argv
	main(argv[1])

