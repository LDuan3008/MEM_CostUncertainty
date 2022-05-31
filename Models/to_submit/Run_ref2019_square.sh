#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --mem=60000
#SBATCH --time=200:00:00
#SBATCH --partition=clab
#SBATCH --job-name=ref2019s
#SBATCH --output=ref2019s



module purge
module load anaconda/anaconda3
module load gurobi/9.0.0

python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi_square.csv 2019 2019 -999