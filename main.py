from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from TextSummaryController import TextSummaryController
import sys

if __name__ == "__main__":
	app = QGuiApplication(sys.argv)
	engine = QQmlApplicationEngine()

	textSummaryController = TextSummaryController()

	context = engine.rootContext()
	context.setContextProperty("textSummaryController", textSummaryController)

	engine.load("main.qml")

	if not engine.rootObjects():
		sys.exit(-1)
	sys.exit(app.exec())