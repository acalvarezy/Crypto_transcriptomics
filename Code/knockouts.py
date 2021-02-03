#!/usr/bin/env python3

#1. Before starting activate the cobra.py environment
#source python-virtual-environments/cobra_py/bin/activate

#2. Run the script
import cobra
import pandas

from cobra.flux_analysis import (
    single_gene_deletion, single_reaction_deletion, double_gene_deletion,
    double_reaction_deletion)

model=cobra.io.read_sbml_model('/Users/catalina/Dropbox/UVA/CareyLab/gf_no_ortho_CparvumIowaII.xml')

#3. Analysis exchange reactions one by one to see if the model is viable after their removal
print(single_reaction_deletion(model, model.exchanges[:60]))
print(single_reaction_deletion(model, model.exchanges[61:120]))
print(single_reaction_deletion(model, model.exchanges[121:180]))

#4. Analyzing single delections with the knockout option
print('complete model: ', model.optimize())
with model:
    model.reactions.PFKhc.knock_out()
    print('pyrophosphate-dependent phosphofructokinase knocked out: ', model.optimize())

#5. Analyzing doble delections with the knockout option
print('complete model: ', model.optimize())
with model:
	model.reactions.GLCt1.knock_out()
	model.reactions.EX_glc__D_e.knock_out()
	model.optimize()
  print('Growth without Glucose as carbon source: ', model.optimize())

print('Completed')
