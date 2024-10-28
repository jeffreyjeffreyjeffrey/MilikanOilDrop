import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import math

def gaussian(trial, n_trials = 1000, points = 61, bins = 100000):
    filename = "charges_second.txt"
    data = np.genfromtxt(filename)
    q1 = data  # Example value

    filename = "uncertainty_q_second.txt"
    data = np.genfromtxt(filename)
    delta_q1 = data  # Example value
    # Create arrays to hold simulated charges
    charges = np.zeros(n_trials*points)

    for j in range(0,points):
        for i in range(n_trials):
            # Randomly sample from normal distributions
            sampled1 = np.random.normal(q1[j], delta_q1[j])
            # Store the sampled charge
            charges[j * n_trials + i] = sampled1
        # Calculate charge for the sampled values

    counts, bin_edges = np.histogram(charges, bins)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2 

    min_prominence = 2  # Minimum prominence of peaks

    # Use find_peaks to locate indices of local peaks
    peak_indices, _ = find_peaks(counts, prominence=min_prominence)
    local_peaks = bin_centers[peak_indices]  # Get the charge values at local peaks
    
    min_value = 3.520e-19
    max_value = 5.137e-17
    local_peaks = local_peaks[(local_peaks > min_value) & (local_peaks < max_value)]

    # Optionally, save the local peaks to a file for each point
    with open("local_peaks_two_{}.txt".format(trial), "w") as f:
        for peak in local_peaks:
            f.write(f"{peak}\n")


for i in range(5):
    gaussian(i)

# plt.figure(figsize=(10, 6))
# plt.hist(charges, bins, color="skyblue", edgecolor="black", alpha=0.7)
# plt.xlabel("Charge (C)")
# plt.ylabel("Frequency")
# plt.title("Monte Carlo Simulated Charge Distribution")
# plt.show()

