# Makefile
#
# Vivek Rai
# vivekrai@umich.edu
# (c) Parker Lab
#
# Oct 14, 2018
#

.PHONY = dry_run run

dry_run:
	@snakemake -npr --jn "snakejob.{jobid}" -j 999  --keep-going --rerun-incomplete \
		--snakefile src/Snakefile \
		--configfile config/config.yaml

run:
	@nohup snakemake --jn "snakejob.{jobid}" -j 999 --keep-going --rerun-incomplete \
		--snakefile src/Snakefile \
		--configfile config/config.yaml \
		--cluster-config config/cluster.yaml \
		--cluster "sbatch --output {cluster.output} --time {cluster.time} --mem {cluster.mem} --cpus-per-task {cluster.cpus}" \
		> logs/snakemake.log&
