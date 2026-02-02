import json
import csv

with open("proteinlist_hw3.json", "r") as f:
    data = json.load(f)

proteins = data["protein_list"]

fieldnames = [
    "primaryAccession",
    "proteinName",
    "geneName",
    "organism_scientificName",
    "sequence_length",
    "sequence_mass",
    "function",
]

with open("proteins.csv", "w", newline="") as out_f:
    writer = csv.DictWriter(out_f, fieldnames=fieldnames)
    writer.writeheader()

    for p in proteins:
        row = {
            "primaryAccession": p.get("primaryAccession", ""),
            "proteinName": p.get("proteinName", ""),
            "geneName": p.get("geneName", ""),
            "organism_scientificName": p.get("organism", {}).get("scientificName", ""),
            "sequence_length": p.get("sequence", {}).get("length", ""),
            "sequence_mass": p.get("sequence", {}).get("mass", ""),
            "function": p.get("function", ""),
        }
        writer.writerow(row)