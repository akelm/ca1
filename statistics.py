
from typing import List

import numpy as np

from calc_mappings import CurrentState, strategies_str, pattern_c

zero_header = "#"+"\t".join(map(str, range(1,34+1))) + "\n"
headers = "#iter f_C f_C_corr av_SUM f_allC f_allD f_kD f_kC f_kDC f_strat_ch " + \
          " ".join( ["f_%dD" % k for k in range(8)] + ["f_%dC" % k for k in range(8)]
                    + ["f_%dDC" % k for k in range(8) ])  + "\n"
fmt = "%d" + " %.4g"*33 +"\n"
headers = headers.replace(" ", "\t")
fmt = fmt.replace(" ", "\t")

neighbourhood_inds=np.array([
    (-1,0), (-1,1), (0,1), (1,1), (1, 0), (1, -1), (0, -1), (-1,-1)
], dtype=int)



def get_neighbourhood(x,y, arr):
    return np.pad(arr,1)[  neighbourhood_inds[:,0] +x +1, neighbourhood_inds[:,1] + y +1]

def statistics_single(history: List[CurrentState]):
    if history:
        output = [zero_header, headers]
        for ind, previous, current in zip(range(len(history)), [history[0]]+history[:-1], history):
            f_C = current.states.sum()/current.states.size
            view: np.ndarray = np.lib.stride_tricks.sliding_window_view(np.pad(current.states, 1), (3, 3)).reshape(
                [-1, 3,3])
            f_C_corr  = np.all(view==pattern_c, axis=(1,2)).sum()/current.states.size

            av_SUM = current.payoff.sum()/current.payoff.size/8
            f_allC = (current.strategies == strategies_str.index('allC')).sum()/current.strategies.size
            f_allD = (current.strategies == strategies_str.index('allD')).sum()/current.strategies.size

            kD_list = np.array([(current.strategies == strategies_str.index('%dD' % k)).sum() for k in range(8)])
            f_kD = kD_list.sum()/current.strategies.size
            f_kD_arr = kD_list/kD_list.sum() if kD_list.sum()!=0 else kD_list

            kC_list = np.array([(current.strategies == strategies_str.index('%dC' % k)).sum() for k in range(8)])
            f_kC = kC_list.sum() / current.strategies.size
            f_kC_arr = kC_list / kC_list.sum()  if kC_list.sum()!=0 else kC_list

            kDC_list = np.array([(current.strategies == strategies_str.index('%dDC' % k)).sum() for k in range(8)])
            f_kDC = kDC_list.sum() / current.strategies.size
            f_kDC_arr = kDC_list / kDC_list.sum()  if kDC_list.sum()!=0 else kDC_list

            f_strat_ch = (current.strategies != previous.strategies).sum()/current.strategies.size

            output.append(
                fmt % (ind, f_C, f_C_corr, av_SUM, f_allC, f_allD, f_kD, f_kC, f_kDC, f_strat_ch, *f_kD_arr.tolist(), *f_kC_arr.tolist(), *f_kDC_arr.tolist())
            )


        with open("results.txt", 'w') as file:
            file.writelines(output)