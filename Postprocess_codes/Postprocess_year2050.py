import numpy as np
import pickle, os
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors



if __name__ == "__main__":
    
    #######################################################################################################################
    # ### Order 1, Select specific cases and plot changes in co2 constraints
    # from Fig_order1 import fig_order1_no_PGP;      fig_order1_no_PGP()
    # from Fig_order1 import fig_order1_with_PGP;    fig_order1_with_PGP()
    from Fig_order1 import fig_order1_dispatch;    fig_order1_dispatch()

    ### Order 2, year-2050, 100p/99p/80p emission reduction, distribution 
    # from Fig_order2 import fig_order2_systemcost;    fig_order2_systemcost()
    # from Fig_order2 import fig_order2_his;           fig_order2_his()
    # from Fig_order2 import fig_order2_dispatch;      fig_order2_dispatch()

    ### Order 3, year-2050, what if low cost confidence
    # from Fig_order3 import fig_order3_cost_uncertainty;   fig_order3_cost_uncertainty()






    """
    # Table 1
    # Year-2019
    natgas_fixed_year2019, natgas_var_year2019 = [12.77831841 / 1000], 10 / 1000
    natgas_CCS_fixed_year2019, natgas_CCS_var_year2019 = [31.98238555 / 1000], 14 / 1000
    solar_fixed_year2019 = [15.42188211 / 1000]
    wind_fixed_year2019 = [18.11895838 / 1000]
    nuclear_fixed_year2019 = [93.51739145 / 1000]
    storage_fixed_year2019 = [7.744342599 / 1000]
    offwind_fixed_year2019 = [57.15517459 / 1000]
    geothermal_fixed_year2019 = [214.3692446 / 1000]
    biopower_fixed_year2019, biopower_var_year2019 = [57.10371115 / 1000], 48 / 1000
    # Year-2050
    natgas_fixed_year2050, natgas_var_year2050 = [11.42601233 / 1000], 10 / 1000
    natgas_CCS_fixed_year2050, natgas_CCS_var_year2050 = [18.83942967 / 1000, 22.48822899 / 1000, 26.25118356 / 1000], 13 / 1000
    solar_fixed_year2050 = [5.794755718 / 1000, 7.581521169 / 1000, 9.079343507 / 1000]
    wind_fixed_year2050 = [7.569390621 / 1000, 10.75863775 / 1000, 12.95979032 / 1000]
    nuclear_fixed_year2050 = [80.4239702 / 1000]
    storage_fixed_year2050 = [1.904751567 / 1000, 2.990759329 / 1000, 5.272872439 / 1000]
    offwind_fixed_year2050 = [25.08663768 / 1000, 30.61419606 / 1000, 42.91331596 / 1000]
    geothermal_fixed_year2050 = [57.24504862 / 1000, 136.349483 / 1000, 187.9210814 / 1000]
    biopower_fixed_year2050, biopower_var_year2050 = [49.8730133 / 1000], 48 / 1000
    # Color info
    color_colors = {'natgas': 'black', 'natgas_ccs': 'grey', 'biopower': 'lightslategrey', 
                'solar': 'wheat', 'wind': 'skyblue', 'offwind': 'darkblue', 
                'nuclear': 'tomato', 'geothermal': 'darkred', 
                'storage': 'lightpink', 'pgp': 'lightgreen'} 

    # def calculate_pChange(value2019, value2050):_year2050)
    # info['wind'] = calculate_pChange(wind_fixed_year2019, solar_fixed_year2050)
    # info['offwind'] = calculate_pChange(offwind_fixed_year2019, offwind_fixed_year2050)
    # info['nuclear'] = calculate_pChange(nuclear_fixed_year2019, nuclear_fixed_year2050)
    # info['geothermal'] = calculate_pChange(geothermal_fixed_year2019, geotherma
    #     # a = (np.array(value2019) - np.array(value2050)) / np.array(value2019) * 100
    #     a = np.array(value2050) / np.array(value2019) * 100
    #     return a
    # info = {} 
    # info['natgas'] = calculate_pChange(natgas_fixed_year2019, natgas_fixed_year2050)
    # info['natgas_ccs'] = calculate_pChange(natgas_CCS_fixed_year2019, natgas_CCS_fixed_year2050)
    # info['biopower'] = calculate_pChange(biopower_fixed_year2019, biopower_fixed_year2050)
    # info['solar'] = calculate_pChange(solar_fixed_year2019, solar_fixedl_fixed_year2050)
    # info['storage'] = calculate_pChange(storage_fixed_year2019, storage_fixed_year2050) 
    # pos_count = 0 
    # tick_list = []
    # ax1=plt.subplot(111)
    # for var_name in ['natgas', 'natgas_ccs', 'biopower', 'solar', 'wind', 'offwind', 'nuclear', 'geothermal', 'storage']:
    #     var = info[var_name]
    #     tick_list.append(pos_count) if len(var) == 1 else tick_list.append(pos_count+1)
    #     for idx in range(len(var)):
    #         if idx == 0: ax1.bar(pos_count, var[idx], width=0.8, color=color_colors[var_name])
    #         if idx == 1: ax1.bar(pos_count, var[idx], width=0.8, color=color_colors[var_name])
    #         if idx == 2: ax1.bar(pos_count, var[idx], width=0.8, color=color_colors[var_name]) # , hatch='*'
    #         pos_count += 1
    # ax1.set_xlim(-1, pos_count)
    # ax1.set_ylim(0, 100)
    # ax1.set_xticks(tick_list)
    # plt.show()
    # # plt.savefig('cost_reduction.ps')
    # # plt.savefig('cost_fraction.ps')
    # plt.clf() 

    # Annual capacity factors
    from Shared_fun import create_table
    year = 2019
    mean_solar, series_solar = create_table(year, '20210921_US_mthd3_1950-2020_solar.csv', normalization=-1)
    mean_wind, series_wind = create_table(year, '20210921_US_mthd3_1950-2020_wind.csv', normalization=-1)
    mean_offwind, series_offwind = create_table(year, '20210921_Eez_mthd3_1980-2020_wind.csv', normalization=-1)
    # mean_solar_MERRA2, series_solar_MERRA2 = create_table(year, 'US_capacity_solar_25pctTop_unnormalized.csv', normalization=-1)
    # mean_wind_MERRA2, series_wind_MERRA2 = create_table(year, 'US_capacity_wind_25pctTop_unnormalized.csv', normalization=-1)

    info = {} 
    info['natgas']     = np.array([ natgas_fixed_year2019[0]+natgas_var_year2019, natgas_fixed_year2050[0]+natgas_var_year2050 ])
    info['natgas_ccs'] = np.array([ natgas_CCS_fixed_year2019[0]+natgas_CCS_var_year2019, natgas_CCS_fixed_year2050[0]+natgas_CCS_var_year2050, natgas_CCS_fixed_year2050[1]+natgas_CCS_var_year2050, natgas_CCS_fixed_year2050[2]+natgas_CCS_var_year2050 ])
    info['biopower']   = np.array([ biopower_fixed_year2019[0]+biopower_var_year2019, biopower_fixed_year2050[0]+biopower_var_year2050 ])
    info['solar']      = np.array([ solar_fixed_year2019[0], solar_fixed_year2050[0], solar_fixed_year2050[1], solar_fixed_year2050[2] ]) / mean_solar
    info['wind']       = np.array([ wind_fixed_year2019[0], wind_fixed_year2050[0], wind_fixed_year2050[1], wind_fixed_year2050[2] ]) / mean_wind
    info['offwind']    = np.array([ offwind_fixed_year2019[0], offwind_fixed_year2050[0], offwind_fixed_year2050[1], offwind_fixed_year2050[2] ]) / mean_offwind
    info['nuclear']    = np.array([ nuclear_fixed_year2019[0], nuclear_fixed_year2050[0] ])
    info['geothermal'] = np.array([ geothermal_fixed_year2019[0], geothermal_fixed_year2050[0], geothermal_fixed_year2050[1], geothermal_fixed_year2050[2] ])
    pos_count = 0 
    tick_list = []
    ax1=plt.subplot(111)
    for var_name in ['natgas', 'natgas_ccs', 'biopower', 'solar', 'wind', 'offwind', 'nuclear', 'geothermal']:
        var = info[var_name]
        tick_list.append(pos_count+0.5) if len(var) == 2 else tick_list.append(pos_count+1.5)
        for idx in range(len(var)):
            if idx == 0: ax1.bar(pos_count, var[idx], width=0.8, color=color_colors[var_name])
            if idx == 1: ax1.bar(pos_count, var[idx], width=0.8, color=color_colors[var_name])
            if idx == 2: ax1.bar(pos_count, var[idx], width=0.8, color=color_colors[var_name]) # , hatch='*'
            if idx == 3: ax1.bar(pos_count, var[idx], width=0.8, color=color_colors[var_name])
            pos_count += 1
    ax1.set_xlim(-1, pos_count)
    ax1.set_ylim(0, 0.25)
    ax1.set_xticks(tick_list)
    # plt.show()
    plt.savefig('cost_generation_onekWh.ps')
    plt.clf() 



    # """



    """
    # Numbers in text 
    # 1. System cost reduction 
    with open('Cost_Uncertainty_Scenario2050_spe.pickle', 'rb') as handle:
        Table_Scenario2050_Full_sub0_AllL, Table_Scenario2050_Full_sub1_GeoL, Table_Scenario2050_Full_sub2_AllH, Table_Scenario2050_Full_sub1_WinL = pickle.load(handle) 
    sc_allH = np.array(Table_Scenario2050_Full_sub2_AllH[3]['system_cost'])
    sc_allL = np.array(Table_Scenario2050_Full_sub0_AllL[3]['system_cost'])
    a = (sc_allH - sc_allL) / sc_allH * 100 
    print ( np.mean(a[-10:]) )
    # """