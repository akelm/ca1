import logging
import os
import shutil

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from plot_mappings import colormaps_dict, vmax_dict, vmin_dict, colorbar_dict, colorbar_ticks, colorbar_labels


def history_to_img(history):
    ax: plt.Axes
    fig: plt.Figure
    fig, ax = plt.subplots()
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='10%', pad=0.15)
    yticks_len, xticks_len  = history[0].states.shape
    xticks = np.arange(xticks_len+1)-0.5
    yticks = np.arange(yticks_len+1)-0.5
    xrange = xticks[0], xticks[-1]
    yrange = yticks[0], yticks[-1]
    logging.debug("plotting, before makedirs")
    shutil.rmtree('img',ignore_errors=True)
    os.makedirs("img", exist_ok=True)
    logging.debug("plotting, after makedirs")
    for ind, current in enumerate(history):
        for label, arr in zip(('state', 'strategy',"payoff"), (current.states, current.strategies, current.payoff)):
            ax.cla()
            cax.cla()

            ims = ax.imshow(arr, cmap = colormaps_dict[label], vmax=vmax_dict[label], vmin=vmin_dict[label])
            if colorbar_dict[label]:
                cbar=fig.colorbar(ims, cax=cax, orientation='vertical')
                cbar.set_ticks(colorbar_ticks[label])
                cbar.ax.set_yticklabels(colorbar_labels[label])

            ax.set_xticks(xticks)
            ax.set_yticks(yticks)
            ax.grid(color = 'blue', linestyle = '--', linewidth = 0.5)
            ax.set_xlim(*xrange)
            ax.set_ylim(*yrange)
            ax.set_yticklabels("")
            ax.set_xticklabels("")
            ax.invert_yaxis()
            filename = "./img/%s_%d.png" % (label, ind)
            fig.savefig(filename)
