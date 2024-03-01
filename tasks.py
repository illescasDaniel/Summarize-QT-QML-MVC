from invoke.tasks import task
from invoke.context import Context
import os

@task
def build(ctx: Context, snapshot_id: str):
	"""
	Build the application using PyInstaller.

	Args:
		ctx (Context): The invoke context.
		snapshot_id (str): The ID of the hugging face model snapshot.

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

	Example:
		`invoke run-executable`
	"""
	ctx.run("./dist/main/main")

@task
def run_executable_debug_logging(ctx: Context):
	"""
	Run the executable, located at './dist/main/main', with DEBUG logging.

	Example:
		`invoke run-executable-debug-logging`
	"""
	ctx.run("./dist/main/main --log DEBUG")

@task
def run(ctx: Context):
	"""
	Run the main.py app. Make sure you have the necessary dependencies installed.

	Example:
		`invoke run`
	"""
	ctx.run('python src/main.py')
