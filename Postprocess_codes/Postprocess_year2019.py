import numpy as np
import pickle, os
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

if __name__ == "__main__":

    # Plot
    xlist = np.array([100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 
                      40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0])/100
    x_axis = 1 - 0.5**( np.log(xlist)/np.log(0.2) )
    xticks_addition_org = np.array([50.0, 10.0, 1.0])/100
    xticks_addition_cov = 1 - 0.5**( np.log(xticks_addition_org)/np.log(0.2) )
    xticks = np.r_[[0, 0.5, 0.75, 1.0], xticks_addition_cov]
    # Costs
    def plot_cost(CurrentCase, ylist_type, default_case_name):
        ax = plt.subplot(111)

        if ylist_type == 'Less':
            y_lists = [np.array(CurrentCase['natgas_tot']), np.array(CurrentCase['natgas_ccs_tot']), 
                       np.array(CurrentCase['solar_fix']),  np.array(CurrentCase['wind_fix']), 
                       np.array(CurrentCase['nuclear_fix']),
                       np.array(CurrentCase['storage_fix'])]
            y_color = ['black', 'grey', 'wheat', 'skyblue', 'tomato', 'lightpink']
        
        if ylist_type == 'Full':
            y_lists = [np.array(CurrentCase['natgas_tot']),  np.array(CurrentCase['natgas_ccs_tot']),  np.array(CurrentCase['biopower_tot']), 
                       np.array(CurrentCase['solar_fix']),   np.array(CurrentCase['wind_fix']),        np.array(CurrentCase['offwind_fix']), 
                       np.array(CurrentCase['nuclear_fix']), np.array(CurrentCase['geothermal_fix']),
                       np.array(CurrentCase['storage_fix'])]
            y_color = ['black', 'grey', 'lightslategrey', 'wheat', 'skyblue', 'darkblue', 'tomato', 'brown', 'lightpink']

        if ylist_type == 'Less_PGP':
            y_lists = [np.array(CurrentCase['natgas_tot']), np.array(CurrentCase['natgas_ccs_tot']), 
                       np.array(CurrentCase['solar_fix']),  np.array(CurrentCase['wind_fix']), 
                       np.array(CurrentCase['nuclear_fix']),
                       np.array(CurrentCase['storage_fix']),
                       np.array(CurrentCase['to_PGP_fix']) + np.array(CurrentCase['PGP_storage_fix']) + np.array(CurrentCase['from_PGP_fix'])]
            y_color = ['black', 'grey', 'wheat', 'skyblue', 'tomato', 'lightpink', 'lightgreen']
        
        if ylist_type == 'Full_PGP':
            y_lists = [np.array(CurrentCase['natgas_tot']),  np.array(CurrentCase['natgas_ccs_tot']),  np.array(CurrentCase['biopower_tot']), 
                       np.array(CurrentCase['solar_fix']),   np.array(CurrentCase['wind_fix']),        np.array(CurrentCase['offwind_fix']), 
                       np.array(CurrentCase['nuclear_fix']), np.array(CurrentCase['geothermal_fix']),
                       np.array(CurrentCase['storage_fix']),
                       np.array(CurrentCase['to_PGP_fix']) + np.array(CurrentCase['PGP_storage_fix']) + np.array(CurrentCase['from_PGP_fix'])]
            y_color = ['black', 'grey', 'lightslategrey', 'wheat', 'skyblue', 'darkblue', 'tomato', 'brown', 'lightpink', 'lightgreen']

        if ylist_type == 'NoBi':
            y_lists = [np.array(CurrentCase['natgas_tot']),  np.array(CurrentCase['natgas_ccs_tot']),  
                       np.array(CurrentCase['solar_fix']),   np.array(CurrentCase['wind_fix']),        np.array(CurrentCase['offwind_fix']), 
                       np.array(CurrentCase['nuclear_fix']), np.array(CurrentCase['geothermal_fix']),
                       np.array(CurrentCase['storage_fix'])]
            y_color = ['black', 'grey', 'wheat', 'skyblue', 'darkblue', 'tomato', 'brown', 'lightpink']
        
        if ylist_type == 'NoNu':
            y_lists = [np.array(CurrentCase['natgas_tot']),  np.array(CurrentCase['natgas_ccs_tot']),  np.array(CurrentCase['biopower_tot']), 
                       np.array(CurrentCase['solar_fix']),   np.array(CurrentCase['wind_fix']),        np.array(CurrentCase['offwind_fix']), 
                       np.array(CurrentCase['geothermal_fix']),
                       np.array(CurrentCase['storage_fix'])]
            y_color = ['black', 'grey', 'lightslategrey', 'wheat', 'skyblue', 'darkblue', 'brown', 'lightpink']
        
        if ylist_type == 'NoBo':
            y_lists = [np.array(CurrentCase['natgas_tot']),  np.array(CurrentCase['natgas_ccs_tot']), 
                       np.array(CurrentCase['solar_fix']),   np.array(CurrentCase['wind_fix']),        np.array(CurrentCase['offwind_fix']), 
                       np.array(CurrentCase['geothermal_fix']),
                       np.array(CurrentCase['storage_fix'])]
            y_color = ['black', 'grey', 'wheat', 'skyblue', 'darkblue', 'brown', 'lightpink']

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
        # ax.set_ylim(0, 0.18)
        plt.show()
        # plt.savefig(default_case_name+'.ps')
        plt.clf()


    with open('Cost_Uncertainty_Scenario2019.pickle', 'rb') as handle:
        Table_scenario2019_Full, Table_scenario2019_Full_PGP, Table_scenario2019_Less, Table_scenario2019_Less_PGP = pickle.load(handle) 
    idx = 3
    plot_cost(Table_scenario2019_Full[idx],     'Full',     'Full2019') 
    # plot_cost(Table_scenario2019_Full_PGP[idx], 'Full_PGP', 'Full_PGP2019') 
    # plot_cost(Table_scenario2019_Less[idx],     'Less',     'Less2019') 
    # plot_cost(Table_scenario2019_Less_PGP[idx], 'Less_PGP', 'Less_PGP2019') 

    # with open('Cost_Uncertainty_Scenario2019_NoBiNu.pickle', 'rb') as handle:
    #     Table_scenario2019_NoBi, Table_scenario2019_NoNu, Table_scenario2019_NoBo = pickle.load(handle) 
    # plot_cost(Table_scenario2019_NoBi[0],     'NoBi',     'NoBi2019')
    # plot_cost(Table_scenario2019_NoNu[0],     'NoNu',     'NoNu2019')
    # plot_cost(Table_scenario2019_NoBo[0],     'NoBo',     'NoBo2019')

