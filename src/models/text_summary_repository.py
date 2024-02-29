from collections.abc import Generator
from math import ceil
from typing import Any
from transformers import pipeline, Pipeline
from models.utils.app_utils import AppUtils
from models.utils.torch_utils import TorchUtils
import numpy as np
import torch
import logging


class TextSummaryRepository:
	summarizer: Pipeline | None = None
	device: torch.device | None = None

	def summarize(self, input_text: str) -> Generator[str, Any, None]:
		if self.device is None:
			logging.debug('Loading device')
			with TorchUtils.get_device() as device:
				self.device = device
				TorchUtils.set_default_device(device)
				logging.debug('device loaded')
		if self.summarizer is None:
			logging.debug('Loading model')
			if AppUtils.is_app_frozen():
				model_directory = AppUtils.app_base_path() / 'model_directory'
				self.summarizer = pipeline(
					task='summarization',
					model=str(model_directory),
					tokenizer=str(model_directory),
					device=self.device
				)
			else:
				self.summarizer = pipeline(
					task='summarization',
					model='facebook/bart-large-cnn',
					device=self.device
				)
			logging.debug('model loaded')
		input_text_tokens = input_text.split(' ')
		max_tokens = 1024
		full_text = str()
		for chunk in np.array_split(input_text_tokens, indices_or_sections=ceil(len(input_text_tokens) / max_tokens)):
			text_tokens: int = len(chunk)
			if text_tokens <= 30:
				full_text += ' '.join(chunk)
			else:
				max_length = int(min(float(text_tokens) / 1.5, 200.0))
				min_length = int(min(30, max_length))
				logging.debug(f"chunk length:{len(chunk)}, max_length{max_length}, min_length{min_length}")
				output: list[dict[str, str]] = self.summarizer(
					' '.join(chunk),
					max_length=max_length,
					min_length=min_length,
					do_sample=False
				)  # type: ignore
				text_output = output[0]['summary_text']
				if len(full_text) == 0:
					full_text += text_output
				else:
					full_text += f' {text_output}'
			yield full_text
		logging.debug('finished')
