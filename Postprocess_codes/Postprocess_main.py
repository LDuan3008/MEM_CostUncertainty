
import numpy as np
import pickle, os
from Postprocess_func import Get_Table



def get_all_tables(tech_list, case_name):

    data_find = '/data/carnegie/leiduan/cesm_archive/MEM_CostUncertainty/save_year2050/'
    file_list = os.listdir(data_find)

    list_1e24, list_50, list_20, list_10, list_1, list_0 = [], [], [], [], [], []
    count = 0
    for file in file_list:
        split_file_name = file.split('_')
        case_mixture = split_file_name[1]
        if case_mixture == case_name and str(file[-5:]) == '1e+24':
            count += 1
            list_1e24.append(file)
            new_name_50 = file[:-5] + '50.0'; list_50.append(new_name_50)
            new_name_20 = file[:-5] + '20.0'; list_20.append(new_name_20)
            new_name_10 = file[:-5] + '10.0'; list_10.append(new_name_10)
            new_name_1 = file[:-5] + '1.0'; list_1.append(new_name_1)
            new_name_0 = file[:-5] + '0.0'; list_0.append(new_name_0)
    print (count)

    Table_1e24, Table_50, Table_20, Table_10, Table_1, Table_0 = [], [], [], [], [], []
    for idx in range(len(list_1e24)):
        print (idx)
        fname1 = list_1e24[idx]; Table_1e24 += [Get_Table(fname1, data_path=data_find, tech_name_list = tech_list)] 
        fname2 = list_50[idx];   Table_50   += [Get_Table(fname2, data_path=data_find, tech_name_list = tech_list)] 
        fname3 = list_20[idx];   Table_20   += [Get_Table(fname3, data_path=data_find, tech_name_list = tech_list)] 
        fname4 = list_10[idx];   Table_10   += [Get_Table(fname4, data_path=data_find, tech_name_list = tech_list)] 
        fname5 = list_1[idx];    Table_1    += [Get_Table(fname5, data_path=data_find, tech_name_list = tech_list)] 
        fname6 = list_0[idx];    Table_0    += [Get_Table(fname6, data_path=data_find, tech_name_list = tech_list)] 
    return Table_1e24, Table_50, Table_20, Table_10, Table_1, Table_0



