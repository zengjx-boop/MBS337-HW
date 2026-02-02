import json
from pydantic import BaseModel


class Sequence(BaseModel):
    value: str
    length: int
    mass: int


class Organism(BaseModel):
    lineage: list


class ProteinEntry(BaseModel):
    proteinName: str
    sequence: Sequence
    organism: Organism


def find_total_mass(proteins):
    total = 0
    for p in proteins:
        total += p.sequence.mass
    print("Total combined mass:", total)


def find_large_proteins(proteins):
    large = []
    for p in proteins:
        if p.sequence.length >= 1000:
            large.append(p.proteinName)
    print("Large proteins (length >= 1000):", large)


def find_non_eukaryotes(proteins):
    non_euks = []
    for p in proteins:
        if "Eukaryota" not in p.organism.lineage:
            non_euks.append(p.proteinName)
    print("Non-eukaryotic proteins:", non_euks)


with open("proteinlist_hw3.json", "r") as f:
    data = json.load(f)

protein_list = []
for entry in data["protein_list"]:
    protein_list.append(ProteinEntry(**entry))

find_total_mass(protein_list)
find_large_proteins(protein_list)
find_non_eukaryotes(protein_list)