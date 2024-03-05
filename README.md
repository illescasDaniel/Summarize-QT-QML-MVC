# Summarize-QT-QML-MVC
Simple app to summarize text. Currently, it is using facebook's "bart-large-cnn". This model has a 1024 tokens limit, but if you are using a larger input the app will split the input into multiple chunks of less or equal than 1024 tokens (so, more than 1024 tokens shouldn't be an issue).

<p align="center">
	<img src="assets/program_macOS.png" alt="macOS program screenshot" width="300" />
	<img src="assets/program_gnome.png" alt="linux GNOME program screenshot" width="300" />
	<img src="assets/program_windows.png" alt="windows program screenshot" width="300" />
</p>


## Requirements
- invoke (Optional, but recommended to easily build and run the app)
- HuggingFace's transformers
- Pytorch
- PySide6
- numpy
- GPU not required but highly recommended. It works with NVIDIA GPUs, Apple Silicon chips and CPUs.

## Development requirements
- pytest (unit tests)
- pyinstaller (create executable in tasks.py)
- pipreqs (genereate requirements.txt in tasks.py)

## Easy installation using conda (Anaconda/miniconda)
1. Clone the repo. `git clone https://github.com/illescasDaniel/Summarize-QT-QML-MVC.git`
`cd Summarize-QT-QML-MVC`
2. Install conda (anaconda or miniconda).
https://www.anaconda.com/download
https://docs.anaconda.com/free/miniconda/
3. Create a conda environment with all its dependencies.
	- Ubuntu/macOS: `./install.sh`
	- Windows (Anaconda Powershell Prompt, outside of VSCode): `.\install.ps1`
3. Activate the new environment: `conda activate Summarize-QT-QML-MVC`
4. Run the app: `invoke run`

**Note:** this is the preferred way, since using pip won't use your system theme.

**NOTE:** The first time you run it, after you press the "Summarize" button it will download the model, please be patient, you can see the progress in the terminal where you run the command.

## Easy installation using pip
1. Clone the repo.
`git clone https://github.com/illescasDaniel/Summarize-QT-QML-MVC.git`
`cd Summarize-QT-QML-MVC`
2. Create a virtual environment: `python3 -m venv summarize-env`
3. Activate the new environment: `source summarize-env/bin/activate`
4. Install dependencies: `pip3 install -r requirements.txt`
4. Run the app with `python3 src/main.py` or install `invoke` with `pip3 install invoke` and then `invoke run`.

**Note**: <sup>"Having Qt installed in your system will not interfere with your PySide6 installation if you do it via pip install, because the Python packages (wheels) include already Qt binaries. Most notably, style plugins from the system won’t have any effect on PySide applications." source: https://doc.qt.io/qtforpython-6/quickstart.html </sup> This means you won't use your system's default style if you use pip to install pyside6, AFAIK.

**NOTE:** The first time you run it, after you press the "Summarize" button it will download the model, please be patient, you can see the progress in the terminal where you run the command.

## Execution
Use `invoke run` to run the python app.

You can use `invoke --list` for all available tasks, use `invoke --help <command>` to get help about a specific command.

<sup>You can use `invoke build --snapshot-id=37f520fa929c961707657b28798b30c003dd100b` to build an executable using `pyinstaller`, just use your specific snapshot id from `{home_path}/.cache/huggingface/hub/models--facebook--bart-large-cnn/snapshots/{snapshot_id}` after you first run the app with `invoke run`.</sup>

**Note about `invoke build`**: on my macOS machine, after I run the invoke build command with the snapshot-id a recursion failure appears, if that happens to you, you may add `import sys ; sys.setrecursionlimit(sys.getrecursionlimit() * 5)` on top of the `main.spec` file (generated because of pyinstaller) and run `pyinstaller main.spec`; unfortunately it still doesn't work on my mac, it gives me the following error: `importlib.metadata.PackageNotFoundError: No package metadata was found for The 'tqdm>=4.27' distribution was not found and is required by this application.`

### TODOs:
- [x] Add unit tests with `pytest` [WIP].
- [ ] Try other models with bigger context.

---

#### Acknowledgments

<sup>This project makes use of the **BART-CNN model** developed by Facebook AI (now Meta AI) for text summarization. We are grateful for their efforts in creating and open-sourcing the model, which has significantly contributed to the capabilities of our application.</sup>

<sup>In addition, this application is built using the **Qt framework via PySide6**, the official set of Python bindings. The versatility and power of Qt have enabled us to create a robust, cross-platform user interface. Our thanks go to the Qt Company and the open-source contributors for making such a valuable resource available to the developer community.</sup>

#### License

<sup>This software is released under the **MIT License**. See the LICENSE file for more details.</sup>

<sup>Portions of this software incorporate the **BART-CNN model**, which is licensed under the "MIT License". For more details on the model and its license, please visit the official repository at [Bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn).</sup>

<sup>Additionally, this application makes use of the **Qt framework and PySide6**, licensed under the GNU Lesser General Public License (LGPL) version 3. We adhere to the licensing terms specified by these projects and appreciate the opportunity to build upon the work provided by the broader open-source community. For more information on Qt and its licensing, please visit [Qt Licensing](https://www.qt.io/licensing/).</sup>
