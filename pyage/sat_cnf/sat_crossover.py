import random
from pyage.core.operator import Operator
from pyage.sat_cnf.sat_genotype import SatGenotype

import logging

logger = logging.getLogger(__name__)


class AbstractCrossover(Operator):
    def __init__(self, type, size):
        super(AbstractCrossover, self).__init__(type)
        self.__size = size

    def process(self, population):
        parents = list(population)
        for i in range(len(population), self.__size):
            p1, p2 = random.sample(parents, 2)
            genotype = self.cross(p1, p2)
            population.append(genotype)

    def cross(self, p1, p2):
        return p1


class CrossoverTwoPoints(AbstractCrossover):
    def __init__(self, size):
        super(CrossoverTwoPoints, self).__init__(SatGenotype, size)

    def cross(self, p1, p2):
        random.seed()

        a, b = random.choice(xrange(len(p1.evaluation))), random.choice(xrange(len(p1.evaluation)))
        a, b = sorted((a, b))
        return SatGenotype(p1.evaluation[:a] + p2.evaluation[a:b] + p1.evaluation[b:], p1.problem)

    def __str__(self):
        return "CrossoverTwoPoints"


class CrossoverOnePoint(AbstractCrossover):
    def __init__(self, size):
        super(CrossoverOnePoint, self).__init__(SatGenotype, size)

    def cross(self, p1, p2):
        random.seed()

        a = random.choice(xrange(len(p1.evaluation)))

        return SatGenotype(p1.evaluation[:a] + p2.evaluation[a:], p1.problem)

    def __str__(self):
        return "CrossoverOnePoint"


class CrossoverUniform(AbstractCrossover):
    def __init__(self, size):
        super(CrossoverUniform, self).__init__(SatGenotype, size)

    def cross(self, p1, p2):
        random.seed()

        new_evaluation = []
        for i in xrange(len(p1.evaluation)):
            val = (p1, p2)[i % 2].evaluation[i]
            new_evaluation.append(val)

        return SatGenotype(new_evaluation, p1.problem)

    def __str__(self):
        return "CrossoverUniform"


class CrossoverRandomGenes(AbstractCrossover):
    def __init__(self, size):
        super(CrossoverRandomGenes, self).__init__(SatGenotype, size)

    def cross(self, p1, p2):
        random.seed()

        new_evaluation = []
        for i in xrange(len(p1.evaluation)):
            val = (p1, p2)[int(random.random() + 0.5)].evaluation[i]
            new_evaluation.append(val)

        return SatGenotype(new_evaluation, p1.problem)

    def __str__(self):
        return "CrossoverRandomGenes"
