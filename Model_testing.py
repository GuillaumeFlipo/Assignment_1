### model testing ###

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import modelFunction

def model_testing() :
    ## test 1 : Concentration decrease without CSO discharge ##
    Test1 = modelFunction(C0=1,CS0_conc=0,coef_V_CSO=0)
    test1_conc = Test1["SimConcentration"]
    
    dist = Test1["Distance"]
    plt.figure()
    plt.plot(dist,test1_conc)
    plt.title("test 1 : Concentration decrease without CSO discharge")
    
    ## test 2 : Important concentration increase when there is a CSO discharge ##
    Test2 = modelFunction(C0=0,CS0_conc=1)
    test2_conc = Test2["SimConcentration"]

    plt.figure()
    plt.plot(dist,test2_conc)
    plt.title("test 2 : Concentration increase when there is a CSO discharge")
    
    ## test 3 : Simulation with real values ##
    Test3 = modelFunction(C0=0,CS0_conc=1.8)
    test3_conc = Test3["SimConcentration"]

    plt.figure()
    plt.plot(dist,test3_conc)
    plt.title("test 3 : Simulation with real values")
    
    plt.show()
    

if __name__ == '__main__':
    model_testing()

