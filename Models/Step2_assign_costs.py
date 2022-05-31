from Step3_run_core_models import run_model_main_fun
from FindRegion import update_series, update_timenum
import sys, numpy as np, random
from itertools import product


###################################################################################################################################################################################
# Define costs here:
# Year-2019
natgas_fixed_year2019, natgas_var_year2019 = 12.77831841 / 1000, 10 / 1000
natgas_CCS_fixed_year2019, natgas_CCS_var_year2019 = 31.98238555 / 1000, 14 / 1000
solar_fixed_year2019 = 15.42188211 / 1000
wind_fixed_year2019 = 18.11895838 / 1000
nuclear_fixed_year2019 = 93.51739145 / 1000
storage_fixed_year2019 = 7.744342599 / 1000
offwind_fixed_year2019 = [55.14762447 / 1000, 57.15517459 / 1000, 60.35696813 / 1000]
geothermal_fixed_year2019 = 214.3692446 / 1000
biopower_fixed_year2019, biopower_var_year2019 = 57.10371115 / 1000, 48 / 1000
# Year-2050
natgas_fixed_year2050, natgas_var_year2050 = 11.42601233 / 1000, 10 / 1000
natgas_CCS_fixed_year2050, natgas_CCS_var_year2050 = [18.83942967 / 1000, 22.48822899 / 1000, 26.25118356 / 1000], 13 / 1000
solar_fixed_year2050 = [5.794755718 / 1000, 7.581521169 / 1000, 9.079343507 / 1000]
wind_fixed_year2050 = [7.569390621 / 1000, 10.75863775 / 1000, 12.95979032 / 1000]
nuclear_fixed_year2050 = 80.4239702 / 1000
storage_fixed_year2050 = [1.904751567 / 1000, 2.990759329 / 1000, 5.272872439 / 1000]
offwind_fixed_year2050 = [25.08663768 / 1000, 30.61419606 / 1000, 42.91331596 / 1000]
geothermal_fixed_year2050 = [57.24504862 / 1000, 136.349483 / 1000, 187.9210814 / 1000]
biopower_fixed_year2050, biopower_var_year2050 = 49.8730133 / 1000, 48 / 1000

# ---- following costs are not from NREL ATB
to_PGP_fixed_year2019 = 0.014812488
PGP_storage_fixed_year2019 = 1.47E-06
from_PGP_fixed_year2019 = 0.063079473
to_PGP_fixed_year2050 = [3.87690982 / 1000, 10.41583661 / 1000, 16.95475499 / 1000]
PGP_storage_fixed_year2050 = 0.001471898 / 1000
from_PGP_fixed_year2050 = 8.975948304 / 1000 


###################################################################################################################################################################################
# single_year_index is the weather and demand year

def year2019_run(single_year_index, case_dic, tech_list, case_name_default, co2_emis_natgas):
    info_idx = {}
    info_idx['solar_flag'  ] = False
    info_idx['wind_flag'   ] = False
    info_idx['offwind_flag'] = False
    for idx in range(len(tech_list)):
        name = tech_list[idx]['tech_name']
        if name == 'demand':     info_idx['demand_idx']  = idx
        if name == 'natgas':                                                                     tech_list[idx]['fixed_cost'] = natgas_fixed_year2019;     tech_list[idx]['var_cost'] = natgas_var_year2019
        if name == 'natgas_ccs':                                                                 tech_list[idx]['fixed_cost'] = natgas_CCS_fixed_year2019; tech_list[idx]['var_cost'] = natgas_CCS_var_year2019
        if name == 'biopower':                                                                   tech_list[idx]['fixed_cost'] = biopower_fixed_year2019;   tech_list[idx]['var_cost'] = biopower_var_year2019
        if name == 'solar':      info_idx['solar_idx'] = idx;   info_idx['solar_flag'] = True;   tech_list[idx]['fixed_cost'] = solar_fixed_year2019
        if name == 'wind':       info_idx['wind_idx'] = idx;    info_idx['wind_flag'] = True;    tech_list[idx]['fixed_cost'] = wind_fixed_year2019
        if name == 'offwind':    info_idx['offwind_idx'] = idx; info_idx['offwind_flag'] = True; tech_list[idx]['fixed_cost'] = offwind_fixed_year2019[1]
        if name == 'nuclear':                                                                    tech_list[idx]['fixed_cost'] = nuclear_fixed_year2019
        if name == 'storage':                                                                    tech_list[idx]['fixed_cost'] = storage_fixed_year2019
        if name == 'geothermal':                                                                 tech_list[idx]['fixed_cost'] = geothermal_fixed_year2019
    co2_constraints_percentage = np.array([1e24, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0])
    upper_co2_emissions = 8760 * 1 * co2_emis_natgas
    co2_constraints_list = upper_co2_emissions * co2_constraints_percentage / 100
    case_name_output = f'{case_name_default}_Scenarios2019'
    pass_variables(single_year_index, case_dic, tech_list, co2_constraints_list, co2_constraints_percentage, case_name_output, info_idx)

