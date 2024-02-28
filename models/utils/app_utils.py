from pathlib import Path
import sys

class AppUtils:

	_app_base_path: Path

	@staticmethod
	def is_app_frozen() -> bool:
		# Define the base path depending on whether we're frozen (via PyInstaller)
		if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
			return True
		else:
			return False
		
	@staticmethod
	def app_base_path() -> Path:
		return AppUtils._app_base_path
	
	@staticmethod
	def set_app_base_path(base_path: Path):
		AppUtils._app_base_path = base_path
