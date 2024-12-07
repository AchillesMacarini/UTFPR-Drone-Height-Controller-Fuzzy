import numpy as np
import matplotlib.pyplot as plt
import math
from simple_pid import PID

# baseado nos rotores https://uav-en.tmotor.com/html/2019/Manned_Aircraft_0618/272.html
# Parâmetros do sistema
g = 9.81
droneMass = 120
kf = 0.01366
simTime = 5
timeStep = 0.1
steps = int(simTime / timeStep)
t = np.linspace(0, simTime, steps)

# PID Controller
targetHeight = 50
pid = PID(Kp=0.8, Ki=0.2, Kd=0.1, setpoint=targetHeight)
pid.output_limits = (0, 100)  # Limites para o controle do rotor (ajuste conforme necessário)

# Variáveis de simulação
verticalVelocity = np.zeros(steps)
verticalPosition = np.zeros(steps)
verticalAcceleration = np.zeros(steps)
rotorVelocity = np.zeros(steps)
rotorVelocityRPM = np.zeros(steps)

rotorVelocity[0] = 2310 * 2 * np.pi / 60  # Velocidade inicial em rad/s
rotorVelocityRPM[0] = 2310

for i in range(steps - 1):
    # PID controla a variação da velocidade do rotor
    pid_output = pid(verticalPosition[i])
    
    # Dinâmica do sistema
    a = (4 / droneMass) * (kf * rotorVelocity[i] ** 2) - g
    verticalAcceleration[i] = a
    verticalVelocity[i + 1] = verticalVelocity[i] + a * timeStep
    verticalPosition[i + 1] = verticalPosition[i] + verticalVelocity[i] * timeStep
    
    # Atualiza velocidade do rotor
    rotorVelocity[i + 1] = max(rotorVelocity[i] + pid_output, 0)
    rotorVelocityRPM[i + 1] = rotorVelocity[i + 1] * 60 / (2 * np.pi)

# Último valor de aceleração
verticalAcceleration[-1] = verticalAcceleration[-2]

# Plots
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, verticalPosition, label="Posição Vertical ($V_p$)", color="blue")
plt.title('Posição Vertical ($V_p$)')
plt.xlabel('Tempo (s)')
plt.ylabel('Altura (m)')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, rotorVelocityRPM, label="Velocidade dos Rotores ($RV_{RPM}$)", color="red")
plt.title('Velocidade dos Rotores ($RV_{RPM}$)')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (RPM)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()