###################################################################################################################################################################################

def year2050_specific(single_year_index, case_dic, tech_list, case_name_default, co2_emis_natgas, scenarios):

    info_idx = {}
    info_idx['solar_flag'  ] = False
    info_idx['wind_flag'   ] = False
    info_idx['offwind_flag'] = False

    natgas_fixed_year2050_NNN, natgas_var_year2050_NNN = 11.42601233 / 1000, 10 / 1000
    nuclear_fixed_year2050_NNN = 80.4239702 / 1000
    biopower_fixed_year2050_NNN, biopower_var_year2050_NNN = 49.8730133 / 1000, 48 / 1000
    # to_PGP_fixed_year2050_NNN = 3.87690982 / 1000
    to_PGP_fixed_year2050_NNN = 16.95475499 / 1000
    PGP_storage_fixed_year2050_NNN = 0.001471898 / 1000
    from_PGP_fixed_year2050_NNN = 8.975948304 / 1000 
    if scenarios == 0:   # All low costs 
        natgas_CCS_fixed_year2050_NNN, natgas_CCS_var_year2050_NNN = 18.83942967 / 1000, 13 / 1000
        solar_fixed_year2050_NNN = 5.794755718 / 1000
        wind_fixed_year2050_NNN = 7.569390621 / 1000
        storage_fixed_year2050_NNN = 1.904751567 / 1000
        offwind_fixed_year2050_NNN = 25.08663768 / 1000
        geothermal_fixed_year2050_NNN = 57.24504862 / 1000
    if scenarios == 1:   # Low geothermal and high others
        natgas_CCS_fixed_year2050_NNN, natgas_CCS_var_year2050_NNN = 26.25118356 / 1000, 13 / 1000
        solar_fixed_year2050_NNN = 9.079343507 / 1000
        wind_fixed_year2050_NNN = 12.95979032 / 1000
        storage_fixed_year2050_NNN = 5.272872439 / 1000
        offwind_fixed_year2050_NNN = 42.91331596 / 1000
        geothermal_fixed_year2050_NNN = 57.24504862 / 1000
    if scenarios == 2:   # All high costs
        natgas_CCS_fixed_year2050_NNN, natgas_CCS_var_year2050_NNN = 26.25118356 / 1000, 13 / 1000
        solar_fixed_year2050_NNN = 9.079343507 / 1000
        wind_fixed_year2050_NNN = 12.95979032 / 1000
        storage_fixed_year2050_NNN = 5.272872439 / 1000
        offwind_fixed_year2050_NNN = 42.91331596 / 1000
        geothermal_fixed_year2050_NNN = 187.9210814 / 1000
    if scenarios == 3:   # Low wind and high others
        natgas_CCS_fixed_year2050_NNN, natgas_CCS_var_year2050_NNN = 26.25118356 / 1000, 13 / 1000
        solar_fixed_year2050_NNN = 9.079343507 / 1000
        wind_fixed_year2050_NNN = 7.569390621 / 1000
        storage_fixed_year2050_NNN = 5.272872439 / 1000
        offwind_fixed_year2050_NNN = 42.91331596 / 1000
        geothermal_fixed_year2050_NNN = 187.9210814 / 1000
    if scenarios == 4:   # Low wind, low geothermal, and high others
        natgas_CCS_fixed_year2050_NNN, natgas_CCS_var_year2050_NNN = 26.25118356 / 1000, 13 / 1000
        solar_fixed_year2050_NNN = 9.079343507 / 1000
        wind_fixed_year2050_NNN = 7.569390621 / 1000
        storage_fixed_year2050_NNN = 5.272872439 / 1000
        offwind_fixed_year2050_NNN = 42.91331596 / 1000
        geothermal_fixed_year2050_NNN = 57.24504862 / 1000


    for idx in range(len(tech_list)):
        name = tech_list[idx]['tech_name']
        if name == 'demand':     info_idx['demand_idx']  = idx
        if name == 'natgas':                                                                     tech_list[idx]['fixed_cost'] = natgas_fixed_year2050_NNN;     tech_list[idx]['var_cost'] = natgas_var_year2050_NNN
        if name == 'natgas_ccs':                                                                 tech_list[idx]['fixed_cost'] = natgas_CCS_fixed_year2050_NNN; tech_list[idx]['var_cost'] = natgas_CCS_var_year2050_NNN
        if name == 'biopower':                                                                   tech_list[idx]['fixed_cost'] = biopower_fixed_year2050_NNN;   tech_list[idx]['var_cost'] = biopower_var_year2050_NNN
        if name == 'solar':      info_idx['solar_idx'] = idx;   info_idx['solar_flag'] = True;   tech_list[idx]['fixed_cost'] = solar_fixed_year2050_NNN
        if name == 'wind':       info_idx['wind_idx'] = idx;    info_idx['wind_flag'] = True;    tech_list[idx]['fixed_cost'] = wind_fixed_year2050_NNN
        if name == 'offwind':    info_idx['offwind_idx'] = idx; info_idx['offwind_flag'] = True; tech_list[idx]['fixed_cost'] = offwind_fixed_year2050_NNN
        if name == 'nuclear':                                                                    tech_list[idx]['fixed_cost'] = nuclear_fixed_year2050_NNN
        if name == 'storage':                                                                    tech_list[idx]['fixed_cost'] = storage_fixed_year2050_NNN
        if name == 'geothermal':                                                                 tech_list[idx]['fixed_cost'] = geothermal_fixed_year2050_NNN
        if name == 'to_PGP':                                                                     tech_list[idx]['fixed_cost'] = to_PGP_fixed_year2050_NNN
        if name == 'PGP_storage':                                                                tech_list[idx]['fixed_cost'] = PGP_storage_fixed_year2050_NNN
        if name == 'from_PGP':                                                                   tech_list[idx]['fixed_cost'] = from_PGP_fixed_year2050_NNN
    
    co2_constraints_percentage = np.array([1e24, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0])
    # co2_constraints_percentage = np.array([1, 0])
    upper_co2_emissions = 8760 * 1 * co2_emis_natgas
    co2_constraints_list = upper_co2_emissions * co2_constraints_percentage / 100
    
    case_name_output = f'{case_name_default}_Scenarios2050_highPGP_sub{str(scenarios)}'
    pass_variables(single_year_index, case_dic, tech_list, co2_constraints_list, co2_constraints_percentage, case_name_output, info_idx)




