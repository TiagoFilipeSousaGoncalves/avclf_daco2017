# Imports
import os 
import numpy as np
import math


# Directories and variables
data_dir = "data"
results_dir = "results"
digits_freqs_fname = "digits_frequencies.npy"


# Define function to compute probabilities
def compute_digits_probs(digits_frequencies):
    # Get the number of total occurences
    total = np.sum(digits_frequencies)


    # Initialise 'digits_probs' variable
    digits_probs = np.zeros_like(digits_frequencies, dtype=np.float)


    # Go for the digits frequencies
    for dfreq_idx, dfreq in enumerate(digits_frequencies):
        digits_probs[dfreq_idx] = dfreq / total 
      

    return digits_probs



# Define function to compute entropy
def compute_entropy(digits_probs):
    # Initialise digits_entropy variable
    digits_entropy = 0


    # Go through the 'digits_probs' array
    for _, dprob in enumerate(digits_probs):
        digits_entropy -= dprob * math.log2(dprob)


    return digits_entropy



# Debug test (from the book)
# example_probs = np.array([0.5, 0.25, 0.125, 0.125])
# entropy = compute_entropy(digits_probs=example_probs)
# print(entropy)



# Load Numpy array with digits frequencies
digits_freqs = np.load(
    file=os.path.join(results_dir, "digits_frequencies.npy"),
    allow_pickle=True
)


# Compute digits probabilities
digits_probs = compute_digits_probs(digits_frequencies=digits_freqs)

# Debug print
# print(digits_freqs, np.sum(digits_freqs))
# print(digits_probs, np.sum(digits_probs))


# Compute digits entropy
digits_entropy = compute_entropy(digits_probs=digits_probs)

# Finish statement with the answer
print(f"The digits entropy is: {digits_entropy}")



# c)
# What if all the digits have the same probabilities?
digits_w_equal_probs = np.array([1/10 for _ in range(10)])

# Debug prints
# print(digits_w_equal_probs, np.sum(digits_w_equal_probs), digits_w_equal_probs.shape)

# Compute entropy here 
digits_entropy_w_equal_probs = compute_entropy(digits_probs=digits_w_equal_probs)
print(f"The entropy if all the digits were equally probable is: {digits_entropy_w_equal_probs}")