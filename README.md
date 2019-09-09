## Islet sci-ATAC-seq 2019

Repository contains code and scripts accompnaying the manuscript _Single-nucleus ATAC-seq
in human pancreatic islets and deep learning upscaling of rare cells reveals cell-specific
type 2 diabetes regulatory signatures_ by Rai and Quang et al (2019).

The code for deep learning strategy within the manuscript is available separately at [ParkerLab/PillowNet](https://github.com/ParkerLab/PillowNet).


### Bulk Islet ATAC-seq processing

Bulk islet samples were processed using the Snakemake pipeline available at
[raivivek/ATACseq-Snakemake](https://github.com/raivivek/ATACseq-Snakemake).

### Single-nucleus ATAC-seq processing

Scripts that drive the corresponding analysis are contained within the `control`
directory. Further details are included within each directory.

## Requirements

General requirements for the code contained in this repository is listed below.

* [Snakemake](https://snakemake.readthedocs.io/en/stable/) (5.5.0+)
* [Slurm](https://slurm.schedmd.com) (16.05.09+) or some other job scheduler.
* [R](https://www.r-project.org) (3.5.1+). Note that individual script may have different package requirements.
* [Python](https://www.python.org) (3.7.3+). Specific packages are listed in `requirements.txt`.

## Questions?

If you see any bug or have any questions, feel free to contact us via GitHub issues or
email.
