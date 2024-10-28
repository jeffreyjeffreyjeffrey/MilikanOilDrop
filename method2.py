import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def gaussian(trial, n_trials=1000, points=61, bins=10000):
    n_trials = 1000 * (trial)
    filename = "charges_second.txt"
    q1 = np.genfromtxt(filename)  # Load charge values

    filename = "uncertainty_q_second.txt"
    delta_q1 = np.genfromtxt(filename)  # Load uncertainty values
    
    # Generate random samples from normal distributions for all trials at once
    charges = np.concatenate([
        np.random.normal(q1[j], delta_q1[j], n_trials) for j in range(points)
    ])

    counts, bin_edges = np.histogram(charges, bins)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2 

    # Use find_peaks to locate indices of local peaks
    peak_indices, _ = find_peaks(counts)
    local_peaks = bin_centers[peak_indices]  # Get the charge values at local peaks
    
    # Filter local peaks based on defined limits
    min_value = 3.520e-19
    max_value = 5.137e-17
    local_peaks = local_peaks[(local_peaks > min_value) & (local_peaks < max_value)]

    # Write the local peaks to a file
    with open(f"local_peaks_two_{trial}.txt", "w") as f:
        for peak in local_peaks:
            f.write(f"{peak}\n")

    # Uncomment to plot histogram
    # plt.figure(figsize=(10, 6))
    # plt.hist(charges, bins, color="skyblue", edgecolor="black", alpha=0.7)
    # plt.xlabel("Charge (C)")
    # plt.ylabel("Frequency")
    # plt.title("Monte Carlo Simulated Charge Distribution")
    # plt.show()

    return

for i in range(200):
    gaussian(i)  # Pass 'i' instead of 'I'





