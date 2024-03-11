from pathlib import Path
import sys
import logging
import argparse


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

	@staticmethod
	def set_up_logging(logging_level: int):
		parser = argparse.ArgumentParser(description="Run the application with specified logging level.")
		parser.add_argument(
			"--log",
			default=logging.getLevelName(logging_level),
			choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
			help="Set the logging level (default: %(default)s)"
		)
		logging.basicConfig(level=logging.getLevelName(str(parser.parse_args().log)),
							format='%(asctime)s - %(levelname)s - %(message)s',
							datefmt='%Y-%m-%d %H:%M:%S')
