#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --mem=60000
#SBATCH --time=200:00:00
#SBATCH --partition=clab
#SBATCH --job-name=LS1
#SBATCH --output=LS1

module purge
module load anaconda/anaconda3
module load gurobi/9.0.0

# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi_LS.csv 2019 20503 0 
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi_LS.csv 2019 20503 1
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi_LS.csv 2019 20503 2 
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi_LS.csv 2019 20192 -999
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi_LS.csv 2019 20503 3 
python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi_LS.csv 2019 20503 4 