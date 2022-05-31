#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --mem=60000
#SBATCH --time=200:00:00
#SBATCH --partition=clab
#SBATCH --job-name=ref2050_2018
#SBATCH --output=ref2050_2018


module purge 
module load anaconda/anaconda3 
module load gurobi/9.0.0 


python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2018 20502 4
