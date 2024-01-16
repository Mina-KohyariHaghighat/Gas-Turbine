import numpy as np
import pandas as pd
from fuelskid import Fuelskid



def txt_exhaust_input (filepath='Fuel/input/input.txt'):

    print('hhhhhhhhhhhhhh')
    file = open(filepath, "r")

    namelist = ['' for i in range(6)]
    for i in range(7):
        namelist[0] = file.readline()

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    projectName = strsplit[1]

    strsplit = namelist[0].split()
    gtType= strsplit[1]
    #
    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    temp=float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    press = float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    rh = float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    fuelType=float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    LHV=float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    volFlowRate=float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    massFlowRate=float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    exhaustTemp=float(strsplit[1])


    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    gtLoad=float(strsplit[1])


    return (projectName,
            gtType,
            temp,
            press,
            rh,
            fuelType,
            LHV,
            volFlowRate,
            massFlowRate,
            exhaustTemp,
            gtLoad)


def txt_fuelskid_input(filepath='Fuel/input/input-fuelskid.txt',
                            filepath1='Fuel/database/Control_Valve.csv',
                            filepath2= 'Fuel/database/Control_Valve.csv',
                            filepath3='Fuel/database/Control_Valve.csv'):

    file = open(filepath, "r")


    namelist = ['' for i in range(6)]
    for i in range(7):
        namelist[0] = file.readline()

    # fuel type
    strsplit = namelist[0].split()
    fueltype= strsplit[1]
    #
    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    fueltemp=float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    fuelgravity=float(strsplit[1])

    valve1 = Fuelskid()
    namelist = ['' for i in range(10)]
    for i in range(3):
        namelist[0] = file.readline()

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve1.Name = strsplit[1]

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve1.upPressure = float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve1.downPressure = float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve1.min_position = float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve1.max_position = float(strsplit[1])


    valve2 = Fuelskid()

    namelist = ['' for i in range(8)]
    for i in range(3):
        namelist[0] = file.readline()

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve2.Name = strsplit[1]

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve2.upPressure = float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve2.downPressure = float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve1.min_position = float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve2.max_position = float(strsplit[1])

    valve3 = Fuelskid()
    namelist = ['' for i in range(8)]
    for i in range(3):
        namelist[0] = file.readline()

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve3.Name = strsplit[1]

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve3.upPressure = float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve3.downPressure = float(strsplit[1])

    # namelist[0] = file.readline()
    # strsplit = namelist[0].split()
    # valve3.position = float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve3.ttxm = float(strsplit[1])


    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve3.cpd = float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve3.min_position= float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve2.max_position = float(strsplit[1])




    valve4 = Fuelskid()
    namelist = ['' for i in range(8)]
    for i in range(3):
        namelist[0] = file.readline()

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve4.Name = strsplit[1]

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve4.upPressure = float(strsplit[1])

    namelist[0] = file.readline()
    strsplit = namelist[0].split()
    valve4.downPressure = float(strsplit[1])


    exceldata1 = pd.read_excel(filepath1, sheet_name=valve1.Name)
    exceldata2 = pd.read_excel(filepath2, sheet_name=valve2.Name)
    exceldata3 = pd.read_excel(filepath3, sheet_name=valve3.Name)
    valve1.valveInfo = exceldata1
    valve2.valveInfo = exceldata2
    valve3.valveInfo = exceldata3

    return (valve1,
            valve2,
            valve3,
            valve3,
            fueltype,
            fueltemp,
            fuelgravity)

