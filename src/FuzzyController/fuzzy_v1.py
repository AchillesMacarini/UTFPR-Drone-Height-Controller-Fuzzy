import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
class FUZZY:
    def __init__(self, setpoint):
        self.setpoint = setpoint
        self.speed = ctrl.Antecedent(np.arange(0,151,1), "Speed")
        self.error = ctrl.Antecedent(np.arange(-100,101,1), "Error")
        self.voltage = ctrl.Consequent(np.arange(0, 251, 1), 'Voltage')

    def pertinence(self):

        self.speed['low'] = fuzz.trimf(self.speed.universe, [0,0, 30])
        self.speed['medium'] = fuzz.trimf(self.speed.universe, [0,30, 90])
        self.speed['high'] = fuzz.trapmf(self.speed.universe, [30,120, 150,150])
        self.speed.view()

        self.error['NEGATIVO'] =  fuzz.trimf(self.error.universe, [-100,-100, 0])
        self.error['ZERO'] =  fuzz.trimf(self.error.universe, [-50,0,50])
        self.error['POSITIVO'] =  fuzz.trimf(self.error.universe, [0,100, 100])
        self.error.view()

        self.voltage['diminuir'] = fuzz.trimf(self.voltage.universe, [0,0, 125])
        self.voltage['manter'] = fuzz.trapmf(self.voltage.universe, [50,100,150, 200])
        self.voltage['aumentar'] = fuzz.trimf(self.voltage.universe, [125,250, 250])
        self.voltage.view()

    def createRules(self):
        rule1 = ctrl.Rule(self.speed['low'] & self.error['NEGATIVO'], self.voltage['aumentar'])
        rule2 = ctrl.Rule(self.speed['low'] & self.error['ZERO'], self.voltage['aumentar'])
        rule3 = ctrl.Rule(self.speed['low'] & self.error['POSITIVO'], self.voltage['manter'])
        rule4 = ctrl.Rule(self.speed['high'] & self.error['NEGATIVO'], self.voltage['manter'])
        rule5 = ctrl.Rule(self.speed['high'] & self.error['ZERO'], self.voltage['diminuir'])
        rule6 = ctrl.Rule(self.speed['high'] & self.error['POSITIVO'], self.voltage['diminuir'])
        rule7 = ctrl.Rule(self.speed['medium'] & self.error['NEGATIVO'], self.voltage['manter'])
        rule8 = ctrl.Rule(self.speed['medium'] & self.error['ZERO'], self.voltage['manter'])
        rule9 = ctrl.Rule(self.speed['medium'] & self.error['POSITIVO'], self.voltage['manter'])

        self.engine =  ctrl.ControlSystemSimulation(ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9]))

    def compute(self, velocidade):
        err = (self.setpoint - velocidade)/self.setpoint * 100

        self.engine.input['Error'] = err
        self.engine.input['Speed'] = velocidade

        self.engine.compute()

        print(self.engine.output['Voltage'])
        self.voltage.view(sim=self.engine)

test = FUZZY(100)
test.pertinence()
test.createRules()

test.compute(0)
plt.show()