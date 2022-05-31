from turtle import fillcolor
import numpy as np
import pickle, os
from pyrsistent import b
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy.stats as st

###################################################################################################################################################################################

color_colors = {'natgas': 'black', 'natgas_ccs': 'grey', 'biopower': 'lightslategrey', 
                'solar': 'wheat', 'wind': 'skyblue', 'offwind': 'darkblue', 
                'nuclear': 'tomato', 'geothermal': 'darkred', 
                'storage': 'lightpink', 'pgp': 'lightgreen'} 

def fig_order2_systemcost():
    def plot_box(ax, pos, list_exist):
        if len(list_exist)>0:
            min_bound = np.min(np.array(list_exist))
            max_bound = np.max(np.array(list_exist))
            ax.plot( np.r_[pos-0.02, pos+0.02],  np.r_[min_bound, min_bound], color='black', linewidth=0.8    )
            ax.plot( np.r_[pos-0.02, pos+0.02],  np.r_[max_bound, max_bound], color='black', linewidth=0.8    )
            # ax.plot( np.r_[pos-0.02, pos-0.02],  np.r_[min_bound, max_bound], color='black', linewidth=0.8    )
            # ax.plot( np.r_[pos+0.02, pos+0.02],  np.r_[min_bound, max_bound], color='black', linewidth=0.8    )
            ax.plot( np.r_[pos,      pos     ],  np.r_[min_bound, max_bound], color='black', linewidth=0.8    )
    def system_cost_distribution(table_in):
        bin_edges = list(np.arange(0, 0.101, 0.001))
        # tech_list_Full = ['natgas', 'natgas_ccs', 'biopower', 'solar', 'wind', 'offwind', 'nuclear', 'geothermal', 'storage']
        tech_list_Full = ['biopower', 'solar', 'wind', 'offwind', 'nuclear', 'geothermal', 'storage']
        system_cost = np.array(table_in['system_cost'])
        cost_tables = table_in['cost']
        ax1 = plt.subplot(111)
        loc = 0.1
        for tech_idx in tech_list_Full:
            tech_cap = np.array(table_in[tech_idx+'_cap'])
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
        ax1.set_ylim(0.05, 0.1)
        ax1.set_xticks(np.arange(0, loc, 0.1))
        plt.show() 
        # plt.savefig('system_cost.ps') 
        plt.clf()
    with open('Cost_Uncertainty_Scenario2050.pickle', 'rb') as handle:
        Table_scenario2050_Full = pickle.load(handle)  #[100p, 99p]
    system_cost_distribution(Table_scenario2050_Full[0])

    
    




def fig_order2_his():
    def system_cost_distribution(table_in):
        bin_edges = list(np.arange(0.05, 0.101, 0.001))
        # tech_list_Full = ['natgas', 'natgas_ccs', 'biopower', 'solar', 'wind', 'offwind', 'nuclear', 'geothermal', 'storage']
        # tech_list_Full = ['solar', 'wind', 'offwind', 'geothermal', 'storage']
        tech_list_Full = ['natgas_ccs', 'solar', 'wind', 'offwind', 'geothermal', 'storage']
        system_cost = np.array(table_in['system_cost'])

        # Numbers in text
        print ()
        print ()
        print (np.max(system_cost), np.min(system_cost), (np.max(system_cost)-np.min(system_cost))/np.min(system_cost)*100) 
        a = (np.max(system_cost)-np.min(system_cost))/np.min(system_cost)*100
        # stop 

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
                    # if tech_fixed_cost[idx] == tech_fixed_cost_unique[0] and tech_cap[idx] > 0: caps_1.append(tech_cap[idx])
                    # if tech_fixed_cost[idx] == tech_fixed_cost_unique[1] and tech_cap[idx] > 0: caps_2.append(tech_cap[idx])
                    # if tech_fixed_cost[idx] == tech_fixed_cost_unique[2] and tech_cap[idx] > 0: caps_3.append(tech_cap[idx])
            # Distribution of costs
            ax1 = plt.subplot(111)
            # x_axis = np.arange(0.05, 0.101, 0.001)
            x_axis = np.arange(0.04, 0.101, 0.001)
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
            
            # Numbers in text
            print ()
            print ()
            print (tech_idx)
            b = (np.max(list_1)-np.min(list_1))/np.min(list_1)*100
            c = (np.max(list_2)-np.min(list_2))/np.min(list_2)*100
            d = (np.max(list_3)-np.min(list_3))/np.min(list_3)*100
            print (np.max(list_1), np.min(list_1), b, (a - b)/a*100 )
            print (np.max(list_2), np.min(list_2), c, (a - c)/a*100 )
            print (np.max(list_3), np.min(list_3), d, (a - d)/a*100 )
            # stop 

            # # Distribution of caps
            # ax1 = plt.subplot(111)
            # ax1.boxplot(list_1, positions=[1], widths=0.6, medianprops=dict(color=color_colors[tech_idx]))
            # ax1.boxplot(list_2, positions=[2], widths=0.6, medianprops=dict(color=color_colors[tech_idx]))
            # ax1.boxplot(list_3, positions=[3], widths=0.6, medianprops=dict(color=color_colors[tech_idx]))
            # # ax1.set_xlim(0.05, 0.1)
            # ax1.set_xlim(0.04, 0.1)
            # ax1.set_ylim(0, 0.15)
            # # plt.legend(loc="upper left")
            # # plt.show() 
            # plt.savefig(f'panel_low_{tech_idx}.ps')
            # plt.clf()

    with open('Cost_Uncertainty_Scenario2050.pickle', 'rb') as handle:
        Table_scenario2050_Full = pickle.load(handle)  #[100p, 99p]
    system_cost_distribution(Table_scenario2050_Full[0])
    # system_cost_distribution(Table_scenario2050_Full[1])






