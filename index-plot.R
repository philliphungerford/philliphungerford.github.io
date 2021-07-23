##############################################################################
# Script name: r-script-template.R
# Purpose:
# Author: 
# Date Created: 2021-07-24
# Copyright (c) Phillip Hungerford, 2021
# Email: phillip.hungerford@gmail.com
##############################################################################
# Notes:
# This is to create a plot as a title for my website on github.
# Objective: line graph with beautiful colours.
##############################################################################
options(scipen = 6, digits = 4) 

##############################################################################
# Dependencies: 
library(ggplot2)

##############################################################################
# Create data for plot
df <- data.frame(x = seq(0,5,1),
                 Statistics = c(0,25,25,50,50,100),
                 MachineLearning = c(0,10,25,25,35,100),
                 Programming = c(0,35,35,35,50,100),
                 Visualisations = c(0,30,30,30,60,100)
)

# Tidy data for ggplot
mdf <- reshape2::melt(df, id.var = "x")

# Rename variable to provide more meaning
names(mdf)[names(mdf) == "variable"] <- "Skills"

#=============================================================================
# Plot characteristics
# Colour palette from (https://colorhunt.co/palette/52006acd113bff7600ffa900)
colors <- c("#52006A", "#CD113B", "#FF7600", "#FFA900")
size_line <- 2
size_point <- 3

# Build plot
p <- 
  ggplot(mdf, (aes(x = x, y=value, color = Skills))) + 
  
  geom_line(size=size_line) + 
  geom_point(size=size_point) +
  scale_color_manual(values=colors) + 
  labs(title = "What You Can Learn", y="Knowledge",x = "Time") + 
  
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
        panel.background = element_rect(fill = "#f7f7f7", colour = "black"), axis.line = element_line(colour = "black"), legend.position="bottom",
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank(),
        axis.text.y=element_blank(),
        axis.ticks.y=element_blank())

# Preview & save
print(p)
ggsave(filename = 'index-plot.png', dpi = 320)
##############################################################################
#################################### END #####################################
##############################################################################