###################################################################################################################################################################################

def year2050_run(single_year_index, case_dic, tech_list, case_name_default, co2_emis_natgas, starting_point=0):

    pool_list = ['natgas_ccs', 'solar', 'wind', 'storage', 'offwind', 'geothermal', 'to_PGP']
    info_idx = {}
    info_idx['solar_flag'  ] = False
    info_idx['wind_flag'   ] = False
    info_idx['offwind_flag'] = False
    loop_var = []
    loop_loc = {}
    loop_idx = 0
    for idx in range(len(tech_list)):
        name = tech_list[idx]['tech_name']
        if name in pool_list:
            if name == 'natgas_ccs': loop_loc[loop_idx] = idx; loop_idx +=1; loop_var += [natgas_CCS_fixed_year2050]; tech_list[idx]['var_cost'] = natgas_CCS_var_year2050
            if name == 'solar':      loop_loc[loop_idx] = idx; loop_idx +=1; loop_var += [solar_fixed_year2050     ]; info_idx['solar_idx'  ] = idx; info_idx['solar_flag'  ] = True
            if name == 'wind':       loop_loc[loop_idx] = idx; loop_idx +=1; loop_var += [wind_fixed_year2050      ]; info_idx['wind_idx'   ] = idx; info_idx['wind_flag'   ] = True
            if name == 'offwind':    loop_loc[loop_idx] = idx; loop_idx +=1; loop_var += [offwind_fixed_year2050   ]; info_idx['offwind_idx'] = idx; info_idx['offwind_flag'] = True
            if name == 'storage':    loop_loc[loop_idx] = idx; loop_idx +=1; loop_var += [storage_fixed_year2050   ]
            if name == 'geothermal': loop_loc[loop_idx] = idx; loop_idx +=1; loop_var += [geothermal_fixed_year2050]
            if name == 'to_PGP':     loop_loc[loop_idx] = idx; loop_idx +=1; loop_var += [to_PGP_fixed_year2050    ]
        else:
            if name == 'demand':     info_idx['demand_idx']  = idx
            if name == 'natgas':                                                                     tech_list[idx]['fixed_cost'] = natgas_fixed_year2050;     tech_list[idx]['var_cost'] = natgas_var_year2050
            if name == 'biopower':                                                                   tech_list[idx]['fixed_cost'] = biopower_fixed_year2050;   tech_list[idx]['var_cost'] = biopower_var_year2050
            if name == 'nuclear':                                                                    tech_list[idx]['fixed_cost'] = nuclear_fixed_year2050
            if name == 'PGP_storage':                                                                tech_list[idx]['fixed_cost'] = PGP_storage_fixed_year2050
            if name == 'from_PGP':                                                                   tech_list[idx]['fixed_cost'] = from_PGP_fixed_year2050

    # co2_constraints_percentage = np.array([1e24, 50, 20, 10, 1.0, 0.0]) 
    co2_constraints_percentage = np.array([0.0]) 
    # co2_constraints_percentage = np.array([20])
    upper_co2_emissions = 8760 * 1 * co2_emis_natgas
    co2_constraints_list = upper_co2_emissions * co2_constraints_percentage / 100


    ensem_idx = 0
    for items in product(*loop_var):
        for i in range(loop_idx):
            tech_list[loop_loc[i]]['fixed_cost'] = items[i]
        if ensem_idx >= starting_point and ensem_idx < starting_point+100:
            case_name_output = f'{case_name_default}_Scenarios2050_GeoMax03_{str(ensem_idx)}'
            pass_variables(single_year_index, case_dic, tech_list, co2_constraints_list, co2_constraints_percentage, case_name_output, info_idx)
        ensem_idx += 1

