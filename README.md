# 🌳 Extract sequences from blastp

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## 📍 General info
This script is for extracting sequences in fasta format from blastp hit file. It produces two types of files: one with only ids and the second is with annotations.
	
## 👾 Technologies
Project is created with:
* pandas 
* sys
* argparse
* Bio 
* SeqIO

## 🚀 Setup 
To run this project, you need to write input and output :

#input
* blast or diamond file (tab formatted)
* proteomefile 

#output
* fasta file with annot 
* fasta file with ids

```
$python extract_seqs_blastp.py blastfile proteomefile fasta_annot fasta_ids
```


## 🧚🏼 Author
Begüm Serra Büyüktarakçı 

* Twitter: [@begumserra1](https://twitter.com/begumserra1) 
* Github: [@BegumSerra](https://github.com/BegumSerra/) 
