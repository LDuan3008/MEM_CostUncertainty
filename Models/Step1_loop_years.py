"""
# Code to determine repeating times;
# Create by Lei Duan on Febrary 08, 2020.
"""

import sys
from Step2_assign_costs import year2019_run, year2050_run, year2050_specific
from Step2_assign_costs import year2019_repeat, year2050_repeat, year2050_GeoRepeat
from Preprocess_Input import preprocess_input
import numpy as np



if __name__ == '__main__':

    if len(sys.argv) < 4:
        print ('input less parameters than required') 
        sys.exit()
    else:
        case_input_path_filename = str(sys.argv[1])
        single_year_index = int(sys.argv[2])
        flag_scenario = int(sys.argv[3])
        starting_point = int(sys.argv[4])

    ### Pre-processing
    print ('Macro_Energy_Model: Pre-processing input')
    case_dic, tech_list = preprocess_input(case_input_path_filename)

    ### Set basic information
    case_name_default = case_dic['case_name']
    case_dic['num_time_periods'] = 8760
    case_dic['output_path'] = '/data/carnegie/leiduan/cesm_archive/MEM_CostUncertainty'
    for idx in range(len(tech_list)): 
        name = tech_list[idx]['tech_name']
        if name == 'natgas':  co2_emis_natgas = tech_list[idx]['var_co2']

    if flag_scenario == 2019: 
        year2019_run(single_year_index, case_dic, tech_list, case_name_default, co2_emis_natgas)
    elif flag_scenario == 2050:
        year2050_run(single_year_index, case_dic, tech_list, case_name_default, co2_emis_natgas, starting_point)
    elif flag_scenario == 20502:
        year2050_specific(single_year_index, case_dic, tech_list, case_name_default, co2_emis_natgas, starting_point)
    elif flag_scenario == 20192: 
        year2019_repeat(single_year_index, case_dic, tech_list, case_name_default, co2_emis_natgas)
    elif flag_scenario == 20503: 
        year2050_repeat(single_year_index, case_dic, tech_list, case_name_default, co2_emis_natgas, starting_point)
    elif flag_scenario == 20504:
        year2050_GeoRepeat(single_year_index, case_dic, tech_list, case_name_default, co2_emis_natgas, starting_point)
    else:
        print ('flag_scenario should be either 2019 or 2050') 
        print ('no optimization is conducted')
