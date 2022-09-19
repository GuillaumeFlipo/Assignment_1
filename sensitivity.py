import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import modelFunction

def sensitivity_analysis(C0, CS0_conc) :
    dParam = np.arange(5,30,5)/100
    result = np.zeros((2,2*len(dParam)))
    
    base_C_C0 = np.max(modelFunction(C0, CS0_conc, EQS)["SimConcentration"])
    base_C_CS0 = np.max(modelFunction(C0, CS0_conc, EQS)["SimConcentration"])
    
    for i in range(len(dParam)) :
        factor = dParam[i]
        
        max_C_C0 = np.max(modelFunction(C0*(1+factor), CS0_conc)["SimConcentration"])
        max_C_CS0 = np.max(modelFunction(C0, CS0_conc*(1+factor))["SimConcentration"])
        
<<<<<<< HEAD
        max_C_C0_minus = np.max(modelFunction(C0*(1-factor), CS0_conc, EQS)["SimConcentration"])
        max_C_CS0_minus = np.max(modelFunction(C0, CS0_conc*(1-factor), EQS)["SimConcentration"])
            
        result[0,len(dParam)+i] = (max_C_C0-base_C_C0)/(C0*(1+factor))
        result[1,len(dParam)+i] = (max_C_CS0-base_C_CS0)/(CS0_conc*(1+factor))
=======
        max_C_C0_minus = np.max(modelFunction(C0*(1-factor), CS0_conc)["SimConcentration"])
        max_C_CS0_minus = np.max(modelFunction(C0, CS0_conc*(1-factor))["SimConcentration"])
>>>>>>> 8e91ba9d0b8d1bdbb4887b587bcde23c541c5760
        
        result[0,len(dParam)-i-1] = (max_C_C0_minus-base_C_C0)/(C0*(1-factor))
        result[1,len(dParam)-i-1] = (max_C_CS0_minus-base_C_CS0)/(CS0_conc*(1-factor))
        
    dParam_rev = dParam.copy()
    dParam_rev = -np.flip(dParam_rev)
    
    percents = np.concatenate([dParam_rev,dParam])
    plt.figure()
    plt.plot(percents,result[0,:],label="C0 senisivity")
    plt.legend()
    plt.plot(percents,result[1,:],label="CS0 senisivity")
    plt.legend()
    plt.show()
    return result # first row is C0, second is CS0
        
if __name__ == '__main__':

    sensitivity_analysis(0.1, 1.8)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        