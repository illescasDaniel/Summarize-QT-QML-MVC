from models.TextSummaryRepository import TextSummaryRepository
from PySide6.QtCore import QObject, Signal, Slot
from threading import Thread

class TextSummaryController(QObject):
	summaryReady = Signal(str)
	enableSummarizeButton = Signal(bool)

	def __init__(self):
		super().__init__()
		self.repository = TextSummaryRepository()

	@Slot(str)
	def summarize(self, input_text):
		self.summaryReady.emit(str())
		self.enableSummarizeButton.emit(False)
		Thread(target=self.generate_summary, args=(input_text,)).start()

	def generate_summary(self, input_text: str):
		for output_chunk in self.repository.summarize(input_text):
			self.summaryReady.emit(output_chunk)
		self.enableSummarizeButton.emit(True)
