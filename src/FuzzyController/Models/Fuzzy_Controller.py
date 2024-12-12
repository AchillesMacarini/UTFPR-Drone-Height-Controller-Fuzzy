import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

import FuzzyController.Models.Fuzzy as Fuzzy
import Motor.Models.Motor as Motor

class fuzzy_controller:
    def FuzzyControl(speed):
        fuzzy = Fuzzy.Fuzzy(100)

        # fuzzy.speed.view()
        # fuzzy.error.view()
        # fuzzy.voltage.view()

        err = ((speed - fuzzy.setpoint)/fuzzy.setpoint) * 100

        ruleList = fuzzy.rules
        motorCtrl = ctrl.ControlSystem(ruleList)
        engine = ctrl.ControlSystemSimulation(motorCtrl)

        engine.input['Error'] = err
        engine.input['Speed'] = speed

        engine.compute()
        # fuzzy.voltage.view(sim=engine)

        return engine.output['Voltage']
        # plt.show()