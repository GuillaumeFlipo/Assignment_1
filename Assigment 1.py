import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def importRiverDataMonth(month, df):
    return df[df['maaned'] == month].reset_index(drop=True)


def modelFunction(C0,CS0_conc,EQS):

    #Initial operations

    CSOdata = pd.read_csv('Hub_dist.csv', sep=",", decimal=".", encoding='latin-1')
    CSOdata.rename(columns={"BygvÃ¦rkst" : "Bygv", "VandmÃ¦ngd" : "water_volume", "Antal over": "Nb_overflow" }, inplace=True)
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

    t_CSO = 4.3*3600


    RiverQ = pd.DataFrame({"flow" :DfbetweenUpandDown["vandfoering"],
                           "node ID" : DfbetweenUpandDown["beregningspunktlokalid"],
                          "X": DfbetweenUpandDown["X"], "Y": DfbetweenUpandDown['Y'],
                           "Distance": np.zeros(RangeIndex),
                           "Qadded": np.zeros(RangeIndex)})
    RiverQ = RiverQ.reset_index()

    RiverC = pd.DataFrame({"SimConcentration" : np.zeros(RangeIndex), "X": RiverQ["X"], "Y": RiverQ['Y'],
                           "Distance": RiverQ["Distance"]})
    RiverC = RiverC.reset_index()

    EQS_exc = RiverC.copy()


    distance_array =[]
    for i in range(RangeIndex):
        stringName = RiverQ['node ID'].iloc[i].split("_")[-1]
        distance_array.append(float(stringName)-3687)
    RiverQ['Distance'] = distance_array
    
    # The simple model advection-dilution model

    RiverC["SimConcentration"][0] = C0
    
    for i in range(1,RangeIndex):
        CSO_vector = CSOdata[CSOdata['HubName'].str.contains(RiverQ['node ID'].iloc[i])]
        
        if (len(CSO_vector) > 0):
            indexCSO = CSO_vector.index.values
            CSO_flux =0
            CSO_Qtot = 0

            for j in range(len(CSO_vector)):
                if float(CSOdata.iloc[indexCSO[j]]["Nb_overflow"])>0:
                    V_CSO = float(CSOdata.iloc[indexCSO[j]]['water_volume']) * (
                                1 / float(CSOdata.iloc[indexCSO[j]]["Nb_overflow"]))
                    Q_CSO = V_CSO / t_CSO
                    CSO_flux += Q_CSO * CS0_conc
                    CSO_Qtot += Q_CSO
                    
            print(len(CSO_vector))
            
            RiverQ["Qadded"][i] = CSO_Qtot + RiverQ["Qadded"][i-1]
            RiverC["SimConcentration"][i] = (RiverC["SimConcentration"][i-1]*(RiverQ["flow"][i-1] + RiverQ["Qadded"][i-1])+CSO_flux)/(RiverQ["flow"][i] + RiverQ["Qadded"][i])

        else:
            RiverQ["Qadded"][i] = RiverQ["Qadded"][i-1]
            RiverC["SimConcentration"][i] = (RiverC["SimConcentration"][i-1]*(RiverQ["flow"][i-1] + RiverQ["Qadded"][i-1]))/(RiverQ["flow"][i] + RiverQ["Qadded"][i])
    
    EQS_exc = RiverC["SimConcentration"]>EQS
    
    plt.plot(RiverQ["Distance"],RiverC["SimConcentration"])
    plt.plot(RiverQ["Distance"],EQS_exc)
    return CSOdata


def sensitivity_analysis(dParam) :
    for dP in dParam:
        pass
    return


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

    df = modelFunction(C0=0.1,CS0_conc=1,EQS=0.3)









