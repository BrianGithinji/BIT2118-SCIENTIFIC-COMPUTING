"""
Task 16 – Modified real-world case
Estimate distance travelled from irregular speedometer readings
using the trapezoidal rule.
"""
import numpy as np
from scipy.integrate import trapezoid

time_min = np.array([0, 5, 12, 20, 28, 35, 45], dtype=float)   # minutes
speed_kmh = np.array([0, 40, 60, 55, 70, 50, 0], dtype=float)

# Convert elapsed minutes to hours so integrating km/h yields distance in kilometres.
time_h = time_min / 60.0
# Integrate speed over the irregularly spaced time samples using trapezoids.
distance = trapezoid(speed_kmh, time_h)

# Display the estimated total distance for the measured trip.
print(f"Estimated distance travelled: {distance:.2f} km")
