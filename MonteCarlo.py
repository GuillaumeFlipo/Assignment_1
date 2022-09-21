import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import modelFunction
from scipy.stats import lognorm, norm

def monteCarlo(C0=0):
    n_MC = 100
    Concentration_df = modelFunction()
    Concentration = Concentration_df['SimConcentration']

    Concentration_MC = np.zeros([len(Concentration), n_MC])

    x1 = 1.1
    p1 = 0.25
    x2 = 5
    p2 = 0.95

    x1 = np.log(x1)
    x2 = np.log(x2)
    p1ppf = norm.ppf(p1)
    p2ppf = norm.ppf(p2)

    scale = (x2 - x1) / (p2ppf - p1ppf)
    mean = ((x1 * p2ppf) - (x2 * p1ppf)) / (p2ppf - p1ppf)

    CSO_conc_sample = lognorm.rvs(s=scale, scale=np.exp(mean), size=n_MC)


    for i in range(n_MC):
        Concentration_MC[:,i] = modelFunction(C0, CSO_conc_sample[i])["SimConcentration"]
    q05 = np.percentile(Concentration_MC, 5, axis=1)
    q50 = np.percentile(Concentration_MC, 50, axis=1)
    q95 = np.percentile(Concentration_MC, 95, axis=1)
    print('max q05', np.max(q05))
    print('max median', np.max(q50))
    print('max q95', np.max(q95))

    t = Concentration_df['Distance']

    plt.figure()
    plt.rcParams.update({'font.size': 20})
    # ax1 = plt.subplot(2, 1, 1)
    # plt.plot(t, Concentration, color='green', linestyle='-', label='deterministic')
    # plt.legend()
    # plt.grid()
    # ax1.set_xlabel("Distance [m]")
    # ax1.set_ylabel("concentration [μg/l]")


    for i in range(n_MC):
        plt.plot(t, Concentration_MC[:, i], color=(.7, .7, .7), linestyle='-')

    plt.plot(t, q05, color='red', linestyle=('--'), label='5% percentile')
    plt.plot(t, q50, color='blue', linestyle=('--'), label='median')
    plt.plot(t, q95, color='red', linestyle=('--'), label='95% percentile')
    plt.legend()
    plt.grid()
    plt.xlabel("Distance [m]")
    plt.ylabel("concentration [μg/l]")
    plt.show()


if __name__ == "__main__":
    monteCarlo(0)

