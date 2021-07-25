"""
Example script to plot 3 variables on a 2D plot.
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

plt.rcParams['mathtext.fontset'] = 'stix' # 'cm'
plt.rcParams["font.family"] = "Times New Roman"

font = {'family' : 'Times New Roman', #'serif',
        'color' : 'black',
        'weight' : 'normal',
        'size' : 14,}

fig, ax = plt.subplots(figsize=(3.8, 4),constrained_layout=False)
plt.subplots_adjust(left=None, bottom=None, right=0.85, top=None, wspace=None, hspace=None)


# Q6p1 = pd.read_csv('fitness_Q6p1_200k.csv') 
# Q6p2 = pd.read_csv('fitness_Q6p2_200k.csv') 

# x = Q6p1.loc[:,"Cost"]
# y = Q6p1.loc[:,"Efficiency"]
# z = Q6p1.loc[:,"Weighted Ripple"]

# x2 = Q6p2.loc[:,"Cost"]
# y2 = Q6p2.loc[:,"Efficiency"]
# z2 = Q6p2.loc[:,"Weighted Ripple"]

# marker= '^'
# label= None

# fig, ax = plt.subplots(figsize=(3.8, 4),constrained_layout=False)

# bbox_props = dict(boxstyle="square,pad=0.5", fc="white", ec="k", lw=1)

# ax.annotate('2', xy=(4.15, -96),  xycoords='data',
            # xytext=(4.5, -95.6), textcoords='data',
            # arrowprops=dict(facecolor='black', shrink=0.01, width=1, headwidth=8),
            # horizontalalignment='left', verticalalignment='center', bbox=bbox_props,
            # fontsize=12, fontweight='bold')

# ax.annotate('1', xy=(6, -97.8),  xycoords='data',
            # xytext=(5.1, -98), textcoords='data',
            # arrowprops=dict(facecolor='black', shrink=0.01, width=1, headwidth=8),
            # horizontalalignment='left', verticalalignment='center', bbox=bbox_props,
            # fontsize=12, fontweight='bold')
 
# scatter_1 = plt.scatter(x, y, c=z, s=40,  edgecolor=None, alpha=0.5, \
    # cmap='viridis', marker='$1$', zorder=99, vmin=0, vmax=20, label=label)
# scatter_2 = plt.scatter(x2, y2, c=z2, s=40,  edgecolor=None, alpha=0.5, \
    # cmap='viridis', marker='$2$', zorder=99, vmin=0, vmax=20, label=label)
    

# plt.grid(True, linewidth = 0.5, color = '#A9A9A9', linestyle = '-.' )

# x_label = r'$\rm {Cost}$ [USD]'
# x_text  = '%.1f'
# y_label = r'$-\eta$ [%]'
# y_text  = '%.1f'
# z_label = r'$\rm Weighted$ $\rm Ripple$ [1]'
# z_text  = '%.1f'

# axins = inset_axes(ax,
                   # width="3%",  # width = 5% of parent_bbox width
                   # height="100%",  # height : 50%
                   # loc='lower left',
                   # bbox_to_anchor=(1, 0., 1, 1),
                   # bbox_transform=ax.transAxes,
                   # borderpad=0,
                   # )
           
# clb = fig.colorbar(scatter_2, cax=axins)
# clb.ax.set_ylabel(z_label, rotation=90, labelpad=20, **font)
# clb.ax.yaxis.set_label_coords(-3,0.5)
# clb.ax.yaxis.set_major_locator(mtick.MaxNLocator(6))

# fig.legend(('Q6p1','Q6p2'),bbox_to_anchor=(0.9, 0.9))

# ax.set_xlabel(x_label, **font)
# ax.set_ylabel(y_label, **font)
# ax.xaxis.set_major_locator(mtick.MaxNLocator(6))
# ax.yaxis.set_major_locator(mtick.MaxNLocator(6))



# # plt.savefig('paretoplot_100k.eps', bbox_inches='tight', format='eps')
# fig.savefig('paretoplot_200k.png', bbox_inches='tight', dpi=600)