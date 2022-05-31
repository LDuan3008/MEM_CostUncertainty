#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --mem=60000
#SBATCH --time=200:00:00
#SBATCH --partition=clab
#SBATCH --job-name=ref2019less
#SBATCH --output=ref2019less



module purge
module load anaconda/anaconda3
module load gurobi/9.0.0

# python Step1_loop_years.py Ref_NgCcsSoWiStNu.csv 2019 2019
# python Step1_loop_years.py Ref_NgCcsSoWiStNuPgp.csv 2019 2019
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBi.csv 2019 2019
# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGeBiPgp.csv 2019 2019


# python Step1_loop_years.py Ref_NgCcsSoWiStNu.csv 2019 2019 -999
# python Step1_loop_years.py Ref_NgCcsSoWiStNu.csv 2018 2019 -999
# python Step1_loop_years.py Ref_NgCcsSoWiStNu.csv 2017 2019 -999
# python Step1_loop_years.py Ref_NgCcsSoWiStNu.csv 2016 2019 -999

# python Step1_loop_years.py Ref_NgCcsSoWiStNuPgp.csv 2019 2019 -999
# python Step1_loop_years.py Ref_NgCcsSoWiStNuPgp.csv 2018 2019 -999
# python Step1_loop_years.py Ref_NgCcsSoWiStNuPgp.csv 2017 2019 -999
# python Step1_loop_years.py Ref_NgCcsSoWiStNuPgp.csv 2016 2019 -999

# python Step1_loop_years.py Ref_NgCcsSoWiStNuOwGe.csv 2019 2019 -999
# python Step1_loop_years.py Ref_NgCcsSoWiStOwGeBi.csv 2019 2019 -999

python Step1_loop_years.py Ref_NgCcsSoWiStOwGe.csv 2019 2019 -999