DIM = 100  # Number of bits in the bit strings (i.e. the "models").
NOISE_STDEV = 0.01  # Standard deviation of the simulated training noise.

import random

def random_architecture():
  return random.randint(0, 2**DIM - 1)

def mutate_arch(parent_arch):
  position = random.randint(0, DIM - 1)  # Index of the bit to flip.

  # Flip the bit at position `position` in `child_arch`.
  child_arch = parent_arch ^ (1 << position)

  return child_arch