###################################################################################################################################################################################


def year2019_repeat(single_year_index, case_dic, tech_list, case_name_default, co2_emis_natgas): 
    info_idx = {} 
    info_idx['solar_flag'  ] = False
    info_idx['wind_flag'   ] = False
    info_idx['offwind_flag'] = False

    PGP_flag = False
    DAC_flag = False
    LSH_flag = False

    for idx in range(len(tech_list)):
        name = tech_list[idx]['tech_name']
        if name == 'demand':     info_idx['demand_idx']  = idx
        if name == 'natgas':                                                                     tech_list[idx]['fixed_cost'] = natgas_fixed_year2019;     tech_list[idx]['var_cost'] = natgas_var_year2019
        if name == 'natgas_ccs':                                                                 tech_list[idx]['fixed_cost'] = natgas_CCS_fixed_year2019; tech_list[idx]['var_cost'] = natgas_CCS_var_year2019
        if name == 'biopower':                                                                   tech_list[idx]['fixed_cost'] = biopower_fixed_year2019;   tech_list[idx]['var_cost'] = biopower_var_year2019
        if name == 'solar':      info_idx['solar_idx'] = idx;   info_idx['solar_flag'] = True;   tech_list[idx]['fixed_cost'] = solar_fixed_year2019
        if name == 'wind':       info_idx['wind_idx'] = idx;    info_idx['wind_flag'] = True;    tech_list[idx]['fixed_cost'] = wind_fixed_year2019
        if name == 'offwind':    info_idx['offwind_idx'] = idx; info_idx['offwind_flag'] = True; tech_list[idx]['fixed_cost'] = offwind_fixed_year2019[1]
        if name == 'nuclear':                                                                    tech_list[idx]['fixed_cost'] = nuclear_fixed_year2019
        if name == 'storage':                                                                    tech_list[idx]['fixed_cost'] = storage_fixed_year2019
        if name == 'geothermal':                                                                 tech_list[idx]['fixed_cost'] = geothermal_fixed_year2019
        if name == 'to_PGP':                                                                     PGP_flag = True; PGP_idx = idx; PGP_default = tech_list[idx]['fixed_cost']
        if name == 'from_PGP':                                                                   PGP_flag = True; ELE_idx = idx; ELE_default = tech_list[idx]['fixed_cost']
        if name == 'dac':                                                                        DAC_flag = True; DAC_idx = idx; DAC_default = tech_list[idx]['var_cost']
        if name == 'load_shift':                                                                 LSH_flag = True; LSH_idx = idx; LSH_default = tech_list[idx]['fixed_cost']
    co2_constraints_percentage = np.array([0])
    upper_co2_emissions = 8760 * 1 * co2_emis_natgas
    co2_constraints_list = upper_co2_emissions * co2_constraints_percentage / 100
    if PGP_flag == True: 
        for scale_idx in [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]:
            tech_list[PGP_idx]['fixed_cost'] = PGP_default * scale_idx
            tech_list[ELE_idx]['fixed_cost'] = ELE_default * scale_idx
            case_name_output = f'{case_name_default}_Scenarios2019_Allscale{str(scale_idx)}'
            pass_variables(single_year_index, case_dic, tech_list, co2_constraints_list, co2_constraints_percentage, case_name_output, info_idx)
    if DAC_flag == True:
        for scale_idx in [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01]:
            tech_list[DAC_idx]['var_cost'] = DAC_default * scale_idx
            case_name_output = f'{case_name_default}_Scenarios2019_scale{str(scale_idx)}'
            pass_variables(single_year_index, case_dic, tech_list, co2_constraints_list, co2_constraints_percentage, case_name_output, info_idx)
    if LSH_flag == True:
        for variable_cost_idx in [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]:
            tech_list[LSH_idx]['var_cost'] = variable_cost_idx
            for cap_idx in [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]:
                tech_list[LSH_idx]['capacity'] = cap_idx
                case_name_output = f'{case_name_default}_Scenarios2019_VcScale{str(variable_cost_idx)}_CapScale{str(cap_idx)}'
                pass_variables(single_year_index, case_dic, tech_list, co2_constraints_list, co2_constraints_percentage, case_name_output, info_idx)


