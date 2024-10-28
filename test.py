import numpy as np

filename = "v_down.txt"
filename = "Volt_rise.txt"

# Load data from file
data = np.genfromtxt(filename)



filename = "Volt_rise.txt"
data = np.genfromtxt(filename) # Example value

#take all number from column 1 of the file and store it in v_down
v_down = data[:,1]
#take all number from column 2 of the file and store it in delta_v_down

import numpy as np

# Simulated data for testing
charges = np.random.normal(1e-19, 1e-20, size=10000)  # Example simulated data
hist_counts, bin_edges = np.histogram(charges, bins=50)  # This should work

print("Histogram counts:", hist_counts)
print("Bin edges:", bin_edges)