from Bio import SeqIO

input_fastq = "sample1_rawReads.fastq"
output_fastq = "sample1_cleanReads.fastq"
quality_threshold = 30

total_reads = 0
passed_reads = []

with open(input_fastq, "r") as infile:
    for record in SeqIO.parse(infile, "fastq-sanger"):
        total_reads += 1

        phred_scores = record.letter_annotations["phred_quality"]
        average_phred = sum(phred_scores) / len(phred_scores)

        if average_phred >= quality_threshold:
            passed_reads.append(record)

with open(output_fastq, "w") as outfile:
    SeqIO.write(passed_reads, outfile, "fastq-sanger")

print(f"Total reads in original file: {total_reads}")
print(f"Reads passing filter: {len(passed_reads)}")