
library(ggplot2)
library(RColorBrewer)   # for colors
library(xtable)         # for godlooking tables 
library(reshape2)       # for merlting data frames
library(plyr)           # for subseting data in Pyramid plot
library(knitr)
library(tidyverse)
setwd("/Users/catalina/Dropbox/UVA/CareyLab/models/")

## Import data
data <- read_delim("/Users/catalina/Dropbox/UVA/CareyLab/models/results","\t")
head(data)
names(data)

## Convert to data frame with the correct classes
new_data <- transform(data, Total_reactions = as.numeric(Total_reactions), Blocked_reactions = as.numeric(Blocked_reactions), P_Blocked_rxns = as.numeric(P_Blocked_rxns))
class(new_data$Model) 
class(new_data$Total_reactions)

#Set the labels
species <- c("C. andersoni 30847", "C. hominis 30976", "C. hominis TU502 2012", "C. hominis TU502", "C. hominis UdeA01" , "C. meleagridis UKMEL1" , "C. muris RN66" , "C. parvum IowaII" , "C. tyzzeri UGA55" , "C. ubiquitum 39726")
reactions <- c("Blocked" , "Unblocked")
species

#Edit the data and variables
complete_data <- new_data %>% mutate(Unblocked_reactions = Total_reactions - Blocked_reactions) %>% mutate(model_species = species) 
final_data <- complete_data %>% select(model_species, Blocked_reactions, Unblocked_reactions)

id.vars = c("model_species")
results <- melt(final_data, id.vars)
results

## Plot the data
ggplot(results, aes(fill=variable, x=value, y=model_species)) + 
  geom_bar(position="stack", stat="identity") +
  xlab("Reactions") +  ylab("Metabolic model") + 
  theme(axis.text.y = element_text(face = "italic")) +
  scale_fill_discrete(name = "Status", labels = c("Blocked", "Unblocked")) +
  scale_y_discrete(labels = c("C. andersoni 30847", "C. hominis 30976", "C. hominis TU502", "C. hominis TU502 2012", "C. hominis UdeA01" , "C. meleagridis UKMEL1" , "C. muris RN66" , expression(bold("C. parvum IowaII")), "C. tyzzeri UGA55" , "C. ubiquitum 39726"))  
 
# Export the results
ggsave('result_parvum.jpg', dpi=300, height=12, width = 16, units='cm')

