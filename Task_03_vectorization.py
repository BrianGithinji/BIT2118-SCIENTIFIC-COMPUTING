import numpy as np
import timeit

# Generate one million reproducible network-latency samples between 5 and 250 ms.
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)

def loop_version():
    # Convert each reading to seconds, square it, and collect the results one by one.
    squared = []
    for value in latency_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)
    return squared

def vectorized_version():
    # Perform the same conversion and squaring on the entire NumPy array at once.
    seconds = latency_ms / 1000.0
    return seconds ** 2 

# Time the loop once and the vectorized calculation three times, then average the latter.
loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

# Calculate vectorized results for display after measuring both approaches.
result = vectorized_version()

# Display a sample of the results and compare execution times.
print("First five squared latency values:", result[:5])
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")

