# Summarize-QT-QML-MVC
Simple app to summarize text. Currently, it is using facebook's "bart-large-cnn". This model has a 1024 tokens limit, but if you are using a larger input the app will split the input into multiple chunks of less or equal than 1024 tokens (so, more than 1024 tokens shouldn't be an issue).

![Program](assets/program.png)

### Requirements
- invoke (Optional, but recommended to easily build and run the app)
- HuggingFace's transformers
- Pytorch
- PySide6
- numpy
- GPU not required but highly recommended. It should work with NVIDIA GPUs, Apple Silicon chips and CPUs.

## Installation
Install requirements inside src folder using `pip install -r requirements.txt` or `conda create --name <env> --file conda-requirements.txt`.
Requirements generated using `pipreqs` and `conda`.

## Execution
Use `invoke --list` for all available tasks, like `invoke build --snapshot-id=37f520fa929c961707657b28798b30c003dd100b` or `invoke run`.
By default, when using `invoke run` (running the python app directly), the bart-larg-cnn model will be downloaded at `{home_path}/.cache/huggingface/hub/models--facebook--bart-large-cnn/snapshots/{snapshot_id}`.

### TODOs:
- [ ] Test installation on clean environments in Ubuntu, macOS and Windows.
- [ ] Add unit tests with `pytest`.