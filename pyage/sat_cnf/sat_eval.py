import random

from pyage.core.operator import Operator
from pyage.sat_cnf.sat_genotype import SatGenotype


class Evaluation(Operator):
    def __init__(self, problem, type=None):
        super(Evaluation, self).__init__(SatGenotype)
        self.problem = problem

    def process(self, population):
        for genotype in population:
            genotype.fitness = self.eval(genotype)

    def eval(self, genotype):
        clauses_satisfied = 0
        for clause in self.problem:
            fitness_sum = 0
            for sign, var in clause:
                if sign == genotype.evaluation[var]:
                    fitness_sum += 1
            if fitness_sum > 0:
                clauses_satisfied += 1.0

        return clauses_satisfied
