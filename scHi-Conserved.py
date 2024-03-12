"""
This script analyzes a collection of binary matrix files, identifying and quantifying cell locations that are conserved across multiple files. A cell location is 
considered conserved if it contains a '1' in the same position across several files. The analysis is useful where the presence of a '1' in a matrix indicates a significant 
feature or interaction, and the goal is to find features that are common across different datasets.

The script processes each file in a specified directory, expecting files to be binary matrices with '1's representing the features of interest and '0's elsewhere. It 
counts the number of files in which each cell location contains a '1', thus identifying conserved features. The results, including the row and column locations along with 
the conservation count (number of files where the feature is present), are saved to a specified output file in CSV format. This output can be used for further analysis or 
visualization.

To use this script:
1. Place all your binary matrix files in a single directory. Ensure each file is named with a 'binary_' prefix.
2. Set 'input_dir' to the path of the directory containing your binary matrix files.
3. Set 'output_file' to the desired path and name of the output file where the results will be saved.
4. Run the script. The script will print progress messages as it processes each file and will notify you once the analysis is complete and the results are saved.

To use the script:
- Set input_dir to point to the directory with the binary files
- Set output_dir to save the output file
"""

import numpy as np
import os
import glob

def find_conserved_cells(input_dir, output_file):
    # Initialize a dictionary to hold the count of 1s at each cell location
    cell_counts = {}
    
    # Number of files processed
    num_files = 0
    
    # Process each binary matrix file in the directory
    for file_path in glob.glob(os.path.join(input_dir, 'binary_*.txt')):
        print(f"Processing {file_path}")
        # Load the binary matrix from the file
        matrix = np.loadtxt(file_path, dtype=int)
        
        # Update the count of 1s for each cell location
        for index, value in np.ndenumerate(matrix):
            if value == 1:
                if index in cell_counts:
                    cell_counts[index] += 1
                else:
                    cell_counts[index] = 1
        
        num_files += 1
    
    # Check if any files were processed
    if num_files == 0:
        print("No files found. Please check the directory.")
        return
    
    # Save the cell locations and their counts to an output file
    with open(output_file, 'w') as f:
        f.write("Row,Column,ConservedInFiles\n")
        for location, count in sorted(cell_counts.items(), key=lambda x: x[1], reverse=True):
            f.write(f"{location[0]},{location[1]},{count}\n")
    
    print(f"Conserved cell locations and counts saved to {output_file}")

# change input and output path

input_dir = 'path/to/your/binary/files'  # Directory containing 'binary_' prefixed files
output_file = 'path/to/your/output/conserved_cells.txt'  # Output file for results

find_conserved_cells(input_dir, output_file)
