from invoke import task
from invoke.context import Context
import os

@task
def build(ctx: Context, snapshot_id: str):
	"""
	Build the application using PyInstaller.

	Args:
		ctx (Context): The invoke context.
		snapshot_id (str): The ID of the snapshot for the model directory.

	Example:
		`invoke build --snapshot-id=37f520fa929c961707657b28798b30c003dd100b`
	"""
	home_path = os.environ.get('HOME')
	command = f"pyinstaller -y --add-data 'src/views:views' --add-data '{home_path}/.cache/huggingface/hub/models--facebook--bart-large-cnn/snapshots/{snapshot_id}:model_directory' src/main.py"
	ctx.run(command)

@task
def run_executable(ctx: Context):
	"""
	Run the executable, located at './dist/main/main'.

	Args:
		ctx (Context): The context object.
	
	Example:
		`invoke run-executable`
	"""
	ctx.run("./dist/main/main")

@task
def run_executable_debug_logging(ctx: Context):
	"""
	Run the executable, located at './dist/main/main', with DEBUG logging.

	Args:
		ctx (Context): The context object.
	
	Example:
		`invoke run-executable-debug-logging`
	"""
	ctx.run("./dist/main/main --log DEBUG")

@task
def generate_requirements(ctx: Context):
	"""
	Generates requirements.txt using pipreqs.
	If pipreqs is not installed, it prints a helpful message.
	"""
	try:
		ctx.run("pipreqs ./src --force")
		print("requirements.txt generated successfully.")
	except Exception as e:
		print("An error occurred while generating requirements.txt: {}".format(e))
		print("Make sure you have pipreqs installed by running `pip install pipreqs`")
	try:
		ctx.run('conda list --export > ./src/conda-requirements.txt')
	except:
		pass

@task
def run(ctx: Context):
	"""
	Run the main.py app. Make sure you have the necessary dependencies installed.
	
	Args:
		ctx (Context): The invoke context object.
	
	Example:
		`invoke run`
	"""
	ctx.run("python src/main.py")
