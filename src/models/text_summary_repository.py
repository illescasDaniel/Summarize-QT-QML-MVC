import logging
from math import ceil
from collections.abc import Generator
from typing import Any, Optional
import torch
import numpy as np
from transformers import pipeline, Pipeline
from models.utils.app_utils import AppUtils
from models.utils.torch_utils import TorchUtils


class TextSummaryRepository:
	__summarizer: Optional[Pipeline] = None
	__device: Optional[torch.device] = None
	__MIN_TOKENS: int = 30
	__MAX_TOKENS: int = 1024

	def initialize(self, device: Optional[torch.device] = None):
		if device is None:
			logging.debug('Loading device')
			with TorchUtils.get_device() as device:
				self.__device = device
				TorchUtils.set_default_device(device)
				logging.debug('device loaded')
		else:
			self.__device = device

		if self.__summarizer is None:
			logging.debug('Loading model')
			if AppUtils.is_app_frozen():
				model_directory = AppUtils.app_base_path() / 'model_directory'
				self.__summarizer = pipeline(
					task='summarization',
					model=str(model_directory),
					tokenizer=str(model_directory),
					device=self.__device
				)
			else:
				self.__summarizer = pipeline(
					task='summarization',
					model='facebook/bart-large-cnn',
					device=self.__device
				)
			logging.debug('model loaded')

	def summarize(self, input_text: str) -> Generator[str, Any, None]:
		if self.__device is None or self.__summarizer is None:
			raise AttributeError('No device or summarizer, you must call initialize first')
		input_text_tokens = input_text.split(' ')
		max_tokens = TextSummaryRepository.__MAX_TOKENS
		for chunk in np.array_split(input_text_tokens, indices_or_sections=ceil(len(input_text_tokens) / max_tokens)):
			text_tokens: int = len(chunk)
			if text_tokens <= TextSummaryRepository.__MIN_TOKENS:
				yield ' '.join(chunk)
			else:
				max_length = int(min(max(TextSummaryRepository.__MIN_TOKENS, float(text_tokens) * 0.5), text_tokens))
				min_length = TextSummaryRepository.__MIN_TOKENS
				logging.debug(f"chunk length:{len(chunk)}, max_length{max_length}, min_length{min_length}")
				output: list[dict[str, str]] = self.__summarizer(
					' '.join(chunk),
					max_length=max_length,
					min_length=min_length,
					do_sample=False
				)  # type: ignore
				text_output = output[0]['summary_text']
				yield text_output
		logging.debug('finished')
