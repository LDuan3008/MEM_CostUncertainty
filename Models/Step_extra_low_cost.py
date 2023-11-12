from Preprocess_Input import preprocess_input
from Step2_assign_costs import year2050_ExtraLow_run
from Step3_run_core_models import run_model_main_fun
from FindRegion import update_series, update_timenum
import sys, numpy as np, os, pickle

### Read input data
if len(sys.argv) < 3:
    print ('input less parameters than required') 
    sys.exit()
else:
    case_input_path_filename = str(sys.argv[1])
    single_year_index = int(sys.argv[2])
    scale = int(sys.argv[3])

### Pre-processing
print ('Macro_Energy_Model: Pre-processing input')
case_dic,tech_list = preprocess_input(case_input_path_filename)


### Set basic information
case_name_default = case_dic['case_name']
case_dic['num_time_periods'] = 8760
case_dic['output_path'] = './tmp_outputs'
co2_emis_natgas = 0.49

year2050_ExtraLow_run(single_year_index, case_dic, tech_list, case_name_default, co2_emis_natgas, scale)
