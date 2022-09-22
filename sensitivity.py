import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import modelFunction


def list_multiply(a,b) :
    c = []
    for i in range(len(a)) :
        c.append(a[i]*b[i])
    return c

def sensitivity_analysis(param) :
    dP = 0.1
    
    C0,CS0_conc,t_CSO,theta,coef_V_CSO,coef_Qi = param
    
    base_C = np.max(modelFunction(C0,CS0_conc,t_CSO,theta)["SimConcentration"])
    
    results = []
    
    for i in range(len(param)) :
        factors = [1]*len(param)
        factors[i] += dP
        
        new_param = list_multiply(param,factors)
        C0,CS0_conc,t_CSO,theta,coef_V_CSO,coef_Qi = new_param
        print(C0,CS0_conc,t_CSO,theta,coef_V_CSO,coef_Qi)
        
        new_C = np.max(modelFunction(C0,CS0_conc,t_CSO,theta,coef_V_CSO,coef_Qi)["SimConcentration"])
        
        sensitivity = (new_C - base_C)/(base_C*dP)
        results.append(sensitivity)
        
        
    return results
        
if __name__ == '__main__':

    result = sensitivity_analysis([0.1, 1.8,4.3,2.31,1,1])
    print(result)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
