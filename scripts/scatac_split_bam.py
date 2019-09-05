#! /usr/bin/env python3

import os
import sys
import argparse

import pysam

parser = argparse.ArgumentParser()

parser.add_argument("--bam", required=True, help="BAM (input)")
parser.add_argument("--index", required=True, help="Index-table")
parser.add_argument("--out_dir", required=True, help="Output directory")

args = parser.parse_args()
inbam = pysam.Samfile(args.bam, "rb")
out_dir = os.path.abspath(args.out_dir)
os.makedirs(out_dir, exist_ok=True)

out_dic = {}

possible_barcodes = {}
with open(args.index, "r") as f:
    for k in [x.strip().split()[0] for x in f]:
        possible_barcodes[k] = True

reads = inbam.fetch()

reads_read = 0
reads_wrote = 0

for line in reads:
    qname = line.qname.split(":")[0]

    reads_read = reads_read + 1
    if not possible_barcodes.get(qname):
        continue

    reads_wrote = reads_wrote + 1
    if out_dic.get(qname):
        out_dic[qname].write(line)
    else:
        out_dic[qname] = pysam.Samfile(
            os.path.join(out_dir, "{}.bam".format(qname)), "wb", template=inbam
        )
        # FIXED: Feb 12 2019 -- should also write the read after creating file
        out_dic[qname].write(line)

inbam.close()

for barcode in out_dic.keys():
    out_dic[barcode].close()

print("Reads read...{}".format(reads_read))
print("Reads wrote...{}".format(reads_wrote))
