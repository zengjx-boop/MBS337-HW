import json
import csv

with open("proteinlist_hw3.json", "r") as f:
    data = json.load(f)

with open("proteins.csv", "w", newline="") as o:
    csv_writer = csv.writer(o)

    header = [
        "primaryAccession",
        "proteinName",
        "geneName",
        "organism_scientificName",
        "sequence_length",
        "sequence_mass",
        "function",
    ]
    csv_writer.writerow(header)

    for protein in data["protein_list"]:
        row = [
            protein.get("primaryAccession", ""),
            protein.get("proteinName", ""),
            protein.get("geneName", ""),
            protein.get("organism", {}).get("scientificName", ""),
            protein.get("sequence", {}).get("length", ""),
            protein.get("sequence", {}).get("mass", ""),
            protein.get("function", ""),
        ]
        csv_writer.writerow(row)