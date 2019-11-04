## Islet sci-ATAC-seq 2019

Repository contains code and scripts accompnaying the manuscript _Single-nucleus ATAC-seq
in human pancreatic islets and deep learning upscaling of rare cells reveals cell-specific
type 2 diabetes regulatory signatures_ by Rai and Quang et al (2019).

Please read the [pre-print](https://www.biorxiv.org/content/10.1101/749283v2) currently
available on BiorXiv.

The code for deep learning strategy within the manuscript is available separately at [ParkerLab/PillowNet](https://github.com/ParkerLab/PillowNet).


### Bulk Islet ATAC-seq processing

Bulk islet samples were processed using the Snakemake pipeline available at
[raivivek/ATACseq-Snakemake](https://github.com/raivivek/ATACseq-Snakemake).

### Single-nucleus ATAC-seq processing

Scripts that drive the corresponding analysis are contained within the `control`
directory. Further details are included within each directory.

## Requirements

### Using our conda environment

Assuming that you have a Linux 64-bit system, download and install Anaconda 3:

```
wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
bash Anaconda3-5.0.1-Linux-x86_64.sh
```

Create the base environment:
```sh
conda env create --file env/meta.yaml
source activate sciatac_seq
```

### Additional packages

R scripts used in the analysis require a few dependencies.

```
packages <- c(
  "ggplot2", "tidyverse", "mclust", "optparse"
)

for(package in packages) {
    install.packages(package, dep = T)
}
```

## Questions?

If you see any bug or have any questions, feel free to contact us via GitHub issues or
email.

## Quick link

![[QR Code](https://www.biorxiv.org/content/10.1101/749283v2)](https://connect.biorxiv.org/qr/qr_img.php?id=749283)
