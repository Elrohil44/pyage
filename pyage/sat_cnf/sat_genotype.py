class SatGenotype(object):
    def __init__(self, evaluation, problem):
        super(SatGenotype, self).__init__()
        self.evaluation = evaluation
        self.fitness = None
        self.problem = problem

    def get_unsatisfied(self):
        array = []
        for clause in self.problem:
            satisfied = False
            for expected, var in clause:
                if expected == self.evaluation[var]:
                    satisfied = True
                    break
            if not satisfied:
                array.extend(list(map(lambda (x, y): y, clause)))
        return list(dict.fromkeys(array))
