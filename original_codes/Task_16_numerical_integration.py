import numpy as np
from scipy.integrate import simpson

# Store power readings and their measurement times; integrating power over time gives energy.
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])

# Estimate total energy from the sampled power curve using two numerical quadrature rules.
energy_trapezoid = np.trapezoid(power_kw, time_hours)
energy_simpson = simpson(power_kw, x=time_hours)

# Display both energy estimates and their absolute difference.
print(f"Energy using trapezoidal rule: {energy_trapezoid:.3f} kWh")
print(f"Energy using Simpson's rule:   {energy_simpson:.3f} kWh")
print(f"Difference between estimates:  {abs(energy_simpson-energy_trapezoid):.3f} kWh")
