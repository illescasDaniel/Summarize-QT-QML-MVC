import pytest
from unittest.mock import MagicMock, Mock, patch
from src.models.text_summary_repository import TextSummaryRepository
from utils.generator_tracker import GeneratorTracker

@pytest.fixture
def mock_pipeline():
	with patch('src.models.text_summary_repository.pipeline') as mock_pipeline_function:
		mock_pipeline_object = MagicMock()
		mock_pipeline_function.return_value = mock_pipeline_object
		yield (mock_pipeline_function, mock_pipeline_object)

def test_given_input_when_summarize_then_smaller_text_expected(mock_pipeline):
	# Given a normal text with more than 30 words
	mock_pipeline_function, mock_pipeline_object = mock_pipeline
	# this below would be equivalent to: mock_pipeline_object.__call__ = ..., but that doesn't work
	mock_pipeline_object.return_value = [{'summary_text': 'This is a summary.'}]

	repository = TextSummaryRepository()
	repository.initialize(device=Mock())
	input_text = 'This is a detailed text that needs to be summarized 11 22 13 14 15 16 17 18 19 20 21 22 23 24 25 26 277 28 29 30 31 32.'

	# When
	summarize_generator = GeneratorTracker(repository.summarize(input_text))
	summary = ''.join(summarize_generator)

	# Then
	assert summary == 'This is a summary.'
	assert summarize_generator.count == 1
	mock_pipeline_function.assert_called_once()
	mock_pipeline_object.assert_called_once()

def test_given_small_input_when_summarize_then_input_is_same_as_output(mock_pipeline):
	# Given a text that is smaller or equal to the minimium length (30 words)
	text = 'This is a detailed text.'
	mock_pipeline_function, mock_pipeline_object = mock_pipeline

	repository = TextSummaryRepository()
	repository.initialize(device=Mock())

	# When
	summarize_generator = GeneratorTracker(repository.summarize(text))
	summary = ''.join(summarize_generator)

	# Then
	assert summary == text
	assert summarize_generator.count == 1
	mock_pipeline_function.assert_called_once()
	mock_pipeline_object.assert_not_called()

def test_given_no_initialization_when_summarize_then_exception_raised(mock_pipeline):
	mock_pipeline_function, mock_pipeline_object = mock_pipeline
	mock_pipeline_object.return_value = None
	with pytest.raises(AttributeError) as error:
		# Given method initialize is not called
		repository = TextSummaryRepository()
		input_text = 'This is a detailed text that needs to be summarized 11 22 13 14 15 16 17 18 19 20 21 22 23 24 25 26 277 28 29 30 31 32.'
		# When we call summarize
		next(repository.summarize(input_text))
	# Then error raised
	assert str(error.value) == "No device or summarizer, you must call initialize first"
	mock_pipeline_function.assert_not_called()
	mock_pipeline_object.assert_not_called()

# TODO: test min and max lengths
# mock_pipeline_object.assert_called_once_with(
# 	input_text,
# 	max_length=32,
# 	min_length=32,
# 	do_sample=False
# )

# TODO: more than 1024 characters (import a file please)
# check that summarize is called multiple times if the input is larger than 1024

# TODO: test other stuff in the app