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



# Function: Compute Conditional Entropy
def compute_conditional_entropy(prob_arr, marg_dist_X, marg_dist_Y, X=None, Y=None):
    # Create conditional_entropy variable
    conditional_entropy = 0

    # H(X|Y), i.e., we want H of X given Y
    if Y == True:
        # Create an array to append all the parcels of the sum
        H_X_given_Y = np.zeros_like(marg_dist_Y, dtype=np.float)

        # Go through Y
        for y_i in range(marg_dist_Y.shape[0]):
            # Get p(Y = y_i)
            pYi = marg_dist_Y[y_i]

            # Get H(X|Y = y_i)
            prob_arr_temp = prob_arr[:, y_i]

            # Create the vector of p(X|Y=y_i)
            pX_given_Y = np.zeros_like(marg_dist_Y)

            # Populate 'pX_given_Y'
            for _idx, _pxy in enumerate(prob_arr_temp):
                pX_given_Y[_idx] = _pxy /marg_dist_Y[_idx]
            

            # Add the final parcel to the array of sums
            _entropy = compute_entropy(pX_given_Y)
            H_X_given_Y[y_i] = pYi * _entropy
        

        # H(X|Y) is equal to the sum of the parcels in the vector
        conditional_entropy = np.sum(H_X_given_Y) 


        return conditional_entropy
    


    # H(X|Y=i), i.e., we want H of X given Y=i
    elif isinstance(Y, int) == True:
        # Create the vector of p(X|Y=i)
        pX_given_Y = np.zeros_like(marg_dist_Y)
        # print(f"pX_given_Y: {pX_given_Y}")

        # Since it's Y, we fix the column
        prob_arr_temp = prob_arr[:, Y]        
        # print(f"prob_arr_temp: {prob_arr_temp}")

        # Populate 'pX_given_Y'
        for _idx, _pxy in enumerate(prob_arr_temp):
            pX_given_Y[_idx] = _pxy / marg_dist_Y[_idx]
        
        # Debug print
        # print(f"pX_given_Y: {pX_given_Y}")

        conditional_entropy = compute_entropy(pX_given_Y)


        return conditional_entropy
    

    # H(Y|X), i.e., we want H of Y given X
    elif X == True:
        # Create an array to append all the parcels of the sum
        H_Y_given_X = np.zeros_like(marg_dist_X, dtype=np.float)

        # Go through Y
        for x_i in range(marg_dist_X.shape[0]):
            # Get p(Y = y_i)
            pXi = marg_dist_X[x_i]

            # Get H(Y|X = x_i)
            prob_arr_temp = prob_arr[x_i, :]

            # Create the vector of p(X|Y=y_i)
            pY_given_X = np.zeros_like(marg_dist_X)

            # Populate 'pX_given_Y'
            for _idx, _pxy in enumerate(prob_arr_temp):
                pY_given_X[_idx] = _pxy /marg_dist_X[_idx]
            

            # Add the final parcel to the array of sums
            _entropy = compute_entropy(pY_given_X)
            H_Y_given_X[x_i] = pXi * _entropy
        

        # H(X|Y) is equal to the sum of the parcels in the vector
        conditional_entropy = np.sum(H_Y_given_X)
    
        return conditional_entropy
    

    # H(Y|X=i), i.e., we want H of Y given X=i
    elif isinstance(X, int) == True:
       # Create the vector of p(Y|X=i)
        pY_given_X = np.zeros_like(marg_dist_X)

        # Since it's X, we fix the row
        prob_arr_temp = prob_arr[X, :]

        # Populate 'pY_given_X'
        for _idx, _pxy in enumerate(prob_arr_temp):
            pY_given_X[_idx] = _pxy / marg_dist_X[_idx]
        

        conditional_entropy = compute_entropy(pY_given_X)
    

        return conditional_entropy



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
H_X_given_Y_0 = compute_conditional_entropy(prob_arr=pXY, marg_dist_X=marg_dist_X, marg_dist_Y=marg_dist_Y, Y=0)
print(f"H(X|Y=0) = {H_X_given_Y_0}")
 
# H(X|Y)
H_X_given_Y = compute_conditional_entropy(prob_arr=pXY, marg_dist_X=marg_dist_X, marg_dist_Y=marg_dist_Y, Y=True)
print(f"H(X|Y) = {H_X_given_Y}")
 
# H(Y|X)
H_Y_given_X = compute_conditional_entropy(prob_arr=pXY, marg_dist_X=marg_dist_X, marg_dist_Y=marg_dist_Y, X=True)
print(f"H(Y|X) = {H_Y_given_X}")


# Sanity Checks
# H(X) − H(X|Y) = H(Y) − H(Y|X)
# print(f"{H_X - H_X_given_Y} = {H_Y - H_Y_given_X} | {(H_X - H_X_given_Y)==(H_Y - H_Y_given_X)}")

# I(X;Y)
# Case 1: I(X; Y) = H(X) − H(X|Y)
print(f"Case 1 | I(X; Y) = H(X) − H(X|Y): {H_X - H_X_given_Y}")

# Case 2: I(X; Y) = H(Y) − H(Y|X)
print(f"Case 2 | I(X; Y) = H(Y) − H(Y|X): {H_Y - H_Y_given_X}")

# Case 3: I(X; Y) = H(X) + H(Y) − H(X,Y)
print(f"Case 3 | I(X; Y) = H(X) + H(Y) − H(X,Y): {H_X + H_Y - H_X_Y}")

# Debug prints
# There is no difference, only rounding errors by Python
# print(f"{(H_X - H_X_given_Y) - (H_X + H_Y - H_X_Y)}")