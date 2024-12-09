class PID:
    def __init__(self, kp, ki, kd, setpoint):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.previous_error = 0
        self.integral = 0

    def calculate(self, measured_value):
        error = self.setpoint - measured_value
        
        proportional = self.kp * error
        
        self.integral += error
        integral = self.ki * self.integral
        
        derivative = self.kd * (error - self.previous_error)
        self.previous_error = error
        
        output = proportional + integral + derivative
        return output