class Duration():
	def __init__(self, delta):
		self.delta = delta

	def __str__(self):
		days = self.delta.seconds // 86400
		hours = (self.delta.seconds // 3600) % 24
		minutes = (self.delta.seconds // 60) % 60
		seconds = self.delta.seconds % 60
		if days > 0:
			return f"{days}d{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
		if hours > 0:
			return f"{hours}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
		return f"{minutes}:{str(seconds).zfill(2)}"

