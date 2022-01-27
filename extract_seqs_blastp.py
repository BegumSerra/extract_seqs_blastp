#-Written by Begüm Serra Büyüktarakçı Nov,21

import pandas as pd
import sys
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("in_blastfile", type=str, help="blastfile path")
parser.add_argument("in_proteomefile", type=str, help="proteomefile path")
parser.add_argument("out_annotation", type=str, help="fasta file with annotation")
parser.add_argument("out_ids", type=str, help="fasta file with only ids")
args = parser.parse_args()

df= pd.read_csv(blastfile, sep='\t', names = ["qseqid", "sseqid", "pident", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send", "evalue", "bitscore", "sseq"])
sseqid = df["sseqid"].values.tolist()

def extract_seqs(proteome):
    outgroups=[]
    for record in SeqIO.parse(proteomefile, "fasta"):
        if (record.id).rstrip() in sseqid:
            outgroups.append(record)
    SeqIO.write(outgroups, annot, "fasta")
    print(annot)
    return annot

def extract_ids(annot):
    with open(annot) as handle:
        accession=[]
        for record in SeqIO.parse(handle, "fasta"):
            record.id=record.id.split("|")[1]
            record.description=""
            accession.append(record)
            #print(accession)
        SeqIO.write(accession, ids, "fasta")
        print(ids)
        return ids

def main(proteomefile, annot):
    outgroups = extract_seqs(proteomefile)
    extract_ids(annot)
    return

main(proteomefile, annot)

#input
blastfile = args.in_blastfile 
proteomefile = args.in_proteomefile 

#output
annot = args.out_annotation 
ids = args.out_ids 
