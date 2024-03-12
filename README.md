# scHi-Conserved

This repository contains a series of Python scripts designed to identify, process, and analyze the nearest contacts from distance matrix files. The workflow is divided 
into three main scripts, each handling a specific part of the process, making it easier to handle and analyze significant interactions within your datasets.

## Overview

- **Script1 - find_nearest1p_contacts.py**: Identifies the nearest contacts from distance matrix files by isolating the bottom 1% of distances, which represent the most 
significant interactions.
- **Script2 - make_binaryFiles.py**: Converts the nearest contact files identified by Script 1 into a binary format for easier handling and analysis. In the binary format, 
nearest contacts are marked with a `1`, while all other values are set to `0`.
- **Script3 - scHi-Conserved.py**: Analyzes the binary files produced by Script 2 to identify contacts conserved across multiple files, providing insights into the most 
consistent and potentially significant interactions.

Follow the instructions in each script for usage
