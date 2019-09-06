## QC pipeline

Pipeline used to call aggregate peaks and collect ATAC-seq QC metrics on aggregate as well
as single cell BAM files.

Pipeline works out of two main directories: `work` and `data` both within a directory
specified by `ROOT`. It also relies on the output of `mapping` pipeline.

Output files are written within `work`. Specifcally, `work/qc`. These destinations
can be changed within the Snakefile.

Finally, the pipeline sources configuration from `config/cluster.yaml` and
`config/config.yaml`. Please check them so that all the paths point to appropriate paths
on your system.

### Running

Use `make dry_run` for a test run. Use `make run` for submitting the pipeline as jobs to SLURM
scheduler.
