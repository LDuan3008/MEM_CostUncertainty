from Preprocess_Input import preprocess_input
from Step3_run_core_models import run_model_main_fun
from FindRegion import update_series, update_timenum
import sys, numpy as np, os, pickle
from itertools import product

### Read input data
if len(sys.argv) < 3:
    print ('give parameter ;;code input region year;;') 
    stop
else:
    case_input_path_filename = sys.argv[1]
    single_year_index = int(sys.argv[2])
    starting_point = int(sys.argv[3])
    
### Pre-processing
print ('Macro_Energy_Model: Pre-processing input')
case_dic,tech_list = preprocess_input(case_input_path_filename)

### Find values
for idx in range(len(tech_list)):
    name = tech_list[idx]['tech_name']
    if name == 'demand':       demand_idx = idx

    if name == 'natgas':       natgas_idx = idx; co2_emis_natgas = tech_list[idx]['var_co2']
    if name == 'natgas_ccs':   natgas_ccs_idx = idx
    if name == 'solar':        solar_idx = idx 
    if name == 'wind':         wind_idx = idx
    if name == 'offwind':      offwind_idx = idx 
    if name == 'nuclear':      nuclear_idx = idx 
    if name == 'geothermal':   geothermal_idx = idx 
    if name == 'biopower':     biopower_idx = idx 
    if name == 'storage':      storage_idx = idx 
    
    if name == 'natgas_fixed':       natgas_fixed_idx = idx 
    if name == 'natgas_ccs_fixed':   natgas_ccs_fixed_idx = idx
    if name == 'solar_fixed':        solar_fixed_idx = idx 
    if name == 'wind_fixed':         wind_fixed_idx = idx
    if name == 'offwind_fixed':      offwind_fixed_idx = idx 
    if name == 'nuclear_fixed':      nuclear_fixed_idx = idx 
    if name == 'geothermal_fixed':   geothermal_fixed_idx = idx 
    if name == 'biopower_fixed':     biopower_fixed_idx = idx 
    if name == 'storage_fixed':      storage_fixed_idx = idx 

with open('Time_transient_cost.pickle', 'rb') as handle:
    cost_transient = pickle.load(handle) 

natgas_fhc = cost_transient['natgas_fhc']
natgas_vhc = cost_transient['natgas_vhc']
ccs_vhc = cost_transient['CCS_vhc']
nuclear_fhc = cost_transient['nuclear_fhc']
biopower_fhc = cost_transient['biopower_fhc']
biopower_vhc = cost_transient['biopower_vhc']

loop_var = []
loop_var += [ [list(cost_transient['CCS_fhc_L']),        list(cost_transient['CCS_fhc_M']),        list(cost_transient['CCS_fhc_H'])] ]
loop_var += [ [list(cost_transient['solar_fhc_L']),      list(cost_transient['solar_fhc_M']),      list(cost_transient['solar_fhc_H'])] ]
loop_var += [ [list(cost_transient['wind_fhc_L']),       list(cost_transient['wind_fhc_M']),       list(cost_transient['wind_fhc_H'])] ]
loop_var += [ [list(cost_transient['offwind_fhc_L']),    list(cost_transient['offwind_fhc_M']),    list(cost_transient['offwind_fhc_H'])] ]
loop_var += [ [list(cost_transient['storage_fhc_L']),    list(cost_transient['storage_fhc_M']),    list(cost_transient['storage_fhc_H'])] ]
loop_var += [ [list(cost_transient['geothermal_fhc_L']), list(cost_transient['geothermal_fhc_M']), list(cost_transient['geothermal_fhc_H'])] ]

ensem_idx = 0

