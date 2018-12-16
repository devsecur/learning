import random

DIM = 100		# Number of bits in the bit strings (i.e. the "models").
NOISE_STDEV = 0.01		# Standard deviation of the simulated training noise.

class Model(object):
    # Birth function - if no parents, the dna is random, else the dna is parent
    # After dna is determined, the dna mutates
	def __init__(self, dna=random.randint(0, 2**DIM - 1)):
		self.dna = dna
		self.mutate()

	def mutate(self):
		position = random.randint(0, DIM - 1)
		self.dna = self.dna ^ (1 << position)

	def __str__(self):
		"""Prints a readable version of this bitstring."""
		return '{0:b}'.format(self.dna)

	def train_and_eval(self):
		accuracy = 0
		dna = self.dna
		for _ in range(DIM):
			accuracy += dna & 1
			dna = (dna >> 1)
		accuracy =	accuracy / float(DIM)
		accuracy += random.gauss(mu=0.0, sigma=NOISE_STDEV)
		accuracy = 0.0 if accuracy < 0.0 else accuracy
		accuracy = 1.0 if accuracy > 1.0 else accuracy
		self.accuracy = accuracy

	def propagation(self):
		child = Model(self.dna)
		return child
