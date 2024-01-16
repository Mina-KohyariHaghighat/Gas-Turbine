import numpy as np
import math


# control valve calculation
class Fuelskid:

    def __init__(self,
                 Name='KT22',
                 upPressure=20,
                 downPressure=18,
                 position=20,
                 valveInfo=np.zeros((10, 3)),
                 cvValve=150,
                 massFlowRate=0.0,
                 volFlowRate=0.0,
                 max_position=75,
                 min_position=25,
                 ttxm=530,
                 cpd=12.0,
                 dpnazle=3):

        self.Name = Name
        self.upPressure = upPressure
        self.downPressure = downPressure
        self.position = position
        self.valveInfo = valveInfo
        self.cvValve = cvValve
        self.massFlowRate = massFlowRate
        self.volFlowRate = volFlowRate
        self.max_position = max_position
        self.min_position = min_position
        self.ttxm = ttxm
        self.cpd = cpd
        self.dpnazle = dpnazle

        pass


    def dpBurner(self):
        pos_coeffs = np.array([-1.567152578471,
                               10.525157214044])
        pos_poly = np.polynomial.Polynomial(pos_coeffs)
        dpnazle = pos_poly(self.massFlowRate)

        return dpnazle


    def ttxmToPosition(self):
        pos_coeffs = np.array([314.349099557152,
                               -0.481791705763])
        pos_poly = np.polynomial.Polynomial(pos_coeffs)
        position = pos_poly(self.ttxm)

        return position

    def cprRatioToPosition(self):
        pos_coeffs = np.array([- 11.552652524905,
                               6.585695167133])
        pos_poly = np.polynomial.Polynomial(pos_coeffs)
        position = pos_poly(self.cpd)

        return position


    # calculate fuel mass flow rate of GCV & SRV
    def FlowCalc(self, fueltype, fueltemp, fuelgravity):
        N1 = 14.42  # constant coefficient-Oil (l/min), (bar)
        N2 = 6950  # constant coefficient-gas (l/min), (bar)

        #  find control valve position
        num_closest = self.valveInfo.iloc[(self.valveInfo['X'] - self.position).abs().argsort()[:1]]
        k = num_closest.index[0]

        if self.valveInfo.iat[k, 0] >= self.position:
            k = k - 1

        # calculate cv valve
        pos_int = np.array([self.valveInfo.iat[k, 0], self.valveInfo.iat[k + 1, 0]])
        cv_int = np.array([self.valveInfo.iat[k, 1], self.valveInfo.iat[k + 1, 1]])
        cvPoly = np.polyfit(pos_int, cv_int, 1)
        cvEqu = np.poly1d(cvPoly)
        cvValue = np.array(self.valveInfo.iat[0, 2]) * cvEqu(self.position) / 100

        # calculate dp valve
        dpValve = self.upPressure - self.downPressure

        if fueltype == 'Gas':
            volFlowRate = N2 * cvValue * self.upPressure * (
                    1 - (2 * dpValve / (3 * self.upPressure))) * math.sqrt(
                dpValve / (self.upPressure * fuelgravity * fueltemp))

            densityFuel=fuelgravity*1.2930

            # print(densityFuel)
            massFlowRate = 0.001 / 60 * volFlowRate * densityFuel
        if fueltype == 'Oil':
            volFlowRate = N1 * cvValue * math.sqrt(dpValve / fuelgravity)
            density = 845 * fuelgravity
            massFlowRate = 0.001 / 60 * volFlowRate * density

        return massFlowRate,\
               volFlowRate

    # calculate  SRV valve position
    def positionCalc(self, fueltype, fueltemp, fuelgravity):
        N1 = 14.42                          # constant coefficient-Oil (l/min), (bar)
        N2 = 6950                           # constant coefficient-gas (l/min), (bar)

        masscalc, volmass = self.volFlowRate
        # calculate dp valve
        dpValve = self.upPressure - self.downPressure

        # calculate cv valve
        if fueltype == 'Gas':
            cvSrv = (volmass) / (N2 * self.upPressure *
                (1 - (2 * dpValve / (3 * self.upPressure))) * math.sqrt(
                dpValve / (self.upPressure * fuelgravity * fueltemp)))
            cvfinal = cvSrv / np.array(self.valveInfo.iat[0, 2]) * 100

        if fueltype == 'Oil':
            cvSrv = (volmass) / (N1 * math.sqrt(dpValve / fuelgravity))
            cvfinal = cvSrv / np.array(self.valveInfo.iat[0, 2]) * 100

        num_closest = self.valveInfo.iloc[(self.valveInfo['CV'] - cvfinal).abs().argsort()[:2]]
        k = num_closest.index[0]

        if self.valveInfo.iat[k, 1] >= cvSrv:
            k = k - 1

        cv_int = np.array([self.valveInfo.iat[k, 1], self.valveInfo.iat[k + 1, 1]])
        pos_int = np.array([self.valveInfo.iat[k, 0], self.valveInfo.iat[k + 1, 0]])
        posPoly = np.polyfit(cv_int, pos_int, 1)
        posEqu = np.poly1d(posPoly)
        posValue = posEqu(cvfinal)

        # e = Fuel.density (fueltemp + 273.2,self.upPressure, fuelgravity)

        return posValue


