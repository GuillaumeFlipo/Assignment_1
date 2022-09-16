import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import model

def task1_2_a():
    # Importing file for using yearly values of water flow
    fileAar = pd.read_csv('aar.csv', sep=",",decimal=".", encoding='latin-1')
    file = pd.read_csv("CSO_Mollea.csv", sep=",")
    # Translating for easier use
    # Nb_overflow is the number of times an overflow occured
    file.rename(columns={'Vandmængd': 'Water_volume', "Antal over": "Nb_overflow", "Bygværkst": "Building_type"},
                inplace=True)
    # Choosing all data from the input node (from the Lyngby lake) based on the assignment
    nodeInput = fileAar[fileAar["beregningspunktlokalid"] == "Novana_Model_MOELLEAA_DK1_4083.0"]
    meanFlow = nodeInput["vandfoering"].mean()
    print(meanFlow)
    # Data is in m3/s, converting to volume per year
    water_volume_input = meanFlow*3600*24*365.25
    # Taking the sum of all yearly volumes from CSOs
    water_volume_CSO = file.Water_volume.sum()
    print(file)
    print(water_volume_CSO)
    print(water_volume_input)
    
    # Importing file to get N concentration in Lyngby lake (mg/L)
    fileNitrogen = pd.read_csv('Data_WatPoll_2022_to_2014_Ordered.csv', sep=",", decimal=".", encoding='UTF-8')
    print(fileNitrogen)
    # Getting only Lyngby lake data
    lyngbyData = fileNitrogen[fileNitrogen['Site'].str.match('Lyngby sø (mg/L)')]
    # # Getting the average Nitrogen concentration (mg/L) and converting to kg
    # lyngbyNitogenMean = lyngbyData.mean()/1000000
    

def task1_1():
    # Reading data exported from QGIS of the 10 CSOs
    file = pd.read_csv("CSO_Mollea.csv", sep=",")
    # Translating for easier use
    # Nb_overflow is the number of times an overflow occured
    file.rename(columns={'Vandmængd': 'Water_volume', "Antal over": "Nb_overflow", "Bygværkst": "Building_type"},
                inplace=True)
    indexOverflow = file[file["Nb_overflow"] > 0].index
    Nb_CS0_overflow = len(indexOverflow)
    NameCSOMostOverflow = file.iloc[file['Nb_overflow'].idxmax()].Navn
    meanDischarge = file.Water_volume.mean()
    medianDischarge = file.Water_volume.median()
    # Ploting distribution with mean and median
    plt.hist(x=file.Water_volume.values, bins=20, alpha=0.65)
    plt.axvline(meanDischarge, color='b', linestyle=':', linewidth=1)
    plt.text(meanDischarge*1.1, 5*0.9, 'Mean: {:.2f}'.format(meanDischarge))
    plt.axvline(medianDischarge, color='r', linestyle='-', linewidth=1)
    plt.text(medianDischarge*20, 5*0.8, 'Median: {:.1f}'.format(medianDischarge))
    plt.xlabel('Volume of water discharged (m^3)')
    plt.ylabel('CSO structures (Dimensionless)')
    plt.title('Distribution of CSO water volumes')

    # Getting the month, year and ID data about the river nodes from the HIP model
    fileMaaned = pd.read_csv('maaned.csv', sep=",", decimal=".", encoding='latin-1')
    fileAar = pd.read_csv('aar.csv', sep=",", decimal=".", encoding='latin-1')
    fileBereg = pd.read_csv('bereg.csv', sep=",", decimal=".", encoding='latin-1')
    # Filtering for Molle A only
    nodeRiverMoelleaBereg = fileBereg[fileBereg["straekningsnavn"].str.contains("MOELLEAA")].reset_index(drop=True)
    nodeRiverMoelleaMaaned = fileMaaned[fileMaaned["beregningspunktlokalid"].str.contains("MOELLEAA")].reset_index(
        drop=True)
    nodeRiverMoelleaAar = fileAar[fileAar["beregningspunktlokalid"].str.contains("MOELLEAA")].reset_index(drop=True)

    # Average flow since 2010

    AverageFlow = nodeRiverMoelleaAar[nodeRiverMoelleaAar['aar'] > 2010].vandfoering.mean()
    nodeRiverMoelleaMaanedFilter = nodeRiverMoelleaMaaned[nodeRiverMoelleaMaaned['aar'] > 2010].reset_index(drop=True)
    df_maaned_mean = nodeRiverMoelleaMaanedFilter.groupby(["maaned"]).vandfoering.mean()
    
if __name__ == '__main__':

    task1_1()
    task1_2_a()

    #df = modelFunction()
    #task1_2_a()