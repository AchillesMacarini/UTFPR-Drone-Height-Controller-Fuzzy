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
    voltage['diminuir'] = fuzz.trimf(voltage.universe, [0,0, 152])
    voltage['manter'] = fuzz.trapmf(voltage.universe, [50,100,150, 200])
    voltage['aumentar'] = fuzz.trimf(voltage.universe, [143,250, 250])
    
    def __init__(self, setpoint):
        self.setpoint = setpoint
        self.rules = Fuzzy.createRules()

    def createRules():
        rules = [
            ctrl.Rule(Fuzzy.speed['low'] & Fuzzy.error['NEGATIVO'], Fuzzy.voltage['aumentar']),
            ctrl.Rule(Fuzzy.speed['low'] & Fuzzy.error['ZERO'], Fuzzy.voltage['aumentar']),
            ctrl.Rule(Fuzzy.speed['low'] & Fuzzy.error['POSITIVO'], Fuzzy.voltage['manter']),
            ctrl.Rule(Fuzzy.speed['high'] & Fuzzy.error['NEGATIVO'], Fuzzy.voltage['manter']),
            ctrl.Rule(Fuzzy.speed['high'] & Fuzzy.error['ZERO'], Fuzzy.voltage['diminuir']),
            ctrl.Rule(Fuzzy.speed['high'] & Fuzzy.error['POSITIVO'], Fuzzy.voltage['diminuir']),
            ctrl.Rule(Fuzzy.speed['medium'] & Fuzzy.error['NEGATIVO'], Fuzzy.voltage['aumentar']),
            ctrl.Rule(Fuzzy.speed['medium'] & Fuzzy.error['ZERO'], Fuzzy.voltage['manter']),
            ctrl.Rule(Fuzzy.speed['medium'] & Fuzzy.error['POSITIVO'], Fuzzy.voltage['diminuir'])
        ]

        return rules