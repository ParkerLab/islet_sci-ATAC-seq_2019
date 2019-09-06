## Mapping pipeline

Pipeline works out of two main directories: `work` and `data` both within a directory
specified by `ROOT`. Put raw FASTQ files in `data/` as per the naming convention used in
the `src/Snakefile`.

Output files are written within `work`. Specifcally, `work/mapping`. These destinations
can be changed within the Snakefile.

Finally, the pipeline sources configuration from `config/cluster.yaml` and
`config/config.yaml`. Please check them so that all the paths point to appropriate paths
on your system.


### Running

Use `make dry_run` for a test run. Use `make run` for submitting the pipeline as jobs to SLURM
scheduler.
