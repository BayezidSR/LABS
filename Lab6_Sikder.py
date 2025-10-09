dna = "gctagctagctagcta"
exons = [(0, 4), (5, 9)]
annot = list(dna.lower()) 

dna_index =[i for s, e in exons for i in range(s, e)]

for i in dna_index: 
    annot[i] = annot[i].upper()

print(''.join(annot))

counts = {nuc: dna.upper().count(nuc) for nuc in 'ATGC'}
print(counts)

print(dna[::-1])