def fig_order2_dispatch():

    def plot_dispatch_distribution(table_in1, tech_in2, tech_list, name):
        # upper_y_list = [0.07, 0.03, 0.4, 0.03, 0.5]
        upper_y_list = [3.0, 0.07, 0.04, 0.1, 0.03, 0.5]
        cost_tables = tech_in2['cost']
        count = 0 
        for tech_idx in tech_list:
            tech_cap = np.array(tech_in2[tech_idx+'_cap'])
            tech_fixed_cost = np.array(cost_tables[tech_idx+'_fix'])
            tech_fixed_cost_unique = np.unique(tech_fixed_cost)
            dispatch_list_1, dispatch_list_2, dispatch_list_3 = [], [], []
            for idx in range(729):
                try:
                    dispatch_tech = table_in1[idx][tech_idx+'_dispatch']
                except:
                    dispatch_tech = table_in1[idx][tech_idx+'_potential']
                # if tech_fixed_cost[idx] == tech_fixed_cost_unique[0] and tech_cap[idx] > 0: dispatch_list_1.append(dispatch_tech)
                # if tech_fixed_cost[idx] == tech_fixed_cost_unique[1] and tech_cap[idx] > 0: dispatch_list_2.append(dispatch_tech)
                # if tech_fixed_cost[idx] == tech_fixed_cost_unique[2] and tech_cap[idx] > 0: dispatch_list_3.append(dispatch_tech)
                if tech_fixed_cost[idx] == tech_fixed_cost_unique[0]: dispatch_list_1.append(dispatch_tech)
                if tech_fixed_cost[idx] == tech_fixed_cost_unique[1]: dispatch_list_2.append(dispatch_tech)
                if tech_fixed_cost[idx] == tech_fixed_cost_unique[2]: dispatch_list_3.append(dispatch_tech)
            ax1 = plt.subplot(111)
            x_axis = np.arange(0, 1.21, 0.01)
            try:
                kde_L = st.gaussian_kde(dispatch_list_1); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_L.pdf(x_axis)*0.01, facecolor='#fdf289', edgecolor='#fdf289', linestyle='--', linewidth=0.8, alpha=0.5, label='L')
            except:
                print ('no L')
            try:
                kde_M = st.gaussian_kde(dispatch_list_2); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_M.pdf(x_axis)*0.01, facecolor='#46edc8', edgecolor='#46edc8', linestyle='--', linewidth=0.8, alpha=0.5, label='M')
            except:
                print ('no M')
            try:
                kde_H = st.gaussian_kde(dispatch_list_3); ax1.fill_between(x_axis, np.zeros(len(x_axis)), kde_H.pdf(x_axis)*0.01, facecolor='#374d7c', edgecolor='#374d7c', linestyle='--', linewidth=0.8, alpha=0.5, label='H')
            except:
                print ('no H')
            ax1.set_xlim(0, 1.2)
            ax1.set_ylim(0, upper_y_list[count])
            plt.show() 
            plt.savefig(f'dispatch_distribution_{tech_idx}.ps') 
            # plt.clf()
            count +=1
    with open('Cost_Uncertainty_dispatch_mean.pickle', 'rb') as handle:
        Table_scenario2050_Full_100p_dispatch, Table_scenario2050_Full_99p_dispatch = pickle.load(handle)
    with open('Cost_Uncertainty_Scenario2050.pickle', 'rb') as handle:
        Table_scenario2050_Full = pickle.load(handle)  #[100p, 99p]
    # tech_list_Full = ['solar', 'wind', 'offwind', 'geothermal', 'storage']
    # plot_dispatch_distribution(Table_scenario2050_Full_100p_dispatch, Table_scenario2050_Full[0], tech_list_Full, 'Year2050_100p')
    # tech_list_Full = ['natgas_ccs', 'solar', 'wind', 'offwind', 'geothermal', 'storage']
    # plot_dispatch_distribution(Table_scenario2050_Full_99p_dispatch, Table_scenario2050_Full[1], tech_list_Full, 'Year2050_99p')
