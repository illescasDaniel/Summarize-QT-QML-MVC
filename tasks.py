from invoke.tasks import task
from invoke.context import Context
import os

@task
def build(ctx: Context, snapshot_id: str):
	'''
	Build the application using PyInstaller. Make sure to pass "--snapshot-id=your hugging face model id here".
	($HOME/.cache/huggingface/hub/models--facebook--bart-large-cnn/snapshots/<snapshot id here>).
	After running the command successfully, run the executable with `invoke run-executable`.

	Args:
		ctx (Context): The invoke context.
		snapshot_id (str): The ID of the hugging face model snapshot.

	Example:
		`invoke build --snapshot-id=37f520fa929c961707657b28798b30c003dd100b`
	'''
	try:
		home_path = os.environ.get('HOME')
		command = f'pyinstaller -y --add-data "src/views:views" --add-data "{home_path}/.cache/huggingface/hub/models--facebook--bart-large-cnn/snapshots/{snapshot_id}:model_directory" src/main.py'
		ctx.run(command)
	except Exception as e:
		print(f'An error occurred while building the executable: {e}')
		print('Make sure you have "pyinstaller" installed by running "conda install pyinstaller" or "pip install pyinstaller"')
		print('If you have recursion limits, simply add "import sys ; sys.setrecursionlimit(sys.getrecursionlimit() * 5)" at the beggining of the "main.spec" file, then run "pyinstaller main.spec"')

@task
def run_executable(ctx: Context):
	'''
	Run the executable, located at './dist/main/main'.

	Example:
		`invoke run-executable`
	'''
	ctx.run('./dist/main/main')

@task
def run_executable_debug_logging(ctx: Context):
	'''
	Run the executable, located at './dist/main/main', with DEBUG logging.

	Example:
		`invoke run-executable-debug-logging`
	'''
	ctx.run('./dist/main/main --log DEBUG')

@task
def generate_requirements(ctx: Context):
	'''
	Generate requirements.txt using `pipreqs`.

	Example:
		`invoke generate-requirements`
	'''
	try:
		ctx.run("pipreqs ./src --savepath ./requirements.txt --force")
		print("requirements.txt generated successfully.")
	except Exception as e:
		print(f'An error occurred while generating requirements.txt: {e}')
		print('Make sure you have pipreqs installed by running "conda install pireqs" or "pip install pipreqs"')

@task
def run(ctx: Context):
	'''
	Run the main.py app. Make sure you have the necessary dependencies installed.

	Example:
		`invoke run`
	'''
	ctx.run('python3 src/main.py')

@task
def test(ctx: Context):
	'''
	Run pytest to execute unit tests.
	'''
	project_root = "./"
	source_code_root = "./src"
	os.environ["PYTHONPATH"] = f"{os.environ.get('PYTHONPATH')}:{project_root}:{source_code_root}"

	ctx.run("pytest --color=yes")

@task
def test_reports(ctx: Context):
	'''
	Run pytest to execute unit tests.
	'''
	project_root = "./src"
	tests_root = "./tests"
	os.environ["PYTHONPATH"] = f"{os.environ.get('PYTHONPATH')}:{project_root}:{tests_root}"

	ctx.run('pytest --color=yes --cov=src/ --cov-report xml tests/')