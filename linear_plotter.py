import matplotlib.pyplot as plt
import numpy as np
import math

max = 5.137e-17
min = 3.520e-19
interval = math.floor(max/min)

# Define the variable n
n = 2  # Example value for n; you can change this as needed

# Generate the filename with the variable n
filename = f"local_peaks_two_{n}.txt"

# Initialize a list to hold the peaks for each point
all_peaks = []

# Read the file and extract peaks
with open(filename, "r") as f:
    for line in f:
        # Skip any empty lines or headers
        if line.strip() and not line.startswith("Point"):
            # Convert the line to a float and append it to the list
            all_peaks.append(float(line.strip()))

scaling_factor = interval/len(all_peaks)

# Generate an index list for x-axis (1, 2, 3, ...) for plotting
x_values = np.array(range(1, len(all_peaks) + 1))
x_values = x_values * scaling_factor
y_values = np.array(all_peaks)

# Calculate the linear best fit
slope, intercept = np.polyfit(x_values, y_values, 1)

# Print the slope
print(f"Slope of the best fit line: {slope}")

# Generate the best fit line for plotting
best_fit_line = slope * x_values + intercept


# Plot the data in a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x_values, all_peaks, color="blue", label=f"Local Peaks from {filename}")
plt.plot(x_values, best_fit_line, color="red", label="Best Fit Line")
plt.xlabel("Index")
plt.ylabel("Charge (C)")
plt.title(f"Scatter Plot of Local Peaks from {filename}")
plt.legend()
plt.show()
