.PHONY: build_one_file build run # TODO: maybe do something about .PHONY?

build_one_file:
	# TODO: change the snapshot id for some dynamic thing
	# Not recommended, since after execution it takes a while to uncrompress all the data into a temporary folder (and this happens every time the executable in run)
	pyinstaller --onefile --add-data 'views:views' --add-data '/home/daniel/.cache/huggingface/hub/models--facebook--bart-large-cnn/snapshots/37f520fa929c961707657b28798b30c003dd100b:model_directory' main.py
build:
	# TODO: change the snapshot id for some dynamic thing
	pyinstaller --add-data 'views:views' --add-data '/home/daniel/.cache/huggingface/hub/models--facebook--bart-large-cnn/snapshots/37f520fa929c961707657b28798b30c003dd100b:model_directory' main.py

run:
	python main.py
