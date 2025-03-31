from Query import Query

class QueryBuilder():
	def __init__(self, queryUrlFormat):
		this.queryUrlFormat = queryUrlFormat
		this.query = None
		this.reset()

	def reset(self):
		this.query = Query(this.queryUrlFormat)

	def getQuery(self):
		returnQuery = this.query
		this.reset()
		return returnQuery

	def setSelect(self, select):
		this.query.select = f"select={select}"

	def setWhere(self, where):
		this.query.where = f"where={where}"

	def setGroupBy(self, groupBy):
		this.query.groupBy = f"group_by={groupBy}"

	def setOrderBy(self, orderBy):
		this.query.orderBy = f"order_by={orderBy}"

	def setLimit(self, limit):
		this.query.limit = f"limit={limit}"

	def setOffset(self, offset):
		this.query.offset = f"offset={offset}"

	def setRefine(self, refine):
		this.query.refine = f"refine={refine}"

	def setExclude(self, exclude):
		this.query.exclude = f"exclude={exclude}"

	def setLang(self, lang):
		this.query.lang = f"lang={lang}"

	def setTimezone(self, timezone):
		this.query.timezone = f"timezone={timezone}"

	def setIncludeLinks(self, includeLinks):
		this.query.includeLinks = f"include_links={includeLinks}"

	def setIncludeAppMetas(self, includeAppMetas):
		this.query.includeAppMetas = f"include_app_metas={includeAppMetas}"

