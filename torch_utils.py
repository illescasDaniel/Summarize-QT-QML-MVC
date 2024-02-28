import torch

class TorchUtils:

	@staticmethod
	def get_device() -> torch.device:
		if torch.cuda.is_available():
			print(f"Using CUDA device: {torch.cuda.get_device_name(torch.device('cuda'))}")
			return torch.device('cuda')
		elif torch.backends.mps.is_available():
			print("Using MPS device")
			return torch.device('mps')
		else:
			print("Using CPU")
			return torch.device('cpu')
	
	@staticmethod
	def set_default_device(device: torch.device):
		torch.set_default_device(device)