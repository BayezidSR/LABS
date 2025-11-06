def read_fasta(file_path):
    sequences = {}
    header = None
    seq_lines = []

    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue 
            if line.startswith(">"):
                if header:
                    sequences[header] = ''.join(seq_lines)
                    seq_lines = []
                header = line[1:] 
            else:
                seq_lines.append(line)

        if header:
            sequences[header] = ''.join(seq_lines)

    return sequences

def base_percentages(seq):
    seq = seq.upper()
    length = len(seq)
    if length == 0:
        return {b: 0 for b in 'ATGC'}

    return {b: round(seq.count(b) / length * 100, 2) for b in 'ATGC'}

file_path = r"C:\Users\iikiy\Downloads\sequence.fasta"
fasta_data = read_fasta(file_path)

for header, sequence in fasta_data.items():
    print(f"Header: {header}")
    print(f"Sequence length: {len(sequence)} bases")
    print(f"First 100 bases: {sequence[:100]}")
    print("Base percentages:")
    print(base_percentages(sequence))
    print("-" * 50)