def plot_multi(data, cols=None, spacing=.1, **kwargs):
    from pandas import plotting
    import matplotlib.colors as mcolors

    if cols is None: cols = data.columns
    if len(cols) == 0: return
    
    # Get default color style from pandas - can be changed to any other color list
    colors = sorted(list(mcolors.BASE_COLORS.keys()))
    ## ['b', 'c', 'g', 'k', 'm', 'r', 'w', 'y']

    # First axis
    ax = data.loc[:, cols[0]].plot(label=cols[0], color=colors[0], **kwargs)
    ax.set_ylabel(ylabel=cols[0])
    lines, labels = ax.get_legend_handles_labels()

    for n in range(1, len(cols)):
        # Multiple y-axes
        ax_new = ax.twinx()
        ax_new.spines['right'].set_position(('axes', 1 + spacing * (n - 1)))
        data.loc[:, cols[n]].plot(ax=ax_new, label=cols[n], color=colors[n % len(colors)], **kwargs)
        ax_new.set_ylabel(ylabel=cols[n])

        # Proper legend position
        line, label = ax_new.get_legend_handles_labels()
        lines += line
        labels += label

    ax.legend(lines, labels, loc='lower right', bbox_to_anchor=(1, 1))
    return ax

def get_api_key():
    import configparser as cp
    import os
    
    config_file = os.path.abspath(os.path.join(os.path.dirname('__file__'), '..', 'tradingeconomics.cfg'))

    cfg = cp.ConfigParser()
    cfg.read(config_file)
    return cfg['API']['key']
