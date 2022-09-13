import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import model

def task1_2_a():

    fileAar = pd.read_csv('aar.csv', sep=",",decimal=".", encoding='latin-1')
    file = pd.read_csv("CSO_Mollea.csv", sep=",")
    file.rename(columns={'Vandmængd': 'Water_volume', "Antal over": "Nb_overflow", "Bygværkst": "Building_type"},
                inplace=True)
    nodeInput = fileAar[fileAar["beregningspunktlokalid"] == "Novana_Model_MOELLEAA_DK1_4083.0"]
    meanFlow = nodeInput["vandfoering"].mean()
    print(meanFlow)
    water_volume_input = meanFlow*3600*24*365.25
    water_volume_CSO = file.Water_volume.sum()
    print(file)
    print(water_volume_CSO)
    print(water_volume_input)
    return file



def task1_1():
    file = pd.read_csv("CSO_Mollea.csv", sep=",")
    file.rename(columns={'Vandmængd': 'Water_volume', "Antal over": "Nb_overflow", "Bygværkst": "Building_type"},
                inplace=True)

    indexOverflow = file[file["Nb_overflow"] > 0].index
    Nb_CS0_overflow = len(indexOverflow)
    NameCSOMostOverflow = file.iloc[file['Nb_overflow'].idxmax()].Navn
    meanDischarge = file.Water_volume.mean()
    medianDischarge = file.Water_volume.median()
    # plt.hist(x=file.Water_volume.values, bins=30)
    # plt.xlabel('Volume of water discharged (m^3)')
    # plt.ylabel('CSO structures (Dimensionless)')
    # plt.title('Distribution of CSO water volumes')

    fileMaaned = pd.read_csv('maaned.csv', sep=",", decimal=".", encoding='latin-1')
    fileAar = pd.read_csv('aar.csv', sep=",", decimal=".", encoding='latin-1')
    fileBereg = pd.read_csv('bereg.csv', sep=",", decimal=".", encoding='latin-1')

    nodeRiverMoelleaBereg = fileBereg[fileBereg["straekningsnavn"].str.contains("MOELLEAA")].reset_index(drop=True)
    nodeRiverMoelleaMaaned = fileMaaned[fileMaaned["beregningspunktlokalid"].str.contains("MOELLEAA")].reset_index(
        drop=True)
    nodeRiverMoelleaAar = fileAar[fileAar["beregningspunktlokalid"].str.contains("MOELLEAA")].reset_index(drop=True)

    # Average flow since 2010

    AverageFlow = nodeRiverMoelleaAar[nodeRiverMoelleaAar['aar'] > 2010].vandfoering.mean()
    nodeRiverMoelleaMaanedFilter = nodeRiverMoelleaMaaned[nodeRiverMoelleaMaaned['aar'] > 2010].reset_index(drop=True)
    df_maaned_mean = nodeRiverMoelleaMaanedFilter.groupby(["maaned"]).vandfoering.mean()
    
if __name__ == '__main__':


    file = task1_2_a()

    #df = modelFunction()
    #task1_2_a()