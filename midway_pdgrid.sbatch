#!/bin/bash

#SBATCH --job-name=abm_pdgrid
#SBATCH --error=abm_pdgrid.err
#SBATCH --output=abm_pdgrid.out
#SBATCH --account=macs30123
#SBATCH --partition=caslake
#SBATCH --ntasks=20
#SBATCH --nodes=1 # Run ntasks on same single node
#SBATCH --mail-type=ALL  
#SBATCH --mail-user=lim1an@rcc.uchicago.edu  


# Load Python module
module load python

# Run the Python script
python3 midway_pdgrid.py
