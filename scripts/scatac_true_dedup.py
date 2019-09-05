#! /usr/bin/env python

"""Removes redundant reads, reads with incorrect aligment from the file"""

import argparse
import sys

import pysam

parser = argparse.ArgumentParser()

parser.add_argument("--bam", required=True, help="BAM (input)")
parser.add_argument("--output", required=True, help="Output BAM")

args = parser.parse_args()

readsin = pysam.AlignmentFile(args.bam, "rb")
readsout = pysam.AlignmentFile(args.output, "wb", template=readsin)

refs = readsin.references

use_chrs = [*["chr" + str(x) for x in range(1, 23)], "chrX", "chrY"]
reads_kept = 0
reads_processed = 0
reads_ambig = 0

for refchrom in refs:
    if refchrom not in use_chrs:
        continue

    readdic = {}
    print("Deduplicating " + refchrom + "...", file=sys.stderr)

    for read in readsin.fetch(refchrom):
        reads_processed = reads_processed + 1

        readname = read.qname.split(":")[0]

        # NOTE: This might have already been removed before; but check anyway
        if "CTF" in readname or "AMBIG" in readname:
            reads_ambig = reads_ambig + 1
            continue

        if read.tlen < 0:
            fragstart = str(read.mpos - read.tlen)
            fragend = str(read.mpos)
        else:
            fragstart = str(read.pos)
            fragend = str(read.pos + read.tlen)

        try:
            readdic[readname + fragstart + fragend]
        except KeyError:
            reads_kept = reads_kept + 1
            readdic[readname + fragstart + fragend] = read
            readsout.write(read)

print("Reads processed.. {}".format(reads_processed))
print("Reads kept... {}".format(reads_kept))
print("Reads ambiguous... {}".format(reads_ambig))
