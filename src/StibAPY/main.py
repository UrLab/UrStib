from HttpGetter import HttpGetter

link = "https://data.stib-mivb.be/api/explore/v2.1/catalog/datasets/waiting-time-rt-production/records?select=passingtimes&limit=100&offset=0&timezone=UTC&include_links=false&include_app_metas=false"

response = HttpGetter().get(link).status_code
print(response)

