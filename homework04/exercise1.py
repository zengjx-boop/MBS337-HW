from Bio.SeqIO.FastaIO import SimpleFastaParser

fasta_file = "immune_proteins.fasta"

num_sequences = 0
total_residues = 0

longest_length = 0
longest_accession = None

shortest_length = None
shortest_accession = None

with open(fasta_file, "r") as f:
    for header, sequence in SimpleFastaParser(f):
        num_sequences += 1

        seq_len = len(sequence)
        total_residues += seq_len

        parts = header.split("|")
        accession = parts[1]

        if seq_len > longest_length:
            longest_length = seq_len
            longest_accession = accession

        if shortest_length is None or seq_len < shortest_length:
            shortest_length = seq_len
            shortest_accession = accession

print(f"Num Sequences: {num_sequences}")
print(f"Total Residues: {total_residues}")
print(f"Longest Accession: {longest_accession} ({longest_length} residues)")
print(f"Shortest Accession: {shortest_accession} ({shortest_length} residues)")