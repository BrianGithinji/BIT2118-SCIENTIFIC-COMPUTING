import numpy as np
import matplotlib.pyplot as plt

# GPS samples: time in seconds and position in metres
time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
position = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])

# Allocate one speed estimate per GPS position reading.
speed = np.zeros_like(position)

# Use a forward difference because there is no earlier sample at the first time.
speed[0] = (position[1] - position[0]) / (time[1] - time[0])

# Use central differences for interior samples to estimate their local speeds.
for i in range(1, len(time) - 1):
    speed[i] = (
        position[i + 1] - position[i - 1]
    ) / (
        time[i + 1] - time[i - 1]
    )

# Use a backward difference because there is no later sample at the final time.
speed[-1] = (
    position[-1] - position[-2]
) / (
    time[-1] - time[-2]
)

# Print each measured position alongside its numerically estimated speed.
for t, x, v in zip(time, position, speed):
    print(f"t={t:.0f}s, position={x:.1f}m, estimated speed={v:.2f}m/s")

# Plot the estimated speed over time.
plt.plot(time, speed, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Estimated speed (m/s)")
plt.title("Speed estimated from GPS position data")
plt.grid(True)
plt.savefig("Task_15_speed.png")
plt.show()
