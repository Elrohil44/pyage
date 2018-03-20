import random
from pyage.core.emas import EmasAgent
from pyage.core.operator import Operator
from pyage.sat_cnf.sat_genotype import SatGenotype
from pyage.core.inject import Inject
import random


class EmasInitializer(object):

    def __init__(self, values, energy, size, problem):
        self.values = values
        self.size = size
        self.energy = energy
        self.problem = problem

    @Inject("naming_service")
    def __call__(self):
        agents = {}
        for value in self.values:
            agent = EmasAgent(SatGenotype(value, self.problem), self.energy, self.naming_service.get_next_agent())
            agents[agent.get_address()] = agent
        return agents


def root_agents_factory(count, type):
    def factory():
        agents = {}
        for i in range(count):
            agent = type('R' + str(i))
            agents[agent.get_address()] = agent
        return agents

    return factory


class SATValuesInitializer(Operator):
    def process(self, population):
        values = self.__call__()
        population.extend(list(map(lambda x: SatGenotype(x, self.problem), values)))

    def __init__(self, variables, size, seed, problem):
        self.size = size
        self.variables = variables
        self.required_type = None
        self.problem = problem
        random.seed(seed)

    def __call__(self):
        return [[0 if random.random() > 0.5 else 1 for _ in xrange(self.variables)] for _ in xrange(self.size)]
