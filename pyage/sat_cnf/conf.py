# coding=utf-8
import logging
import os
import math

from pyage.core import address

from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition

from pyage.sat_cnf.sat_crossover import CrossoverUniform, CrossoverTwoPoints, CrossoverOnePoint, CrossoverRandomGenes
from pyage.sat_cnf.sat_eval import Evaluation
from pyage.sat_cnf.sat_init import EmasInitializer, root_agents_factory, SATValuesInitializer
from pyage.sat_cnf.sat_mutation import MutationRandomGenes, MutationXorTemplate, MutationReverse
from pyage.sat_cnf.naming_service import NamingService
from pyage.sat_cnf.sat_loader import load_file

logger = logging.getLogger(__name__)

problem, variables, clauses = load_file('zebra_v155_c1135.cnf')
print(variables, clauses)
size = 30
values = SATValuesInitializer(variables, size, 0, problem)()

agents_count = 2
logger.debug("EMAS, %s agents", agents_count)
agents = root_agents_factory(agents_count, AggregateAgent)

stop_condition = lambda: StepLimitStopCondition(100000)

agg_size = 40
aggregated_agents = EmasInitializer(values, energy=40, size=agg_size, problem=problem)

emas = EmasService

minimal_energy = lambda: 10
reproduction_minimum = lambda: 150
migration_minimum = lambda: 120
newborn_energy = lambda: 100
transferred_energy = lambda: 80

budget = 0

probability = 0.5
evaluation = lambda: Evaluation(problem)
crossover = lambda: CrossoverUniform(size=40)
mutation = lambda: MutationRandomGenes(probability=probability, evol_probability=0.5)


def simple_cost_func(x): return abs(x) * 10


address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics('fitness_%s_%s_%f_pyage_EMAS.txt' % (crossover(), mutation(), probability))

naming_service = lambda: NamingService(starting_number=2)
