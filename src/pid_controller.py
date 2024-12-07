import numpy as np
import matplotlib.pyplot as plt
import math
# baseado nos rotores https://uav-en.tmotor.com/html/2019/Manned_Aircraft_0618/272.html
g = 9.81
droneMass = 120
kf = 0.01366
rotorVelocity = 100
simTime = 5
timeStep = 0.1
steps = int(simTime/timeStep)
t = np.linspace(0, simTime, steps)

def simulate_takeOff(mass, kf,rotorInitialVelocityRPM,targetHeight,steps,pid = False, kp=0,ki=0,kd =0):
    verticalVelocity = np.zeros(steps)
    verticalPosition = np.zeros(steps)
    verticalAcceleration = np.zeros(steps)
    rotorVelocity = np.zeros(steps)
    rotorVelocity[0] = rotorInitialVelocityRPM*2*math.pi/60
    rotorVelocityRPM = np.zeros(steps)
    rotorVelocityRPM[0] = rotorInitialVelocityRPM
    pid_output = 0
    if pid:
        integralError = 0
        previousError = 0
    
    for i in range(steps - 1):
        
        if pid:
            error = targetHeight - verticalPosition[i]
            integralError += error*timeStep
            derivativeError = (error - previousError)/timeStep
            pid_output = kp* error + ki * integralError + kd * derivativeError
            previousError = error
        
        
        a = (4 / mass) * (kf * rotorVelocity[i] ** 2) - g
        verticalAcceleration[i] = a
        verticalVelocity[i + 1] = verticalVelocity[i] + a * timeStep
        verticalPosition[i + 1] = verticalPosition[i] + verticalVelocity[i] * timeStep
        rotorVelocity[i + 1] = rotorVelocity[i] + pid_output
        print(rotorVelocity[i + 1])
        rotorVelocityRPM[i + 1] = rotorVelocity[i + 1] * 60 / (2 * math.pi)

    return verticalPosition, verticalAcceleration, rotorVelocity, rotorVelocityRPM


vp, va, rv, rvRPM = simulate_takeOff(mass = droneMass, kf = kf, rotorInitialVelocityRPM=2310,steps=steps,targetHeight=0)

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, vp, label="Posição Vertical ($V_p$)", color="blue")
plt.title(f'Posição Vertical ($V_p$)')
plt.xlabel('Tempo (s)')
plt.ylabel('Altura (m)')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, rvRPM, label="Velocidade rotores ($RV_RPM$)", color="red")
plt.title(f'Velocidade rotores ($RV_RPM$)')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (RPM)')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

vp, va, rv, rvRPM = simulate_takeOff(mass = droneMass, kf = kf, rotorInitialVelocityRPM=2310,steps=steps,targetHeight=50,pid=True,kp = 0.8, ki = 0.2, kd = 0.1)

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, vp, label="Posição Vertical ($V_p$)", color="blue")
plt.title(f'Posição Vertical ($V_p$)')
plt.xlabel('Tempo (s)')
plt.ylabel('Altura (m)')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, rvRPM, label="Velocidade rotores ($RV_RPM$)", color="red")
plt.title(f'Velocidade rotores ($RV_RPM$)')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (RPM)')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()