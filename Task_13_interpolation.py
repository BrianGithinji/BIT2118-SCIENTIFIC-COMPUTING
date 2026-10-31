import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Store measured temperatures at hourly sample times.
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])

# Create linear and cubic-spline interpolators from the measured points.
linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

# Generate sample times at ten-minute intervals over the measurement period.
ten_minute_times = np.arange(8, 14 + 1/6, 1/6)

# Evaluate both interpolation methods at all generated times.
linear_estimates = linear(ten_minute_times)
cubic_estimates = cubic(ten_minute_times)

# Compare the two methods at 10:30, midway between hourly measurements.
target_time = 10.5  # 10:30
print(f"Linear estimate at 10:30: {float(linear(target_time)):.2f} C")
print(f"Cubic estimate at 10:30:  {float(cubic(target_time)):.2f} C")

# Plot the measurements and both interpolated curves for visual comparison.
plt.scatter(hours, temperature, label="Hourly measurements")
plt.plot(ten_minute_times, linear_estimates, label="Linear")
plt.plot(ten_minute_times, cubic_estimates, label="Cubic spline")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (C)")
plt.title("Temperature interpolation")
plt.legend()
plt.grid(True)
plt.savefig("Task_13_interpolation.png")
plt.show()
