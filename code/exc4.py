# Imports
import numpy as np 


# Kraft-McMillan Inequality Tester
def kraft_mcmillan(code_word_lens, D=2):
    # Results list to append values
    results = list()

    # Go through codeword lengths
    for li in code_word_lens:
        r = D ** (-1 * li)
        results.append(r)
    
    # Get the sum
    r_sum = np.sum(results)

    # Check the inequality
    if r_sum <= 1:
        satisfies = True
    
    else:
        satisfies = False 


    return r_sum, satisfies


# Analyse the codeword lenghts of Exercise 4
# (a) 1, 2, 2, 3
a = [1, 2, 2, 3]
a_sum, a_satisfies = kraft_mcmillan(code_word_lens=a, D=2)
print(f"(a) | Sum: {a_sum} | Satisfies Kraft-McMillan Inequality? {a_satisfies}")

# (b) 1, 2, 3, 3
b = [1, 2, 3, 3]
b_sum, b_satisfies = kraft_mcmillan(code_word_lens=b, D=2)
print(f"(b) | Sum: {b_sum} | Satisfies Kraft-McMillan Inequality? {b_satisfies}")

# (c) 1, 2, 2, 2
c = [1, 2, 2, 2]
c_sum, c_satisfies = kraft_mcmillan(code_word_lens=c, D=2)
print(f"(c) | Sum: {c_sum} | Satisfies Kraft-McMillan Inequality? {c_satisfies}")

# (d) 2, 2, 2, 2, 2
d = [2, 2, 2, 2, 2]
d_sum, d_satisfies = kraft_mcmillan(code_word_lens=d, D=2)
print(f"(d) | Sum: {d_sum} | Satisfies Kraft-McMillan Inequality? {d_satisfies}")