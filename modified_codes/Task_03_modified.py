"""
Task 3 – Modified real-world case
Convert 1 million 8-bit pixel intensities (0-255) to normalised [0,1]
and then square them (common in image-processing pipelines).
Compare pure-Python loop vs vectorised NumPy.
"""
import numpy as np
import timeit

rng = np.random.default_rng(42)
# Generate one million reproducible unsigned 8-bit pixel intensities from 0 through 255.
pixels = rng.integers(0, 256, size=1_000_000, dtype=np.uint8)

def loop_version():
    # Normalize and square each pixel individually using a Python loop.
    result = []
    for p in pixels:
        norm = p / 255.0
        result.append(norm ** 2)
    return result

def vectorized_version():
    # Normalize and square all pixel values using array operations.
    norm = pixels / 255.0
    return norm ** 2

# Time both implementations, averaging five runs of the vectorized operation.
loop_time   = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=5) / 5

# Display sample output and compare the elapsed time and relative speed.
print("First five normalised-squared values:", vectorized_version()[:5])
print(f"Loop time      : {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Speed-up       : {loop_time/vector_time:.1f}x")
