"""
This script processes 'bottom 1 percent' distance matrix files by converting all non-zero values to 1 and keeping zero values. 
This is useful for emphasizing significant values in the matrix while reducing file size and simplifying analysis. The resulting binary 
matrices are saved as integer values.

Each file processed is saved with a 'binary_' prefix. 

To use the script:
- Set 'input_dir' to directory containing 'bottom 1 percent' files.
- Set 'output_dir' to directory where you want the binary files saved.
"""

import numpy as np
import os
import glob

def convert_to_binary_and_save(input_dir, output_dir=None):
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    elif not output_dir:
        output_dir = input_dir  # If input directory not specified use output directory

    for file_path in glob.glob(os.path.join(input_dir, 'bottom1p_*.txt')):
        print(f"Processing {file_path}")
        matrix = np.loadtxt(file_path)
        
        binary_matrix = (matrix > 0).astype(int)  # Convert non-zero to 1, keep zero as 0, int type
        
        file_name = os.path.basename(file_path)
        output_file_path = os.path.join(output_dir, f"binary_{file_name}")  # Prefix output with 'binary_'
        
        np.savetxt(output_file_path, binary_matrix, fmt='%d')  # Save as integer
        print(f"Saved binary matrix to {output_file_path}")

# set input and output path

input_dir = 'path/to/your/input/files'  # Directory containing 'bottom 1 percent' files
output_dir = 'path/to/your/output/files'  # Output directory for binary files

convert_to_binary_and_save(input_dir, output_dir)
