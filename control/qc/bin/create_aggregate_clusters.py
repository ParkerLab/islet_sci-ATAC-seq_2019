#! /usr/bin/env python3

# Vivek Rai
# vivekrai@umich.edu
# (c) Parker Lab
#
# 23 Dec 2018

import os
import sys
import pysam
import argparse


def create_aggregate(args):
    out_dir = os.path.abspath(args.out_dir)
    os.makedirs(out_dir, exist_ok=True)

    print("Processing BAM file...", file=sys.stderr)
    bam_f = pysam.Samfile(args.bam, "rb")

    indexes = {}
    out_dic = {}
    print("Reading index file...", file=sys.stderr)
    with open(args.index, "r") as f:
        for line in f:
            barcode, cluster, *_ = line.strip().split()
            indexes[barcode] = cluster

    print("Read {} lines (may include header)...".format(len(indexes)), file=sys.stderr)

    print("Creating aggregate BAM file(s)...", file=sys.stderr)
    for read in bam_f.fetch():
        barcode = read.qname.split(":")[0]
        # Retrieve cluster assignment for the barcode
        cluster = indexes.get(barcode)

        if cluster is None:
            continue

        if out_dic.get(cluster):
            out_dic[cluster].write(read)
        else:
            out_dic[cluster] = pysam.Samfile(
                os.path.join(out_dir, "{}.bam".format(cluster)), "wb", template=bam_f
            )

    print("Writing output file(s)...", file=sys.stderr)

    # close file handles
    bam_f.close()

    for read in out_dic.keys():
        out_dic[read].close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--bam", required=True, help="BAM file")
    parser.add_argument("--index", required=True, help="Index file (Barcode, Cluster, *)")
    parser.add_argument("--out_dir", required=True, help="Output directory")

    args = parser.parse_args()
    create_aggregate(args)
