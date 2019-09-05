#! /usr/bin/env python

import sys
import pysam
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--bam", required=True, help="BAM")
parser.add_argument("--index", required=True, help="Index of possible barcodes (with label)")
parser.add_argument("--output", required=True, help="Output file")

args = parser.parse_args()

inbam = args.bam
index = args.index
out = args.output

totalct = {}
descriptor = {}
descdic = {}

# get barcode description
if index != 'NA':
    with open(index, 'r') as f:
        for line in f:
            _line = line.strip().split()
            descdic[_line[0]] = _line[1]

print("Counting total reads...", file=sys.stderr)

bamfile = pysam.Samfile(args.bam,'rb')

# count reads and save whether the barcode comes from experiment or background
for read in bamfile.fetch():
    tagger = read.qname.split(':')[0]
    try:
        totalct[tagger] += 1
    except KeyError:
        totalct[tagger] = 1
        try:
            descriptor[tagger] = descdic[tagger]
        except KeyError:
            descriptor[tagger] = 'bkgd'

bamfile.close()

outter = open(out, 'w')

print("Writing file...", file=sys.stderr)

print('Barcode\tExperiment\tReadCount', file=outter)
for tag in sorted(totalct.keys()):
    print(tag + '\t' + descriptor[tag] + '\t' + str(totalct[tag]), file=outter)

outter.close()
