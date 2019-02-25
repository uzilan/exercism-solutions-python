import re

transtab = str.maketrans("GCTA", "CGAU")


def to_rna(dna_strand):
    uppercase_dna_strand = dna_strand.upper()
    for c in uppercase_dna_strand:
        if not re.match(r"[GCTA]", c):
            raise ValueError("Unknown nucleotides in dna strand")

    return uppercase_dna_strand.translate(transtab)
