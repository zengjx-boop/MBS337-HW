def base_percentage(seq):
    length = len(seq)
    
    base_dir = {
        "A": seq.count("A") / length * 100,
        "T": seq.count("T") / length * 100,
        "G": seq.count("G") / length * 100,
        "C": seq.count("C") / length * 100
    }
    
    return base_dir


dna_seq = "GAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAA"
result = base_percentage(dna_seq)

for base, percent in result.items():
    print("{base}: {percent:.2f}%")