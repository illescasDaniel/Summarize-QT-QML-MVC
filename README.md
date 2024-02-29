# Summarize-QT-QML-MVC
Simple app to summarize text. Currently, it is using facebook's "bart-large-cnn". This model has a 1024 tokens limit, but if you are using a larger input the app will split the input into multiple chunks of less or equal than 1024 tokens (so, more than 1024 tokens shouldn't be an issue).

![Program](assets/program.png)

## Requirements
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

By default, when using `invoke run` (running the python app directly), the bart-large-cnn model will be downloaded at `{home_path}/.cache/huggingface/hub/models--facebook--bart-large-cnn/snapshots/{snapshot_id}`. There you can see the snapshot-id.

### TODOs:
- [ ] Test installation on clean environments in Ubuntu, macOS and Windows.
- [ ] Add unit tests with `pytest`.

---

#### Acknowledgments

<sup>This project makes use of the **BART-CNN model** developed by Facebook AI (now Meta AI) for text summarization. We are grateful for their efforts in creating and open-sourcing the model, which has significantly contributed to the capabilities of our application.</sup>

<sup>In addition, this application is built using the **Qt framework via PySide6**, the official set of Python bindings. The versatility and power of Qt have enabled us to create a robust, cross-platform user interface. Our thanks go to the Qt Company and the open-source contributors for making such a valuable resource available to the developer community.</sup>

#### License

<sup>This software is released under the **MIT License**. See the LICENSE file for more details.</sup>

<sup>Portions of this software incorporate the **BART-CNN model**, which is licensed under the "MIT License". For more details on the model and its license, please visit the official repository at [Bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn).</sup>

<sup>Additionally, this application makes use of the **Qt framework and PySide6**, licensed under the GNU Lesser General Public License (LGPL) version 3. We adhere to the licensing terms specified by these projects and appreciate the opportunity to build upon the work provided by the broader open-source community. For more information on Qt and its licensing, please visit [Qt Licensing](https://www.qt.io/licensing/).</sup>
