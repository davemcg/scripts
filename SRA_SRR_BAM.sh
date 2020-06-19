#!/bin/bash

SRR=$1

wget `wget -qO- https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=$SRR | grep aws | grep bam | sed 's/<[^>]*>/\n/g'`
bam=$(basename `wget -qO- https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=$SRR | grep aws | grep bam | sed 's/<[^>]*>/\n/g'`)
mv $bam $SRR.bam
