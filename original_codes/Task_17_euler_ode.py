import numpy as np
import matplotlib.pyplot as plt

# Newton's law of cooling:
# dT/dt = -k(T - T_ambient)
T_ambient = 25.0
T_initial = 90.0
k = 0.12
h = 1.0  # minutes
end_time = 30.0

def cooling_rate(T):
    # Return the temperature's rate of change according to Newton's cooling law.
    return -k * (T - T_ambient)

# Create minute-by-minute sample times and initialize the temperature array.
time = np.arange(0, end_time + h, h)
temperature = np.zeros_like(time)
temperature[0] = T_initial

# Apply one explicit Euler update per time step using the current temperature.
for i in range(len(time) - 1):
    temperature[i + 1] = (
        temperature[i] + h * cooling_rate(temperature[i])
    )

# Compute the analytical cooling curve to check the numerical Euler approximation.
exact = T_ambient + (T_initial - T_ambient) * np.exp(-k * time)

print(f"Euler temperature after 30 min: {temperature[-1]:.2f} C")
print(f"Exact temperature after 30 min: {exact[-1]:.2f} C")
print(f"Final absolute error: {abs(temperature[-1]-exact[-1]):.4f} C")

# Plot the numerical and exact temperature curves for comparison.
plt.plot(time, temperature, marker="o", label="Euler")
plt.plot(time, exact, label="Exact solution")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (C)")
plt.title("Cooling of a hot object")
plt.legend()
plt.grid(True)
plt.savefig("Task_17_cooling.png")
plt.show()
