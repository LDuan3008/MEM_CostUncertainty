import numpy as np
import pickle, os
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors



def fig_order1_no_PGP():
    xlist = np.array([100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                       60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                       20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0])/100
    x_axis = 1 - 0.5**( np.log(xlist)/np.log(0.2) )
    xticks_addition_org = np.array([50.0, 10.0, 1.0])/100
    xticks_addition_cov = 1 - 0.5**( np.log(xticks_addition_org)/np.log(0.2) )
    xticks = np.r_[[0, 0.5, 0.75, 1.0], xticks_addition_cov]
    def plot_cost(CurrentCase, default_case_name):
        ax = plt.subplot(111)
        y_lists = [np.array(CurrentCase['natgas_tot']),  np.array(CurrentCase['natgas_ccs_tot']),  np.array(CurrentCase['biopower_tot']), 
                   np.array(CurrentCase['solar_fix']),   np.array(CurrentCase['wind_fix']),        np.array(CurrentCase['offwind_fix']), 
                   np.array(CurrentCase['nuclear_fix']), np.array(CurrentCase['geothermal_fix']),
                   np.array(CurrentCase['storage_fix'])]
        y_color = ['black', 'grey', 'lightslategrey', 'wheat', 'skyblue', 'darkblue', 'tomato', 'brown', 'lightpink']
        ax.stackplot(x_axis, y_lists, colors=y_color)
        ax.plot(x_axis, np.array(CurrentCase['system_cost']), color='black', linestyle='--')
        ax.plot(x_axis, np.zeros(len(x_axis)), color='black')
        ax.set_xlabel('Emissions reduction constration (%)', fontsize=14)
        ax.set_ylabel('System cost ($/kWh)', fontsize=14)
        ax.xaxis.labelpad = 8
        ax.yaxis.labelpad = 8
        ax.set_xticks( xticks )
        ax.set_xticklabels( ['0', '80', '96', '100', '50', '90', '99'] )
        ax.set_xlim(0, 1)
        # ax.set_ylim(0, 0.12)
        ax.set_ylim(0, 0.14)
        # plt.show()
        plt.savefig(default_case_name+'.ps')
        plt.clf()

    with open('Cost_Uncertainty_Scenario2050_spe.pickle', 'rb') as handle:
        Table_Scenario2050_sub0, Table_Scenario2050_sub1, Table_Scenario2050_sub2, Table_Scenario2050_sub3, Table_Scenario2050_sub4 = pickle.load(handle) 
    idx = 3
    plot_cost(Table_Scenario2050_sub4[0], 'WinGeoL2016') 
    plot_cost(Table_Scenario2050_sub4[1], 'WinGeoL2017') 
    plot_cost(Table_Scenario2050_sub4[2], 'WinGeoL2018') 
    plot_cost(Table_Scenario2050_sub4[3], 'WinGeoL2019') 

    

