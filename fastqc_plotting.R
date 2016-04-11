#fastqc_plotting
library(ggplot2)
library(data.table)
library(reshape2)
library(directlabels)

#http://directlabels.r-forge.r-project.org/docs/densityplot/plots/chemscore.html

# per base pair sequence content
pbsc <- fread("Per_base_sequence_content")
pbsc$Base <- as.numeric(sapply(pbsc$Base, function(x) strsplit(x,"-")[[1]][1]))
pbsc2 <- melt(pbsc,id.vars=c("Base","Filename","FastQC_Filter"))
ggplot(pbsc2,aes(x=Base,y=value,colour=Filename,linetype=variable)) + scale_y_continuous(limits=c(0,100)) +
  geom_line() + theme_bw() + ylab("Base Type") + xlab("Position in Read") 

# per base pair sequence quality
pbsq <- fread("Per_base_sequence_quality")
pbsq$Base <- as.numeric(sapply(pbsq$Base, function(x) strsplit(x,"-")[[1]][1]))
ggplot(pbsq,aes(x=Base,y=Mean,colour=Filename)) + 
  geom_line() + theme_bw() + ylab("Sequence Quality") + xlab("Position in Read")

# Per sequence quality scores
psqs <- fread("Per_sequence_quality_scores")
ggplot(psqs,aes(x=Quality,y=Count,colour=Filename)) + 
  geom_line() + theme_bw() + ylab("Read Counts of Quality") + xlab("Sequence Quality (Phred)")

# Per sequence GC content
psGCc <- fread("Per_sequence_GC_content")
ggplot(psGCc,aes(x=`GC Content`,y=Count,colour=Filename)) + 
  geom_line() + theme_bw() + ylab("Read Counts of GC content") + xlab("% GC Content")

# Sequence Duplication Levels
sdl <- fread("Sequence_Duplication_Levels")
sdl$`Duplication Level` <- gsub('k','000',sdl$`Duplication Level`)
sdl$`Duplication Level` <- gsub('>','',sdl$`Duplication Level`)
sdl$`Duplication Level` <- gsub('+','',sdl$`Duplication Level`)
ggplot(sdl,aes(x=log(as.numeric(`Duplication Level`)),y=`Percentage of total`,colour=Filename)) + 
  geom_line() + theme_bw() + ylab("Sequence Duplication Levels") + xlab("Enrichment")
