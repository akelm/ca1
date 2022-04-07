import random

import numpy as np

C = True
D = False
N = 8  # neighbours


strategies_mapping = {
    "2C": lambda n: C if n <= 2 else D,
    "2D": lambda n: C if (N - n) <= 2 else D,
    "2DC": lambda n: C if (N - n) >= 2 else D,  
    "allC": lambda n: C,
    "allD": lambda n: D
}

payoffC = lambda c: c
payoffD = lambda c: 1.2 * c + 0.1 * (N - c)

payoff = {C: payoffC, D: payoffD}


neigh_list = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def get_neighbours(i, j, n_rows, n_cols):
    result = []
    for neigh in neigh_list:
        n_i = (i + neigh[0]) % n_cols
        n_j = (j + neigh[1]) % n_rows
        result.append((n_i, n_j) )
    return result


def calc_C_neighbrous_number(state: np.ndarray):
    n_rows, n_cols = state.shape
    assert n_rows>0
    assert n_cols > 0
    c_neigh = np.zeros([n_rows, n_cols], dtype=int)
    for i in range(n_rows):
        for j in range(n_cols):
            for n_i, n_j in get_neighbours(i, j, n_rows, n_cols):
                c_neigh[i, j] += (state[n_i, n_j] == C)
    return c_neigh

def change_state(state, strategies, neighbours):
    n_rows, n_cols = state.shape
    assert n_rows>0
    assert n_cols > 0
    new_state = state.copy()
    for i in range(n_rows):
        for j in range(n_cols):
            new_state[i, j ] = strategies_mapping[strategies[i,j]](neighbours[i,j])
    return new_state



def change_strategy(strategies: np.ndarray, payoff_table):
    n_rows, n_cols = strategies.shape
    assert n_rows>0
    assert n_cols > 0
    new_strategies = strategies.copy()
    # best strategy
    for i in range(n_rows):
        for j in range(n_cols):
            # find neighbours with best score
            best_score = payoff_table[i, j]
            best_score_list = [ (i,j) ]
            for n_i, n_j in get_neighbours(i,j, n_rows,n_cols):
                if payoff_table[n_i, n_j] > best_score:
                    best_score_list = [ (n_i, n_j) ]
                    best_score = payoff_table[n_i, n_j]
                elif payoff_table[n_i, n_j] == best_score:
                    best_score_list.append((n_i,n_j))
            # copy_i, copy_j = random.choice(best_score_list)
            copy_i, copy_j = best_score_list[0]
            new_strategies[i,j] = strategies[copy_i, copy_j]
    return new_strategies

if __name__ == "__main__":


    # t0
    state = np.array([[C, C, D, D], [D, C, D, D], [D, D, D, C], [C, D, D, C]], dtype=int)
    strategies = np.array([["2C", "allC", "allD", "2C"], ["2C", "2C", "2D", "2DC"], ["allD", "2D", "2C", "2C"], ["allD", "2C", "allD", "2C"]])
    payoff_table = np.zeros(state.shape)
    neighbours = calc_C_neighbrous_number(state) # number of C neighbours

    iteration_list = []
    iteration_list.append( (state.copy(), strategies.copy(), payoff_table.copy()) )


    for i in range(3):
        # t i+1

        # new state
        state = change_state(state,strategies,neighbours)
        # new C neighbours
        neighbours = calc_C_neighbrous_number(state)
        # calculate payoff
        payoff_table = payoffD(neighbours) * (state == D) + payoffC(neighbours) * state
        # calculate new strategies
        strategies = change_strategy(strategies,payoff_table)
        # add to state list
        iteration_list.append((state.copy(), strategies.copy(), payoff_table.copy()))


