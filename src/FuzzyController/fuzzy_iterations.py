import matplotlib.pyplot as plt
import FuzzyController.Models.Fuzzy_Controller as fuzzy_controller
import Motor.Models.Motor as Motor

motor = Motor.Motor()
iterations = []
measured_speeds = []
control_signals = []

for i in range(200):
    measured_speed = motor.speed
    control_signal = fuzzy_controller.fuzzy_controller.FuzzyControl(measured_speed)
    motor.apply_voltage(control_signal)
    
    iterations.append(i + 1)
    measured_speeds.append(measured_speed)
    control_signals.append(control_signal)