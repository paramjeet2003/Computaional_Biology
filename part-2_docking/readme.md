# Molecular Docking Automation Tool

This Python script automates the process of molecular docking using AutoDock Vina. It prepares the receptor and ligand files, runs docking simulations, and analyzes the docking results to identify close interactions between the receptor and the ligand.

## Features

- Conversion of PDB files to PDBQT format.
- Docking with AutoDock Vina.
- Analysis of docking results to identify nearby residues to the ligands.

## Prerequisites

- Python 3.x
- Biopython
- OpenBabel
- AutoDock Vina

Ensure you have the above prerequisites installed on your system. You can install Biopython and OpenBabel using pip:

```bash
pip install biopython
pip install openbabel
sudo apt install obabel

## Usage
```bash
python docking_ms.py protein.pdb ligand.sdf

## Contributor
- Name:- Paramjeet Singh
- Roll no:- 210106044
- This is under development project. I was working on this project but i stopped because of the End Semester exams and i will definetly start working again after endsems.

## Contact
- For any query, please contact s.paramjeet@iitg.ac.in