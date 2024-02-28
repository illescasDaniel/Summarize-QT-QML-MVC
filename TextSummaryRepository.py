from math import ceil
from transformers import pipeline
from torch_utils import TorchUtils
import numpy as np

class TextSummaryRepository:

	def __init__(self):
		super().__init__()
		with TorchUtils.get_device() as device:
			TorchUtils.set_default_device(device)
			self.summarizer = pipeline(
				task='summarization', 
				model='facebook/bart-large-cnn', 
				device=device
			)

	def summarize(self, input_text):
		input_text_tokens =  input_text.split(' ')
		max_tokens = 1024
		full_text = str()
		for chunk in np.array_split(input_text_tokens, indices_or_sections=ceil(len(input_text_tokens)/max_tokens)):
			text_tokens: int = len(chunk)
			if text_tokens <= 30:
				full_text += ' '.join(chunk)
			else:
				max_length = int(min(float(text_tokens) / 1.5, 200.0))
				min_length = int(min(30, max_length))
				print(len(chunk), max_length, min_length)
				output: list[dict[str, str]] = self.summarizer(
					' '.join(chunk), 
					max_length=max_length, 
					min_length=min_length, 
					do_sample=False
				) # type: ignore
				text_output = output[0]['summary_text']
				full_text += text_output
			yield full_text
		print('finished')
