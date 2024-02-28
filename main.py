from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from controllers.TextSummaryController import TextSummaryController
import sys
from pathlib import Path

if __name__ == "__main__":
	app = QGuiApplication(sys.argv)
	engine = QQmlApplicationEngine()

	textSummaryController = TextSummaryController()

	context = engine.rootContext()
	context.setContextProperty("textSummaryController", textSummaryController)

	# Define the base path depending on whether we're frozen (via PyInstaller)
	if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
		base_path = Path(sys._MEIPASS) # type: ignore
	else:
		base_path = Path(__file__).resolve().parent

	qml_file_path = base_path / 'views' / 'main.qml'
	engine.load(qml_file_path)

	if not engine.rootObjects():
		sys.exit(-1)
	sys.exit(app.exec())