import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import modelFunction

def sensitivity_analysis(C0, CS0_conc) :
    EQS = 2
    dParam = np.arange(5,30,5)/100
    result = np.zeros((2,2*len(dParam)))
    for i in range(len(dParam)) :
        factor = dParam[i]
        
        max_C_C0 = np.max(modelFunction(C0*(1+factor), CS0_conc, EQS)["SimConcentration"])
        max_C_CS0 = np.max(modelFunction(C0, CS0_conc*(1+factor), EQS)["SimConcentration"])
        
        max_C_C0_minus = np.max(modelFunction(C0*(1-factor), CS0_conc, EQS)["SimConcentration"])
        max_C_CS0_minus = np.max(modelFunction(C0, CS0_conc*(1-factor), EQS)["SimConcentration"])
        
        result[0,len(dParam)+i] = (max_C_C0-C0)/(C0*(1+factor))
        result[1,len(dParam)+i] = (max_C_CS0-CS0_conc)/(CS0_conc*(1+factor))
        
        result[0,len(dParam)-i-1] = (max_C_C0_minus-C0)/(C0*(1-factor))
        result[1,len(dParam)-i-1] = (max_C_CS0_minus-CS0_conc)/(CS0_conc*(1-factor))
        
    dParam_rev = dParam.copy()
    dParam_rev = -np.flip(dParam_rev)
    
    percents = np.concatenate([dParam_rev,dParam])
    plt.figure()
    plt.plot(percents,result[0,:],label="C0 senisivity")
    plt.legend()
    plt.figure()
    plt.plot(percents,result[1,:],label="CS0 senisivity")
    plt.legend()
    plt.show()
    return result # first row is C0, second is CS0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        