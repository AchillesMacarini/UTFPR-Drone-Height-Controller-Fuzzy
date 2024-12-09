import PIDController.Models.PID as pidModel
import PIDController.Models.Motor as Motor

kp = 1.5
ki = 0.5
kd = 0.2
setpoint = 100

pid = pidModel.PID(kp, ki, kd, setpoint)
motor = Motor.Motor()
motor_no_pid = Motor.Motor()

pid.previous_error = 0
pid.integral = 0

iterations = []
measured_speeds = []
control_signals = []

no_pid_speeds = []

for i in range(200):
    measured_speed = motor.speed
    
    control_signal = pid.calculate(measured_speed)
    
    motor.apply_voltage(control_signal)
    
    iterations.append(i + 1)
    measured_speeds.append(measured_speed)
    control_signals.append(control_signal)

    motor_no_pid.apply_voltage(56.93)
    no_pid_speeds.append(motor_no_pid.speed)