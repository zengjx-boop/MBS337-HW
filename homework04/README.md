# homework04

## Overview
This homework contains four Python scripts that perform FASTA statistics and filtering, FASTQ quality filtering, and mmCIF structure analysis using Biopython.

## Input Files
The following input files are required to run the scripts:

- **immune_proteins.fasta**  
  Multi-sequence FASTA file containing immune-related protein sequences.

- **sample1_rawReads.fastq**  
  FASTQ file containing raw sequencing reads.

- **4HHB.cif**  
  mmCIF structure file of human hemoglobin.

## Scripts
- **exercise1.py**  
  Reads immune_proteins.fasta and reports the total number of sequences, total residues, and the longest and shortest accessions.

- **exercise2.py**  
  Writes a new FASTA file (long_only.fasta) containing only sequences with length ≥ 1000 residues, preserving original headers.

- **exercise3.py**  
  Filters sample1_rawReads.fastq by average Phred quality (≥ 30) and writes sample1_cleanReads.fastq.

- **exercise4.py**  
  Parses 4HHB.cif and reports, for each chain, the number of non-hetero residues and the number of atoms.

