# Makefile
#
# Vivek Rai
# vivekrai@umich.edu
# (c) Parker Lab
#
# 2018-10-16
#

.PHONY = dry_run run

dry_run:
	@snakemake -n --quiet --jn "sciATAC.{jobid}" -j 999  --keep-going --rerun-incomplete \
		--snakefile src/Snakefile \
		--configfile config/config.yaml \
		--latency-wait 60 \
		--cluster-config config/cluster.yaml

run:
	@nohup snakemake ${DRY} --jn "sciATAC.{jobid}" -j 1500  --keep-going --rerun-incomplete \
		--snakefile src/Snakefile \
		--configfile config/config.yaml \
		--latency-wait 60 \
		--cluster-config config/cluster.yaml \
		--cluster "sbatch --output {cluster.output} --time {cluster.time} --mem {cluster.mem} --cpus-per-task {cluster.cpus}" \
		> logs/snakemake.log&
