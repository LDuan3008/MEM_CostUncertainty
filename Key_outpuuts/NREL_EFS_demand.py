import numpy as np
import pickle
import matplotlib.pyplot as plt
from Shared_fun import create_table, update_series

data_path = '/Users/leiduan/Desktop/File/Research/Paper/Lei/Ongoing/Duan et al. 2021_cost_uncertainties/code/NREL_EFS_data/'

# file_list = ['ProcessedEFSLoadProfile_High_Moderate.pickle',
#              'ProcessedEFSLoadProfile_High_Rapid.pickle',
#              'ProcessedEFSLoadProfile_High_Slow.pickle',
#              'ProcessedEFSLoadProfile_Medium_Moderate.pickle',
#              'ProcessedEFSLoadProfile_Medium_Rapid.pickle',
#              'ProcessedEFSLoadProfile_Medium_Slow.pickle',
#              'ProcessedEFSLoadProfile_Reference_Moderate.pickle',
#              'ProcessedEFSLoadProfile_Reference_Rapid.pickle',
#              'ProcessedEFSLoadProfile_Reference_Slow.pickle']

year_ref = {'2018':0, '2020':1, '2024':2, '2030':3, '2040':4, '2050':5}
state_ref = {'AL':0, 'AR':1, 'AZ':2, 'CA':3, 'CO':4, 'CT':5, 'DE':6, 'FL':7, 'GA':8, 'IA':9, 'ID':10, 'IL':11, 'IN':12, 'KS':13,
 'KY':14, 'LA':15, 'MA':16, 'MD':17, 'ME':18, 'MI':19, 'MN':20, 'MO':21, 'MS':22, 'MT':23, 'NC':24, 'ND':25, 'NE':26, 'NH':27,
 'NJ':28, 'NM':29, 'NV':30, 'NY':31, 'OH':32, 'OK':33, 'OR':34, 'PA':35, 'RI':36, 'SC':37, 'SD':38, 'TN':39, 'TX':40, 'UT':41,
 'VA':42, 'VT':43, 'WA':44, 'WI':45, 'WV':46, 'WY':47}
sector_ref = {'Commercial':0, 'Industrial':1, 'Residential':2, 'Transportation':3}
EST, CST, MST, PST = -5, -6, -7, -8
time_zero_ref = {'AL':CST, 'AR':CST, 'AZ':MST, 'CA':PST, 'CO':MST, 'CT':EST, 'DE':EST, 'FL':EST, 'GA':EST, 'IA':CST,
                 'ID':MST, 'IL':CST, 'IN':EST, 'KS':CST, 'KY':CST, 'LA':CST, 'MA':EST, 'MD':EST, 'ME':EST, 'MI':EST,
                 'MN':CST, 'MO':CST, 'MS':CST, 'MT':MST, 'NC':EST, 'ND':CST, 'NE':CST, 'NH':EST, 'NJ':EST, 'NM':MST,
                 'NV':PST, 'NY':EST, 'OH':EST, 'OK':CST, 'OR':PST, 'PA':EST, 'RI':EST, 'SC':EST, 'SD':CST, 'TN':CST,
                 'TX':CST, 'UT':MST, 'VA':EST, 'VT':EST, 'WA':PST, 'WI':CST, 'WV':EST, 'WY':MST}

def get_load_profile(fname):
    with open(data_path + fname, 'rb') as handle:
        OpenArray = pickle.load(handle) #(year, state, sector, hour)
    state_sum = np.sum(OpenArray, axis=1)
    secto_sum = np.sum(state_sum, axis=1)
    return secto_sum[-1]

def get_flexibleload_profile(fname):
    with open(data_path + fname, 'rb') as handle:
        OpenArray = pickle.load(handle) #(sce1, sce2, year, state, sector, hour)
    state_sum = np.sum(OpenArray, axis=3)
    secto_sum = np.sum(state_sum, axis=3)
    return secto_sum[:, :, -1]

def get_monthly_mean(inputs):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return_outputs = []
    total_days_counted = 0
    for i in range(len(days_in_months)): 
        current_days_in_month = days_in_months[i]
        start = total_days_counted * 24
        end = (total_days_counted + current_days_in_month) * 24
        monthly_mean = np.mean(inputs[start:end])
        return_outputs.append(monthly_mean)
        total_days_counted += current_days_in_month
    return return_outputs


###########
# After some exploration, it seems that the EFS data is at local CST time
# We assume it's CST time and convert to UTC for futher use 

