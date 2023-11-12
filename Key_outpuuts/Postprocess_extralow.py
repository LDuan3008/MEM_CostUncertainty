import os
import pickle

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from scipy import stats

color_colors = {'natgas': 'black', 'natgas_ccs': 'grey', 'biopower': 'lightslategrey', 
                'solar': 'wheat', 'wind': 'skyblue', 'offwind': 'darkblue', 
                'nuclear': 'tomato', 'geothermal': 'darkred', 
                'storage': 'lightpink', 'pgp': 'lightgreen'} 




""" 

def system_cost_distribution(table_in, table_in_dispatch):

    tech_list_Full = ['solar', 'wind', 'offwind', 'geothermal', 'storage']
    system_cost = np.array(table_in['system_cost'])
    cost_tables = table_in['cost']

    # for tech_idx in tech_list_Full:
    #     tech_cap = np.array(table_in[tech_idx+'_cap'])
    #     tech_fixed_cost = np.array(cost_tables[tech_idx+'_fix'])
    #     tech_fixed_cost_unique = np.unique(tech_fixed_cost)
    #     if len(tech_fixed_cost_unique) == 3: 
    #         list_1, list_2, list_3 = [], [], []
    #         for idx in range(len(tech_fixed_cost)): 
    #             if tech_fixed_cost[idx] == tech_fixed_cost_unique[0]: list_1.append(system_cost[idx])
    #             if tech_fixed_cost[idx] == tech_fixed_cost_unique[1]: list_2.append(system_cost[idx])
    #             if tech_fixed_cost[idx] == tech_fixed_cost_unique[2]: list_3.append(system_cost[idx])
    #     ax1 = plt.subplot(111)
    #     x_axis = np.arange(0.00, 0.071, 0.001)
    #     try:
    #         kde_L = st.gaussian_kde(list_1); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_L.pdf(x_axis)*0.001, facecolor='#fdf289', edgecolor='#fdf289', linestyle='--', linewidth=0.8, alpha=0.5, label='L')
    #     except:
    #         print ('no L')
    #     try:
    #         kde_M = st.gaussian_kde(list_2); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_M.pdf(x_axis)*0.001, facecolor='#46edc8', edgecolor='#46edc8', linestyle='--', linewidth=0.8, alpha=0.5, label='M')
    #     except:
    #         print ('no M')
    #     try:
    #         kde_H = st.gaussian_kde(list_3); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_H.pdf(x_axis)*0.001, facecolor='#374d7c', edgecolor='#374d7c', linestyle='--', linewidth=0.8, alpha=0.5, label='H')
    #     except:
    #         print ('no H')
    #     ax1.set_xlim(0.00, 0.07)
    #     ax1.set_ylim(0, 0.16)
    #     # plt.show() 
    #     plt.savefig('panel1_' + str(tech_idx) + '.ps') 
    #     plt.clf() 

    for tech_idx in tech_list_Full:
        tech_cap = np.array(table_in[tech_idx+'_cap'])
        tech_fixed_cost = np.array(cost_tables[tech_idx+'_fix'])
        tech_fixed_cost_unique = np.unique(tech_fixed_cost)
        dispatch_list_1, dispatch_list_2, dispatch_list_3 = [], [], []
        for idx in range(242):
            try:
                dispatch_tech = table_in_dispatch[idx][tech_idx+'_dispatch']
            except:
                dispatch_tech = table_in_dispatch[idx][tech_idx+'_potential']
            if tech_fixed_cost[idx] == tech_fixed_cost_unique[0]: dispatch_list_1.append(dispatch_tech)
            if tech_fixed_cost[idx] == tech_fixed_cost_unique[1]: dispatch_list_2.append(dispatch_tech)
            if tech_fixed_cost[idx] == tech_fixed_cost_unique[2]: dispatch_list_3.append(dispatch_tech)
        ax1 = plt.subplot(111)
        x_axis = np.arange(0.00, 3, 0.1)
        try:
            kde_L = st.gaussian_kde(dispatch_list_1); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_L.pdf(x_axis)*0.1, facecolor='#fdf289', edgecolor='#fdf289', linestyle='--', linewidth=0.8, alpha=0.5, label='L')
        except:
            print ('no L')
        try:
            kde_M = st.gaussian_kde(dispatch_list_2); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_M.pdf(x_axis)*0.1, facecolor='#46edc8', edgecolor='#46edc8', linestyle='--', linewidth=0.8, alpha=0.5, label='M')
        except:
            print ('no M')
        try:
            kde_H = st.gaussian_kde(dispatch_list_3); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_H.pdf(x_axis)*0.1, facecolor='#374d7c', edgecolor='#374d7c', linestyle='--', linewidth=0.8, alpha=0.5, label='H')
        except:
            print ('no H')
        ax1.set_xlim(0, 3)
        ax1.set_ylim(0, 1)
        # plt.show() 
        plt.savefig('panel2_' + str(tech_idx) + '.ps') 
        plt.clf() 

with open('Cost_Uncertainty_Scenario2050_ExtraLow.pickle', 'rb') as handle:
    Table_scenario2050_ExtraLow = pickle.load(handle)  #[100p]
with open('Cost_Uncertainty_dispatch_ExtraLow.pickle', 'rb') as handle:
    Table_scenario2050_ExtraLow_dispatch = pickle.load(handle) 
system_cost_distribution(Table_scenario2050_ExtraLow[0], Table_scenario2050_ExtraLow_dispatch[0])

# """




