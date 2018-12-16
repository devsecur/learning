from model import Model
from plot import plot

import collections
import random

cycles = 20000

class World(object):
    def __init__(self, cycles, population_size, sample_size):
        self.cycles = cycles
        self.population_size = population_size
        self.sample_size = sample_size
        self.population = collections.deque()
        self.history = []

        while len(self.population) < self.population_size:
            model = Model()
            model.train_and_eval()
            self.population.append(model)
            self.history.append(model)

    def cruel_world(self):
        while len(self.history) < self.cycles:
          sample = []
          while len(sample) < self.sample_size:
            candidate = random.choice(list(self.population))
            sample.append(candidate)

          parent = max(sample, key=lambda i: i.accuracy)

          child = parent.propagation()
          child.train_and_eval()
          self.population.append(child)
          self.history.append(child)

          self.population.popleft()


world = World(cycles=cycles, population_size=100, sample_size=10)
world.cruel_world()

plot(world.history, world.cycles)
