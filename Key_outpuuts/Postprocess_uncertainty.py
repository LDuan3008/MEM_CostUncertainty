import numpy as np
import pickle, os
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy.stats as st

if __name__ == "__main__":

    base_to_PGP = -999
    base_from_PGP = -999

    """
    def plot_cost(CurrentCase, ylist_type, default_case_name):
        ax = plt.subplot(111)
        if ylist_type == 'PGP':
            x_axis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
            y_lists = [np.array(CurrentCase['natgas_tot']),  np.array(CurrentCase['natgas_ccs_tot']),  np.array(CurrentCase['biopower_tot']), 
                       np.array(CurrentCase['solar_fix']),   np.array(CurrentCase['wind_fix']),        np.array(CurrentCase['offwind_fix']), 
                       np.array(CurrentCase['nuclear_fix']), np.array(CurrentCase['geothermal_fix']),
                       np.array(CurrentCase['storage_fix']),
                       np.array(CurrentCase['to_PGP_fix']) + np.array(CurrentCase['PGP_storage_fix']) + np.array(CurrentCase['from_PGP_fix'])]
            y_color = ['black', 'grey', 'lightslategrey', 'wheat', 'skyblue', 'darkblue', 'tomato', 'brown', 'lightpink', 'lightgreen']
            ax.stackplot(x_axis, y_lists, colors=y_color)
            ax.plot(x_axis, np.array(CurrentCase['system_cost']), color='black', linestyle='--')
            ax.plot(x_axis, np.zeros(len(x_axis)), color='black')
            ax.set_xlabel('PGP cost scale (%)', fontsize=14)
            ax.set_ylabel('System cost ($/kWh)', fontsize=14)
            ax.xaxis.labelpad = 8
            ax.yaxis.labelpad = 8
            ax.set_xticks( x_axis )
            ax.set_xticklabels( x_axis )
            ax.set_xlim(0.1, 1)
            # ax.set_xscale('log', basex=10)
            ax.set_ylim(0, 0.12)
            # plt.show()
            plt.savefig(default_case_name+'.ps')
            plt.clf()
        if ylist_type == 'DAC':
            x_axis = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
            y_lists = [np.array(CurrentCase['natgas_tot']),  np.array(CurrentCase['natgas_ccs_tot']),  np.array(CurrentCase['biopower_tot']), 
                       np.array(CurrentCase['solar_fix']),   np.array(CurrentCase['wind_fix']),        np.array(CurrentCase['offwind_fix']), 
                       np.array(CurrentCase['nuclear_fix']), np.array(CurrentCase['geothermal_fix']),
                       np.array(CurrentCase['storage_fix']),
                       np.array(CurrentCase['dac_tot'])]
            y_color = ['black', 'grey', 'lightslategrey', 'wheat', 'skyblue', 'darkblue', 'tomato', 'brown', 'lightpink', 'lightgreen']
            ax.stackplot(x_axis, y_lists, colors=y_color)
            ax.plot(x_axis, np.array(CurrentCase['system_cost']), color='black', linestyle='--')
            ax.plot(x_axis, np.zeros(len(x_axis)), color='black')
            ax.set_xlabel('PGP cost scale (%)', fontsize=14)
            ax.set_ylabel('System cost ($/kWh)', fontsize=14)
            ax.xaxis.labelpad = 8
            ax.yaxis.labelpad = 8
            ax.set_xticks( x_axis )
            ax.set_xticklabels( x_axis )
            ax.set_xlim(0.01, 1)
            ax.set_xscale('log', basex=10)
            ax.set_ylim(0, 0.12)
            # plt.show()
            plt.savefig(default_case_name+'.ps')
            plt.clf()
        if ylist_type == 'demand':
            xlist = np.array([100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 
                      40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0])/100
            x_axis = 1 - 0.5**( np.log(xlist)/np.log(0.2) )
            xticks_addition_org = np.array([50.0, 10.0, 1.0])/100
            xticks_addition_cov = 1 - 0.5**( np.log(xticks_addition_org)/np.log(0.2) )
            xticks = np.r_[[0, 0.5, 0.75, 1.0], xticks_addition_cov]
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
            ax.set_ylim(0, 0.14)
            # plt.show()
            plt.savefig(default_case_name+'.ps')
            plt.clf()
        if ylist_type == 'GeoCap':
            x_axis = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5])
            y_lists = [np.array(CurrentCase['natgas_tot']),  np.array(CurrentCase['natgas_ccs_tot']),  np.array(CurrentCase['biopower_tot']), 
                       np.array(CurrentCase['solar_fix']),   np.array(CurrentCase['wind_fix']),        np.array(CurrentCase['offwind_fix']), 
                       np.array(CurrentCase['nuclear_fix']), np.array(CurrentCase['geothermal_fix']),
                       np.array(CurrentCase['storage_fix'])]
            y_color = ['black', 'grey', 'lightslategrey', 'wheat', 'skyblue', 'darkblue', 'tomato', 'brown', 'lightpink']
            ax.stackplot(x_axis, y_lists, colors=y_color)
            ax.plot(x_axis, np.array(CurrentCase['system_cost']), color='black', linestyle='--')
            ax.plot(x_axis, np.zeros(len(x_axis)), color='black')
            ax.set_xlim(0, 1.5)
            ax.set_ylim(0, 0.10)
            plt.show()
            # plt.savefig(default_case_name+'.ps')
            plt.clf()


    with open('Cost_Uncertainty_PGP_scale.pickle', 'rb') as handle:
        table_dispatch_ToPGP, table_dispatch_FromPGP, table_dispatch_AllPGP = pickle.load(handle) 
    # # plot_cost(table_dispatch_ToPGP[0], 'PGP', 'tPGP2019') 
    # plot_cost(table_dispatch_ToPGP[1], 'PGP', 'tPGP2050_sub0') 
    # plot_cost(table_dispatch_ToPGP[2], 'PGP', 'tPGP2050_sub1') 
    # plot_cost(table_dispatch_ToPGP[3], 'PGP', 'tPGP2050_sub2') 
    # plot_cost(table_dispatch_ToPGP[4], 'PGP', 'tPGP2050_sub3') 
    # plot_cost(table_dispatch_ToPGP[5], 'PGP', 'tPGP2050_sub4') 
    # # plot_cost(table_dispatch_FromPGP[0], 'PGP', 'fPGP2019') 
    # plot_cost(table_dispatch_FromPGP[1], 'PGP', 'fPGP2050_sub0') 
    # plot_cost(table_dispatch_FromPGP[2], 'PGP', 'fPGP2050_sub1') 
    # plot_cost(table_dispatch_FromPGP[3], 'PGP', 'fPGP2050_sub2') 
    # plot_cost(table_dispatch_FromPGP[4], 'PGP', 'fPGP2050_sub3') 
    # plot_cost(table_dispatch_FromPGP[5], 'PGP', 'fPGP2050_sub4') 
    # # plot_cost(table_dispatch_AllPGP[0], 'PGP', 'aPGP2019') 
    # plot_cost(table_dispatch_AllPGP[1], 'PGP', 'aPGP2050_sub0') 
    # plot_cost(table_dispatch_AllPGP[2], 'PGP', 'aPGP2050_sub1') 
    # plot_cost(table_dispatch_AllPGP[3], 'PGP', 'aPGP2050_sub2') 
    # plot_cost(table_dispatch_AllPGP[4], 'PGP', 'aPGP2050_sub3') 
    # plot_cost(table_dispatch_AllPGP[5], 'PGP', 'aPGP2050_sub4') 

    with open('Cost_Uncertainty_Dac_scale.pickle', 'rb') as handle:
        table_dispatch_DAC = pickle.load(handle) 
    # plot_cost(table_dispatch_DAC[0], 'DAC', 'DAC2019') 
    # plot_cost(table_dispatch_DAC[1], 'DAC', 'DAC2050_sub0') 
    # plot_cost(table_dispatch_DAC[2], 'DAC', 'DAC2050_sub1') 
    # plot_cost(table_dispatch_DAC[3], 'DAC', 'DAC2050_sub2') 
    # plot_cost(table_dispatch_DAC[4], 'DAC', 'DAC2050_sub3') 
    # plot_cost(table_dispatch_DAC[5], 'DAC', 'DAC2050_sub4') 

    with open('Cost_Uncertainty_Demand.pickle', 'rb') as handle:
        Table_ESF2050, Table_square = pickle.load(handle) 
    # plot_cost(Table_ESF2050[0], 'demand', 'ESF2050_2019') 
    # plot_cost(Table_ESF2050[1], 'demand', 'ESF2050_2050_sub0') 
    # plot_cost(Table_ESF2050[2], 'demand', 'ESF2050_2050_sub1') 
    # plot_cost(Table_ESF2050[3], 'demand', 'ESF2050_2050_sub2') 
    # plot_cost(Table_ESF2050[4], 'demand', 'ESF2050_2050_sub3') 
    # plot_cost(Table_ESF2050[5], 'demand', 'ESF2050_2050_sub4') 
    # plot_cost(Table_square[0], 'demand', 'square_2019') 
    # plot_cost(Table_square[1], 'demand', 'square_2050_sub0') 
    # plot_cost(Table_square[2], 'demand', 'square_2050_sub1') 
    # plot_cost(Table_square[3], 'demand', 'square_2050_sub2') 
    # plot_cost(Table_square[4], 'demand', 'square_2050_sub3') 
    # plot_cost(Table_square[5], 'demand', 'square_2050_sub4') 

    # with open('Cost_Uncertainty_GeoCapLimit.pickle', 'rb') as handle:
    #     table_dispatch_GeoCap = pickle.load(handle) 
    # plot_cost(table_dispatch_GeoCap[0], 'GeoCap', 'ER10') 
    # plot_cost(table_dispatch_GeoCap[1], 'GeoCap', 'ER1') 
    # plot_cost(table_dispatch_GeoCap[2], 'GeoCap', 'ER0') 
    # """



    """
    color_colors = {'natgas': 'black', 'natgas_ccs': 'grey', 'biopower': 'lightslategrey', 
                'solar': 'wheat', 'wind': 'skyblue', 'offwind': 'darkblue', 
                'nuclear': 'tomato', 'geothermal': 'darkred', 
                'storage': 'lightpink', 'pgp': 'lightgreen'} 
    def system_cost_distribution(table_in):
        bin_edges = list(np.arange(0.05, 0.101, 0.001))
        tech_list_Full = ['solar', 'wind', 'offwind', 'geothermal', 'storage']
        system_cost = np.array(table_in['system_cost'])
        cost_tables = table_in['cost']
        for tech_idx in tech_list_Full:
            tech_cap = np.array(table_in[tech_idx+'_cap'])
            tech_fixed_cost = np.array(cost_tables[tech_idx+'_fix'])
            tech_fixed_cost_unique = np.unique(tech_fixed_cost)
            if len(tech_fixed_cost_unique) == 3: 
                list_1, list_2, list_3 = [], [], []
                caps_1, caps_2, caps_3 = [], [], []
                for idx in range(len(tech_fixed_cost)): 
                    if tech_fixed_cost[idx] == tech_fixed_cost_unique[0]: list_1.append(system_cost[idx])
                    if tech_fixed_cost[idx] == tech_fixed_cost_unique[1]: list_2.append(system_cost[idx])
                    if tech_fixed_cost[idx] == tech_fixed_cost_unique[2]: list_3.append(system_cost[idx])
            ax1 = plt.subplot(111)
            x_axis = np.arange(0.05, 0.101, 0.001)
            try:
                kde_L = st.gaussian_kde(list_1); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_L.pdf(x_axis)*0.001, facecolor='#fdf289', edgecolor='#fdf289', linestyle='--', linewidth=0.8, alpha=0.5, label='L')
            except:
                print ('no L')
            try:
                kde_M = st.gaussian_kde(list_2); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_M.pdf(x_axis)*0.001, facecolor='#46edc8', edgecolor='#46edc8', linestyle='--', linewidth=0.8, alpha=0.5, label='M')
            except:
                print ('no M')
            try:
                kde_H = st.gaussian_kde(list_3); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_H.pdf(x_axis)*0.001, facecolor='#374d7c', edgecolor='#374d7c', linestyle='--', linewidth=0.8, alpha=0.5, label='H')
            except:
                print ('no H')
            ax1 = plt.subplot(111)
            ax1.boxplot(caps_1, positions=[1], widths=0.6, medianprops=dict(color=color_colors[tech_idx]))
            ax1.boxplot(caps_2, positions=[2], widths=0.6, medianprops=dict(color=color_colors[tech_idx]))
            ax1.boxplot(caps_3, positions=[3], widths=0.6, medianprops=dict(color=color_colors[tech_idx]))
            ax1.set_xlim(0.05, 0.1)
            ax1.set_ylim(0, 0.15)
            # plt.show() 
            plt.savefig(f'panel_low_{tech_idx}.ps')
            plt.clf()
    # with open('Cost_Uncertainty_GeoCapEnsemble.pickle', 'rb') as handle:
    #     Table_scenario2050_GeoCap = pickle.load(handle) 
    # system_cost_distribution(Table_scenario2050_GeoCap[0])
    # system_cost_distribution(Table_scenario2050_GeoCap[1])
    # system_cost_distribution(Table_scenario2050_GeoCap[2])
    # """


    """
    def plot_transient(CurrentCase, default_case_name):
        ax = plt.subplot(111)
        x_axis = np.arange(2019, 2051, 1)
        y_lists = [np.array(CurrentCase['natgas_tot']) + np.array(CurrentCase['natgas_fixed_tot']), 
                   np.array(CurrentCase['natgas_ccs_tot']) + np.array(CurrentCase['natgas_ccs_fixed_tot']),
                   np.array(CurrentCase['biopower_tot']) + np.array(CurrentCase['biopower_fixed_tot']), 
                   np.array(CurrentCase['solar_fix']) + np.array(CurrentCase['solar_fixed_fix']), 
                   np.array(CurrentCase['wind_fix']) + np.array(CurrentCase['wind_fixed_fix']), 
                   np.array(CurrentCase['offwind_fix']) + np.array(CurrentCase['offwind_fixed_fix']), 
                   np.array(CurrentCase['nuclear_fix']) + np.array(CurrentCase['nuclear_fixed_fix']), 
                   np.array(CurrentCase['geothermal_fix']) + np.array(CurrentCase['geothermal_fixed_fix']),
                   np.array(CurrentCase['storage_fix']) + np.array(CurrentCase['storage_fixed_fix'])]
        y_color = ['black', 'grey', 'lightslategrey', 'wheat', 'skyblue', 'darkblue', 'tomato', 'brown', 'lightpink']
        ax.stackplot(x_axis, y_lists, colors=y_color)
        ax.plot(x_axis, np.array(CurrentCase['system_cost']), color='black', linestyle='--')
        ax.plot(x_axis, np.zeros(len(x_axis)), color='black')
        ax.set_xlabel('PGP cost scale (%)', fontsize=14)
        ax.set_ylabel('System cost ($/kWh)', fontsize=14)
        ax.xaxis.labelpad = 8
        ax.yaxis.labelpad = 8
        ax.set_xticks( x_axis )
        ax.set_xticklabels( x_axis )
        ax.set_xlim(2019, 2050)
        ax.set_ylim(0, 0.12)
        # plt.show()
        plt.savefig(default_case_name+'.ps')
        plt.clf()
    def plot_right_panel_bar(CurrentCase, type, name):
        ax = plt.subplot(111)
        bot = 0
        if type == 0:
            ax.bar(0, np.array(CurrentCase['natgas_tot'][-1]) + np.array(CurrentCase['natgas_fixed_tot'][-1]),         bottom = bot, color='black');          bot = bot + CurrentCase['natgas_tot'][-1] + np.array(CurrentCase['natgas_fixed_tot'][-1])
            ax.bar(0, np.array(CurrentCase['natgas_ccs_tot'][-1]) + np.array(CurrentCase['natgas_ccs_fixed_tot'][-1]), bottom = bot, color='grey');           bot = bot + CurrentCase['natgas_ccs_tot'][-1] + np.array(CurrentCase['natgas_ccs_fixed_tot'][-1])
            ax.bar(0, np.array(CurrentCase['biopower_tot'][-1]) + np.array(CurrentCase['biopower_fixed_tot'][-1]),     bottom = bot, color='lightslategrey'); bot = bot + CurrentCase['biopower_tot'][-1] + np.array(CurrentCase['biopower_fixed_tot'][-1])
            ax.bar(0, np.array(CurrentCase['solar_fix'][-1]) + np.array(CurrentCase['solar_fixed_fix'][-1]),           bottom = bot, color='wheat');          bot = bot + CurrentCase['solar_fix'][-1] + np.array(CurrentCase['solar_fixed_fix'][-1])
            ax.bar(0, np.array(CurrentCase['wind_fix'][-1]) + np.array(CurrentCase['wind_fixed_fix'][-1]),             bottom = bot, color='skyblue');        bot = bot + CurrentCase['wind_fix'][-1] + np.array(CurrentCase['wind_fixed_fix'][-1])
            ax.bar(0, np.array(CurrentCase['offwind_fix'][-1]) + np.array(CurrentCase['offwind_fixed_fix'][-1]),       bottom = bot, color='darkblue');       bot = bot + CurrentCase['offwind_fix'][-1] + np.array(CurrentCase['offwind_fixed_fix'][-1])
            ax.bar(0, np.array(CurrentCase['nuclear_fix'][-1]) + np.array(CurrentCase['nuclear_fixed_fix'][-1]),       bottom = bot, color='tomato');         bot = bot + CurrentCase['nuclear_fix'][-1] + np.array(CurrentCase['nuclear_fixed_fix'][-1])
            ax.bar(0, np.array(CurrentCase['geothermal_fix'][-1]) + np.array(CurrentCase['geothermal_fixed_fix'][-1]), bottom = bot, color='brown');          bot = bot + CurrentCase['geothermal_fix'][-1] + np.array(CurrentCase['geothermal_fixed_fix'][-1])
            ax.bar(0, np.array(CurrentCase['storage_fix'][-1]) + np.array(CurrentCase['storage_fixed_fix'][-1]),       bottom = bot, color='lightpink');      bot = bot + CurrentCase['storage_fix'][-1] + np.array(CurrentCase['storage_fixed_fix'][-1])
        if type == 1:
            ax.bar(0, np.array(CurrentCase['natgas_tot'][-1]),     bottom = bot, color='black');          bot = bot + CurrentCase['natgas_tot'][-1]
            ax.bar(0, np.array(CurrentCase['natgas_ccs_tot'][-1]), bottom = bot, color='grey');           bot = bot + CurrentCase['natgas_ccs_tot'][-1]
            ax.bar(0, np.array(CurrentCase['biopower_tot'][-1]),   bottom = bot, color='lightslategrey'); bot = bot + CurrentCase['biopower_tot'][-1]
            ax.bar(0, np.array(CurrentCase['solar_fix'][-1]),      bottom = bot, color='wheat');          bot = bot + CurrentCase['solar_fix'][-1]
            ax.bar(0, np.array(CurrentCase['wind_fix'][-1]),       bottom = bot, color='skyblue');        bot = bot + CurrentCase['wind_fix'][-1]
            ax.bar(0, np.array(CurrentCase['offwind_fix'][-1]),    bottom = bot, color='darkblue');       bot = bot + CurrentCase['offwind_fix'][-1]
            ax.bar(0, np.array(CurrentCase['nuclear_fix'][-1]),    bottom = bot, color='tomato');         bot = bot + CurrentCase['nuclear_fix'][-1]
            ax.bar(0, np.array(CurrentCase['geothermal_fix'][-1]), bottom = bot, color='brown');          bot = bot + CurrentCase['geothermal_fix'][-1]
            ax.bar(0, np.array(CurrentCase['storage_fix'][-1]),    bottom = bot, color='lightpink'); bot = bot + CurrentCase['storage_fix'][-1]
        ax.set_ylim(0, 0.12)
        # plt.show()
        plt.savefig(name+'.ps')
        plt.clf() 
    # with open('Cost_Uncertainty_Transient.pickle', 'rb') as handle:
    #     Table_Transient = pickle.load(handle) 
    # with open('Cost_Uncertainty_Scenario2050_spe.pickle', 'rb') as handle:
    #     Table_Scenario2050_Full_sub0_AllL, Table_Scenario2050_Full_sub1_GeoL, Table_Scenario2050_Full_sub2_AllH = pickle.load(handle) 
    # plot_transient(Table_Transient[0], 'transient_sub0')
    # plot_transient(Table_Transient[1], 'transient_sub1')
    # plot_transient(Table_Transient[2], 'transient_sub2')
    # plot_right_panel_bar(Table_Scenario2050_Full_sub2_AllH[3], 1, 'bar_allH')
    # plot_right_panel_bar(Table_Scenario2050_Full_sub1_GeoL[3], 1, 'bar_GeoL')
    # plot_right_panel_bar(Table_Scenario2050_Full_sub0_AllL[3], 1, 'bar_allL')
    # plot_right_panel_bar(Table_Transient[0], 0, 'bar_allH')
    # plot_right_panel_bar(Table_Transient[1], 0, 'bar_GeoL')
    # plot_right_panel_bar(Table_Transient[2], 0, 'bar_allL')
    # """


    """
    # Load-shifting 
    def cal_plot(CurrentCase, type, vc):
        ax = plt.subplot(111)
        if type == 'stack':
            x_axis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
            y_lists = [np.array(CurrentCase['natgas_tot']),  np.array(CurrentCase['natgas_ccs_tot']),  np.array(CurrentCase['biopower_tot']), 
                       np.array(CurrentCase['solar_fix']),   np.array(CurrentCase['wind_fix']),        np.array(CurrentCase['offwind_fix']), 
                       np.array(CurrentCase['nuclear_fix']), np.array(CurrentCase['geothermal_fix']),
                       np.array(CurrentCase['storage_fix']),
                       np.array(CurrentCase['load_shift_tot'])]
            y_color = ['black', 'grey', 'lightslategrey', 'wheat', 'skyblue', 'darkblue', 'tomato', 'brown', 'lightpink', 'lightgreen']
            ax.stackplot(x_axis, y_lists, colors=y_color)
            ax.plot(x_axis, np.array(CurrentCase['system_cost']), color='black', linestyle='--')
            ax.plot(x_axis, np.zeros(len(x_axis)), color='black')
            ax.set_xlabel('PGP cost scale (%)', fontsize=14)
            ax.set_ylabel('System cost ($/kWh)', fontsize=14)
            ax.xaxis.labelpad = 8
            ax.yaxis.labelpad = 8
            ax.set_xticks( x_axis )
            ax.set_xticklabels( x_axis )
            ax.set_xlim(0.1, 1)
            ax.set_xscale('log', basex=10)
            ax.set_ylim(0, 0.12)
            plt.show()
            # plt.savefig(default_case_name+'.ps')
            plt.clf()
        if type == 'calculation':
            cap = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1][::-1]
            tot_shifted = (np.array(CurrentCase['load_shift_tot']) - np.array(cap) * 1e-8 ) / vc * 8760 / cap # kWh * hour 
            print (tot_shifted) 
    # with open('NgCcsSoWiStNu_LS.pickle', 'rb') as handle:
    #     table_LS_y2019, table_LS_y2050_sub0, table_LS_y2050_sub1, table_LS_y2050_sub2 = pickle.load(handle) 
    # var = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1][::-1]
    # cap = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1][::-1]
    # for var_idx in range(len(var)):
    #     cal_plot(table_LS_y2019[var_idx], 'stack', var[var_idx])
    #     cal_plot(table_LS_y2050_sub0[var_idx], 'stack', var[var_idx])
    #     cal_plot(table_LS_y2050_sub1[var_idx], 'stack', var[var_idx])
    #     cal_plot(table_LS_y2050_sub2[var_idx], 'stack', var[var_idx])
    # with open('Cost_Uncertainty_Transient_ensemble.pickle', 'rb') as handle:
    #     table_transient_2050 = pickle.load(handle) 
    # system_cost_lockin = []
    # for idx in range(len(table_transient_2050)):
    #     system_cost_lockin.append(table_transient_2050[idx]['system_cost'][0])
    # system_cost_lockin = np.array(system_cost_lockin)
    # with open('Cost_Uncertainty_Scenario2050.pickle', 'rb') as handle:
    #     Table_scenario2050_Full = pickle.load(handle) 
    # system_cost = Table_scenario2050_Full[0]['system_cost']
    # print (np.mean(system_cost_lockin), np.std(system_cost_lockin)) 
    # print (np.mean(system_cost), np.std(system_cost)) 
    # plt.scatter(np.ones(729)*1, system_cost_lockin)
    # plt.scatter(np.ones(729)*2, system_cost)
    # plt.xlim(0, 3)
    # plt.show()
    # plt.clf()
    # """


    """
    def plot_box(ax, pos, list_exist):
        if len(list_exist)>0:
            min_bound = np.min(np.array(list_exist))
            max_bound = np.max(np.array(list_exist))
            ax.plot( np.r_[pos-0.02, pos+0.02],  np.r_[min_bound, min_bound], color='black', linewidth=0.8    )
            ax.plot( np.r_[pos-0.02, pos+0.02],  np.r_[max_bound, max_bound], color='black', linewidth=0.8    )
            ax.plot( np.r_[pos,      pos     ],  np.r_[min_bound, max_bound], color='black', linewidth=0.8    )
    def system_cost_distribution(table_in, name):
        bin_edges = list(np.arange(0, 0.101, 0.001))
        # tech_list_Full = ['natgas', 'natgas_ccs', 'biopower', 'solar', 'wind', 'offwind', 'nuclear', 'geothermal', 'storage']
        tech_list_Full = ['natgas', 'natgas_ccs', 'biopower', 'solar', 'wind', 'offwind', 'nuclear', 'geothermal', 'storage']
        system_cost = np.array(table_in['system_cost'])
        cost_tables = table_in['cost']
        ax1 = plt.subplot(111)
        loc = 0.1
        for tech_idx in tech_list_Full:
            tech_cap = np.array(table_in[tech_idx+'_cap']) + np.array(table_in[tech_idx+'_fixed_cap'])
            tech_fixed_cost = np.array(cost_tables[tech_idx+'_fix'])
            tech_fixed_cost_unique = np.unique(tech_fixed_cost)
            if len(tech_fixed_cost_unique) == 1: 
                list_unique, list_unique_exist = [], []
                for idx in range(len(tech_fixed_cost)):
                    list_unique.append(system_cost[idx])
                    if tech_cap[idx] > 0: list_unique_exist.append(system_cost[idx]) 
                ax1.scatter(np.ones(len(list_unique))*loc+0.0, list_unique, s=1, c=color_colors[tech_idx])
                plot_box(ax1, loc+0.0, list_unique_exist)
                loc += 0.1 
                pass
            elif len(tech_fixed_cost_unique) == 3: 
                list_1, list_2, list_3 = [], [], []
                list_1_exist, list_2_exist, list_3_exist = [], [], []
                for idx in range(len(tech_fixed_cost)):
                    if tech_fixed_cost[idx] == tech_fixed_cost_unique[0]: 
                        list_1.append(system_cost[idx])
                        if tech_cap[idx] > 0: 
                            list_1_exist.append(system_cost[idx])
                    if tech_fixed_cost[idx] == tech_fixed_cost_unique[1]: 
                        list_2.append(system_cost[idx])
                        if tech_cap[idx] > 0: 
                            list_2_exist.append(system_cost[idx])
                    if tech_fixed_cost[idx] == tech_fixed_cost_unique[2]: 
                        list_3.append(system_cost[idx])
                        if tech_cap[idx] > 0: 
                            list_3_exist.append(system_cost[idx])
                ax1.scatter(np.ones(len(list_1))*loc+0.0, list_1, s=1, c=color_colors[tech_idx])
                plot_box(ax1, loc+0.0, list_1_exist)
                ax1.scatter(np.ones(len(list_2))*loc+0.1, list_2, s=1, c=color_colors[tech_idx])
                plot_box(ax1, loc+0.1, list_2_exist)
                ax1.scatter(np.ones(len(list_3))*loc+0.2, list_3, s=1, c=color_colors[tech_idx])
                plot_box(ax1, loc+0.2, list_3_exist)
                loc = loc + 0.3
        system_cost_min = np.min(system_cost)
        ax1.plot(np.r_[0.0, loc], np.r_[system_cost_min, system_cost_min], color='black', linewidth=0.8, linestyle='--')
        ax1.plot(np.r_[0.0, loc], np.r_[system_cost_min*1.05, system_cost_min*1.05], color='black', linewidth=0.8, linestyle='--')
        ax1.plot(np.r_[0.0, loc], np.r_[system_cost_min*1.1, system_cost_min*1.1], color='black', linewidth=0.8, linestyle='--')
        ax1.plot(np.r_[0.0, loc], np.r_[system_cost_min*1.2, system_cost_min*1.2], color='black', linewidth=0.8, linestyle='--')
        ax1.plot(np.r_[0.0, loc], np.r_[system_cost_min*1.5, system_cost_min*1.5], color='black', linewidth=0.8, linestyle='--')
        ax1.set_xlim(0.0, loc)
        ax1.set_ylim(0.05, 0.12)
        ax1.set_xticks(np.arange(0, loc, 0.1))
        # plt.show() 
        plt.savefig(name + '_sc.ps') 
        plt.clf()
    # """
    



    # """
    def system_cost_distribution_PDF(table_in):
        tech_list_Full = ['natgas_ccs', 'solar', 'wind', 'offwind', 'nuclear', 'geothermal', 'storage']
        system_cost = np.array(table_in['system_cost'])
        cost_tables = table_in['cost']
        for tech_idx in tech_list_Full:
            tech_cap = np.array(table_in[tech_idx+'_cap']) + np.array(table_in[tech_idx+'_fixed_cap'])
            tech_fixed_cost = np.array(cost_tables[tech_idx+'_fix'])
            tech_fixed_cost_unique = np.unique(tech_fixed_cost)
            if len(tech_fixed_cost_unique) == 3: 
                list_1, list_2, list_3 = [], [], []
                caps_1, caps_2, caps_3 = [], [], []
                for idx in range(len(tech_fixed_cost)): 
                    if tech_fixed_cost[idx] == tech_fixed_cost_unique[0]: list_1.append(system_cost[idx])
                    if tech_fixed_cost[idx] == tech_fixed_cost_unique[1]: list_2.append(system_cost[idx])
                    if tech_fixed_cost[idx] == tech_fixed_cost_unique[2]: list_3.append(system_cost[idx])
            # Distribution of costs
            ax1 = plt.subplot(111)
            x_axis = np.arange(0.05, 0.111, 0.001)
            try:
                kde_L = st.gaussian_kde(list_1); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_L.pdf(x_axis)*0.001, facecolor='#fdf289', edgecolor='#fdf289', linestyle='--', linewidth=0.8, alpha=0.5, label='L')
            except:
                print ('no L')
            try:
                kde_M = st.gaussian_kde(list_2); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_M.pdf(x_axis)*0.001, facecolor='#46edc8', edgecolor='#46edc8', linestyle='--', linewidth=0.8, alpha=0.5, label='M')
            except:
                print ('no M')
            try:
                kde_H = st.gaussian_kde(list_3); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_H.pdf(x_axis)*0.001, facecolor='#374d7c', edgecolor='#374d7c', linestyle='--', linewidth=0.8, alpha=0.5, label='H')
            except:
                print ('no H')
            ax1.set_xlim(0.05, 0.11)
            ax1.set_ylim(0, 0.15)
            plt.show() 
            # plt.savefig(f'panel_low_{tech_idx}.ps')
            plt.clf()
        
    
    def system_cost_distribution_PDF_whole(table_in, name):
        system_cost = np.array(table_in['system_cost'])
        x_axis = np.arange(0.05, 0.111, 0.001)
        ax1 = plt.subplot(111)
        kde = st.gaussian_kde(system_cost)
        ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde.pdf(x_axis)*0.001, facecolor='black', edgecolor='black', linestyle='--', linewidth=0.8, alpha=0.5)
        ax1.set_xlim(0.05, 0.10)
        ax1.set_ylim(0, 0.08)
        plt.show() 
        # plt.savefig(f'whole{name}.ps')
        plt.clf() 


    def cal_cap_range(table_in1, table_in2):
        bin_edges = list(np.arange(0, 0.101, 0.001))
        tech_list_Full = ['natgas', 'natgas_ccs', 'biopower', 'solar', 'wind', 'offwind', 'nuclear', 'geothermal', 'storage']
        # Numbers in text
        system_cost1 = np.array(table_in1['system_cost'])
        system_cost2 = np.array(table_in2['system_cost'])
        sc1_least = np.min(system_cost1); sc1_max = np.max(system_cost1)
        sc2_least = np.min(system_cost2); sc2_max = np.max(system_cost2)
        print (sc2_least, sc1_least, (sc2_least-sc1_least)/sc1_least*100)
        print (sc1_max)
        sc1_std = np.std(system_cost1)
        sc2_std = np.std(system_cost2) 
        print (sc2_std, sc1_std, (sc2_std-sc1_std)/sc1_std*100 )
        print (sc2_max, (sc1_max-sc2_max)/sc1_max*100)
        sc_50plarger = sc2_least * 1.5
        sc_ensemble_50pm = system_cost2[system_cost2>sc_50plarger]
        print (len(sc_ensemble_50pm)/len(system_cost2)*100)
        stop 
        ax1 = plt.subplot(111)
        loc = 1
        for tech_idx in tech_list_Full:
            cap_greenfield = np.array(table_in1[tech_idx+'_cap'])
            cap_transients = np.array(table_in2[tech_idx+'_cap']) + np.array(table_in2[tech_idx+'_fixed_cap'])
            diff = np.mean(cap_transients - cap_greenfield)
            ax1.bar(loc, diff, width=0.8, color=color_colors[tech_idx])
            loc += 1
        ax1.plot(np.r_[0, loc], np.r_[0, 0], color='black', linewidth=0.5)
        ax1.set_xlim(0, loc)
        ax1.set_xticks(np.arange(1, loc, 1))
        ax1.set_ylim(-0.2, 0.7)
        # plt.show()
        plt.savefig('change_cap.ps')
        plt.clf() 

    with open('Cost_Uncertainty_Transient_ensemble2050.pickle', 'rb') as handle:
        table_transient_2050 = pickle.load(handle) 
    with open('Cost_Uncertainty_Scenario2050.pickle', 'rb') as handle:
        Table_scenario2050_Full = pickle.load(handle) 
    # with open('Cost_Uncertainty_GeoCapEnsemble.pickle', 'rb') as handle:
    #     Table_scenario2050_GeoCap = pickle.load(handle) 

    # system_cost_distribution(Table_scenario2050_Full[0], 'greeofield')
    # system_cost_distribution(table_transient_2050[0], 'transient')
    # system_cost_distribution_PDF(table_transient_2050[0])

    # system_cost_distribution_PDF_whole(Table_scenario2050_Full[0], 'noS')
    # system_cost_distribution_PDF_whole(Table_scenario2050_GeoCap[0], 'withS07')
    # system_cost_distribution_PDF_whole(Table_scenario2050_GeoCap[1], 'withS05')
    # system_cost_distribution_PDF_whole(Table_scenario2050_GeoCap[2], 'withS03')

    cal_cap_range(Table_scenario2050_Full[0], table_transient_2050[0])
    # """


    # # Transient new gas
    # with open('Cost_Uncertainty_Transient_NewGas.pickle', 'rb') as handle:
    #     table_transient_NewGas = pickle.load(handle) 
    # initial_cap_list = []
    # no_new_additions = []
    # final_capacities = []
    # for idx in range(729):
    #     natgas_cap = np.array(table_transient_NewGas[idx]['natgas_cap']).astype('float') 
    #     natgas_ccs_cap = np.array(table_transient_NewGas[idx]['natgas_ccs_cap']).astype('float')
    #     natgas_fixed_cap = np.array(table_transient_NewGas[idx]['natgas_fixed_cap']).astype('float')
    #     natgas_ccs_fixed_cap = np.array(table_transient_NewGas[idx]['natgas_ccs_fixed_cap']).astype('float') 
    #     total_fossil_cap = natgas_cap + natgas_ccs_cap + natgas_fixed_cap + natgas_ccs_fixed_cap
    #     initial_cap_list.append(total_fossil_cap[0])
    #     no_new_additions.append(total_fossil_cap[0]*(1-1/30)**31)
    #     final_capacities.append(total_fossil_cap[-1])
    # diff = np.array(final_capacities) - np.array(no_new_additions)
    # print (diff) 