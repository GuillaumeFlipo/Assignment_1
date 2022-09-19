import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import modelFunction

def sensitivity_analysis(C0, CS0_conc) :
    dParam = np.arange(5,30,5)/100
    result = np.zeros((2,2*len(dParam)))
    
    base_C = np.max(modelFunction(C0, CS0_conc)["SimConcentration"])
    
    for i in range(len(dParam)) :
        factor = dParam[i]
        
        max_C_C0 = np.max(modelFunction(C0*(1+factor), CS0_conc)["SimConcentration"])
        max_C_CS0 = np.max(modelFunction(C0, CS0_conc*(1+factor))["SimConcentration"])
        

        max_C_C0_minus = np.max(modelFunction(C0*(1-factor), CS0_conc)["SimConcentration"])
        max_C_CS0_minus = np.max(modelFunction(C0, CS0_conc*(1-factor))["SimConcentration"])
            
        result[0,len(dParam)+i] = (max_C_C0-base_C)/(C0*factor)
        result[1,len(dParam)+i] = (max_C_CS0-base_C)/(CS0_conc*factor)
        
        result[0,len(dParam)-i-1] = (max_C_C0_minus-base_C)/(C0*(-factor))
        result[1,len(dParam)-i-1] = (max_C_CS0_minus-base_C)/(CS0_conc*(-factor))
        
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
    print(result)
    return result # first row is C0, second is CS0
        
if __name__ == '__main__':

    sensitivity_analysis(0.1, 1.8)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        