from .Query import Query

class QueryBuilder():
	def __init__(self):
		self.query = None
		self.reset()

	def reset(self):
		self.query = Query()

	def getQuery(self):
		returnQuery = self.query
		self.reset()
		return returnQuery

	def setSelect(self, select):
		self.query.select = f"select={select}"

	def setWhere(self, where):
		self.query.where = f"where={where}"

	def setGroupBy(self, groupBy):
		self.query.groupBy = f"group_by={groupBy}"

	def setOrderBy(self, orderBy):
		self.query.orderBy = f"order_by={orderBy}"

	def setLimit(self, limit):
		self.query.limit = f"limit={limit}"

	def setOffset(self, offset):
		self.query.offset = f"offset={offset}"

	def setRefine(self, refine):
		self.query.refine = f"refine={refine}"

	def setExclude(self, exclude):
		self.query.exclude = f"exclude={exclude}"

	def setLang(self, lang):
		self.query.lang = f"lang={lang}"

	def setTimezone(self, timezone):
		self.query.timezone = f"timezone={timezone}"

	def setIncludeLinks(self, includeLinks):
		self.query.includeLinks = f"include_links={includeLinks}"

	def setIncludeAppMetas(self, includeAppMetas):
		self.query.includeAppMetas = f"include_app_metas={includeAppMetas}"

