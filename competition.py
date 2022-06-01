import logging

import numpy as np
import pandas as pd

from parameters import COMP_PROP, COMP_TOUR
import calc_mappings

def change_strategy(payoff_arr, strat_arr, sync_prob, competition_type=None, min_payoff=0):

    def log_change_strategy():
        view_payoff: np.ndarray = np.lib.stride_tricks.sliding_window_view(
            np.pad(payoff_arr.astype(str), 1, constant_values="_"), (3, 3)).reshape(
            [-1, 3,3])
        view_strat: np.ndarray = np.lib.stride_tricks.sliding_window_view(
            np.pad(calc_mappings.strat_translate(strat_arr), 1, constant_values="_"), (3, 3)).reshape(
            [-1, 3,3])
        df = pd.DataFrame({
            "i": np.indices(strat_arr.shape).reshape([-1, 2])[:, 0] + 1,
            "j": np.indices(strat_arr.shape).reshape([-1, 2])[:, 1] + 1,
            "strat": calc_mappings.strat_translate(strat_arr.flat),
            "payoff": payoff_arr.flat,
            "neigh_pay": list(map(', '.join, view_payoff[:, calc_mappings.neigh_list[0], calc_mappings.neigh_list[1]])),
            "neigh_strat": list(map(', '.join, view_strat[:, calc_mappings.neigh_list[0], calc_mappings.neigh_list[1]])),
            "win" : calc_mappings.neigh_flat_translate(selected_ind.flat),
            "new_strat": calc_mappings.strat_translate(new_strat.flat)


        })
        logging.custom(" CHANGE STRATEGY ".center(80,"#"))
        logging.custom(df.to_string(index=False))

    def log_strategy():
        logging.custom(" STRATEGY ARRAY ".center(80,"#"))
        logging.custom(pd.DataFrame(calc_mappings.strat_translate(new_strat.reshape(strat_arr.shape))).to_string(index=False, header=False))



    # tutaj bedzie competition type
    if competition_type == COMP_PROP:
        view: np.ndarray = np.lib.stride_tricks.sliding_window_view(
            np.pad(payoff_arr, 1, constant_values=min_payoff), (3, 3)).reshape(
            [-1, 9]) - min_payoff
        rand_arr: np.ndarray = calc_mappings.rng.uniform(0, 1, view.shape[0])[:, None]
        steps = view.cumsum(axis=1)/view.sum(axis=1)[:,None]

        selected_ind = (rand_arr <= steps).argmax(axis=1)
    # elif competition_type == COMP_TOUR:
    #     view: np.ndarray = np.lib.stride_tricks.sliding_window_view(
    #         np.pad(payoff_arr, 1, constant_values=np.nan), (3, 3)).reshape(
    #         [-1, 9])
    #     index_view = np.repeat(np.arange(0.0, 9.0)[None,:], view.shape[0], axis=0)
    #     index_view[np.isnan(view)] = np.nan
    #     tour_size = 2
    #     tour_inds = calc_mappings.rng.permutation(index_view, axis=1)
    #     tour_inds = np.apply_along_axis(lambda row: np.concatenate([row[~np.isnan(row)], row[np.isnan(row)]]), axis=1, arr=tour_inds)
    #     tour_inds = tour_inds[:, :tour_size].astype(int)
    #     tour_vals = view[np.repeat(np.arange(view.shape[0])[:,None], tour_size, axis=1),tour_inds]
    #     max_vals = np.nanmax(tour_vals,axis=1)
    #     mask = tour_vals == max_vals[:,None]
    #     mask = np.apply_along_axis(lambda row: np.nonzero(row)[0][0], axis=1, arr=mask)
    #     selected_ind = tour_inds[np.arange(mask.size),mask]
    else:
        view: np.ndarray = np.lib.stride_tricks.sliding_window_view(np.pad(payoff_arr, 1, constant_values=np.iinfo(int).min), (3, 3)).reshape(
            [-1, 9])
        max_vals = np.max(view, axis=1)
        center_is_max = view[:,4] == max_vals
        selected_ind = np.argmax(view, axis=1)
        selected_ind[center_is_max] = 4

    sync_array = np.random.uniform(0, 1, selected_ind.size)
    selected_ind[sync_array > sync_prob] = 4

    view: np.ndarray = np.lib.stride_tricks.sliding_window_view(
        np.pad(strat_arr, 1, constant_values=np.iinfo(int).min), (3, 3)).reshape(
        [-1, 9])
    new_strat =view[np.arange(selected_ind.size),selected_ind]

    log_change_strategy()
    log_strategy()
    return new_strat.reshape(strat_arr.shape)