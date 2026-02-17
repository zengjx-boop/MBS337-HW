# **Homework05**



## **Overview**

This homework contains a structured Python script that parses an mmCIF file and generates a per-chain residue summary in JSON format.  

The script applies Unit 4 best practices including:

- Code organization with functions and `main()`
- Logging with configurable log levels
- Argument parsing using `argparse`
- Error handling with `try/except`
- Structured JSON output

---

## **Input File**

The following input file is required to run the script:

**4HHB.cif**  
mmCIF structure file of human hemoglobin.

Download with:

```bash
wget https://files.rcsb.org/download/4HHB.cif.gz
gunzip 4HHB.cif.gz
```

Place `4HHB.cif` in the same directory as `mmcif_summary.py`.

---

## **Script**

### **mmcif_summary.py**

Parses `4HHB.cif` using `MMCIFParser`, computes per-chain residue statistics for the **first model only**, and writes the results to a JSON file.

For each chain, the script reports:

- `total_residues`
- `standard_residues` (non-hetero residues)
- `hetero_residue_count` (waters, ligands, ions, etc.)

Run with:

```bash
python mmcif_summary.py -l INFO
```

The log level may be set to:

```
DEBUG, INFO, WARNING, ERROR, CRITICAL
```

---

## **Output File**

The following output file is generated and written to the `output_files/` directory:

- `4HHB_summary.json`

---
