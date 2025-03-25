from Query import Query

baseUrl = "https://data.stib-mivb.be/api/explore/v2.1"
queryUrlFormat = "?select={}&where={}&group_by={}&order_by={}&limit={}&offset={}&refine={}&exclude={}&lang={}&timezone={}&include_links={}&include_app_metas={}"
q = Query(queryUrlFormat)

print(baseUrl+ "/catalog/datasets/stop-details-production/records" + str(q))

def main(search):
	apiClient = ApiClient(baseUrl, EndpointUrlRepository(), EndPointFactory(), QueryBuilder())
	stopConverter = JSONStopConverter()
	stopRepository = StopRepository([], stopConverter, apiClient)
	stopService = StopService(stopRepository)