# US demand from EIA
d_input_name = 'US_demand_unnormalized.csv'
d1, load_profile_now = create_table(2019, d_input_name, 1)
load_profile_now_shifted = np.concatenate( (load_profile_now[6:], load_profile_now[:6]), axis=0 )
load_profile_now_normalized = load_profile_now_shifted / np.mean(load_profile_now_shifted)
load_profile_now_hours = np.mean(load_profile_now_normalized.reshape(-1, 24), axis=0)
load_profile_now_daily = np.mean(load_profile_now_normalized.reshape(-1, 24), axis=1)
load_profile_now_month = get_monthly_mean(load_profile_now_normalized)

# US 2050 demand from NREL EFS report 
to_compare = 'ProcessedEFSLoadProfile_High_Moderate.pickle' 
load_profile_2050 = get_load_profile(to_compare) 

# US 2050 flexible demand from NREL EFS report 
flexible_demand = 'ProcessedEFSFlexLoadProfiles_High.pickle'
flexibleload_profile_2050 = get_flexibleload_profile(flexible_demand)


print () 
print () 
idx1 = 0
idx2 = 1
a = np.mean(load_profile_2050)
b = np.mean(flexibleload_profile_2050[idx1,idx2])
print (b/a)
c = flexibleload_profile_2050[idx1,idx2] / load_profile_2050
print (np.max(c), np.min(c))



# # Produce demand outputs
# shift_load_frm_CST_to_UTC = np.concatenate( (load_profile_2050[-6:], load_profile_2050[:-6]), axis=0 )
# np.savetxt('test.csv', shift_load_frm_CST_to_UTC, fmt='%s')
# # with open('NREL_EFS_2050demand_High_Moderate.pickle', 'wb') as handle:
# #     pickle.dump(shift_load_frm_CST_to_UTC, handle, protocol=pickle.HIGHEST_PROTOCOL) 
# stop 

# load_profile_2050_normalized = load_profile_2050 / np.mean(load_profile_2050) 
# load_profile_2050_hours = np.mean(load_profile_2050_normalized.reshape(-1, 24), axis=0) 
# load_profile_2050_daily = np.mean(load_profile_2050_normalized.reshape(-1, 24), axis=1) 
# load_profile_2050_month = get_monthly_mean(load_profile_2050_normalized) 

# ax1 = plt.subplot(211) 
# ax1.plot(np.arange(len(load_profile_now_hours))+1, load_profile_now_hours, color='black', linestyle='solid')
# ax1.plot(np.arange(len(load_profile_2050_hours))+1, load_profile_2050_hours, color='firebrick', linestyle='solid')
# ax1.set_xlim(1, 24)
# ax1.set_xticks(np.arange(1, 25, 1))
# ax2 = plt.subplot(212) 
# ax2.plot(np.arange(len(load_profile_now_month))+1, load_profile_now_month, color='black', linestyle='solid')
# ax2.plot(np.arange(len(load_profile_2050_month))+1, load_profile_2050_month, color='firebrick', linestyle='solid')
# ax2.set_xlim(1, 12)
# ax2.set_xticks(np.arange(1, 13, 1))
# ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
# plt.show() 
# plt.clf() 









"""
print () 
print () 
print (np.std(load_profile_now_normalized) )
print (np.std(load_profile_2050_normalized) ) 

list1, list2 = [], []
for day_idx in range(365):
    tmp1 = np.std( load_profile_now_normalized[day_idx*24:day_idx*24+24] )
    tmp2 = np.std( load_profile_2050_normalized[day_idx*24:day_idx*24+24] )
    list1.append(tmp1)
    list2.append(tmp2)
print () 
print ()
print ( np.mean(list1) ) 
print ( np.mean(list2) )
plt.plot(np.arange(365), np.array(list1), color='black')
plt.plot(np.arange(365), np.array(list2), color='firebrick')
plt.show() 
plt.clf()

list1_con = np.convolve(load_profile_now_normalized, np.ones(24)/24, mode='valid')
list2_con = np.convolve(load_profile_2050_normalized, np.ones(24)/24, mode='valid')
print () 
print ()
print ( np.std(list1_con) )
print ( np.std(list2_con) )
plt.plot(np.arange(8737), np.array(list1_con), color='black')
plt.plot(np.arange(8737), np.array(list2_con), color='firebrick')
plt.show() 
plt.clf()
# """