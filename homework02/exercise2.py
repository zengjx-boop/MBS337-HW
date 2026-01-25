from Bio.Seq import Seq

seq = Seq("GAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAA")
length = len(seq)

g = seq.count("G")
c = seq.count("C")

gc = (g + c) / length *100


print("GC content:", gc, "%")