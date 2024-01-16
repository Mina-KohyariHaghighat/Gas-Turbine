
import input_output
new_valve1, new_valve2, new_valve3, new_valve4, fueltype, fueltemp, fuelgravity = input_output.txt_fuelskid_input(filepath= 'Fuel/input/input-fuelskid.txt',
                                                                                                           filepath1= 'Fuel/database/Control_Valve.csv',
                                                                                                           filepath3= 'Fuel/database/Control_Valve.csv')



new_valve3.position = new_valve3.cprRatioToPosition()
new_valve3.volFlowRate = new_valve3.FlowCalc(fueltype, fueltemp, fuelgravity)

new_valve2.volFlowRate = new_valve3.FlowCalc(fueltype, fueltemp, fuelgravity)
new_valve2.position = new_valve2.positionCalc(fueltype, fueltemp, fuelgravity)

new_valve1.volFlowRate = new_valve3.FlowCalc(fueltype, fueltemp, fuelgravity)
new_valve1.position = new_valve1.positionCalc(fueltype, fueltemp, fuelgravity)

new_valve4.massFlowRate,_ = new_valve3.FlowCalc(fueltype, fueltemp, fuelgravity)
print(new_valve4.massFlowRate)



pos1 = new_valve1.positionCalc(fueltype, fueltemp, fuelgravity)
pos2 = new_valve2.positionCalc(fueltype, fueltemp, fuelgravity)
pos3 = new_valve3.positionCalc(fueltype, fueltemp, fuelgravity)

massFlow, volFlow = new_valve3.FlowCalc(fueltype, fueltemp, fuelgravity)

print('fuel skid information')
print('---------------------------------------------')
print(f'Position regulator valve (%): {pos1: >14.2f}')
print(f'Position SRV valve (%): {pos2: >20.2f}')
print(f'Position GCV valve (%): {pos3: >20.2f}')
print(f'fuel vol. flow rate (L/min): {volFlow : >16.0f}')
print(f'fuel mass flow rate (kg/s): {massFlow : >16.3f}')
print('---------------------------------------------')





# from SingleShaft.fuel import Fuel
# # density=Fuel.density(fueltemp+273.2, 30.0, fuelgravity)

