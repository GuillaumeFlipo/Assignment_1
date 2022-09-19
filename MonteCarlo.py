import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import modelFunction
from scipy.stats import lognorm, norm

def monteCarlo(C0=0):
    n_MC = 100
    Concentration_df = modelFunction(C0,CS0_conc=1)
    Concentration = Concentration_df['Concentration']
    CSO_conc_sample = lognorm(s=1, scale=1, size=n_MC )
    Concentration_MC = np.zeros([len(Concentration), n_MC])

    for i in range(n_MC):
        Concentration_MC[:,i] = modelFunction(C0, CSO_conc_sample[i])["SimConcentration"]
    q05 = np.percentile(Concentration_MC, 5, axis=1)
    q50 = np.percentile(Concentration_MC, 50, axis=1)
    q95 = np.percentile(Concentration_MC, 95, axis=1)

    t = Concentration_df['time']
    plt.figure()
    plt.rcParams.update({'font.size': 20})
    ax1 = plt.subplot(2, 1, 1)
    plt.plot(t, Concentration, color='green', linestyle='-', label='deterministic')
    plt.legend()
    plt.grid()
    ax1.set_xlabel("time [d]")
    ax1.set_ylabel("concentration [mg/l]")

    ax2 = plt.subplot(2, 1, 2)
    for i in range(n_MC):
        plt.plot(t, Concentration_MC[:, i], color=(.7, .7, .7), linestyle='-')

    plt.plot(t, q05, color='red', linestyle=('--'), label='5% percentile')
    plt.plot(t, q50, color='blue', linestyle=('--'), label='median')
    plt.plot(t, q95, color='red', linestyle=('--'), label='95% percentile')
    plt.legend()
    plt.grid()
    ax2.set_xlabel("time [d]")
    ax2.set_ylabel("concentration [mg/l]")

