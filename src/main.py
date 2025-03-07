from StopFactory import StopFactory
from StibAPIEndPoint import StibAPIEndPoint

dataset = "stop-details-production"
endpointURL = "https://data.stib-mivb.be/api/explore/v2.1/catalog/datasets/" + dataset + "/records"
query = "?where=name%20like%20%22ULB%22&limit=100&offset=0&timezone=UTC&include_links=false&include_app_metas=false"


def main():
	url = endpointURL
	stopfactory = StopFactory()
	endpoint = StibAPIEndPoint(url, stopfactory)
	coll = endpoint.get(query)
	for stop in coll:
		print(stop.getName(), stop.getPointId())


main()

