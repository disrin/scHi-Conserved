"""
This script is designed to process distance matrix files, specifically focusing on identifying and isolating the bottom 1% of distance values within each matrix. The aim is to highlight the genomic bins that are in closest proximity in 3D space.

The code performs the following steps for each distance matrix file in the specified input directory:
1. Loads the distance matrix from a text file into a NumPy array.
2. Flattens the matrix to a 1D array to simplify the calculation of percentile values.
3. Filters out zero values to exclude them from percentile calculations, assuming that zero distances represent a lack of interaction.
4. Determines the bottom 1% threshold of distances, using NumPy's percentile function.
5. Creates a modified matrix, where all values above threshold are set to zero, thereby keeping the shortest 
distances only.
6. Saves this modified matrix to a new file in the specified output directory, prefixing the filename with 'bottom1p_' to denote its processed status.

To use this script, adjust the 'input_dir' to point to your directory containing the original distance matrix files and set 'output_dir' to where you'd like the processed 
files to be saved. It will create the output directory if it doesn't already exist.
"""

import numpy as np
import os
import glob

def process_and_save_bottom_1_percent(file_path, output_dir):
    # Load the distance matrix from the file
    matrix = np.loadtxt(file_path)
    
    # Flatten the matrix to work with it as a 1D array
    flat_matrix = matrix.flatten()
    
    # Find the threshold value for the bottom 1%
    # Use numpy's percentile function. Exclude zeros by filtering them out
    nonzero_flat_matrix = flat_matrix[flat_matrix > 0]
    if len(nonzero_flat_matrix) == 0:
        print(f"No nonzero values found in {file_path}. Skipping.")
        return
    
    bottom_1_percent_threshold = np.percentile(nonzero_flat_matrix, 1)
    
    # Set all values above the bottom 1% threshold to zero
    # Operate on the original matrix for this
    modified_matrix = np.where(matrix <= bottom_1_percent_threshold, matrix, 0)
    
    # Prepare the output file path
    file_name = os.path.basename(file_path)
    output_file_path = os.path.join(output_dir, f"bottom1p_{file_name}")
    
    # Save the modified matrix to the new file
    np.savetxt(output_file_path, modified_matrix, fmt='%f')
    print(f"Processed and saved bottom 1% matrix to {output_file_path}")

# Specify the directory containing the distance matrix files and the output directory
input_dir = 'path/to/input/files'
output_dir = 'path/to/output/files'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Process each file in the input directory
for file_path in glob.glob(os.path.join(input_dir, '*.txt')):
    process_and_save_bottom_1_percent(file_path, output_dir)

