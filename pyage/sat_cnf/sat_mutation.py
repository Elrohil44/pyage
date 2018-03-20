import logging
import random
from pyage.core.operator import Operator
from pyage.sat_cnf.sat_genotype import SatGenotype

logger = logging.getLogger(__name__)


class AbstractMutation(Operator):
    def __init__(self, type, probability):
        super(AbstractMutation, self).__init__()
        self.probability = probability

    def process(self, population):
        for genotype in population:
            if random.random() < self.probability:
                self.mutate(genotype)

    def mutate(self, genotype):
        pass


class MutationXorTemplate(AbstractMutation):
    def __init__(self, probability, evol_probability):
        super(MutationXorTemplate, self).__init__(SatGenotype, evol_probability)
        self.probability = probability
        self.evol_probability = evol_probability

    def mutate(self, genotype):
        random.seed()
        rand = random.random()
        if rand < self.evol_probability:
            start = 1
        else:
            start = 0
        try:
            for i in xrange(start, len(genotype.evaluation), 2):
                    genotype.evaluation[i] = 1 - genotype.evaluation[i]
        except:
            pass

    def __str__(self):
        return "MutationXorTemplate"


class MutationReverse(AbstractMutation):
    def __init__(self, probability, evol_probability):
        super(MutationReverse, self).__init__(SatGenotype, evol_probability)
        self.probability = probability
        self.evol_probability = evol_probability

    def mutate(self, genotype):
        genotype.evaluation = list(reversed(genotype.evaluation))

    def __str__(self):
        return "MutationReverse"


class MutationRandomGenes(AbstractMutation):
    def __init__(self, probability, evol_probability):
        super(MutationRandomGenes, self).__init__(SatGenotype, evol_probability)
        self.probability = probability
        self.evol_probability = evol_probability

    def mutate(self, genotype):
        random.seed()
        for i in xrange(len(genotype.evaluation)):
            if random.random() < self.evol_probability:
                genotype.evaluation[i] = 1 - genotype.evaluation[i]

    def __str__(self):
        return "MutationRandomGenes"
