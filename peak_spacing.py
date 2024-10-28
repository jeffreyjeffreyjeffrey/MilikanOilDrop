import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

peak_spacings = []

trials = 60

for trial in range(1,trials):
    # Step 1: Load the data
    filename = "local_peaks_two_{}.txt".format(trial)
    charges = np.loadtxt(filename)

    # Ensure the data is sorted
    charges = np.sort(charges)

    # Step 2: Calculate the differences (spacing) between consecutive peaks
    spacings = np.diff(charges)

    # Step 4: Calculate the mean peak spacing
    mean_peak_spacing = np.mean(spacings)

    # Step 5: Estimate uncertainty
    uncertainty = np.std(spacings) / np.sqrt(len(spacings))

    print(f"Estimated elementary charge (mean peak spacing): {mean_peak_spacing:.3e} C")

    peak_spacings.append(mean_peak_spacing)


# Define the logarithmic function
def log_func(x, a, b, c, d):
    result = a * np.log(b*x + c) + d
    return result

# Function to fit the logarithmic model and plot it
def fit_logarithmic(x, y):
    # Fit the logarithmic model to the data
    try:
        params, _ = curve_fit(log_func, x, y)
        print(params)
        y_fit = log_func(x, *params)
        r2 = r2_score(y, y_fit)
        
        # Plot data and best-fit curve
        plt.scatter(x, y, color='blue', label="Data points")
        plt.plot(x, y_fit, color='red', label=f"Logarithmic fit (R^2 = {r2:.3f})")
        plt.title("Logarithmic Fit")
        plt.xlabel("Trial Number")
        plt.ylabel("Mean Peak Spacing (C)")
        plt.legend()
        plt.show()
        
        print(f"Fitted parameters: a = {params[0]:.3f}, b = {params[1]:.3f}, c = {params[2]:.3f}, d = {params[3]:.3f}")
        print(f"R^2 value: {r2:.3f}")
        
    except Exception as e:
        print("Logarithmic fit failed:", e)
# Example usage
# Assuming 'x' is the trial numbers and 'y' is the array of mean peak spacings
x = np.arange(1,len(peak_spacings)+1)  # if x values are just sequential trial numbers
fit_logarithmic(x, peak_spacings)

