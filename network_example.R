library(tidyverse)
library(tidygraph)
library(ggraph)
ogvfb <- tibble::tribble(
                  ~from,  ~to, ~count,
                   "Br", "Bh",     4L,
                   "Br", "Ta",     2L,
                   "Br", "Hu",    13L,
                   "Br", "Hu",    10L,
                   "Br", "Je",     3L,
                   "Br", "Ma",     2L,
                   "Br", "Se",     1L,
                   "Br", "Mc",     1L,
                   "He", "Se",     1L,
                   "Bh", "Ta",     1L,
                   "Bh", "Hu",     1L,
                   "Bh", "Hu",     1L,
                   "Bh", "Ma",     7L,
                   "Bh", "Mc",     2L,
                   "Ta", "Hu",     1L,
                   "Ta", "Hu",     4L,
                   "Ta", "Je",     1L,
                   "Ta", "Ma",     1L,
                   "Hu", "Hu",    10L,
                   "Hu", "Je",     1L,
                   "Hu", "Se",     1L,
                   "Hu", "Mc",     1L,
                   "Hu", "Je",     2L,
                   "Hu", "Ma",     1L,
                   "Ma", "Mc",     1L
                  )
ogvfb_graph <- igraph::graph_from_data_frame(ogvfb)

ogvfb_layout <- igraph::layout_with_kk(ogvfb_graph) %>% 
  data.frame() %>% 
  rename(x=X1,y=X2)
# customize number 2 position
ogvfb_layout[2,] <- c(0.3, y = 0.0)

# graph
ggraph(graph = ogvfb_graph, layout = ogvfb_layout) + 
  geom_edge_link(aes(color = count, edge_width = count)) + 
  geom_node_label(aes(label = name)) +
  scale_edge_color_viridis() +
  ggraph::theme_graph() 
