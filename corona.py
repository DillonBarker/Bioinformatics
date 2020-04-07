# import packages
from Bio.Seq import Seq
import os
from Bio.Alphabet import generic_dna

# set wd on laptop
#os.chdir('C:/Users/barke/Documents/2020/Github-Repositories/Bioinformatics')
# set wd on pc
os.chdir('C:/Users/barke/Documents/2020/Coding and Stats/Github-Repositories/Bioinformatics')

# load the sequence
from Bio import SeqIO
for record in SeqIO.parse("genome.fasta", "fasta"):
    genome_id  = record.id
    genome_seq = record.seq

# id gives the id of the genome, whilst seq is the fill sequence

# translate the sequence
genome_translated_seq = genome_seq.translate()

# load in the spike protein translated sequence from the .fasta file in the directory
for record in SeqIO.parse("spike.fasta", "fasta"):
    spike_id  = record.id
    spike_translated_seq = record.seq
``` align the spike sequence to the genome sequence
from Bio.Blast.Applications import NcbiblastpCommandline
from io import StringIO
#from StringIO import StringIO ## i dont know if I need this package, also says I dont have it.
from Bio.Blast import NCBIXML


# Run BLAST and parse the output as XML
output = NcbiblastpCommandline(cmd ="C:/Program Files/NCBI/blast-2.10.0+/bin/blastp.exe", query="spike.fasta", subject="genome.fasta", outfmt=5)()[0]
blast_result_record = NCBIXML.read(StringIO(output))

# Print some information on the result
for alignment in blast_result_record.alignments:
    for hsp in alignment.hsps:
        print('****Alignment****')
        print('sequence:', alignment.title)
        print('length:', alignment.length)
        print('e value:', hsp.expect)
        print(hsp.query)
        print(hsp.match)
        print(hsp.sbjct)```


