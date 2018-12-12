import random

DIM = 100		# Number of bits in the bit strings (i.e. the "models").
NOISE_STDEV = 0.01		# Standard deviation of the simulated training noise.

class Model(object):
	def __init__(self):
		self.arch = None
		self.accuracy = None

	def __str__(self):
		"""Prints a readable version of this bitstring."""
		return '{0:b}'.format(self.arch)

	def train_and_eval(self):
		accuracy =	float(self._sum_bits()) / float(DIM)
		accuracy += random.gauss(mu=0.0, sigma=NOISE_STDEV)
		accuracy = 0.0 if accuracy < 0.0 else accuracy
		accuracy = 1.0 if accuracy > 1.0 else accuracy
		self.accuracy = accuracy

	def _sum_bits(self):
		total = 0
		arch = self.arch
		for _ in range(DIM):
			total += arch & 1
			arch = (arch >> 1)
		return total
