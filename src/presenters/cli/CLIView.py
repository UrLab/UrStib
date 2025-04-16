class CLIView:
	def __init__(self, printer, passingTimesPresenter):
		self.printer = printer
		self.passingTimesPresenter = passingTimesPresenter

	def display(self, passingTimes):
		table = self.passingTimesPresenter.present(passingTimes)
		for row in table:
			self.printer.display(row)

