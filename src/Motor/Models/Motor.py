class Motor:
    def __init__(self):
        self.speed = 0

    def apply_voltage(self, voltage):
        self.speed += voltage * 0.1
        self.speed *= 0.95