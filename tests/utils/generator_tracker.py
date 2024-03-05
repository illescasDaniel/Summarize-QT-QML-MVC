from typing import Generator, TypeVar, Generic, Iterator

T = TypeVar('T')  # Generic type variable

class GeneratorTracker(Iterator[T], Generic[T]):
	count: int
	__generator: Generator[T, None, None]

	def __init__(self, generator: Generator[T, None, None]):
		self.__generator = generator
		self.count = 0

	def __iter__(self) -> 'GeneratorTracker[T]':
		return self

	def __next__(self) -> T:
		try:
			next_item = next(self.__generator)
			self.count += 1
			return next_item
		except StopIteration:
			raise

# Example usage remains the same
