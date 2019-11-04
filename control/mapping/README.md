## Mapping pipeline

Pipeline works out of two main directories: `work` and `data` both within a directory
specified by `ROOT`.

The main input ingrediants of the pipeline are:
* FASTQ files (read1, read2)
* Indextable (contains list of barcodes)

Both of these are available in dbGap repository under accession `phs001188.v2.p1`.

When both files are available, put them in `data/raw` as per the naming convention used in
the `src/Snakefile`.

Output files are written within `work`. Specifcally, `work/mapping`. These destinations
can be changed within the Snakefile.

Finally, the pipeline sources configuration from `config/cluster.yaml` and
`config/config.yaml`. Please check them so that all the paths point to appropriate paths
on your system.

### Configuration

Please carefully check `config/config.yaml`. You must specify path to 1) Bwa genome index
directory, 2) an email address (to get any error messages), and 3) the path of the root analysis
directory.

### Running

Use `make dry_run` for a test run. Use `make run` for submitting the pipeline as jobs to SLURM
scheduler.
