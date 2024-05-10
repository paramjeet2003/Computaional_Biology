# Protein Sequence Generator and Converter

This script is designed to generate random protein sequences, save these sequences in a custom ribosomal format (.rib), and potentially convert these to the Protein Data Bank format (.pdb) using an external command. The script randomly selects amino acids to create sequences of specified length, which are then annotated with random dihedral angles (phi and psi) and written to .rib files.

## Features
### Random Sequence Generation: 
Generates sequences of amino acids of specified lengths.

### Rib File Creation: 
Saves sequences in a .rib file format with associated structural information.

### Automated File Conversion: 
Converts .rib files to .pdb using an external ribosome software tool.

## Requirements
    1) Python 3.x

    2) Access to a Unix-like shell if executing external commands.

## Usage
To use the script, follow these steps:

Open your terminal or command prompt.

Navigate to the directory containing the script.

Run the script by typing:

Copy code:

    python3 automation.py

Follow the on-screen prompts to enter the number of sequences, their length, and the output directory for saving the .pdb files.

## Input Parameters
    Number of Sequences: How many sequences you want to generate.
    Sequence Length: The length of each sequence.
    Output Directory: Directory where you want the .pdb files to be saved (optional).

## Troubleshooting
#### Script Fails to Execute:  
Ensure Python is correctly installed and that your PATH environment variable is set up correctly.


#### File Conversion Issues: 
Check that the "ribosome" is correctly installed, especially if you receive errors related to file conversion. Verify that the ribosome and res.zmat files are in the correct locations and accessible to the script.

## Contributors
- Paramjeet Singh

## Contact
For any query, please contact s.paramjeet@iitg.ac.in
