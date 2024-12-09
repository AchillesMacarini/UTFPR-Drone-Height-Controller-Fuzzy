import matplotlib.pyplot as plt
import PIDController.pid_controller as pid

plt.figure(figsize=(10, 10))

plt.subplot(1, 1, 1)
plt.plot(pid.iterations, pid.no_pid_speeds, label="Without PID", color="orange")
plt.axhline(pid.setpoint, color="red", linestyle="--", label="Setpoint")
plt.title("Motor Speed without PID Control")
plt.xlabel("Time (s)")
plt.ylabel("Speed (RPM)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 10))

plt.subplot(2, 1, 1)
plt.plot(pid.iterations, pid.measured_speeds, label="Measured Speed")
plt.axhline(y=pid.setpoint, color='r', linestyle='--', label="Setpoint")
plt.title("PID Control: Motor Speed Over Time")
plt.xlabel("Iteration")
plt.ylabel("Speed (RPM)")
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(pid.iterations, pid.control_signals, label="Control Signal (Voltage)", color="orange")
plt.title("PID Control: Voltage Applied Over Time")
plt.xlabel("Iteration")
plt.ylabel("Voltage")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()