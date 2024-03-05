import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch

from regex import P
from src.models.text_summary_repository import TextSummaryRepository
from utils.generator_tracker import GeneratorTracker

def test_given_input_when_summarize_then_summarized_text_expected(mock_pipeline, mock_torch_utils):
	mock_pipeline_function, mock_pipeline_object = mock_pipeline
	# this below would be equivalent to: mock_pipeline_object.__call__.return_value = ..., but that doesn't work
	mock_pipeline_object.return_value = [{'summary_text': 'This is a summary.'}]
	repository = TextSummaryRepository()
	repository.initialize()
	# a normal text with more than 30 words
	input_text = 'This is a detailed text that needs to be summarized 11 22 13 14 15 16 17 18 19 20 21 22 23 24 25 26 277 28 29 30 31 32.'

	summarize_generator = GeneratorTracker(repository.summarize(input_text))
	summary = ''.join(summarize_generator)

	assert summary == 'This is a summary.'
	assert summarize_generator.count == 1
	mock_pipeline_function.assert_called_once()
	mock_pipeline_object.assert_called_once()
	mock_torch_utils.get_device.assert_called_once()
	mock_torch_utils.set_default_device.assert_called_once()

def test_given_small_input_when_summarize_then_input_is_same_as_output(mock_pipeline, mock_torch_utils):
	# a text that is smaller or equal to the minimium length (30 words)
	text = 'This is a detailed text.'
	mock_pipeline_function, mock_pipeline_object = mock_pipeline
	repository = TextSummaryRepository()
	repository.initialize()

	summarize_generator = GeneratorTracker(repository.summarize(text))
	summary = ''.join(summarize_generator)

	assert summary == text
	assert summarize_generator.count == 1
	mock_pipeline_function.assert_called_once()
	mock_pipeline_object.assert_not_called()
	mock_torch_utils.get_device.assert_called_once()
	mock_torch_utils.set_default_device.assert_called_once()

def test_given_large_input_when_summarize_then_summarized_text_expected(mock_pipeline, mock_torch_utils):
	mock_pipeline_function, mock_pipeline_object = mock_pipeline
	# this below would be equivalent to: mock_pipeline_object.__call__.return_value = ..., but that doesn't work
	mock_pipeline_object.return_value = [{'summary_text': 'something'}]
	repository = TextSummaryRepository()
	repository.initialize()
	input_text = ' '.join(['something'] * 2000)

	summarize_generator = GeneratorTracker(repository.summarize(input_text))
	summary = ' '.join(summarize_generator)

	assert summary == 'something something'
	assert summarize_generator.count == 2
	mock_pipeline_function.assert_called_once()
	assert mock_pipeline_object.call_count == 2
	mock_torch_utils.get_device.assert_called_once()
	mock_torch_utils.set_default_device.assert_called_once()

def test_given_no_initialization_when_summarize_then_exception_raised(mock_pipeline):
	mock_pipeline_function, mock_pipeline_object = mock_pipeline
	repository = TextSummaryRepository()
	input_text = 'This is a detailed text that needs to be summarized 11 22 13 14 15 16 17 18 19 20 21 22 23 24 25 26 277 28 29 30 31 32.'

	with pytest.raises(AttributeError) as error:
		next(repository.summarize(input_text))

	assert str(error.value) == "No device or summarizer, you must call initialize first"

	mock_pipeline_function.assert_not_called()
	mock_pipeline_object.assert_not_called()

def test_given_specific_device_when_summarize_check_we_used_device(mock_pipeline):
	mock_pipeline_function, _ = mock_pipeline
	repository = TextSummaryRepository()
	device_mock = MagicMock()

	repository.initialize(device=device_mock)

	mock_pipeline_function.assert_called_once_with(
		task='summarization',
		model='facebook/bart-large-cnn',
		device=device_mock
	)

def test_given_app_is_frozen_when_summarize_check_model(mock_pipeline, mock_app_utils):
	mock_pipeline_function, _ = mock_pipeline
	mock_app_utils.is_app_frozen.return_value = True
	app_base_path = Path('/')
	mock_app_utils.app_base_path.return_value = app_base_path
	repository = TextSummaryRepository()
	device_mock = MagicMock()
	model_directory = app_base_path / 'model_directory'

	repository.initialize(device=device_mock)

	mock_pipeline_function.assert_called_once_with(
		task='summarization',
		model=str(model_directory),
		tokenizer=str(model_directory),
		device=device_mock
	)

# TODO: test min and max lengths
# mock_pipeline_object.assert_called_once_with(
# 	input_text,
# 	max_length=32,
# 	min_length=32,
# 	do_sample=False
# )

# TODO: more than 1024 characters (import a file please or just generate an array)
# check that summarize is called multiple times if the input is larger than 1024

# TODO: test other stuff in the app

# FIXTURES:

@pytest.fixture
def mock_pipeline():
	with patch('src.models.text_summary_repository.pipeline') as mock_pipeline_function:
		mock_pipeline_object = MagicMock()
		mock_pipeline_object.return_value = None
		mock_pipeline_function.return_value = mock_pipeline_object
		yield (mock_pipeline_function, mock_pipeline_object)

@pytest.fixture
def mock_torch_utils():
	with patch('src.models.text_summary_repository.TorchUtils') as mock_torch_utils:
		mock_torch_utils.get_device.return_value = MagicMock()
		mock_torch_utils.set_default_device.return_value = None
		yield mock_torch_utils

@pytest.fixture
def mock_app_utils():
	with patch('src.models.text_summary_repository.AppUtils') as mock_app_utils:
		mock_app_utils.is_app_frozen.return_value = False
		mock_app_utils.app_base_path.return_value = Path('/')
		yield mock_app_utils