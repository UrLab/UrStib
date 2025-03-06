from StopFactory import StopFactory
from StibAPIEndPoint import StibAPIEndPoint

baseURL = "https://data.stib-mivb.be/api/explore/v2.1/catalog/datasets/"
dataset = "stop-details-production"
query = "/records?where=name%20like%20%22ULB%22&limit=100&offset=0&timezone=UTC&include_links=false&include_app_metas=false"


def main():
	url = baseURL + dataset
	stopfactory = StopFactory()
	endpoint = StibAPIEndPoint(url, stopfactory)
	coll = endpoint.get(query)
	for stop in coll:
		print(stop.getName(), stop.getPointId())


main()

