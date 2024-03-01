# Summarize-QT-QML-MVC
Simple app to summarize text. Currently, it is using facebook's "bart-large-cnn". This model has a 1024 tokens limit, but if you are using a larger input the app will split the input into multiple chunks of less or equal than 1024 tokens (so, more than 1024 tokens shouldn't be an issue).

![Program](assets/program.png)

## Requirements
- invoke (Optional, but recommended to easily build and run the app)
- HuggingFace's transformers
- Pytorch
- PySide6
- numpy
- GPU not required but highly recommended. It works with NVIDIA GPUs, Apple Silicon chips and CPUs.

## Easy installation
1. Clone the repo.
`git clone https://github.com/illescasDaniel/Summarize-QT-QML-MVC.git`
`cd Summarize-QT-QML-MVC`
2. Install conda (anaconda or miniconda).
https://www.anaconda.com/download
3. Create a conda environment with all its dependencies.
`./install.sh`
3. Activate the new environment.
`conda activate Summarize-QT-QML-MVC`
4. Run the app.
`invoke run`

**NOTE:** The first time you run it, after you press the "Summarize" button it will download the model, please be patient, you can see the progress in the terminal where you run the command.

## Execution
Use `invoke run` to run the python app.

You can use `invoke --list` for all available tasks, like `invoke build --snapshot-id=37f520fa929c961707657b28798b30c003dd100b` to build an executable using `pyinstaller`.

**NOTE:** By default, when using `invoke run` (running the python app directly), the bart-large-cnn model will be downloaded at `{home_path}/.cache/huggingface/hub/models--facebook--bart-large-cnn/snapshots/{snapshot_id}`. There you can see the snapshot-id.

**Note about `invoke build`**: on my macOS machine, after I run the invoke build command with the snapshot-id a recursion failure appears, if that happens to you, you may add `import sys ; sys.setrecursionlimit(sys.getrecursionlimit() * 5)` on top of the `main.spec` file (generated because of pyinstaller) and run `pyinstaller main.spec`; unfortunately it still doesn't work on my mac, it gives me the following error: `importlib.metadata.PackageNotFoundError: No package metadata was found for The 'tqdm>=4.27' distribution was not found and is required by this application.`

### TODOs:
- [ ] Test installation on clean environments in Ubuntu, macOS and Windows.
	- [x] Ubuntu
	- [x] MacOS
	- [ ] Windows
- [ ] Add unit tests with `pytest`.
- [ ] Try other models with bigger context.

---

#### Acknowledgments

<sup>This project makes use of the **BART-CNN model** developed by Facebook AI (now Meta AI) for text summarization. We are grateful for their efforts in creating and open-sourcing the model, which has significantly contributed to the capabilities of our application.</sup>

<sup>In addition, this application is built using the **Qt framework via PySide6**, the official set of Python bindings. The versatility and power of Qt have enabled us to create a robust, cross-platform user interface. Our thanks go to the Qt Company and the open-source contributors for making such a valuable resource available to the developer community.</sup>

#### License

<sup>This software is released under the **MIT License**. See the LICENSE file for more details.</sup>

<sup>Portions of this software incorporate the **BART-CNN model**, which is licensed under the "MIT License". For more details on the model and its license, please visit the official repository at [Bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn).</sup>

<sup>Additionally, this application makes use of the **Qt framework and PySide6**, licensed under the GNU Lesser General Public License (LGPL) version 3. We adhere to the licensing terms specified by these projects and appreciate the opportunity to build upon the work provided by the broader open-source community. For more information on Qt and its licensing, please visit [Qt Licensing](https://www.qt.io/licensing/).</sup>
