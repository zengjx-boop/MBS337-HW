from Bio.PDB.MMCIFParser import MMCIFParser

parser = MMCIFParser()
with open('4HHB.cif', 'r') as f:
    structure = parser.get_structure('hemoglobin', f)

for model in structure:
    for chain in model:
        chain_id = chain.get_id()

        num_residues = 0
        num_atoms = 0

        for residue in chain:
            hetfield, resseq, icode = residue.get_id()

            # Only count non-hetero residues
            if hetfield == ' ':
                num_residues += 1
                for atom in residue:
                    num_atoms += 1

        print(f"Chain {chain_id}: {num_residues} residues, {num_atoms} atoms")