def year2050_repeat(single_year_index, case_dic, tech_list, case_name_default, co2_emis_natgas, scenarios):
    info_idx = {}
    info_idx['solar_flag'  ] = False
    info_idx['wind_flag'   ] = False
    info_idx['offwind_flag'] = False

    PGP_flag = False
    DAC_flag = False
    LSH_flag = False

    natgas_fixed_year2050_NNN, natgas_var_year2050_NNN = 11.42601233 / 1000, 10 / 1000
    nuclear_fixed_year2050_NNN = 80.4239702 / 1000
    biopower_fixed_year2050_NNN, biopower_var_year2050_NNN = 49.8730133 / 1000, 48 / 1000
    if scenarios == 0:   # All low costs 
        natgas_CCS_fixed_year2050_NNN, natgas_CCS_var_year2050_NNN = 18.83942967 / 1000, 13 / 1000
        solar_fixed_year2050_NNN = 5.794755718 / 1000
        wind_fixed_year2050_NNN = 7.569390621 / 1000
        storage_fixed_year2050_NNN = 1.904751567 / 1000
        offwind_fixed_year2050_NNN = 25.08663768 / 1000
        geothermal_fixed_year2050_NNN = 57.24504862 / 1000
    if scenarios == 1:   # Low geothermal and high others
        natgas_CCS_fixed_year2050_NNN, natgas_CCS_var_year2050_NNN = 26.25118356 / 1000, 13 / 1000
        solar_fixed_year2050_NNN = 9.079343507 / 1000
        wind_fixed_year2050_NNN = 12.95979032 / 1000
        storage_fixed_year2050_NNN = 5.272872439 / 1000
        offwind_fixed_year2050_NNN = 42.91331596 / 1000
        geothermal_fixed_year2050_NNN = 57.24504862 / 1000
    if scenarios == 2:   # All high costs
        natgas_CCS_fixed_year2050_NNN, natgas_CCS_var_year2050_NNN = 26.25118356 / 1000, 13 / 1000
        solar_fixed_year2050_NNN = 9.079343507 / 1000
        wind_fixed_year2050_NNN = 12.95979032 / 1000
        storage_fixed_year2050_NNN = 5.272872439 / 1000
        offwind_fixed_year2050_NNN = 42.91331596 / 1000
        geothermal_fixed_year2050_NNN = 187.9210814 / 1000
    if scenarios == 3:   # Low wind and high others
        natgas_CCS_fixed_year2050_NNN, natgas_CCS_var_year2050_NNN = 26.25118356 / 1000, 13 / 1000
        solar_fixed_year2050_NNN = 9.079343507 / 1000
        wind_fixed_year2050_NNN = 7.569390621 / 1000
        storage_fixed_year2050_NNN = 5.272872439 / 1000
        offwind_fixed_year2050_NNN = 42.91331596 / 1000
        geothermal_fixed_year2050_NNN = 187.9210814 / 1000
    if scenarios == 4:   # Low wind, low geothermal, and high others
        natgas_CCS_fixed_year2050_NNN, natgas_CCS_var_year2050_NNN = 26.25118356 / 1000, 13 / 1000
        solar_fixed_year2050_NNN = 9.079343507 / 1000
        wind_fixed_year2050_NNN = 7.569390621 / 1000
        storage_fixed_year2050_NNN = 5.272872439 / 1000
        offwind_fixed_year2050_NNN = 42.91331596 / 1000
        geothermal_fixed_year2050_NNN = 57.24504862 / 1000

    for idx in range(len(tech_list)):
        name = tech_list[idx]['tech_name']
        if name == 'demand':     info_idx['demand_idx']  = idx
        if name == 'natgas':                                                                     tech_list[idx]['fixed_cost'] = natgas_fixed_year2050_NNN;     tech_list[idx]['var_cost'] = natgas_var_year2050_NNN
        if name == 'natgas_ccs':                                                                 tech_list[idx]['fixed_cost'] = natgas_CCS_fixed_year2050_NNN; tech_list[idx]['var_cost'] = natgas_CCS_var_year2050_NNN
        if name == 'biopower':                                                                   tech_list[idx]['fixed_cost'] = biopower_fixed_year2050_NNN;   tech_list[idx]['var_cost'] = biopower_var_year2050_NNN
        if name == 'solar':      info_idx['solar_idx'] = idx;   info_idx['solar_flag'] = True;   tech_list[idx]['fixed_cost'] = solar_fixed_year2050_NNN
        if name == 'wind':       info_idx['wind_idx'] = idx;    info_idx['wind_flag'] = True;    tech_list[idx]['fixed_cost'] = wind_fixed_year2050_NNN
        if name == 'offwind':    info_idx['offwind_idx'] = idx; info_idx['offwind_flag'] = True; tech_list[idx]['fixed_cost'] = offwind_fixed_year2050_NNN
        if name == 'nuclear':                                                                    tech_list[idx]['fixed_cost'] = nuclear_fixed_year2050_NNN
        if name == 'storage':                                                                    tech_list[idx]['fixed_cost'] = storage_fixed_year2050_NNN
        if name == 'geothermal':                                                                 tech_list[idx]['fixed_cost'] = geothermal_fixed_year2050_NNN
        if name == 'to_PGP':                                                                     PGP_flag = True; PGP_idx = idx; PGP_default = tech_list[idx]['fixed_cost']
        if name == 'from_PGP':                                                                   PGP_flag = True; ELE_idx = idx; ELE_default = tech_list[idx]['fixed_cost']
        if name == 'dac':                                                                        DAC_flag = True; DAC_idx = idx; DAC_default = tech_list[idx]['var_cost']
        if name == 'load_shift':                                                                 LSH_flag = True; LSH_idx = idx; LSH_default = tech_list[idx]['fixed_cost']
    co2_constraints_percentage = np.array([0])
    upper_co2_emissions = 8760 * 1 * co2_emis_natgas
    co2_constraints_list = upper_co2_emissions * co2_constraints_percentage / 100
    if PGP_flag == True: 
        for scale_idx in [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]:
            # tech_list[PGP_idx]['fixed_cost'] = PGP_default * scale_idx
            tech_list[ELE_idx]['fixed_cost'] = ELE_default * scale_idx
            case_name_output = f'{case_name_default}_Scenarios2050_sub{str(scenarios)}_Fromscale{str(scale_idx)}'
            pass_variables(single_year_index, case_dic, tech_list, co2_constraints_list, co2_constraints_percentage, case_name_output, info_idx)
    if DAC_flag == True:
        for scale_idx in [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01]:
            tech_list[DAC_idx]['var_cost'] = DAC_default * scale_idx
            case_name_output = f'{case_name_default}_Scenarios2050_sub{str(scenarios)}_scale{str(scale_idx)}'
            pass_variables(single_year_index, case_dic, tech_list, co2_constraints_list, co2_constraints_percentage, case_name_output, info_idx)
    if LSH_flag == True:
        for variable_cost_idx in [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]:
            tech_list[LSH_idx]['var_cost'] = variable_cost_idx
            for cap_idx in [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]:
                tech_list[LSH_idx]['capacity'] = cap_idx
                case_name_output = f'{case_name_default}_Scenarios2050_sub{str(scenarios)}_VcScale{str(variable_cost_idx)}_CapScale{str(cap_idx)}'
                pass_variables(single_year_index, case_dic, tech_list, co2_constraints_list, co2_constraints_percentage, case_name_output, info_idx)



