# Imports
import numpy as np
import math 


# Custom Functions
# Function: Compute Entropy
def compute_entropy(prob_arr):
    # Create entropy variable
    entropy = 0

    # Go through array
    for dprob in prob_arr.flatten():
        
        
        if dprob == 0:
            entropy -= 0.0
        
        else:
            entropy -= dprob * math.log2(dprob)

        # Debug print
        # print(dprob, entropy)
    
    return entropy



# Function: Compute Mutual Information for BSC
def compute_MI_BSC(Y_prob_arr, p_arr):
    # Compute H(Y)
    H_Y = compute_entropy(prob_arr=Y_prob_arr)

    # Compute H(p)
    H_p = compute_entropy(prob_arr=p_arr)

    # I(X; Y) = H(Y) − H(p)
    mutual_information = H_Y - H_p


    return mutual_information



# Function: Compute BSC Channel Capacity
def compute_BSC_capacity(p_arr):
    # Compute H(p)
    H_p = compute_entropy(p_arr)

    # Compute C = 1 − H(p)
    max_capacity = 1 - H_p


    return max_capacity



# a) What’s the mutual information between the input and the output when p(X=0) = 0.25 and p=0.1?
p = 0.1
px_eq_0 = 0.25

# We may compute p(X=1)
px_eq_1 = 1 - px_eq_0
# print(f"p(X=1): {px_eq_1}")

# We may now compute p(Y=0), i.e., P(Y = 0) = (1 − p)P(X = 0) + pP(X = 1)
py_eq_0 = ((1-p) * px_eq_0) + (p * px_eq_1)
# print(f"p(Y=0): {py_eq_0}")

# And P(Y = 1) = pP(X = 0) + (1 − p)P(X = 1)
py_eq_1 = (p * px_eq_0) + ((1-p) * px_eq_1)
# print(f"P(Y=1): {py_eq_1}")

# Sanity check
# print(f"Are these probabilities correct? | {py_eq_0 + py_eq_1 == 1.0}")

# Now, let's build the arrays
p_Y = np.array([py_eq_0, py_eq_1], dtype=np.float)
p_arr = np.array([1-p, p], dtype=np.float)
print(f"P_Y: {p_Y} | p_arr: {p_arr}")

# Compute MI
MI = compute_MI_BSC(Y_prob_arr=p_Y, p_arr=p_arr)
print(f"Mutual Information in this case (a) is: {MI}")

###################

# b) What’s the mutual information between the input and the output when p(X=0) = 0.25 and p=0.9?
p = 0.9
px_eq_0 = 0.25

# We may compute p(X=1)
px_eq_1 = 1 - px_eq_0
# print(f"p(X=1): {px_eq_1}")

# We may now compute p(Y=0), i.e., P(Y = 0) = (1 − p)P(X = 0) + pP(X = 1)
py_eq_0 = ((1-p) * px_eq_0) + (p * px_eq_1)
# print(f"p(Y=0): {py_eq_0}")

# And P(Y = 1) = pP(X = 0) + (1 − p)P(X = 1)
py_eq_1 = (p * px_eq_0) + ((1-p) * px_eq_1)
# print(f"P(Y=1): {py_eq_1}")

# Sanity check
# print(f"Are these probabilities correct? | {py_eq_0 + py_eq_1 == 1.0}")

# Now, let's build the arrays
p_Y = np.array([py_eq_0, py_eq_1], dtype=np.float)
p_arr = np.array([1-p, p], dtype=np.float)
print(f"P_Y: {p_Y} | p_arr: {p_arr}")

# Compute MI
MI = compute_MI_BSC(Y_prob_arr=p_Y, p_arr=p_arr)
print(f"Mutual Information in this case (b) is: {MI}")

###################

# c) What’s the capacity of the channel for p=0.75?
p = 0.75

# Create the array of probabilities
p_arr = np.array([1-p, p], dtype=np.float)
print(f"(c) p_arr: {p_arr}")

# Compute capacity for this p
max_C = compute_BSC_capacity(p_arr=p_arr)
print(f"The max capacity for this BSC of (c) is: {max_C}")