import numpy as np
import pickle, os
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


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
to_PGP_fixed_year2019 = 0.0148
PGP_storage_fixed_year2019 = 0.001471898 / 1000
from_PGP_fixed_year2019 = 0.063
to_PGP_fixed_year2050 = [3.87690982 / 1000, 10.41583661 / 1000, 16.95475499 / 1000]
PGP_storage_fixed_year2050 = 0.001471898 / 1000
from_PGP_fixed_year2050 = 8.975948304 / 1000 

color_colors = {'natgas': 'black', 'natgas_ccs': 'grey', 'biopower': 'lightslategrey', 
                'solar': 'wheat', 'wind': 'skyblue', 'offwind': 'darkblue', 
                'nuclear': 'tomato', 'geothermal': 'darkred', 
                'storage': 'lightpink', 'pgp': 'lightgreen'} 


def fig_order3_cost_uncertainty():

    def cost_uncertainty(table_in, name):
        cap_dict = {}
        cap_dict['natgas_cap']     = np.array(table_in['natgas_cap']).astype('float')
        cap_dict['natgas_ccs_cap'] = np.array(table_in['natgas_ccs_cap']).astype('float')
        cap_dict['solar_cap']      = np.array(table_in['solar_cap']).astype('float')
        cap_dict['wind_cap']       = np.array(table_in['wind_cap']).astype('float')
        cap_dict['offwind_cap']    = np.array(table_in['offwind_cap']).astype('float')
        cap_dict['geothermal_cap'] = np.array(table_in['geothermal_cap']).astype('float')
        cap_dict['biopower_cap']   = np.array(table_in['biopower_cap']).astype('float')
        cap_dict['storage_cap']    = np.array(table_in['storage_cap']).astype('float')
        ##### Get original system costs and other costs
        system_cost = np.array(table_in['system_cost']).astype('float')
        nuclear_fix = np.array(table_in['nuclear_fix']).astype('float')
        natgas_tot = np.array(table_in['natgas_tot']).astype('float')
        natgas_ccs_rest = np.array(table_in['natgas_ccs_var']).astype('float') + np.array(table_in['natgas_ccs_tax']).astype('float')
        biopower_tot = np.array(table_in['biopower_tot']).astype('float')
        ##### Now calculate uncertainties
        total_ensemble = len(system_cost)
        cost_posibility = np.zeros([total_ensemble, total_ensemble])  # (all cost combinations, all ensemble members)
        count = 0
        for natgas_CCS_fixed_year2050_idx in natgas_CCS_fixed_year2050:
            for solar_fixed_year2050_idx in solar_fixed_year2050:
                for wind_fixed_year2050_idx in wind_fixed_year2050:
                    for storage_fixed_year2050_idx in storage_fixed_year2050:
                        for offwind_fixed_year2050_idx in offwind_fixed_year2050:
                            for geothermal_fixed_year2050_idx in geothermal_fixed_year2050:
                                system_cost_idx = natgas_tot + \
                                                  cap_dict['natgas_ccs_cap'] * natgas_CCS_fixed_year2050_idx + natgas_ccs_rest + \
                                                  cap_dict['solar_cap'] * solar_fixed_year2050_idx + \
                                                  cap_dict['wind_cap'] * wind_fixed_year2050_idx + \
                                                  nuclear_fix + \
                                                  cap_dict['offwind_cap'] * offwind_fixed_year2050_idx + \
                                                  cap_dict['geothermal_cap'] * geothermal_fixed_year2050_idx + \
                                                  biopower_tot + \
                                                  cap_dict['storage_cap'] * storage_fixed_year2050_idx
                                cost_posibility[count] = system_cost_idx
                                count += 1
        ##### Now calculate extreme cases
        info_cont = {}
        info_cont['natgas_CCS_contribute'] = cap_dict['natgas_ccs_cap'] * ( natgas_CCS_fixed_year2050[-1] - natgas_CCS_fixed_year2050[0] ) + natgas_ccs_rest
        info_cont['solar_contribute'] = cap_dict['solar_cap'] * ( solar_fixed_year2050[-1] - solar_fixed_year2050[0] )
        info_cont['wind_contribute'] = cap_dict['wind_cap'] * ( wind_fixed_year2050[-1] - wind_fixed_year2050[0] )
        info_cont['offwind_contribute'] = cap_dict['offwind_cap'] * ( offwind_fixed_year2050[-1] - offwind_fixed_year2050[0] )
        info_cont['geothermal_contribute'] = cap_dict['geothermal_cap'] * ( geothermal_fixed_year2050[-1] - geothermal_fixed_year2050[0] )
        info_cont['storage_contribute'] = cap_dict['storage_cap'] * ( storage_fixed_year2050[-1] - storage_fixed_year2050[0] )
        return cost_posibility, system_cost, cap_dict, info_cont
    tech_list2 = ['natgas', 'natgas_ccs', 'biopower', 'solar', 'wind', 'offwind', 'nuclear', 'geothermal', 'storage'] # 0 - 728
    
    with open('Cost_Uncertainty_Scenario2050.pickle', 'rb') as handle:
        Table_scenario2050_Full = pickle.load(handle)  #[100p, 99p]
    cost_possibility, system_cost, cap_dict, info_cont = cost_uncertainty(Table_scenario2050_Full[0], '')

    
    
    #### To look for:
    #### (1) change in capacity of different technologies;
    #### (2) Contributions of different technoloiges to difference in system costs (use two extreme cases);
    #### (3) Then we can find: (a) why lowest does not change very much; (b) what contributes to those differences. 
    mean = np.average( np.array(cost_possibility) , axis=0)
    std = np.std( np.array(cost_possibility), axis=0)
    # #### Case 1
    # ax1 = plt.subplot(121)
    # ax1.scatter(mean, std, s=1)
    # ax1.set_ylim(0, 0.06)
    # #### Case 2
    # system_cost_diff = np.array(np.max(cost_possibility, axis=0)) - np.array(np.min(cost_possibility, axis=0))
    # arg_sort = np.argsort(system_cost_diff)[::3]
    # total_number = len(arg_sort) 
    # ax2 = plt.subplot(122)
    # ax2.stackplot(np.arange(total_number), 
    #               [info_cont['solar_contribute'][arg_sort],
    #                info_cont['wind_contribute'][arg_sort],
    #                info_cont['offwind_contribute'][arg_sort],
    #                info_cont['geothermal_contribute'][arg_sort],
    #                info_cont['storage_contribute'][arg_sort]],
    #              colors = ['wheat', 'skyblue', 'darkblue', 'darkred', 'lightpink'])
    # ax2.set_xlim(0, 242)
    # ax2.set_ylim(0, 0.14)
    # plt.show() 
    # # plt.savefig('cost_uncertainty.ps') 
    # plt.clf()

    #### Case 2, define cost of regret 
    cost_of_regret = np.copy(cost_possibility)
    for idx in range(729):
        cost_of_regret[idx] = cost_possibility[idx] - system_cost
    new_mean = np.average( np.array(cost_of_regret) , axis=0)
    new_std = np.std( np.array(cost_of_regret), axis=0)

    ax1 = plt.subplot(121)
    ax1.scatter(new_mean, new_std, s=1)
    ax1.set_ylim(10**-3, 10**-1)
    ax1.set_yscale('log', basey=10)
    # plt.show() 
    # # plt.savefig('cost_uncertainty.ps') 
    # plt.clf()
    system_cost_diff = np.array(np.max(cost_of_regret, axis=0)) - np.array(np.min(cost_of_regret, axis=0))
    arg_sort = np.argsort(system_cost_diff)[::3]
    total_number = len(arg_sort) 
    ax2 = plt.subplot(122)
    ax2.stackplot(np.arange(total_number), 
                  [info_cont['solar_contribute'][arg_sort],
                   info_cont['wind_contribute'][arg_sort],
                   info_cont['offwind_contribute'][arg_sort],
                   info_cont['geothermal_contribute'][arg_sort],
                   info_cont['storage_contribute'][arg_sort]],
                 colors = ['wheat', 'skyblue', 'darkblue', 'darkred', 'lightpink'])
    ax2.set_xlim(0, 242)
    ax2.set_ylim(0, 0.14)
    # plt.show() 
    plt.savefig('cost_of_regret.ps') 
    plt.clf()


    # #### Case 3, check cap
    # system_cost_diff = np.array(np.max(cost_possibility, axis=0)) - np.array(np.min(cost_possibility, axis=0))
    # arg_sort = np.argsort(system_cost_diff)[::3]
    # total_number = len(arg_sort) 
    # ax1 = plt.subplot(111)
    # ax1.plot(np.arange(total_number), cap_dict['solar_cap'][arg_sort], color='wheat')
    # ax1.plot(np.arange(total_number), cap_dict['wind_cap'][arg_sort], color='skyblue')
    # ax1.plot(np.arange(total_number), cap_dict['offwind_cap'][arg_sort], color='darkblue')
    # ax1.plot(np.arange(total_number), cap_dict['geothermal_cap'][arg_sort], color='darkred')
    # ax1.plot(np.arange(total_number), cap_dict['storage_cap'][arg_sort], color='lightpink')
    # ax1.set_xlim(0, 242)
    # ax1.set_ylim(0, 9)
    # plt.show()
    # plt.clf()




