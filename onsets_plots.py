# This file consists of the functions used in the Jupyter Notebook Pulse_Analysis_Biosppy-EnergyMaps-GitHub
import pylab as plt
import numpy as np
import matplotlib as matplotlib
import matplotlib.animation as animation

# Get the onset of task activity based on the time stamp (interval) and the sampling frequency (fs) for needle data (data). 
def get_needle_onset_cts(data, fs, interval): 
    onset_cts = [] 
    for i in range(len(interval)): 
        st = interval[i][0]*fs
        sp = interval[i][1]*fs
        onset_cts.append(len([i for i in data['onsets'] if i > st and i < sp]) )
    return onset_cts

# Get the onset of task activity based on the time stamp (interval) and the sampling frequency (fs) for surface data (data). 
def get_surface_onset_cts(data, fs, interval): 
    S_onset_cts = {} 
    for c in range(len(data)): 
        temp = []
        for i in range(len(interval)): 
            st = interval[i][0]*fs
            sp = interval[i][1]*fs
            temp.append(len([i for i in data['Ch'+str(c)]['onsets'] if i > st and i < sp]))
        S_onset_cts['Ch'+str(c)]= temp
    return S_onset_cts

# Generating Bar Plot of the data's average onsets during specific tasks 
def generate_bar_plot_tasks(n_task1,n_task2, s_task, dataDQ, dataDC, dataS, s_colors, title, x_axis, x_labels, rotation): 
    plt.figure() 
    plt.bar([1], np.mean(dataDQ[n_task1:n_task2]), color = 'k')
    plt.bar([2], np.mean(dataDC[n_task1:n_task2]), color ='C7')
    for i in range(8): 
        plt.bar([i+3], dataS[i,s_task], color='C%s'%s_colors[i])

    plt.title(title, fontsize = 20)
    plt.ylabel('Average Pulse Counts', fontsize = 18)
    plt.xticks(x_axis, x_labels, rotation=rotation, fontsize = 14)

# Generating the Heat map for the surface data's average onset counts 
def generate_surface_heat_map(dataS, task, title): 
    fig, ax = plt.subplots(1,1, figsize=(8,6))
    cmap = matplotlib.cm.PuBu
    cbar_ax = fig.add_axes([.92, .25, .04, .5])
    xCh= np.arange(1,5)
    yCh= np.arange(1,3)

    im0 =ax.imshow( dataS[:,task].reshape(2,4), cmap=cmap, interpolation = 'none', vmin = 0, vmax = 110, origin = "lower")
    ax.set_title(title, fontsize = 18)
    ax.set_xticks(np.arange(0, 4, 1), minor=False)
    ax.set_yticks(np.arange(0, 2, 1), minor=False)
    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
    ax.set_xticklabels(xCh, fontsize = 16);
    ax.set_yticklabels(yCh, fontsize = 16);
    cbar = fig.colorbar(im0,cax=cbar_ax)
    cbar.ax.tick_params(labelsize=14)