def year2050_GeoRepeat(single_year_index, case_dic, tech_list, case_name_default, co2_emis_natgas, scenarios):

    info_idx = {}
    info_idx['solar_flag'  ] = False
    info_idx['wind_flag'   ] = False
    info_idx['offwind_flag'] = False

    natgas_fixed_year2050_NNN, natgas_var_year2050_NNN = 11.42601233 / 1000, 10 / 1000
    nuclear_fixed_year2050_NNN = 80.4239702 / 1000
    biopower_fixed_year2050_NNN, biopower_var_year2050_NNN = 49.8730133 / 1000, 48 / 1000
    if scenarios == 1:   # Low geothermal and high others
        natgas_CCS_fixed_year2050_NNN, natgas_CCS_var_year2050_NNN = 26.25118356 / 1000, 13 / 1000
        solar_fixed_year2050_NNN = 9.079343507 / 1000
        wind_fixed_year2050_NNN = 12.95979032 / 1000
        storage_fixed_year2050_NNN = 5.272872439 / 1000
        offwind_fixed_year2050_NNN = 42.91331596 / 1000
        geothermal_fixed_year2050_NNN = 57.24504862 / 1000

    for idx in range(len(tech_list)):
        name = tech_list[idx]['tech_name']
        if name == 'demand':     info_idx['demand_idx']  = idx
        if name == 'natgas':                                                                     tech_list[idx]['fixed_cost'] = natgas_fixed_year2050_NNN;     tech_list[idx]['var_cost'] = natgas_var_year2050_NNN
        if name == 'natgas_ccs':                                                                 tech_list[idx]['fixed_cost'] = natgas_CCS_fixed_year2050_NNN; tech_list[idx]['var_cost'] = natgas_CCS_var_year2050_NNN
        if name == 'biopower':                                                                   tech_list[idx]['fixed_cost'] = biopower_fixed_year2050_NNN;   tech_list[idx]['var_cost'] = biopower_var_year2050_NNN
        if name == 'solar':      info_idx['solar_idx'] = idx;   info_idx['solar_flag'] = True;   tech_list[idx]['fixed_cost'] = solar_fixed_year2050_NNN
        if name == 'wind':       info_idx['wind_idx'] = idx;    info_idx['wind_flag'] = True;    tech_list[idx]['fixed_cost'] = wind_fixed_year2050_NNN
        if name == 'offwind':    info_idx['offwind_idx'] = idx; info_idx['offwind_flag'] = True; tech_list[idx]['fixed_cost'] = offwind_fixed_year2050_NNN
        if name == 'nuclear':                                                                    tech_list[idx]['fixed_cost'] = nuclear_fixed_year2050_NNN
        if name == 'storage':                                                                    tech_list[idx]['fixed_cost'] = storage_fixed_year2050_NNN
        if name == 'geothermal':                                                                 tech_list[idx]['fixed_cost'] = geothermal_fixed_year2050_NNN;  info_idx['geo_idx'] = idx
        if name == 'to_PGP':                                                                     tech_list[idx]['fixed_cost'] = to_PGP_fixed_year2050_NNN
        if name == 'PGP_storage':                                                                tech_list[idx]['fixed_cost'] = PGP_storage_fixed_year2050_NNN
        if name == 'from_PGP':                                                                   tech_list[idx]['fixed_cost'] = from_PGP_fixed_year2050_NNN
    
    # geotherm_cap_constraint = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5])
    geotherm_cap_constraint = np.array([0])
    co2_constraints_percentage = np.array([10, 1, 0])
    upper_co2_emissions = 8760 * 1 * co2_emis_natgas
    co2_constraints_list = upper_co2_emissions * co2_constraints_percentage / 100
    for geo_cap_idx in geotherm_cap_constraint:
        tech_list[info_idx['geo_idx']]['max_capacity'] = geo_cap_idx
        case_name_output = f'{case_name_default}_GeoCapLimit{str(geo_cap_idx)}_Scenarios2050_sub{str(scenarios)}'
        pass_variables(single_year_index, case_dic, tech_list, co2_constraints_list, co2_constraints_percentage, case_name_output, info_idx)