def fig_order1_with_PGP():
    xlist = np.array([100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                       60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                       20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0])/100
    x_axis = 1 - 0.5**( np.log(xlist)/np.log(0.2) )
    xticks_addition_org = np.array([50.0, 10.0, 1.0])/100
    xticks_addition_cov = 1 - 0.5**( np.log(xticks_addition_org)/np.log(0.2) )
    xticks = np.r_[[0, 0.5, 0.75, 1.0], xticks_addition_cov]
    def plot_cost(CurrentCase, default_case_name):
        ax = plt.subplot(111)
        y_lists = [np.array(CurrentCase['natgas_tot']),  np.array(CurrentCase['natgas_ccs_tot']),  np.array(CurrentCase['biopower_tot']), 
                   np.array(CurrentCase['solar_fix']),   np.array(CurrentCase['wind_fix']), np.array(CurrentCase['offwind_fix']), 
                   np.array(CurrentCase['nuclear_fix']), np.array(CurrentCase['geothermal_fix']),
                   np.array(CurrentCase['storage_fix']),
                   np.array(CurrentCase['to_PGP_fix']) + np.array(CurrentCase['PGP_storage_fix']) + np.array(CurrentCase['from_PGP_fix'])]
        y_color = ['black', 'grey', 'lightslategrey', 'wheat', 'skyblue', 'darkblue', 'tomato', 'brown', 'lightpink', 'lightgreen']

        ax.stackplot(x_axis, y_lists, colors=y_color)
        ax.plot(x_axis, np.array(CurrentCase['system_cost']), color='black', linestyle='--')
        ax.plot(x_axis, np.zeros(len(x_axis)), color='black')
        ax.set_xlabel('Emissions reduction constration (%)', fontsize=14)
        ax.set_ylabel('System cost ($/kWh)', fontsize=14)
        ax.xaxis.labelpad = 8
        ax.yaxis.labelpad = 8
        ax.set_xticks( xticks )
        ax.set_xticklabels( ['0', '80', '96', '100', '50', '90', '99'] )
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 0.12)
        plt.show()
        # plt.savefig(default_case_name+'.ps')
        plt.clf()
    with open('Cost_Uncertainty_Scenario2050_PGP_spe.pickle', 'rb') as handle:
        Table_Scenario2050_Full_sub0_AllL_PGP, Table_Scenario2050_Full_sub1_GeoL_PGP, Table_Scenario2050_Full_sub2_AllH_PGP = pickle.load(handle) 
    idx = 0
    plot_cost(Table_Scenario2050_Full_sub0_AllL_PGP[idx], 'AllL_PGP2019') 
    plot_cost(Table_Scenario2050_Full_sub1_GeoL_PGP[idx], 'GeoL_PGP2019') 
    plot_cost(Table_Scenario2050_Full_sub2_AllH_PGP[idx], 'AllH_PGP2019')



