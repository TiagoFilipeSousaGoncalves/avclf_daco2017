# Imports
import os
import numpy as np


# Directories and filenames
results_dir = "results"
data_dir = "data"
spreadsheet_name = "spreadsheet.txt"


# Important variables
digits_dict = [str(i) for i in range(10)]

# Debug print
# print(digits_dict)


# Create a 
all_lines = list()

# Debug print
# print(all_lines)

# Open spreadsheet
with open(os.path.join(data_dir, spreadsheet_name), "r", encoding="ascii") as s:
    for line in s.readlines():
        all_lines += line.split()

# Debug print
# print(all_lines)

# Create lists to get the numbers with more than two digits and to dividem them into floats and non floats
single_digits = list()
not_single_digits = list()

# Go through the extracted lines
for s in all_lines:
    if len(s) <= 2:
        single_digits.append(s)
    
    else:
        not_single_digits.append(s)


# Debug prints
# print(not_single_digits)
# print(single_digits)
# print(len(all_lines), len(single_digits)+len(not_single_digits))


# Now, let's remove the float points of the 'not_single_digits' list
not_single_digits_proc = list()

# Iterate through not_single_digits
for s in not_single_digits:
    temp_s = s.split('.')
    s_wout_point = temp_s[0] + temp_s[1]
    
    # Debug print
    # print(s_wout_point)

    # Append this processed string to the new list
    not_single_digits_proc.append(s_wout_point)


# Debug prints
# print(len(all_lines), len(single_digits)+len(not_single_digits_proc))

# Now we can append both lists
all_lines_proc = single_digits + not_single_digits_proc

# Debug prints
# print(len(all_lines), len(all_lines_proc))


# Create a unique string with all the digits
full_string = str()

# Go through 'all_lines_proc' list
for s in all_lines_proc:
    full_string += s


# Debug print
# print(full_string, len(full_string))

# Get frequencies of the digits
digits_freq = np.zeros(shape=(10,), dtype=int)

# Debug print
# print(digits_dict)
# print(digits_freq)

# Get the frequencies
for d_idx, d in enumerate(digits_dict):
    # Count the occurences in 'full_string'
    d_freq = full_string.count(d)
    
    # Append this to table of frequencies
    digits_freq[d_idx] = int(d_freq)


# Debug prints
# print(digits_freq)
# print(np.sum(digits_freq), len(full_string))

# Save the table of frequencies into a Numpy array
np.save(
    file=os.path.join(results_dir, "digits_frequencies.npy"),
    arr=digits_freq,
    allow_pickle=True
    )

# Finished statement
print(f"Table of Frequencies, {digits_freq}, saved.")