###################################################################################################################################################################################


def pass_variables(single_year_index, 
                   case_dic,
                   tech_list,
                   co2_constraints_list,
                   co2_constraints_percentage,
                   case_name_output,
                   info_idx):

    if single_year_index == -1:
        for year_cycle_idx in range(3):
            year = 2016 + year_cycle_idx
            case_dic['year_start'] = year
            case_dic['year_end'] = year
            mean_demand = update_series(case_dic, tech_list[info_idx['demand_idx']])
            if info_idx['solar_flag'] == True:   mean_solar   = update_series(case_dic, tech_list[info_idx['solar_idx']])
            if info_idx['wind_flag'] == True:    mean_wind    = update_series(case_dic, tech_list[info_idx['wind_idx']])
            if info_idx['offwind_flag'] == True: mean_offwind = update_series(case_dic, tech_list[info_idx['offwind_idx']])
            for idx in range(len(co2_constraints_list)):
                case_dic['co2_constraint'] = co2_constraints_list[idx]
                case_dic['case_name'] = f'{case_name_output}_Year{str(year)}_Co2Con{str(co2_constraints_percentage[idx])}'
                run_model_main_fun(case_dic, tech_list) 
    
    elif single_year_index != -1 and single_year_index > 0:
        case_dic['year_start'] = single_year_index
        case_dic['year_end'] = single_year_index
        mean_demand = update_series(case_dic, tech_list[info_idx['demand_idx']])
        if info_idx['solar_flag'] == True:   mean_solar   = update_series(case_dic, tech_list[info_idx['solar_idx']])
        if info_idx['wind_flag'] == True:    mean_wind    = update_series(case_dic, tech_list[info_idx['wind_idx']])
        if info_idx['offwind_flag'] == True: mean_offwind = update_series(case_dic, tech_list[info_idx['offwind_idx']])
        for idx in range(len(co2_constraints_list)):
            case_dic['co2_constraint'] = co2_constraints_list[idx]
            case_dic['case_name'] = f'{case_name_output}_Year{str(single_year_index)}_Co2Con{str(co2_constraints_percentage[idx])}'
            run_model_main_fun(case_dic, tech_list) 
    
    else:
        print('error of input year') 
        sys.exit() 
        
###################################################################################################################################################################################