def fig_order1_dispatch():

    def plot_dispatch(table_in, idx, name):
        natgas_dispatch      = table_in[idx]['natgas_dispatch']
        natgas_ccs_dispatch  = table_in[idx]['natgas_ccs_dispatch']
        biopower_dispatch    = table_in[idx]['biopower_dispatch']
        solar_potential      = table_in[idx]['solar_potential']
        wind_potential       = table_in[idx]['wind_potential']
        offwind_potential    = table_in[idx]['offwind_potential']
        nuclear_potential    = table_in[idx]['nuclear_potential']
        geothermal_potential = table_in[idx]['geothermal_potential']
        storage_dispatch     = table_in[idx]['storage_dispatch']
        demand_potential     = table_in[idx]['demand_potential']

        # Daily averaged
        stack_list, color_list = [], []
        nuclear_potential_daily    = np.mean(nuclear_potential.reshape(-1,24), axis=1)       ; stack_list.append(nuclear_potential_daily)     ; color_list.append('tomato')
        geothermal_potential_daily = np.mean(geothermal_potential.reshape(-1,24), axis=1)    ; stack_list.append(geothermal_potential_daily)  ; color_list.append('brown')
        solar_potential_daily      = np.mean(solar_potential.reshape(-1,24), axis=1)         ; stack_list.append(solar_potential_daily)       ; color_list.append('wheat')
        wind_potential_daily       = np.mean(wind_potential.reshape(-1,24), axis=1)          ; stack_list.append(wind_potential_daily)        ; color_list.append('skyblue')
        offwind_potential_daily    = np.mean(offwind_potential.reshape(-1,24), axis=1)       ; stack_list.append(offwind_potential_daily)     ; color_list.append('darkblue') 
        natgas_dispatch_daily      = np.mean(natgas_dispatch.reshape(-1,24), axis=1)         ; stack_list.append(natgas_dispatch_daily)       ; color_list.append('black')
        natgas_ccs_dispatch_daily  = np.mean(natgas_ccs_dispatch.reshape(-1,24), axis=1)     ; stack_list.append(natgas_ccs_dispatch_daily)   ; color_list.append('grey')
        biopower_dispatch_daily    = np.mean(biopower_dispatch.reshape(-1,24), axis=1)       ; stack_list.append(biopower_dispatch_daily)     ; color_list.append('lightslategrey')
        storage_dispatch_daily     = np.mean(storage_dispatch.reshape(-1,24), axis=1)        ; stack_list.append(storage_dispatch_daily)      ; color_list.append('lightpink')
        demand_potential_daily     = np.mean(demand_potential.reshape(-1,24), axis=1)
        ax1 = plt.subplot2grid((1,5), (0,0), colspan=3)
        ax1.stackplot(np.arange(365), stack_list, colors=color_list)
        ax1.plot(np.arange(365), demand_potential_daily, color='black', linewidth=1)
        ax1.set_xlim(0, 364)
        plt.xticks([0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334])
        ax1.set_ylim(0, 3)
        # Hourly1
        ax2 = plt.subplot2grid((1,5), (0,3), colspan=1)
        ax2.stackplot(np.arange(8760)[15*24:20*24], 
                      nuclear_potential[15*24:20*24], 
                      geothermal_potential[15*24:20*24], 
                      solar_potential[15*24:20*24],
                      wind_potential[15*24:20*24], 
                      offwind_potential[15*24:20*24], 
                      natgas_dispatch[15*24:20*24], 
                      natgas_ccs_dispatch[15*24:20*24], 
                      biopower_dispatch[15*24:20*24], 
                      storage_dispatch[15*24:20*24], 
                      colors = ['tomato', 'brown', 'wheat', 'skyblue', 'darkblue', 'black', 'grey', 'lightslategrey', 'lightpink'] )
        ax2.plot(np.arange(8760)[15*24:20*24], demand_potential[15*24:20*24], color='black', linewidth=1)
        ax2.set_xlim(15*24, 20*24)
        ax2.set_xticks([15*24, 16*24, 17*24, 18*24, 19*24, 20*24])
        ax2.set_ylim(0, 3)
        ax2.set_yticks([])
        # Hourly2
        ax3 = plt.subplot2grid((1,5), (0,4), colspan=1)
        ax3.stackplot(np.arange(8760)[(181+15)*24:(181+20)*24], 
                      nuclear_potential[(181+15)*24:(181+20)*24], 
                      geothermal_potential[(181+15)*24:(181+20)*24],
                      solar_potential[(181+15)*24:(181+20)*24],
                      wind_potential[(181+15)*24:(181+20)*24],
                      offwind_potential[(181+15)*24:(181+20)*24],
                      natgas_dispatch[(181+15)*24:(181+20)*24],
                      natgas_ccs_dispatch[(181+15)*24:(181+20)*24],
                      biopower_dispatch[(181+15)*24:(181+20)*24],
                      storage_dispatch[(181+15)*24:(181+20)*24],
                      colors = ['tomato', 'brown', 'wheat', 'skyblue', 'darkblue', 'black', 'grey', 'lightslategrey', 'lightpink'] )
        ax3.plot(np.arange(8760)[(181+15)*24:(181+20)*24], demand_potential[(181+15)*24:(181+20)*24], color='black', linewidth=1)
        ax3.set_xlim((181+15)*24, (181+20)*24)
        ax3.set_xticks([4704, 4728, 4752, 4776, 4800, 4824])
        ax3.set_ylim(0, 3)
        ax3.set_yticks([])
        # plt.show()
        plt.savefig(f'{name}.ps')
        plt.clf()
    
    with open('Cost_Uncertainty_dispatch_spe.pickle', 'rb') as handle:
        table_dispatch_100p, table_dispatch_99p, table_dispatch_80p, table_dispatch_50p, table_dispatch_20p, table_dispatch_10p = pickle.load(handle)
    # plot_dispatch(table_dispatch_100p, 0, 'Year2019_100p')
    # plot_dispatch(table_dispatch_100p, 1, 'Year2050AllL_100p')
    # plot_dispatch(table_dispatch_100p, 2, 'Year2050GeoL_100p')
    # plot_dispatch(table_dispatch_100p, 3, 'Year2050AllH_100p')
    # plot_dispatch(table_dispatch_100p, 4, 'Year2050WinL_100p')
    # plot_dispatch(table_dispatch_100p, 5, 'Year2050BothL_100p')
    # plot_dispatch(table_dispatch_80p, 0, 'Year2019_80p')
    # plot_dispatch(table_dispatch_80p, 1, 'Year2050AllL_80p')
    # plot_dispatch(table_dispatch_80p, 2, 'Year2050GeoL_80p')
    # plot_dispatch(table_dispatch_80p, 3, 'Year2050AllH_80p')
    # plot_dispatch(table_dispatch_80p, 4, 'Year2050WinL_80p')
    # plot_dispatch(table_dispatch_80p, 5, 'Year2050BothL_80p')

    # plot_dispatch(table_dispatch_10p, 0, 'Year2019_10p')
    # plot_dispatch(table_dispatch_10p, 1, 'Year2050AllL_10p')
    # plot_dispatch(table_dispatch_10p, 2, 'Year2050GeoL_10p')
    # plot_dispatch(table_dispatch_10p, 3, 'Year2050AllH_10p')
    # plot_dispatch(table_dispatch_10p, 4, 'Year2050WinL_10p')
    # plot_dispatch(table_dispatch_10p, 5, 'Year2050BothL_10p')
    # plot_dispatch(table_dispatch_20p, 0, 'Year2019_20p')
    # plot_dispatch(table_dispatch_20p, 1, 'Year2050AllL_20p')
    # plot_dispatch(table_dispatch_20p, 2, 'Year2050GeoL_20p')
    # plot_dispatch(table_dispatch_20p, 3, 'Year2050AllH_20p')
    # plot_dispatch(table_dispatch_20p, 4, 'Year2050WinL_20p')
    # plot_dispatch(table_dispatch_20p, 5, 'Year2050BothL_20p')
    # plot_dispatch(table_dispatch_50p, 0, 'Year2019_50p')
    # plot_dispatch(table_dispatch_50p, 1, 'Year2050AllL_50p')
    # plot_dispatch(table_dispatch_50p, 2, 'Year2050GeoL_50p')
    # plot_dispatch(table_dispatch_50p, 3, 'Year2050AllH_50p')
    # plot_dispatch(table_dispatch_50p, 4, 'Year2050WinL_50p')
    # plot_dispatch(table_dispatch_50p, 5, 'Year2050BothL_50p')

    plot_dispatch(table_dispatch_99p, 0, 'Year2019_99p')
    plot_dispatch(table_dispatch_99p, 1, 'Year2050AllL_99p')
    plot_dispatch(table_dispatch_99p, 2, 'Year2050GeoL_99p')
    plot_dispatch(table_dispatch_99p, 3, 'Year2050AllH_99p')
    plot_dispatch(table_dispatch_99p, 4, 'Year2050WinL_99p')
    plot_dispatch(table_dispatch_99p, 5, 'Year2050BothL_99p')


    with open('Cost_Uncertainty_dispatch_spe_additional.pickle', 'rb') as handle:
        table_dispatch_90p,table_dispatch_96p = pickle.load(handle)
    plot_dispatch(table_dispatch_90p, 0, 'Year2019_90p')
    plot_dispatch(table_dispatch_90p, 1, 'Year2050AllL_90p')
    plot_dispatch(table_dispatch_90p, 2, 'Year2050GeoL_90p')
    plot_dispatch(table_dispatch_90p, 3, 'Year2050AllH_90p')
    plot_dispatch(table_dispatch_90p, 4, 'Year2050WinL_90p')
    plot_dispatch(table_dispatch_90p, 5, 'Year2050BothL_90p')
    plot_dispatch(table_dispatch_96p, 0, 'Year2019_96p')
    plot_dispatch(table_dispatch_96p, 1, 'Year2050AllL_96p')
    plot_dispatch(table_dispatch_96p, 2, 'Year2050GeoL_96p')
    plot_dispatch(table_dispatch_96p, 3, 'Year2050AllH_96p')
    plot_dispatch(table_dispatch_96p, 4, 'Year2050WinL_96p')
    plot_dispatch(table_dispatch_96p, 5, 'Year2050BothL_96p')

