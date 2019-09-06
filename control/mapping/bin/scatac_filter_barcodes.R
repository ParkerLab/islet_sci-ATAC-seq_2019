#! /usr/bin/env Rscript

suppressPackageStartupMessages({
  library(optparse)
  library(mclust)
})

parser <- OptionParser()

options <- list(
  make_option(c('--counts'), help = "Read counts (aka Index table) file"),
  make_option(c('--cutoff', default = "auto", help = "Cutoff for filtering (default: %default)")),
  make_option(c('--prefix', help = "Experiment prefix")),
  make_option(c('--output', help = "Output file"))
)

args <- parse_args(OptionParser(option_list=options))

#prefix: current experiment
currexpt <- args$prefix

#cutoff: required read-depth for a "cell"
#Provide a value or use "mclust" to calculate it automatically
read_cutoff <- args$cutoff

read_counts <- read.table(args$counts, header = T)
bkgd.ind <- grep("bkgd", read_counts$Experiment)

if(length(bkgd.ind) > 0){
  nobkgdmat <- read_counts[-bkgd.ind, ]
} else {
  nobkgdmat <- read_counts
}

cell_call <- Mclust(data.frame(log10(nobkgdmat$ReadCount)),G<-2)

if(read_cutoff == "auto"){
  read_cutoff <- min(nobkgdmat[which(cell_call$classification == 2 & cell_call$uncertainty < 0.05), 3])
}else{
  read_cutoff <- as.numeric(read_cutoff)
}

subsetmat <- nobkgdmat[which(nobkgdmat$ReadCount >= read_cutoff), ]

write(paste("read cutoff used...", read_cutoff), stderr())
write(paste("barcodes kept...", nrow(subsetmat)), stderr())
write(paste("writing (w/o colnames) to...", args$output), stderr())

write.table(subsetmat,
            args$output,
            row.names = F,
            col.names = F,
            sep = '\t',
            quote = F)
