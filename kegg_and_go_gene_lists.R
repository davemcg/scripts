# BiocManager::install(c('clusterProfiler','biomaRt'))
library(tidyverse)
library(clusterProfiler)
library(biomaRt) # WARNING NOW "SELECT" will not work in dplyr...must use `dplyr::select`

# GO example
ensembl = useMart("ensembl",dataset="hsapiens_gene_ensembl") #uses human ensembl annotations
gene_data <- getBM(attributes=c('hgnc_symbol', 'ensembl_transcript_id', 'go_id'),
                   filters = 'go', values = 'GO:0006979', mart = ensembl)

gene_data %>% head()

# how to get gene sets from KEGG
## uses clusterProfiler
## annoying code chunk to get all hgnc gene symbols
## skip if you are doing RNAseq and have a count matrix or whatever
all_genes <- getBM(attributes=c('hgnc_symbol'),
                  filters = 'chromosome_name', values = c(seq(1:22),'X','Y'), mart = ensembl)
ids <- bitr(all_genes$hgnc_symbol %>% unique(), fromType="SYMBOL", toType=c("UNIPROT", "ENSEMBL", "ENTREZID"), OrgDb="org.Hs.eg.db")
kegg_map <- left_join(ids, download_KEGG('hsa')$KEGGPATHID2EXTID,
                      by=c('ENTREZID'='to')) %>%
  left_join( download_KEGG('hsa')$KEGGPATHID2NAME)

kegg_map %>% filter(to == 'Melanogenesis')
kegg_map %>% filter(from == 'hsa04810')


