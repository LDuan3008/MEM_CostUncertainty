#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --mem=60000
#SBATCH --time=200:00:00
#SBATCH --partition=clab
#SBATCH --job-name=ref2050_Fullspes
#SBATCH --output=ref2050_Fullspes


module purge 
module load anaconda/anaconda3 
module load gurobi/9.0.0 

# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi_square.csv 2019 20502 0 
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi_square.csv 2019 20502 1 
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi_square.csv 2019 20502 2 
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi_square.csv 2019 20502 3 
python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi_square.csv 2019 20502 4 
