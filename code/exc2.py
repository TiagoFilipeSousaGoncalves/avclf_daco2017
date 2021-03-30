# Imports
import numpy as np
import math


# Custom Functions
def compute_entropy(prob_arr):
    # Create entropy variable
    entropy = 0

    # Go through array
    for dprob in prob_arr.flatten():
        
        
        if dprob == 0:
            entropy -= 0
        
        else:
            entropy -= dprob * math.log2(dprob)

        # Debug print
        # print(dprob, entropy)
    
    return entropy

# Create joint probability table (X are rows, Y are cols)
pXY = np.zeros(shape=(2, 2), dtype=np.float)

# Populate distribution
# pXY(0,0)=1/2
pXY[0, 0] = 1/2

# pXY(0,1)=1/6
pXY[0, 1] = 1/6

# pXY(1,0)=0
pXY[1, 0] = 0
 
# pXY(1,1)=1/3
pXY[1, 1] = 1/3

# Debug print
print(f"Joint Distribution pXY:\n{pXY}")
print(f"Sum of pXY: {np.sum(pXY)}")



# We need to compute the marginal distributions first
# X
marg_dist_X = np.zeros(shape=(2, ), dtype=np.float)
marg_dist_X[0] = np.sum(pXY[0, :])
marg_dist_X[1] = np.sum(pXY[1, :])

# Debug print
print(f"Marginal Distribution X: {marg_dist_X} |  Sum: {np.sum(marg_dist_X)}")


# Y
marg_dist_Y = np.zeros(shape=(2, ), dtype=np.float)
marg_dist_Y[0] = np.sum(pXY[:, 0])
marg_dist_Y[1] = np.sum(pXY[:, 1])

# Debug print
print(f"Marginal Distribution Y: {marg_dist_Y} | Sum: {np.sum(marg_dist_Y)}")

# Compute
# H(X,Y)
H_X_Y = compute_entropy(pXY)
print(f"H(X,Y) = {H_X_Y}")

# H(X)
H_X = compute_entropy(marg_dist_X)
print(f"H(X) = {H_X}")
 
# H(Y)
H_Y = compute_entropy(marg_dist_Y)
print(f"H(Y) = {H_Y}")
 
# H(X|Y=0)
 
# H(X|Y)
 
# H(Y|X)
 
# I(X;Y)