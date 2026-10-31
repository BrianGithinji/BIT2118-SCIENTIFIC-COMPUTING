"""
Task 14 – Modified real-world case
Fit a logistic growth model to a small population time series.
"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

years = np.array([0, 5, 10, 15, 20, 25, 30], dtype=float)
pop   = np.array([100, 180, 320, 520, 780, 980, 1100], dtype=float)

# Define population as a logistic curve with carrying capacity, growth rate, and midpoint.
def logistic(t, K, r, t0):
    return K / (1 + np.exp(-r*(t - t0)))

# Fit the curve to the observations, using the supplied values as initial parameter guesses.
popt, _ = curve_fit(logistic, years, pop, p0=[1200, 0.15, 15])
K, r, t0 = popt
print(f"Carrying capacity K = {K:.0f}")
print(f"Growth rate r       = {r:.3f}")
print(f"Mid-point t0        = {t0:.1f} years")

# Generate a smooth fitted curve and compare it visually with the population data.
t_plot = np.linspace(0, 40, 200)
plt.scatter(years, pop, label="Data")
plt.plot(t_plot, logistic(t_plot, *popt), label="Logistic fit")
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Logistic population growth fit")
plt.legend()
plt.grid(True)
plt.savefig("Task_14_modified_logistic.png")
plt.show()
