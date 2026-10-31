# Import NumPy and give it the conventional short name "np".
import numpy as np

# Store one day's 24 hourly temperature readings, in degrees Celsius, as a NumPy array.
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

# Calculate the average of all 24 Celsius readings.
mean_temp = np.mean(temperatures_c)
# Find the lowest Celsius reading in the array.
min_temp = np.min(temperatures_c)
# Find the highest Celsius reading in the array.
max_temp = np.max(temperatures_c)

# Convert every Celsius value to Fahrenheit using F = (C * 1.8) + 32.
# NumPy applies this formula to all array elements at once.
temperatures_f = 1.8 * temperatures_c + 32

# Print the daily average in Celsius, rounded to two decimal places.
print(f"Daily mean temperature: {mean_temp:.2f} C")
# Print the day's lowest temperature in Celsius.
print(f"Minimum temperature: {min_temp:.2f} C")
# Print the day's highest temperature in Celsius.
print(f"Maximum temperature: {max_temp:.2f} C")
# Print the first six converted readings (the first six hours) in Fahrenheit.
print("First six Fahrenheit readings:", temperatures_f[:6])
