## Islet sci-ATAC-seq 2019

Repository contains code and scripts accompnaying the manuscript _Single-nucleus ATAC-seq
in human pancreatic islets and deep learning upscaling of rare cells reveals cell-specific
type 2 diabetes regulatory signatures_ by Rai and Quang et al (2019).

The code for deep learning strategy within the manuscript is available separately:
[ParkerLab/PillowNet](https://github.com/ParkerLab/PillowNet)


### Bulk Islet ATAC-seq processing

Bulk islet samples were processed using the Snakemake pipeline available at
[raivivek/ATACseq-Snakemake](https://github.com/raivivek/ATACseq-Snakemake).

### Single-nucleus ATAC-seq processing

Scripts that drive the corresponding analysis are contained within the `control`
directory. Further details are included within each directory.
