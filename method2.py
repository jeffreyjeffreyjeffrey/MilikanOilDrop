import numpy as np
import matplotlib.pyplot as plt

# Number of simulations
n_trials = 10000
points = 70
"""
# Measured values and uncertainties (replace these with your actual data)
C1 = 6.40*pow(10,-9)  # Example value
delta_C1 = 0  # Example uncertainty
filename = "v_down.txt"
data = np.genfromtxt(filename) # Example value
v_down = data[:,0]
delta_v_down = data[:,1]  # Example uncertainty

filename = "v_up.txt"
data = np.genfromtxt(filename)
v_up = data[:,0]  # Example value
delta_v_up = data[:,1] # Example uncertainty

filename = "Volt_rise.txt"
data = np.genfromtxt(filename)
V_rise = data[:,0]  # Example value
delta_V_rise = data[:,1]  # Example uncertainty
"""

filename = "charges.txt"
data = np.genfromtxt(filename)
q1 = data[:,0]  # Example value
q2 = data[:,1]  # Example uncertainty

filename = "uncertainty_q.txt"
data = np.genfromtxt(filename)
delta_q1 = data[:,0]  # Example value
delta_q2 = data[:,1]  # Example uncertainty

# Create arrays to hold simulated charges
charges = np.zeros(n_trials*points)

for j in range(0,points):
    for i in range(n_trials):
        # Randomly sample from normal distributions
        """
        sampled_C1 = np.random.normal(C1, delta_C1)
        sampled_v_down = np.random.normal(v_down[j], delta_v_down[j])
        sampled_v_up = np.random.normal(v_up[j], delta_v_up[j])
        sampled_V_rise = np.random.normal(V_rise[j], delta_V_rise[j])
        """
        sampled1 = np.random.normal(q1[j], delta_q1[j])
        #sampled2 = np.random.normal(q2, delta_q2)


        # Calculate charge for the sampled values
        charges[j * n_trials + i] = sampled1

plt.figure(figsize=(10, 6))
plt.hist(charges, bins=100000, color="skyblue", edgecolor="black", alpha=0.7)
plt.xlabel("Charge (C)")
plt.ylabel("Frequency")
plt.title("Monte Carlo Simulated Charge Distribution")
plt.show()

"""
charges = np.array(charges)
print(charges)
charges = np.random.normal(1e-19, 1e-20, size=10000)
hist_counts, bin_edges = np.histogram(charges, bins=100)

print("Histogram counts:", hist_counts)
print("Bin edges:", bin_edges)
"""