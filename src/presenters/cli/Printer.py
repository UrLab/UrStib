class Printer:
	def __init__(self):
		self.data = []

	def display(self, message):
		data.append(message)
		self.refresh()
		print("\n".join(self.data))

	def refresh(self):
		print("\033c", end="")

	def clear(self):
		self.data = []

