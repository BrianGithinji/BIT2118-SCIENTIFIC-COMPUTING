import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000

# Random demand scenarios
demand = rng.normal(mean_demand, std_demand, N)

overloaded = demand > capacity
overload_probability = overloaded.mean()

print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")

# Running probability to show convergence
running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)

indices = np.unique(
    np.linspace(0, N - 1, 500, dtype=int)
)

plt.plot(indices + 1, running_probability[indices])
plt.xlabel("Number of simulations")
plt.ylabel("Running overload probability")
plt.title("Monte Carlo convergence of overload probability")
plt.grid(True)
plt.savefig("Task_20_monte_carlo.png")
plt.show()
