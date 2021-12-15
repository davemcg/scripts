#!/bin/bash
# Example: SRA_SRR_BAM.sh SRR10759485
# downloads orig 10X bam, then renames to SRR10759485.bam

SRR=$1
wget `wget -qO- https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=$SRR | grep aws | grep bam | sed 's/<[^>]*>/\n/g'`
bam=$(basename `wget -qO- https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=$SRR | grep aws | grep bam | sed 's/<[^>]*>/\n/g'`)
mv $bam $SRR.bam
