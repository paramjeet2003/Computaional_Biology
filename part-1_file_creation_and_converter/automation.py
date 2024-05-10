import random
import os
from subprocess import call

# Function to generate a random integer between 0 and 19
def randomInt():
    return random.randint(0, 19)

# Function to generate all the sequences of given length
def seqGenerate(noSequence, seqLength):
    amino_acids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
    sequences = []
    for _ in range(noSequence):
        temp = ''.join(random.choice(amino_acids) for _ in range(seqLength))
        sequences.append(temp)
    return sequences

# Function to create Rib File
def createRib(seq, x):
    aa = {
        'A': 'ala', 'C': 'cys', 'D': 'asp', 'E': 'glu',
        'F': 'phe', 'G': 'gly', 'H': 'his', 'I': 'ile',
        'K': 'lys', 'L': 'leu', 'M': 'met', 'N': 'asn',
        'P': 'pro', 'Q': 'gln', 'R': 'arg', 'S': 'ser',
        'T': 'thr', 'V': 'val', 'W': 'trp', 'Y': 'tyr'
    }
    filename = f"file{x}.rib"
    with open(filename, 'w') as file:
        file.write(f"# {seq}\n\n# ")
        file.write('-'.join(aa[ch] for ch in seq))
        file.write(f"\n\nTITLE {filename}\n\n")
        phi = random.uniform(-75,-45)
        psi = random.uniform(-60,-30)
        for ch in seq:
            file.write(f"res {aa[ch]} phi {phi:.2f} psi {psi:.2f}\n\n")

# Function to execute commands
def execution1(outputDirectory="."):
    command = "./ribosome"
    zmatFilename = "res.zmat"

    for entry in os.listdir('.'):
        if entry.endswith('.rib'):
            newfile = entry[:-4]
            outputFilename = f"{outputDirectory}/{newfile}.pdb"
            fullCommand = f"{command} {newfile}.rib {outputFilename} {zmatFilename}"
            result = call(fullCommand, shell=True)
            if result == 0:
                print(f"Command executed successfully for: {newfile}")
            else:
                print(f"Error executing command for: {newfile}")

def main():
    noSequence = int(input("Enter the No. of Sequence: "))
    seqLength = int(input("Enter the Sequence Length: "))
    sequences = seqGenerate(noSequence, seqLength)
    for i, seq in enumerate(sequences):
        createRib(seq, i + 1)
    outputDirectory = input("Enter the Output directory(use . for current directory): =")
    execution1(outputDirectory)

if __name__ == "__main__":
    main()