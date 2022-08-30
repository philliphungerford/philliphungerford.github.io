##############################################################################
# Script name: index-plot.py
# Purpose: Creating the plot for my website
# Author: Phillip Hungerford
# Date Created: 2021-07-24
# Copyright (c) Phillip Hungerford, 2021
# Email: phillip.hungerford@gmail.com
##############################################################################
# Notes:
# This is to create a plot as a title for my website on github.
# Objective: line graph with beautiful colours.
##############################################################################
# Dependencies: 
import pandas as pd
from plotnine import *

##############################################################################
# Create data for plot
df = pd.DataFrame({
        'x':[0,1,2,3,4,5],
        'Statistics': [0,25,25,50,50,100],
        'MachineLearning':[0,10,25,25,35,100],
        'Programming':[0,35,35,35,50,100],
        'Visualisations':[0,30,30,30,60,100]
        })

# Tidy data for ggplot
mdf = pd.melt(df,
              id_vars=['x'],
              value_vars=["Statistics", "MachineLearning", "Programming", "Visualisations"],
              var_name='Skills', value_name='value')
#=============================================================================
# Plot characteristics
# Colour palette from (https://colorhunt.co/palette/52006acd113bff7600ffa900)
colors = ["#52006A", "#CD113B", "#FF7600", "#FFA900"]

            
p = (
    ggplot(mdf)  # What data to use
    + aes(x="x", y="value", color='Skills')  # What variable to use
    + geom_line(size=2)  # Geometric object to use for drawing
    + geom_point(size=3)
    + scale_color_manual(values=colors)
    + labs(title = "What You Can Learn", y="Knowledge",x = "Time")
    +   theme(panel_grid_major = element_blank(), panel_grid_minor = element_blank(),
        panel_background = element_rect(fill = "#f7f7f7", colour = "black"), axis_line = element_line(colour = "black"), legend_position="bottom",
        axis_text_x=element_blank(),
        axis_text_y=element_blank(), axis_ticks = element_blank(), legend_background=element_blank())
)
print(p)
ggsave(filename='C:/Users/Phillip/Documents/index-plot-py.png',
       plot=p,
       device='png',
       dpi=320, width = 101.6/5, height=57.15/5, units="cm",)
##############################################################################
#################################### END #####################################
##############################################################################