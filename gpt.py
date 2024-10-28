"""
import numpy as np
import matplotlib.pyplot as plt

#Sample data: a list of measured charges (in Coulombs) and their uncertainties
#Replace with actual experimental values if needed
charges = [3.2e-19, 4.8e-19, 1.6e-19, 6.4e-19]  # Example charges in Coulombs
uncertainties = [0.1e-19, 0.1e-19, 0.1e-19, 0.1e-19]  # Standard deviations for each charge

#Number of Monte Carlo samples per charge
num_samples = 10000

#Generate samples for each charge using Gaussian (normal) distributions
all_samples = []
for q_i, delta_q_i in zip(charges, uncertainties):
    samples = np.random.normal(loc=q_i, scale=delta_q_i, size=num_samples)
    all_samples.extend(samples)

#Plot histogram of all sampled charges
plt.figure(figsize=(10, 6))
plt.hist(all_samples, bins=100, color="skyblue", edgecolor="black", alpha=0.7)
plt.xlabel("Charge (C)")
plt.ylabel("Frequency")
plt.title("Monte Carlo Simulated Charge Distribution")
plt.show()

"""