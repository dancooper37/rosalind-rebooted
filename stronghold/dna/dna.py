"""Given: A DNA string 's' of length at most 1000 nt. Return: Four integers (separated by spaces) counting the
respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in 's'. """

with open("sample_dna", "r") as f:
    dna_string = f.readline().strip()
