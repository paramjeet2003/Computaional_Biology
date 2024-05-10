#we can use dock thor website for the online docking

import subprocess
from Bio.PDB import PDBParser, NeighborSearch, Selection
import sys

def convert_to_pdbqt(pdb_file, sdf_file, output_pdbqt_pdb, output_pdbqt_ligand):
    # Convert PDB to PDBQT for the receptor
    subprocess.run(['obabel', pdb_file, '-O', output_pdbqt_pdb])
    # Convert SDF to PDBQT for the ligand
    subprocess.run(['obabel', sdf_file, '-O', output_pdbqt_ligand])


def run_vina(receptor_pdbqt, ligand_pdbqt, output_file):
    vina_command = [
        './vina.exe', 
        '--receptor', receptor_pdbqt, 
        '--ligand', ligand_pdbqt, 
        '--out', output_file,
        '--center_x', '0', '--center_y', '0', '--center_z', '0',  # Adjust these based on the binding site
        '--size_x', '20', '--size_y', '20', '--size_z', '20'  # Adjust the box size as necessary
    ]
    subprocess.run(vina_command)

def analyze_docking_results(protein_file, ligand_file):
    parser = PDBParser()
    structure = parser.get_structure('complex', protein_file)

    # Assuming ligand_file is a PDB format of the docked ligand
    ligand_structure = parser.get_structure('ligand', ligand_file)
    ligand_atoms = Selection.unfold_entities(ligand_structure, 'A')  # Get all atoms in the ligand

    # Create a NeighborSearch object for the protein
    atom_list = Selection.unfold_entities(structure, 'A')  # Get all atoms in the protein
    ns = NeighborSearch(atom_list)

    # Find all protein atoms within 5 Ångstroms of any ligand atom
    close_atoms = set()
    for atom in ligand_atoms:
        nearby_atoms = ns.search(atom.coord, 5.0, 'A')  # 5.0 Å cutoff
        close_atoms.update(nearby_atoms)

    # Collect residues from these atoms
    close_residues = set(atom.get_parent() for atom in close_atoms)
    for res in close_residues:
        print(f'Residue {res.get_resname()} at {res.get_id()}')

def main():
     if len(sys.argv) != 3:
        print("Usage! Python docking_ms.py protein.pdb ligand.sdf")
     else:
        convert_to_pdbqt(sys.argv[1] , sys.argv[2], 'receptor.pdbqt', 'ligand.pdbqt')
        run_vina('receptor_pdbqt.pdbqt', 'ligand_pdbqt.pdbqt', 'docked_output.pdbqt')
        analyze_docking_results('docked_output.pdb', 'ligand.pdb')


if __name__ == main():
    main()