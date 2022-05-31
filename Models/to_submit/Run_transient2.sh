#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --mem=60000
#SBATCH --time=200:00:00
#SBATCH --partition=clab
#SBATCH --job-name=transient2
#SBATCH --output=transient2

module purge
module load anaconda/anaconda3
module load gurobi/9.0.0

# python Step_new_transient.py Ref_NgCcsSoWiStNuOwGeBi_transient.csv 2019 2 
python Step_new_transient_all.py Ref_NgCcsSoWiStNuOwGeBi_transient.csv 2019 200 

