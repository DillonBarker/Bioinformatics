# import packages
from Bio.Seq import Seq
import os
from Bio.Alphabet import generic_dna

# set wd
os.chdir('C:/Users/barke/Documents/2020/Github-Repositories/Bioinformatics')

# load the sequence
from Bio import SeqIO
for record in SeqIO.parse("genome.fasta", "fasta"):
    id  = record.id
    seq = record.seq

# id gives the id of the genome, whilst seq is the fill sequence
print(len(seq))
# translate the sequence
translated_seq = seq.translate()
print(translated_seq)