# """

###################################################################################################################################################################################
# Define costs here:
# Year-2050
nuclear_fixed_year2050 = 80.4239702 / 1000
offwind_fixed_year2050 = [25.08663768 / 1000, 30.61419606 / 1000, 42.91331596 / 1000]
geothermal_fixed_year2050 = [57.24504862 / 1000, 136.349483 / 1000, 187.9210814 / 1000]
biopower_fixed_year2050, biopower_var_year2050 = 49.8730133 / 1000, 48 / 1000


solar_fixed_year2050_1   = [5.794755718 / 1000, 7.581521169 / 1000, 9.079343507 / 1000]
wind_fixed_year2050_1    = [7.569390621 / 1000, 10.75863775 / 1000, 12.95979032 / 1000]
storage_fixed_year2050_1 = [1.904751567 / 1000, 2.990759329 / 1000, 5.272872439 / 1000]

solar_fixed_year2050_2   = [5.794755718 / 1000 * 0.3, 5.794755718 / 1000 * 0.5, 5.794755718 / 1000 * 0.7]
wind_fixed_year2050_2    = [7.569390621 / 1000 * 0.3, 7.569390621 / 1000 * 0.5, 7.569390621 / 1000 * 0.7]
storage_fixed_year2050_2 = [1.904751567 / 1000 * 0.3, 1.904751567 / 1000 * 0.5, 1.904751567 / 1000 * 0.7]

solar_fixed_year2050_3   = [5.794755718 / 1000 * 0.3, 5.794755718 / 1000 * 0.5, 5.794755718 / 1000 * 0.7, 5.794755718 / 1000, 7.581521169 / 1000, 9.079343507 / 1000]
wind_fixed_year2050_3    = [7.569390621 / 1000 * 0.3, 7.569390621 / 1000 * 0.5, 7.569390621 / 1000 * 0.7, 7.569390621 / 1000, 10.75863775 / 1000, 12.95979032 / 1000]
storage_fixed_year2050_3 = [1.904751567 / 1000 * 0.3, 1.904751567 / 1000 * 0.5, 1.904751567 / 1000 * 0.7, 1.904751567 / 1000, 2.990759329 / 1000, 5.272872439 / 1000]


color_colors = {'natgas': 'black', 'natgas_ccs': 'grey', 'biopower': 'lightslategrey', 
                'solar': 'wheat', 'wind': 'skyblue', 'offwind': 'darkblue', 
                'nuclear': 'tomato', 'geothermal': 'darkred', 
                'storage': 'lightpink', 'pgp': 'lightgreen'} 