if __name__ == "__main__":


    #########################################################################################################################################################
    
    """ 
    # Get Year-2019 simulation results
    data_find = '/data/carnegie/leiduan/cesm_archive/MEM_CostUncertainty/Folder_2019/'
    co2_constraints_percentage = np.array([1e24, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0])
    Table_scenario2019_Full = []
    Table_scenario2019_Full_PGP = []
    Table_scenario2019_Less = []
    Table_scenario2019_Less_PGP = []
    for year in np.arange(2016, 2020, 1):
        case_name_Full = f'NgCcsSoWiStNuOwGeBi_Scenarios2019_Year{str(year)}_Co2Con'
        tech_list_Full = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'nuclear', 'offwind', 'geothermal', 'biopower']
        Table_scenario2019_Full += [Get_Table(case_name_Full, data_path=data_find, tech_name_list = tech_list_Full, repeat_list=co2_constraints_percentage)] 
        case_name_Full_PGP = f'NgCcsSoWiStNuOwGeBiPgp_Scenarios2019_Year{str(year)}_Co2Con'
        tech_list_Full_PGP = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'nuclear', 'offwind', 'geothermal', 'biopower', 'pgp']
        Table_scenario2019_Full_PGP += [Get_Table(case_name_Full_PGP, data_path=data_find, tech_name_list = tech_list_Full_PGP, repeat_list=co2_constraints_percentage)] 
        case_name_Less = f'NgCcsSoWiStNu_Scenarios2019_Year{str(year)}_Co2Con'
        tech_list_Less = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'nuclear']
        Table_scenario2019_Less += [Get_Table(case_name_Less, data_path=data_find, tech_name_list = tech_list_Less, repeat_list=co2_constraints_percentage)] 
        case_name_Less_PGP = f'NgCcsSoWiStNuPgp_Scenarios2019_Year{str(year)}_Co2Con'
        tech_list_Less_PGP = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'nuclear', 'pgp']
        Table_scenario2019_Less_PGP += [Get_Table(case_name_Less_PGP, data_path=data_find, tech_name_list = tech_list_Less_PGP, repeat_list=co2_constraints_percentage)] 
    with open('Cost_Uncertainty_Scenario2019.pickle', 'wb') as handle:
        pickle.dump([Table_scenario2019_Full, Table_scenario2019_Full_PGP, Table_scenario2019_Less, Table_scenario2019_Less_PGP], handle, protocol=pickle.HIGHEST_PROTOCOL) 
    # """ 




    """ 
    # Get Year-2050 ensemble simulation results
    data_find = '/data/carnegie/leiduan/cesm_archive/MEM_CostUncertainty/Folder_2050/'
    Table_scenario2050_Full = []
    def get_ensemble_full(table, fname):
        tech_list = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'nuclear', 'offwind', 'geothermal', 'biopower'] # 0 - 728
        table += [Get_Table(fname, data_path=data_find, tech_name_list = tech_list, repeat_list=np.arange(729), dividing_name_point=len('NgCcsSoWiStNuOwGeBi_Scenarios2050_'))] 
    case_name_Full_100p = f'NgCcsSoWiStNuOwGeBi_Scenarios2050__Year2019_Co2Con0.0'
    get_ensemble_full(Table_scenario2050_Full, case_name_Full_100p)
    case_name_Full_99p = f'NgCcsSoWiStNuOwGeBi_Scenarios2050__Year2019_Co2Con1.0'
    get_ensemble_full(Table_scenario2050_Full, case_name_Full_99p)
    with open('Cost_Uncertainty_Scenario2050.pickle', 'wb') as handle:
        pickle.dump(Table_scenario2050_Full, handle, protocol=pickle.HIGHEST_PROTOCOL) 
    # """ 




    # """ 
    # Get Year-2050 specific simulation results
    data_find = '/data/carnegie/leiduan/cesm_archive/MEM_CostUncertainty/Folder_2050/'
    co2_constraints_percentage = np.array([1e24, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0])
    Table_Scenario2050_Full_sub0_AllL = []
    Table_Scenario2050_Full_sub1_GeoL = []
    Table_Scenario2050_Full_sub2_AllH = []
    tech_list1 = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'nuclear', 'offwind', 'geothermal', 'biopower']
    for year in np.arange(2016, 2020, 1):
        case_name1 = f'NgCcsSoWiStNuOwGeBi_Scenarios2050_highPGP_sub0_Year{str(year)}_Co2Con'
        Table_Scenario2050_Full_sub0_AllL += [Get_Table(case_name1, data_path=data_find, tech_name_list = tech_list1, repeat_list=co2_constraints_percentage)] 
        case_name2 = f'NgCcsSoWiStNuOwGeBi_Scenarios2050_highPGP_sub1_Year{str(year)}_Co2Con'
        Table_Scenario2050_Full_sub1_GeoL += [Get_Table(case_name2, data_path=data_find, tech_name_list = tech_list1, repeat_list=co2_constraints_percentage)] 
        case_name3 = f'NgCcsSoWiStNuOwGeBi_Scenarios2050_highPGP_sub2_Year{str(year)}_Co2Con'
        Table_Scenario2050_Full_sub2_AllH += [Get_Table(case_name3, data_path=data_find, tech_name_list = tech_list1, repeat_list=co2_constraints_percentage)] 
    Table_Scenario2050_Full_sub0_AllL_PGP = []
    Table_Scenario2050_Full_sub1_GeoL_PGP = []
    Table_Scenario2050_Full_sub2_AllH_PGP = []
    tech_list2 = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'nuclear', 'offwind', 'geothermal', 'biopower', 'pgp']
    year = 2019
    case_name4 = f'NgCcsSoWiStNuOwGeBiPgp_Scenarios2050_highPGP_sub0_Year{str(year)}_Co2Con'
    Table_Scenario2050_Full_sub0_AllL_PGP += [Get_Table(case_name4, data_path=data_find, tech_name_list = tech_list2, repeat_list=co2_constraints_percentage)] 
    case_name5 = f'NgCcsSoWiStNuOwGeBiPgp_Scenarios2050_highPGP_sub1_Year{str(year)}_Co2Con'
    Table_Scenario2050_Full_sub1_GeoL_PGP += [Get_Table(case_name5, data_path=data_find, tech_name_list = tech_list2, repeat_list=co2_constraints_percentage)] 
    case_name6 = f'NgCcsSoWiStNuOwGeBiPgp_Scenarios2050_highPGP_sub2_Year{str(year)}_Co2Con'
    Table_Scenario2050_Full_sub2_AllH_PGP += [Get_Table(case_name6, data_path=data_find, tech_name_list = tech_list2, repeat_list=co2_constraints_percentage)] 
    with open('Cost_Uncertainty_Scenario2050_spe.pickle', 'wb') as handle:
        pickle.dump([Table_Scenario2050_Full_sub0_AllL, Table_Scenario2050_Full_sub1_GeoL, Table_Scenario2050_Full_sub2_AllH], handle, protocol=pickle.HIGHEST_PROTOCOL) 
    with open('Cost_Uncertainty_Scenario2050_PGP_spe.pickle', 'wb') as handle:
        pickle.dump([Table_Scenario2050_Full_sub0_AllL_PGP, Table_Scenario2050_Full_sub1_GeoL_PGP, Table_Scenario2050_Full_sub2_AllH_PGP], handle, protocol=pickle.HIGHEST_PROTOCOL) 
    # """ 




    """ 
    Table_Scenario2050_Full_sub0_AllL_PGP = []
    Table_Scenario2050_Full_sub1_GeoL_PGP = []
    Table_Scenario2050_Full_sub2_AllH_PGP = []
    tech_list2 = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'nuclear', 'offwind', 'geothermal', 'biopower', 'pgp']
    year = 2019
    case_name4 = f'NgCcsSoWiStNuOwGeBiPgp_Scenarios2050_highPGP_sub0_Year{str(year)}_Co2Con'
    Table_Scenario2050_Full_sub0_AllL_PGP += [Get_Table(case_name4, data_path=data_find, tech_name_list = tech_list2, repeat_list=co2_constraints_percentage)] 
    case_name5 = f'NgCcsSoWiStNuOwGeBiPgp_Scenarios2050_highPGP_sub1_Year{str(year)}_Co2Con'
    Table_Scenario2050_Full_sub1_GeoL_PGP += [Get_Table(case_name5, data_path=data_find, tech_name_list = tech_list2, repeat_list=co2_constraints_percentage)] 
    case_name6 = f'NgCcsSoWiStNuOwGeBiPgp_Scenarios2050_highPGP_sub2_Year{str(year)}_Co2Con'
    Table_Scenario2050_Full_sub2_AllH_PGP += [Get_Table(case_name6, data_path=data_find, tech_name_list = tech_list2, repeat_list=co2_constraints_percentage)] 
    # """ 
