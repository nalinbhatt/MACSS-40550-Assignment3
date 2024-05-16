#!/bin/bash

# Load necessary modules
module load python mpich cuda

# Install required packages
pip install --user numba==0.57.1 numpy==1.22.4 mpi4py-mpich==3.1.5 mesa~=2.0
pip install jupyter matplotlib
