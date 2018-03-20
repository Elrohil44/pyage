# coding=utf-8
import logging
import os
import math

from pyage.core import address
from pyage.core.agent.agent import generate_agents, Agent

from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition

from pyage.sat_cnf.sat_crossover import CrossoverUniform, CrossoverOnePoint, CrossoverTwoPoints
from pyage.sat_cnf.sat_eval import Evaluation
from pyage.sat_cnf.sat_init import EmasInitializer, root_agents_factory, SATValuesInitializer
from pyage.sat_cnf.sat_mutation import MutationRandomGenes, MutationReverse, MutationXorTemplate
from pyage.sat_cnf.naming_service import NamingService
from pyage.sat_cnf.sat_loader import load_file
from pyage.sat_cnf.sat_selection import TournamentSelection

logger = logging.getLogger(__name__)

problem, variables, clauses = load_file('zebra_v155_c1135.cnf')


agents_count = 2
agents = generate_agents("agent", agents_count, Agent)

stop_condition = lambda: StepLimitStopCondition(10000)

probability = 0.5
crossover = lambda: CrossoverUniform(size=40)
mutation = lambda: MutationRandomGenes(probability=probability, evol_probability=0.5)

operators = lambda: [Evaluation(problem), TournamentSelection(size=20, tournament_size=20),
                     crossover(),
                     mutation()]

initializer = lambda: SATValuesInitializer(variables, 30, 0, problem=problem)


def simple_cost_func(x): return abs(x)*10

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics('fitness_%s_%s_%f_pyage_EV.txt' % (crossover(), mutation(), probability))

naming_service = lambda: NamingService(starting_number=2)
