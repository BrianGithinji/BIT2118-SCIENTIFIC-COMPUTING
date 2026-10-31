"""
Task 2 – Modified real-world case
Rainfall totals recorded every hour by a weather station.
Store them, compute daily total, mean, max and convert mm → inches.
"""
import numpy as np

# Store the station's 24 hourly rainfall measurements in millimetres.
rainfall_mm = np.array([
    0.0, 0.2, 1.5, 3.8, 5.1, 2.4,
    0.9, 0.0, 0.0, 0.3, 1.1, 2.7,
    4.0, 3.2, 1.8, 0.5, 0.0, 0.0,
    0.1, 0.4, 0.8, 1.2, 0.6, 0.0
])

# Summarize the full day and the typical and largest hourly rainfall amounts.
daily_total = np.sum(rainfall_mm)
mean_hourly = np.mean(rainfall_mm)
max_hourly  = np.max(rainfall_mm)

# Convert all millimetre readings to inches at once (25.4 mm equals one inch).
rainfall_in = rainfall_mm / 25.4

# Print daily statistics and the first six converted hourly readings.
print(f"Daily total rainfall : {daily_total:.1f} mm")
print(f"Mean hourly rainfall : {mean_hourly:.2f} mm")
print(f"Maximum hourly rain  : {max_hourly:.1f} mm")
print("First six readings in inches:", np.round(rainfall_in[:6], 3))
