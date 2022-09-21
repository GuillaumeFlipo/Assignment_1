# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:47:43 2022

@author: jerem
"""

# clean the workspace
from IPython import get_ipython
get_ipython().magic('reset -sf')
# close all figures
import matplotlib.pyplot as plt
plt.close('all')

import pandas as pd
import numpy as np

#


#get inflow data
flowData=pd.read_csv('riverNodes.csv',sep=",",decimal=".",encoding='latin-1')

CSOData=pd.read_csv('Export_RBU_data_from_PULS.csv',sep=",",decimal=".",encoding='latin-1')

#Extracting discharge data for all years
flowinput = flowData[flowData["beregningspunktlokalid"] == "Novana_Model_MOELLEAA_DK1_4083.0"]
    
flowDataMean = flowinput['vandfoering'].mean()
print(flowDataMean)

#So the mean flow is 0.56
# The total volume entering the lake:
water_volume_input = flowDataMean*3600*24*365.25
print(water_volume_input)

#
water_volume_CSO = CSOData.Vandmaengde.sum()
print(water_volume_CSO,'m3')
print(water_volume_CSO/water_volume_input*100,"%")
print("The CSO discharge only counts for 1.41% of the total volume entering the lake")

#Nitrogen
path = r'C:\Users\jerem\Dropbox\12104 Environmental Modelling\Week 2\Assignment 1\Data WatPoll 2002 to 2014.xlsx'
dfN = pd.read_excel(path, skiprows=5)
Lyngby_N = pd.DataFrame(dfN, columns = ['Year','Lyngby sø'])
#Lyngby_N = pd.DataFrame({'Year':dfN['Year'], 'Lyngby sø':dfN['Lyngby sø']  })
#print(Lyngby_N['Lyngby sø'])
N_mean = Lyngby_N['Lyngby sø'].mean()
print(N_mean,'(mg N)/l')
N_lake = N_mean*water_volume_CSO*1000 #mg N
print(N_lake/1000000,'kg N')

CSOMoelleAA = pd.read_csv('CSO_Mollea.csv',sep=",",decimal=".",encoding='latin-1')
print("As observed in the CSO-data, the total nitrogen in the discharge is 260 kg N, while in the lake it's 26.75 kg N, so the discharge is approximately 10 times higher.")

#Extracting discharge data from 2019
flowData2019=flowData.iloc[7028:7278]
flowData2019total=sum(flowData2019['vandfoering'])
#print(flowData2019total)