def cost_uncertainty(table_in1, table_in2, name):

    cap_dict = {}
    cap_dict['solar_cap']      = np.r_[np.array(table_in1['solar_cap']).astype('float'), np.array(table_in2['solar_cap']).astype('float')]
    cap_dict['wind_cap']       = np.r_[np.array(table_in1['wind_cap']).astype('float'), np.array(table_in2['wind_cap']).astype('float')]
    cap_dict['offwind_cap']    = np.r_[np.array(table_in1['offwind_cap']).astype('float'), np.array(table_in2['offwind_cap']).astype('float')]
    cap_dict['geothermal_cap'] = np.r_[np.array(table_in1['geothermal_cap']).astype('float'), np.array(table_in2['geothermal_cap']).astype('float')]
    cap_dict['biopower_cap']   = np.r_[np.array(table_in1['biopower_cap']).astype('float'), np.array(table_in2['biopower_cap']).astype('float')]
    cap_dict['storage_cap']    = np.r_[np.array(table_in1['storage_cap']).astype('float'), np.array(table_in2['storage_cap']).astype('float')]

    ##### Get original system costs and other costs
    system_cost   = np.r_[np.array(table_in1['system_cost']).astype('float'), np.array(table_in2['system_cost']).astype('float')]
    nuclear_fix   = np.r_[np.array(table_in1['nuclear_fix']).astype('float'), np.array(table_in2['nuclear_fix']).astype('float')]
    biopower_tot  = np.r_[np.array(table_in1['biopower_tot']).astype('float'), np.array(table_in2['biopower_tot']).astype('float')]

    ##### Now calculate uncertainties
    total_ensemble = len(system_cost)
    cost_posibility = np.zeros([6*6*6*3*3*3, 3**6+3**5])  # (all cost combinations, )
    count = 0
    for solar_fixed_year2050_idx in solar_fixed_year2050_3:
        for wind_fixed_year2050_idx in wind_fixed_year2050_3:
            for storage_fixed_year2050_idx in storage_fixed_year2050_3:
                for offwind_fixed_year2050_idx in offwind_fixed_year2050:
                    for geothermal_fixed_year2050_idx in geothermal_fixed_year2050:
                        system_cost_idx = cap_dict['solar_cap'] * solar_fixed_year2050_idx + \
                                            cap_dict['wind_cap'] * wind_fixed_year2050_idx + \
                                            nuclear_fix + \
                                            cap_dict['offwind_cap'] * offwind_fixed_year2050_idx + \
                                            cap_dict['geothermal_cap'] * geothermal_fixed_year2050_idx + \
                                            biopower_tot + \
                                            cap_dict['storage_cap'] * storage_fixed_year2050_idx
                        cost_posibility[count] = system_cost_idx
                        count += 1

    # ##### Now calculate extreme cases
    # info_cont = {}
    # info_cont['solar_contribute'] = cap_dict['solar_cap'] * ( solar_fixed_year2050[-1] - solar_fixed_year2050[0] )
    # info_cont['wind_contribute'] = cap_dict['wind_cap'] * ( wind_fixed_year2050[-1] - wind_fixed_year2050[0] )
    # info_cont['offwind_contribute'] = cap_dict['offwind_cap'] * ( offwind_fixed_year2050[-1] - offwind_fixed_year2050[0] )
    # info_cont['geothermal_contribute'] = cap_dict['geothermal_cap'] * ( geothermal_fixed_year2050[-1] - geothermal_fixed_year2050[0] )
    # info_cont['storage_contribute'] = cap_dict['storage_cap'] * ( storage_fixed_year2050[-1] - storage_fixed_year2050[0] )
    
    return cost_posibility, system_cost, cap_dict #, info_cont


tech_list2 = ['biopower', 'solar', 'wind', 'offwind', 'nuclear', 'geothermal', 'storage'] 
with open('Cost_Uncertainty_Scenario2050.pickle', 'rb') as handle:
    Table_scenario2050_Full = pickle.load(handle)  #[100p, 99p]
with open('Cost_Uncertainty_Scenario2050_ExtraLow.pickle', 'rb') as handle:
    Table_scenario2050_ExtraLow = pickle.load(handle)  #[100p]
# cost_possibility, system_cost, cap_dict, info_cont = cost_uncertainty(Table_scenario2050_Full[0], Table_scenario2050_ExtraLow[0], '')
cost_possibility, system_cost, cap_dict = cost_uncertainty(Table_scenario2050_Full[0], Table_scenario2050_ExtraLow[0], '')


#### To look for:
#### (1) change in capacity of different technologies;
#### (2) Contributions of different technoloiges to difference in system costs (use two extreme cases);
#### (3) Then we can find: (a) why lowest does not change very much; (b) what contributes to those differences. 
mean = np.average( np.array(cost_possibility) , axis=0)
std = np.std( np.array(cost_possibility), axis=0)

#### Case 1
ax1 = plt.subplot(111)
ax1.scatter(mean, std, s=1)
ax1.set_xlim(0.02, 0.05)
ax1.set_ylim(0, 0.08)
# plt.show() 
plt.savefig('cost_uncertainty.ps') 
plt.clf()

# """