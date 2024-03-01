from threading import Thread
from PySide6.QtCore import QObject, Signal, Slot
from models.text_summary_repository import TextSummaryRepository


class TextSummaryController(QObject):
	summaryReady = Signal(str)
	isLoading = Signal(bool)

	def __init__(self):
		super().__init__()
		self.repository = TextSummaryRepository()

	@Slot(str)
	def summarize(self, input_text: str):
		self.summaryReady.emit(str())
		self.isLoading.emit(True)
		Thread(target=self.generate_summary, args=(input_text,)).start()

	def generate_summary(self, input_text: str):
		for output_chunk in self.repository.summarize(input_text):
			self.summaryReady.emit(output_chunk)
		self.isLoading.emit(False)
