#!/usr/bin/env python3

#1. Before starting activate the cobra.py environment
#source python-virtual-environments/cobra_py/bin/activate

#2. Run the script
import cobra
from riptide import *

#Load the model
model=cobra.io.read_sbml_model('/Users/catalina/Dropbox/UVA/CareyLab/gf_no_ortho_CparvumIowaII.xml')

#Load the transcriptomics data - integrate de data - export the results
transcript_abundances_1 = riptide.read_transcription_file('/Users/catalina/Dropbox/UVA/CareyLab/lung_24h_f.tsv', replicates=True)
riptide_object_1 = riptide.contextualize(model=model, transcriptome=transcript_abundances_1)
riptide.save_output(riptide_obj=riptide_object_1, path='/Users/catalina/Dropbox/UVA/CareyLab/lung_24h_output')

transcript_abundances_2 = riptide.read_transcription_file('/Users/catalina/Dropbox/UVA/CareyLab/lung_72h_f.tsv', replicates=True)
riptide_object_2 = riptide.contextualize(model=model, transcriptome=transcript_abundances_2)
riptide.save_output(riptide_obj=riptide_object_2, path='/Users/catalina/Dropbox/UVA/CareyLab/lung_72h_output')

transcript_abundances_3 = riptide.read_transcription_file('/Users/catalina/Dropbox/UVA/CareyLab/SI_24h_f.tsv', replicates=True)
riptide_object_3 = riptide.contextualize(model=model, transcriptome=transcript_abundances_3)
riptide.save_output(riptide_obj=riptide_object_3, path='/Users/catalina/Dropbox/UVA/CareyLab/SI_24h_output')

transcript_abundances_4 = riptide.read_transcription_file('/Users/catalina/Dropbox/UVA/CareyLab/SI_72h_f.tsv', replicates=True)
riptide_object_4 = riptide.contextualize(model=model, transcriptome=transcript_abundances_4)
riptide.save_output(riptide_obj=riptide_object_4, path='/Users/catalina/Dropbox/UVA/CareyLab/SI_72h_output')
