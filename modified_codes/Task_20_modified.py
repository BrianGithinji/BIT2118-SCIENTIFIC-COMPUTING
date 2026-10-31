"""
Task 20 – Modified real-world case
Monte-Carlo estimate of the probability that a project finishes late.
Activity durations ~ Normal; critical-path sum compared with deadline.
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
N = 50_000
deadline = 45.0          # days

# Define mean durations and standard deviations for the three critical-path activities.
means = np.array([12.0, 18.0, 10.0])
stds  = np.array([2.0,  3.0,  1.5])

# Simulate each activity duration for every project and sum durations per project.
durations = rng.normal(means, stds, size=(N, 3))
total = durations.sum(axis=1)
late  = total > deadline
prob  = late.mean()

print(f"Estimated P(late) = {prob:.4%}")
print(f"Number of late projects: {late.sum()} / {N}")

# Calculate the running fraction of late projects to illustrate estimate convergence.
running = np.cumsum(late) / np.arange(1, N+1)
# Choose evenly spaced simulation counts for a compact convergence plot.
idx = np.unique(np.linspace(0, N-1, 400, dtype=int))
# Plot the estimated late-project probability as more simulations are included.
plt.plot(idx+1, running[idx])
plt.xlabel("Simulations")
plt.ylabel("Running P(late)")
plt.title("Monte-Carlo project-delay probability")
plt.grid(True)
plt.savefig("Task_20_modified_project.png")
plt.show()
