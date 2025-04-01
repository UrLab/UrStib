class Query:
	# limit, offset, lang and timezone must be set
	def __init__(self):
		self.select = ""
		self.where = ""
		self.groupBy = ""
		self.orderBy = ""
		self.limit = ""
		self.offset = ""
		self.refine = ""
		self.exclude = ""
		self.lang = ""
		self.timezone = ""
		self.includeLinks = ""
		self.includeAppMetas = ""

	def __str__(self):
		return "?" + "&".join([self.select, self.where, self.groupBy, self.orderBy, self.limit, self.offset, self.refine, self.exclude, self.lang, self.timezone, self.includeLinks, self.includeAppMetas])

