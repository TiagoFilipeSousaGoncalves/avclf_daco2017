# Imports
import numpy as np
import math

from numpy.lib.utils import source



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



# Function: Compute Average Codeword Length
def compute_avg_cdw_len(prob_arr, cdw_len_arr):
    # Initialise avg_cdw_len variable
    avg_cdw_len = 0

    # Go through the probabilities and the codeword lenghts
    for i in range(prob_arr.shape[0]):
        avg_cdw_len += prob_arr[i] * cdw_len_arr[i]
    

    return avg_cdw_len



# 5.2 The average number of transmitted binary digits per code word.
# Symbols = [S1, S2, S3, S4, S5, S6]
symbols_probs = np.array([0.4, 0.06, 0.1, 0.3, 0.1, 0.04], dtype=np.float)
print(f"Symbols [S1, S2, S3, S4, S5, S6] and their probabilities {symbols_probs}")

# Codeword lenghts
codeword_lens = np.array([1, 5, 3, 2, 4, 5], dtype=np.float)
print(f"Symbols [S1, S2, S3, S4, S5, S6] and their codeword lengths {codeword_lens}")

# Compute average codeword length
avg_cdw_len = compute_avg_cdw_len(prob_arr=symbols_probs, cdw_len_arr=codeword_lens)
print(f"The average number of transmitted binary digits per code word is: {avg_cdw_len}")

#######################

# 5.3 Compare the average word length with the entropy of the source.
# First compute the entropy of the source
source_entropy = compute_entropy(prob_arr=symbols_probs)
print(f"The entropy of the source is: {source_entropy}")

# This allows to compute the redundancy of the source
source_redundancy = avg_cdw_len - source_entropy
print(f"The source redundancy is: {source_redundancy} bits/symbol")