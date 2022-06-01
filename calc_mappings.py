import sys
from collections import namedtuple
from functools import partial
from typing import List

import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap


def k_d(k, num_c):
    return 1 if (8 - num_c) <= k else 0

def k_c(k, num_c):
    return 1 if num_c <= k else 0

def k_dc(k, num_c):
    return 1 if (8 - num_c) >= k else 0

def all_d(_):
    return 0

def all_c(_):
    return 1

neigh_list = [[0, 0, 1, 2, 2, 2, 1, 0], [1, 2, 2, 2, 1, 0, 0, 0]]
neigh_list_flat = [8, 1, 2, 7, 0, 3, 6, 5, 4]
neigh_flat_translate = np.vectorize(neigh_list_flat.__getitem__)

strategies_str : List[str]
strategies_str, strategies_fun = zip(*( ((str(k)+key), partial(fun, k))   for key, fun in zip(('D', 'C', 'DC'),(k_d, k_c, k_dc))  for k in range(8) ))
strategies_str += ('allD', 'allC')
strategies_str_lower = tuple(map(str.lower, strategies_str))
strategies_fun+=(all_d, all_c)

strat_translate = np.vectorize(strategies_str.__getitem__)
strat_to_ind = np.vectorize(lambda x: strategies_str_lower.index(x.lower()))

strategy_mutation_str = {
    'allC':['allD'],
    'allD':['allC']
}
strategy_mutation_str.update({str(k) + key : ['allC', 'allD'] for k, key in enumerate(('D',) * 8)})
strategy_mutation_str.update({str(k) + key : ['allC', 'allD', str(k) + 'D', str(k) + 'DC'] for k, key in enumerate(('C',) * 8)})
strategy_mutation_str.update({str(k) + key : ['allC', 'allD', str(k) + 'D', str(k) + 'C'] for k, key in enumerate(('DC',) * 8)})

strategy_mutation_dict = {strategies_str.index(key):list(map(strategies_str.index, value)) for key,value in strategy_mutation_str.items()}

CurrentState = namedtuple("CurrentState", {"states", "strategies","payoff"})

pattern_c = np.array((
    (0,0,0),
    (0,1,0),
    (0,0,0)
))

pattern_d2a = np.array((
    (0,0,0),
    (1,0,1),
    (0,0,0)
))

pattern_d2b = np.array((
    (0,1,0),
    (0,0,0),
    (0,1,0)
))

pattern_d4 = np.array((
    (1,0,1),
    (0,0,0),
    (1,0,1)
))

rng: np.random.Generator


