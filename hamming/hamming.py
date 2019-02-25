def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strand a and strand b must have same length")

    zipped = zip(strand_a, strand_b)
    return len([1 for (a, b) in zipped if a != b])