for items in product(*loop_var):
    
    ccs_fhc        = items[0]
    solar_fhc      = items[1]
    wind_fhc       = items[2]
    offwind_fhc    = items[3]
    storage_fhc    = items[4]
    geothermal_fhc = items[5]

    if ensem_idx >= starting_point and ensem_idx < starting_point+100:

        co2_constraints_percentage = np.linspace(0, 100, num=32)[::-1]
        upper_co2_emissions = 8760 * 1 * co2_emis_natgas
        co2_constraints_list = upper_co2_emissions * co2_constraints_percentage / 100
        case_dic['num_time_periods'] = 8760
        case_dic['output_path'] = '/data/carnegie/leiduan/cesm_archive/MEM_CostUncertainty'
        for year_idx in np.arange(2019, 2051, 1):
            current_idx = year_idx - 2019
            tech_list[natgas_idx]['fixed_cost']     = natgas_fhc[current_idx];     tech_list[natgas_idx]['var_cost'] = natgas_vhc
            tech_list[natgas_ccs_idx]['fixed_cost'] = ccs_fhc[current_idx];        tech_list[natgas_ccs_idx]['var_cost'] = ccs_vhc
            tech_list[solar_idx]['fixed_cost']      = solar_fhc[current_idx]
            tech_list[wind_idx]['fixed_cost']       = wind_fhc[current_idx]
            tech_list[offwind_idx]['fixed_cost']    = offwind_fhc[current_idx]
            tech_list[nuclear_idx]['fixed_cost']    = nuclear_fhc[current_idx]
            tech_list[geothermal_idx]['fixed_cost'] = geothermal_fhc[current_idx]
            tech_list[biopower_idx]['fixed_cost']   = biopower_fhc[current_idx];   tech_list[biopower_idx]['var_cost'] = biopower_vhc
            tech_list[storage_idx]['fixed_cost']    = storage_fhc[current_idx]
            tech_list[natgas_fixed_idx]['fixed_cost']     = natgas_fhc[current_idx];     tech_list[natgas_fixed_idx]['var_cost'] = natgas_vhc
            tech_list[natgas_ccs_fixed_idx]['fixed_cost'] = ccs_fhc[current_idx];        tech_list[natgas_ccs_fixed_idx]['var_cost'] = ccs_vhc
            tech_list[solar_fixed_idx]['fixed_cost']      = solar_fhc[current_idx]
            tech_list[wind_fixed_idx]['fixed_cost']       = wind_fhc[current_idx]
            tech_list[offwind_fixed_idx]['fixed_cost']    = offwind_fhc[current_idx]
            tech_list[nuclear_fixed_idx]['fixed_cost']    = nuclear_fhc[current_idx]
            tech_list[geothermal_fixed_idx]['fixed_cost'] = geothermal_fhc[current_idx]
            tech_list[biopower_fixed_idx]['fixed_cost']   = biopower_fhc[current_idx];   tech_list[biopower_fixed_idx]['var_cost'] = biopower_vhc
            tech_list[storage_fixed_idx]['fixed_cost']    = storage_fhc[current_idx]
            if current_idx == 0:
                print ('check: ', current_idx)
                tech_list[natgas_fixed_idx]['capacity']     = 0
                tech_list[natgas_ccs_fixed_idx]['capacity'] = 0
                tech_list[solar_fixed_idx]['capacity']      = 0
                tech_list[wind_fixed_idx]['capacity']       = 0
                tech_list[offwind_fixed_idx]['capacity']    = 0
                tech_list[nuclear_fixed_idx]['capacity']    = 0
                tech_list[geothermal_fixed_idx]['capacity'] = 0
                tech_list[storage_fixed_idx]['capacity']    = 0
            else:
                print ('check: ', current_idx)
                search_list = case_dic['output_path'] + '/' + f'time_transient_ensemble{str(ensem_idx)}_year{str(year_idx-1)}'
                file_list = os.listdir(search_list)
                for file in file_list:
                    print (file)
                    if file[-6:] == "pickle": 
                        case_name_open = file
                        break
                print ('check: ', search_list) 
                print ('check: ', case_name_open) 
                with open(f'{search_list}/{case_name_open}', 'rb') as handle:
                    [[input_case_dic, input_tech_list, input_time_dic], 
                    [results_case_dic, results_tech_dic, results_time_dic]] = pickle.load(handle)
                tech_list[natgas_fixed_idx]['capacity']     = (results_tech_dic['natgas capacity']     + results_tech_dic['natgas_fixed capacity']    )  * (1-1/30)
                tech_list[natgas_ccs_fixed_idx]['capacity'] = (results_tech_dic['natgas_ccs capacity'] + results_tech_dic['natgas_ccs_fixed capacity'])  * (1-1/30)
                tech_list[solar_fixed_idx]['capacity']      = (results_tech_dic['solar capacity']      + results_tech_dic['solar_fixed capacity']     )  * (1-1/30)
                tech_list[wind_fixed_idx]['capacity']       = (results_tech_dic['wind capacity']       + results_tech_dic['wind_fixed capacity']      )  * (1-1/30)
                tech_list[offwind_fixed_idx]['capacity']    = (results_tech_dic['offwind capacity']    + results_tech_dic['offwind_fixed capacity']   )  * (1-1/30)
                tech_list[nuclear_fixed_idx]['capacity']    = (results_tech_dic['nuclear capacity']    + results_tech_dic['nuclear_fixed capacity']   )  * (1-1/30)
                tech_list[geothermal_fixed_idx]['capacity'] = (results_tech_dic['geothermal capacity'] + results_tech_dic['geothermal_fixed capacity'])  * (1-1/30)
                tech_list[storage_fixed_idx]['capacity']    = (results_tech_dic['storage capacity']    + results_tech_dic['storage_fixed capacity']   )  * (1-1/15)
            case_dic['year_start'] = single_year_index
            case_dic['year_end'] = single_year_index
            mean_demand  = update_series(case_dic, tech_list[demand_idx])
            mean_solar   = update_series(case_dic, tech_list[solar_idx])
            mean_wind    = update_series(case_dic, tech_list[wind_idx])
            mean_offwind = update_series(case_dic, tech_list[offwind_idx])
            mean_solar_fixed   = update_series(case_dic, tech_list[solar_fixed_idx])
            mean_wind_fixed    = update_series(case_dic, tech_list[wind_fixed_idx])
            mean_offwind_fixed = update_series(case_dic, tech_list[offwind_fixed_idx])
            case_dic['co2_constraint'] = co2_constraints_list[current_idx]
            case_dic['case_name'] = f'time_transient_ensemble{str(ensem_idx)}_year{str(year_idx)}'
            run_model_main_fun(case_dic, tech_list) 
    ensem_idx += 1