# 🌳 Extract sequences from blastp

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## 📍 General info
This script is for extracting sequences in fasta format from blastp hit file. It produces two types of files: one with only ids and the second is with annotations.
	
## 👾 Technologies
Project is created with:
* pandas=1.3.4
* python=3.10.0  
* biopython=1.79 
* sys
* argparse
* Bio 
* SeqIO

## 🚀 Setup 
Run this script with [extract_seqs_blastp.py](extract_seqs_blastp.py) and write you need to write input and output in the command line:

### input
* blast or diamond file (tab formatted)
* proteome file 

### output
* fasta file with annot 
* fasta file with ids

```
$python extract_seqs_blastp.py blastfile proteomefile fasta_annot fasta_ids
```

## 🧚🏼 Author
Begüm Serra Büyüktarakçı 

* Twitter: [@begumserra1](https://twitter.com/begumserra1) 
* Github: [@BegumSerra](https://github.com/BegumSerra/) 
