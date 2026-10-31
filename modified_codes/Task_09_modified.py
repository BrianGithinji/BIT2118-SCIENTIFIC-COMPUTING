"""
Task 9 – Modified real-world case
Simple PageRank on a small directed web graph (5 pages).
"""
import numpy as np

# Column-stochastic Google matrix (damping factor 0.85)
M = np.array([
    [0.05, 0.05, 0.9 , 0.05, 0.05],
    [0.9 , 0.05, 0.05, 0.05, 0.05],
    [0.05, 0.9 , 0.05, 0.05, 0.05],
    [0.05, 0.05, 0.05, 0.05, 0.9 ],
    [0.05, 0.05, 0.05, 0.9 , 0.05]
])

# Start with equal page scores and repeatedly apply the Google matrix to update ranks.
rank = np.ones(5) / 5
for _ in range(50):
    rank = M @ rank

# Pair each computed rank with its corresponding page label for display.
pages = ["Home", "About", "Products", "Blog", "Contact"]
print("PageRank scores:")
for p, r in zip(pages, rank):
    print(f"  {p:10s}: {r:.4f}")
