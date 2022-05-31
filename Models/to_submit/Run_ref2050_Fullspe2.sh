#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --mem=60000
#SBATCH --time=200:00:00
#SBATCH --partition=clab
#SBATCH --job-name=ref2050_Fullspe2
#SBATCH --output=ref2050_Fullspe2


module purge 
module load anaconda/anaconda3 
module load gurobi/9.0.0 

# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2019 2050 0
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2019 2050 100
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2019 2050 200
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2019 2050 300
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2019 2050 400
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2019 2050 500
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2019 2050 600
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2019 2050 700

python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2018 20502 0 
python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2018 20502 1 
python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2018 20502 2 

python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2017 20502 0 
python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2017 20502 1 
python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2017 20502 2 

python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2016 20502 0 
python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2016 20502 1 
python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2016 20502 2 

