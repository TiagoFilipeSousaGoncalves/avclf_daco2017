# Imports
import os
import numpy as np
import pandas as pd
import string



# Directories and filenames
results_dir = "results"
data_dir = "data"
pt_text_fname = "exc10_string.txt"

# PT Frequency Letters
# pt_letters_freqs = "pt_letters_freqs.csv"
pt_letters_freqs = "pt_letters_freqs.txt"



# A list containing all characters
all_letters = string.ascii_letters

# Debug print
# print(all_letters)

# Only the lower-case characters
lower_case_letters = all_letters[0:26]

# Debug print
# print(lower_case_letters, len(lower_case_letters))


# Read the CSV that contains the PT letters frequencies
# pt_freqs = pd.read_csv(os.path.join(data_dir, pt_letters_freqs), delimiter=',')
# print(pt_freqs.head())


# Convert this into Numpy array 
# pt_freqs_arr = pt_freqs.values

# Debug print
# print(pt_freqs_arr)

# Where the first col represents the letters and the second col represents the relative frequencies
# pt_freqs_arr = pt_freqs_arr[:, 0:2]

pt_freqs_arr = np.genfromtxt(os.path.join(data_dir, pt_letters_freqs), delimiter=',', dtype=str)
# print(pt_freqs_arr)

pt_freqs_arr = np.array(pt_freqs_arr, dtype=object)

# Convert the second col (strings) to floats (relative frequency)
for i in range(pt_freqs_arr.shape[0]):
    pt_freqs_arr[i, 1] = np.float(pt_freqs_arr[i, 1])


# Debug print
# print(pt_freqs_arr)


# Get only the main 26 letters
# Create an array to append the results
pt_freqs_proc = np.zeros(shape=(len(lower_case_letters), 2), dtype=object)

# Go through the frquencies array
for li in range(len(lower_case_letters)):
    for _, arr in enumerate(pt_freqs_arr):
        if arr[0] == lower_case_letters[li]:
            pt_freqs_proc[li, 0] = arr[0]
            pt_freqs_proc[li, 1] = arr[1]

# Debug print
# print(pt_freqs_proc)

# Debug print
# print(df_pt_freq_letters)

# Convert to array
pt_freq_letters = pt_freqs_proc.copy()

# Debug print
# print(df_pt_freq_letters)



# Debug print
# print(curr_idx)
# print(pt_freqs_proc, pt_freqs_proc.shape)


# Create a list to append all lines
all_lines = list()


# Open portuguese text
with open(os.path.join(data_dir, pt_text_fname), "r", encoding="ascii") as s:
    for line in s.readlines():
        all_lines += line.split()


# Debug print
# print(f"All lines of the Portuguese text:\n{all_lines}")


# Create a unique string with all the text
cipher_string = str()

# Go through 'all_lines' list
for s in all_lines:
    cipher_string += s


# Debug print
# print(f"Full Portuguese text:\n{cipher_string}")


# Sanity check
# len_all_lines = 0
# for s in all_lines:
#     len_all_lines += len(s)

# print(f"Length of the text in all lines: {len_all_lines}")
# print(f"Length of the full text: {len(cipher_string)}")
# print(f"Are they the same? {len_all_lines == len(cipher_string)}")


# Get frequencies of the letters in the text
text_letters_freq = np.zeros(shape=(pt_freq_letters.shape[0], 2), dtype=object)


# Get the frequencies
for l_idx, l in enumerate(lower_case_letters):
    # Count the occurences in 'cipher_string'
    # print(l)
    l_freq = cipher_string.count(l)
    
    # Append this to table of frequencies
    text_letters_freq[l_idx, 0] = l
    text_letters_freq[l_idx, 1] = int(l_freq)

# Debug print
# print(f"Frequency of letters in this encrypted text:\n{text_letters_freq}")

# Get relative frequencies so we can compare to the Portuguese relative frequencies
total = np.sum(text_letters_freq[:, 1])
# print(total)

for idx, arr in enumerate(text_letters_freq):
    # print(arr)
    text_letters_freq[idx, 1] = (arr[1] / total) * 100


# Debug prints
print(text_letters_freq, text_letters_freq.shape)
print(pt_freq_letters, pt_freq_letters.shape)


# Create a dict
alphabet = [f for f in pt_freq_letters[:, 0]]
alphabet_freqs = [f for f in pt_freq_letters[:, 1]]

ciphered_alphabet = [f for f in text_letters_freq[:, 0]]
ciphered_freqs = [f for f in text_letters_freq[:, 1]]

# Loop
decrypt_dict = dict()

while len(decrypt_dict) < 26:
    a_idx = np.argmax(alphabet_freqs)
    curr_letter = alphabet[a_idx]

    m_idx = np.argmax(ciphered_freqs)
    curr_map = ciphered_alphabet[m_idx]

    decrypt_dict[curr_map] = curr_letter

    del alphabet[a_idx]
    del alphabet_freqs[a_idx]
    del ciphered_alphabet[m_idx]
    del ciphered_freqs[m_idx]

print(decrypt_dict)


# loop to recover plain text
decrypt_txt = str()
  
for char in cipher_string:
    if char in lower_case_letters:
        decrypt_txt += decrypt_dict[char]
          

print("Decrypted text :", decrypt_txt) 