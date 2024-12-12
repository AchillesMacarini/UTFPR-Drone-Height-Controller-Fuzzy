import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

class Fuzzy:
    speed = ctrl.Antecedent(np.arange(0,151,1), "Speed")
    error = ctrl.Antecedent(np.arange(-100,101,1), "Error")
    voltage = ctrl.Consequent(np.arange(0, 251, 1), 'Voltage')
    
    speed['low'] = fuzz.trimf(speed.universe, [0,0, 30])
    speed['medium'] = fuzz.trimf(speed.universe, [0,30, 90])
    speed['high'] = fuzz.trapmf(speed.universe, [30,120, 150,150])
    error['NEGATIVO'] =  fuzz.trimf(error.universe, [-100,-100, 0])
    error['ZERO'] =  fuzz.trimf(error.universe, [-50,0,50])
    error['POSITIVO'] =  fuzz.trimf(error.universe, [0,100, 100])
    voltage['diminuir'] = fuzz.trimf(voltage.universe, [0,0, 125])
    voltage['manter'] = fuzz.trapmf(voltage.universe, [50,100,150, 200])
    voltage['aumentar'] = fuzz.trimf(voltage.universe, [125,250, 250])
    
    def __init__(self, setpoint):
        self.setpoint = setpoint
        self.rules = Fuzzy.createRules()

    def createRules():
        rule1 = ctrl.Rule(Fuzzy.speed['low'] & Fuzzy.error['NEGATIVO'], Fuzzy.voltage['aumentar'])
        rule2 = ctrl.Rule(Fuzzy.speed['low'] & Fuzzy.error['ZERO'], Fuzzy.voltage['aumentar'])
        rule3 = ctrl.Rule(Fuzzy.speed['low'] & Fuzzy.error['POSITIVO'], Fuzzy.voltage['manter'])
        rule4 = ctrl.Rule(Fuzzy.speed['high'] & Fuzzy.error['NEGATIVO'], Fuzzy.voltage['manter'])
        rule5 = ctrl.Rule(Fuzzy.speed['high'] & Fuzzy.error['ZERO'], Fuzzy.voltage['diminuir'])
        rule6 = ctrl.Rule(Fuzzy.speed['high'] & Fuzzy.error['POSITIVO'], Fuzzy.voltage['diminuir'])
        rule7 = ctrl.Rule(Fuzzy.speed['medium'] & Fuzzy.error['NEGATIVO'], Fuzzy.voltage['manter'])
        rule8 = ctrl.Rule(Fuzzy.speed['medium'] & Fuzzy.error['ZERO'], Fuzzy.voltage['manter'])
        rule9 = ctrl.Rule(Fuzzy.speed['medium'] & Fuzzy.error['POSITIVO'], Fuzzy.voltage['manter'])

        return [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9]