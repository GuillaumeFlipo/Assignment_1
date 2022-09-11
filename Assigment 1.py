import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def importRiverDataMonth(month, df):
    return df[df['maaned'] == month].reset_index(drop=True)


def modelFunction():

    #Initial operations

    CSOdata = pd.read_csv('bereg.csv', sep=",", decimal=".", encoding='latin-1')
    RiverData = pd.read_csv('maaned.csv', sep=",",decimal=".", encoding='latin-1')

    #Data preperation

    RiverData = RiverData[RiverData['beregningspunktlokalid'].str.contains("MOELLEAA")].reset_index(drop=True)
    RiverDataYY = RiverData[RiverData['aar'] == 2019].reset_index(drop=True)
    RiverDataMM = importRiverDataMonth("januar", RiverDataYY)
    indexUp = RiverDataMM['beregningspunktlokalid'] == "Novana_Model_MOELLEAA_DK1_3687.0"
    indexDown = RiverDataMM['beregningspunktlokalid'] == "Novana_Model_MOELLEAA_DK1_13500.0"
    dfIndexUp = RiverDataMM[indexUp]
    dfIndexDown = RiverDataMM[indexDown]
    indexUpNb = dfIndexUp.index.values[0]
    indexDownNb = dfIndexDown.index.values[0]
    RangeIndex = np.abs(indexDownNb-indexUpNb)+1
    DfbetweenUpandDown = RiverDataMM.drop(RiverDataMM.index[0:indexUpNb]).drop(RiverDataMM.index[indexDownNb:-1])




    # Initialize variable needed by the model


    RiverQ = pd.DataFrame({"flow" :DfbetweenUpandDown["vandfoering"],
                           "node ID" : DfbetweenUpandDown["beregningspunktlokalid"],
                          "X": DfbetweenUpandDown["X"], "Y": DfbetweenUpandDown['Y'],
                           "Distance": np.empty(RangeIndex),
                           "CSOFlow": np.empty(RangeIndex)})

    RiverC = pd.DataFrame({"SimConcentration" : np.zeros(RangeIndex), "X": RiverQ["X"], "Y": RiverQ['Y'],
                           "Distance": RiverQ["Distance"]})

    EQS_exc = RiverC.copy()
    print(RiverQ['node ID'].iloc[0].split("_")[-1])

    distance_array =[]
    for i in range(RangeIndex):
        stringName = RiverQ['node ID'].iloc[i].split("_")[-1]
        distance_array.append(float(stringName)-3687)
    RiverQ['Distance'] = distance_array

    # The simple model advection-dilution model

    

    return RiverQ




def task1_2_a():

    fileAar = pd.read_csv('aar.csv', sep=",",decimal=".", encoding='latin-1')
    nodeInput = fileAar[fileAar["beregningspunktlokalid"] == "Novana_Model_MOELLEAA_DK1_4083.0"]
    print(nodeInput)
    meanFlow = nodeInput["vandfoering"].mean()
    print(meanFlow)








if __name__ == '__main__':

    #task1_2_a()

    df = modelFunction()

    # file = pd.read_csv("CSO_Mollea.csv", sep=",")
    # file.rename(columns={'Vandmængd': 'Water_volume', "Antal over": "Nb_overflow", "Bygværkst": "Building_type"}, inplace=True)
    #
    # indexOverflow = file[file["Nb_overflow"] > 0].index
    # Nb_CS0_overflow = len(indexOverflow)
    # NameCSOMostOverflow = file.iloc[file['Nb_overflow'].idxmax()].Navn
    # meanDischarge = file.Water_volume.mean()
    # medianDischarge = file.Water_volume.median()
    # # plt.hist(x=file.Water_volume.values, bins=30)
    # # plt.xlabel('Volume of water discharged (m^3)')
    # # plt.ylabel('CSO structures (Dimensionless)')
    # # plt.title('Distribution of CSO water volumes')
    #
    # fileMaaned = pd.read_csv('maaned.csv', sep=",",decimal=".", encoding='latin-1')
    # fileAar = pd.read_csv('aar.csv', sep=",",decimal=".", encoding='latin-1')
    # fileBereg = pd.read_csv('bereg.csv', sep=",",decimal=".", encoding='latin-1')
    #
    #
    # nodeRiverMoelleaBereg = fileBereg[fileBereg["straekningsnavn"].str.contains("MOELLEAA")].reset_index(drop=True)
    # nodeRiverMoelleaMaaned = fileMaaned[fileMaaned["beregningspunktlokalid"].str.contains("MOELLEAA")].reset_index(drop=True)
    # nodeRiverMoelleaAar = fileAar[fileAar["beregningspunktlokalid"].str.contains("MOELLEAA")].reset_index(drop=True)
    #
    #
    # # Average flow since 2010
    #
    # AverageFlow = nodeRiverMoelleaAar[nodeRiverMoelleaAar['aar'] > 2010].vandfoering.mean()
    # nodeRiverMoelleaMaanedFilter = nodeRiverMoelleaMaaned[nodeRiverMoelleaMaaned['aar'] > 2010].reset_index(drop=True)
    # df_maaned_mean = nodeRiverMoelleaMaanedFilter.groupby(["maaned"]).vandfoering.mean()
    #
    # CSOdata = pd.read_csv('bereg.csv', sep=",", decimal=".", encoding='latin-1')
    # RiverData = fileMaaned.copy()
    # RiverData = RiverData[RiverData['beregningspunktlokalid'].str.contains("MOELLEAA")].reset_index(drop=True)
    # RiverDataYY = RiverData[RiverData['aar'] == 2019 ].reset_index(drop=True)
    # RiverDataMM = importRiverDataMonth("januar", RiverDataYY)
    # indexUp = RiverDataMM['beregningspunktlokalid'  == "Novana_Model_MOELLEAA_DK1_3687.0"]
    # indexDown = RiverDataMM['beregningspunktlokalid'  == "Novana_Model_MOELLEAA_DK1_13500.0"]






