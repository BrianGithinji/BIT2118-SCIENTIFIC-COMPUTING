"""
Task 18 – Modified real-world case
Simple SIR epidemic model solved with solve_ivp.
dS/dt = -β S I
dI/dt =  β S I - γ I
dR/dt =  γ I
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

beta, gamma = 0.3, 0.1
N_pop = 1000
y0 = [990, 10, 0]          # S, I, R

def sir(t, y):
    # Calculate the susceptible, infected, and recovered population rates of change.
    S, I, R = y
    dS = -beta * S * I / N_pop
    dI =  beta * S * I / N_pop - gamma * I
    dR =  gamma * I
    return [dS, dI, dR]

# Numerically integrate the SIR equations over 60 days and return 300 sample points.
sol = solve_ivp(sir, [0, 60], y0, t_eval=np.linspace(0, 60, 300),
                rtol=1e-8, atol=1e-10)

# Report each population group at the final simulated day.
print("Final susceptible :", int(sol.y[0, -1]))
print("Final infected    :", int(sol.y[1, -1]))
print("Final recovered   :", int(sol.y[2, -1]))

# Plot how each compartment changes throughout the simulated outbreak.
plt.plot(sol.t, sol.y[0], label="Susceptible")
plt.plot(sol.t, sol.y[1], label="Infected")
plt.plot(sol.t, sol.y[2], label="Recovered")
plt.xlabel("Days")
plt.ylabel("Population")
plt.title("SIR epidemic model")
plt.legend()
plt.grid(True)
plt.savefig("Task_18_modified_sir.png")
plt.show()
