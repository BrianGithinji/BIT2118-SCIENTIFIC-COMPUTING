import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Define the system capacity and draw 100,000 independent demand scenarios.
capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000

# Sample demand from the specified normal distribution and flag scenarios above capacity.
demand = rng.normal(mean_demand, std_demand, N)

overloaded = demand > capacity
overload_probability = overloaded.mean()

print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")

# Compute the cumulative fraction of overloads after each simulation.
running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)

# Select evenly spaced simulation counts to keep the convergence plot concise.
indices = np.unique(
    np.linspace(0, N - 1, 500, dtype=int)
)

# Plot the running probability estimate at the selected simulation counts.
plt.plot(indices + 1, running_probability[indices])
plt.xlabel("Number of simulations")
plt.ylabel("Running overload probability")
plt.title("Monte Carlo convergence of overload probability")
plt.grid(True)
plt.savefig("Task_20_monte_carlo.png")
plt.show()
