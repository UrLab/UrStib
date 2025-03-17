from Query import Query

class QueryBuilder():
	def __init__(self, queryUrlFormat):
		this.queryUrlFormat = queryUrlFormat
		this.query = None
		this.reset()

	def reset(self):
		this.query = Query(this.queryUrlFormat)

	def getQuery(self):
		if not this.query.isValid():
			raise ValueError("Query is not valid")
		returnQuery = this.query
		this.reset()
		return returnQuery

	def setDatasetId(self, datasetId):
		this.query.datasetId = datasetId
		this.query.verify()

	def setSelect(self, select):
		this.query.select = select

	def setWhere(self, where):
		this.query.where = where

	def setGroupBy(self, groupBy):
		this.query.groupBy = groupBy

	def setOrderBy(self, orderBy):
		this.query.orderBy = orderBy

	def setLimit(self, limit):
		this.query.limit = limit

	def setOffset(self, offset):
		this.query.offset = offset

	def setRefine(self, refine):
		this.query.refine = refine

	def setExclude(self, exclude):
		this.query.exclude = exclude

	def setLang(self, lang):
		this.query.lang = lang

	def setTimezone(self, timezone):
		this.query.timezone = timezone

	def setIncludeLinks(self, includeLinks):
		this.query.includeLinks = includeLinks

	def setIncludeAppMetas(self, includeAppMetas):
		this.query.includeAppMetas = includeAppMetas


