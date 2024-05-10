#!/usr/bin/env python3
import CIAlign.utilityFunctions as utilityFunctions
import numpy as np

# Set the working directory
mydir = '/home/katy/roman_work_experience'

# Read the sequence alignment into an array and sequence names into a list
arr, nams = utilityFunctions.FastaToArray(
    "%s/small/small_alignment.fasta" % mydir)

# Read the consensus sequence and convert it to a list, then an array
file_contents = open("%s/small/small_consensus.fasta" % mydir).readlines()
sequence = file_contents[1].strip()
sequence_array = np.array(list(sequence))

# Examples
# See the first column of the alignment array
arr_col_1 = arr[:, 0]

# See the third row of the array
arr_row_3 = arr[2, :]

# See which cells are equal to "A"
is_A = arr == "A"

# Count the number of "As" in the first column
nAs = sum(is_A[:, 0])

# Count the number of "As" in all columns
nAs_all = sum(arr == "A")