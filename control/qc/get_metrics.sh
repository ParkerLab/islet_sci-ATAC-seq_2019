#! /bin/bash

extractAtaqvMetric2 \
  --metrics hqaa hqaa_in_peaks hqaa_overlapping_peaks_percent tss_enrichment \
  --files ../ataqv/*.json.gz \
  --threads 4 \
  --sanitize_names \
  --output metrics_all.txt
