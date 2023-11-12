import numpy as np 
import pickle 

def capital_recovery_factor(lifetime, Discount_rate=0.07):
    crf = Discount_rate*(1+Discount_rate)**lifetime/((1+Discount_rate)**lifetime-1)
    return crf

info = {}
######################################## Natural gas 
natgas_capital_cost = np.array([1054, 1049, 1044, 1042, 1030, 1025, 1025, 1021, 1012, 1008, 1003, 999, 996, 991, 985, 981, 977, 971, 967, 964, 959, 955, 951, 946, 943, 939, 935, 932, 928, 922, 918, 907])
natgas_fixed_OandM = 27 
natgas_var_OandM = 2
natgas_fuel_cost = 8
natgas_lifetime = 30
info['natgas_fhc'] = (natgas_capital_cost * capital_recovery_factor(natgas_lifetime) + natgas_fixed_OandM) / 8760
info['natgas_vhc'] = (natgas_var_OandM + natgas_fuel_cost) / 1000
######################################## CCS
CCS_capital_cost_L = np.array([2670, 2490, 2312, 2139, 2094, 2064, 2039, 2005, 1967, 1933, 1900, 1866, 1834, 1800, 1765, 1716, 1667, 1616, 1569, 1522, 1509, 1496, 1481, 1468, 1456, 1444, 1432, 1419, 1406, 1391, 1378, 1353])
CCS_capital_cost_M = np.array([2670, 2571, 2474, 2380, 2342, 2320, 2304, 2277, 2247, 2219, 2193, 2167, 2141, 2114, 2084, 2049, 2015, 1979, 1945, 1911, 1896, 1879, 1861, 1845, 1830, 1814, 1799, 1783, 1766, 1749, 1731, 1700])
CCS_capital_cost_H = np.array([2670, 2652, 2636, 2622, 2590, 2576, 2569, 2550, 2525, 2505, 2487, 2466, 2448, 2426, 2403, 2384, 2363, 2342, 2321, 2301, 2283, 2263, 2241, 2221, 2203, 2184, 2167, 2147, 2126, 2105, 2085, 2047])
CCS_fixed_OandM_L = np.array([65, 65, 65, 65, 65, 64, 64, 63, 63, 62, 62, 62, 61, 61, 60, 59, 58, 58, 57, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56])
CCS_fixed_OandM_M = np.array([65, 65, 65, 65, 65, 65, 64, 64, 64, 64, 64, 63, 63, 63, 63, 62, 62, 61, 61, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60])
CCS_fixed_OandM_H = np.array([65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65])
CCS_var_OandM = 5
CCS_fuel_cost = 8
CCS_lifetime = 30
info['CCS_fhc_L'] = (CCS_capital_cost_L * capital_recovery_factor(CCS_lifetime) + CCS_fixed_OandM_L) / 8760
info['CCS_fhc_M'] = (CCS_capital_cost_M * capital_recovery_factor(CCS_lifetime) + CCS_fixed_OandM_M) / 8760
info['CCS_fhc_H'] = (CCS_capital_cost_H * capital_recovery_factor(CCS_lifetime) + CCS_fixed_OandM_H) / 8760
info['CCS_vhc'] = (CCS_var_OandM + CCS_fuel_cost) / 1000
######################################## Solar
solar_capital_cost_L = np.array([1391, 1377, 1303, 1229, 1155, 1081, 1007, 933,  859,  785,  712,  638,  630,  622,  614,  606,  598,  591,  583,  575,  567, 559, 551, 544, 536, 528, 520, 512, 504, 496, 489, 481])
solar_capital_cost_M = np.array([1391, 1377, 1316, 1256, 1196, 1136, 1076, 1016, 956,  896,  836,  776,  769,  762,  755,  748,  741,  734,  728,  721,  714, 707, 700, 693, 686, 679, 672, 665, 658, 651, 645, 638])
solar_capital_cost_H = np.array([1391, 1377, 1357, 1338, 1318, 1299, 1279, 1260, 1241, 1221, 1202, 1182, 1162, 1142, 1121, 1101, 1081, 1060, 1040, 1020, 999, 979, 959, 938, 918, 898, 878, 857, 837, 817, 796, 776])
solar_fixed_OandM_L = np.array([23, 23, 23, 22, 21, 20, 19, 18, 17, 17, 16, 15, 15, 15, 15, 14, 14, 14, 14, 14, 14, 14, 14, 13, 13, 13, 13, 13, 13, 13, 13, 12])
solar_fixed_OandM_M = np.array([23, 23, 23, 22, 21, 21, 20, 19, 19, 18, 17, 17, 17, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 15, 15, 15, 15, 15, 15, 15])
solar_fixed_OandM_H = np.array([23, 23, 23, 23, 23, 22, 22, 22, 22, 21, 21, 21, 21, 20, 20, 20, 20, 20, 19, 19, 19, 19, 19, 18, 18, 18, 18, 17, 17, 17, 17, 17])
solar_lifetime = 30
info['solar_fhc_L'] = (solar_capital_cost_L * capital_recovery_factor(solar_lifetime) + solar_fixed_OandM_L) / 8760
info['solar_fhc_M'] = (solar_capital_cost_M * capital_recovery_factor(solar_lifetime) + solar_fixed_OandM_M) / 8760
info['solar_fhc_H'] = (solar_capital_cost_H * capital_recovery_factor(solar_lifetime) + solar_fixed_OandM_H) / 8760
######################################## Wind 
wind_capital_cost_L = np.array([1436, 1369, 1302, 1235, 1168, 1101, 1035, 968,  901,  834,  767,  700,  691, 683, 674, 665, 656, 648, 639, 630, 621, 613, 604, 595, 586, 578, 569, 560, 551, 543, 534, 525])
wind_capital_cost_M = np.array([1436, 1392, 1348, 1303, 1259, 1215, 1171, 1127, 1083, 1038, 994,  950,  941, 931, 922, 912, 903, 893, 884, 874, 865, 855, 846, 836, 827, 817, 808, 798, 789, 779, 770, 760])
wind_capital_cost_H = np.array([1436, 1396, 1357, 1317, 1277, 1238, 1198, 1159, 1119, 1079, 1040, 1000, 995, 990, 985, 980, 975, 970, 965, 960, 955, 950, 945, 940, 935, 930, 925, 920, 915, 910, 905, 900])
wind_fixed_OandM_L = np.array([43, 42, 41, 41, 40, 39, 38, 38, 37, 36, 35, 34, 34, 33, 33, 32, 32, 31, 31, 30, 30, 29, 29, 28, 28, 27, 27, 26, 26, 25, 25, 24])
wind_fixed_OandM_M = np.array([43, 43, 42, 42, 42, 41, 41, 40, 40, 40, 39, 39, 39, 38, 38, 38, 37, 37, 37, 37, 36, 36, 36, 35, 35, 35, 35, 34, 34, 34, 33, 33])
wind_fixed_OandM_H = np.array([43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 41, 41, 41, 41, 41])
wind_lifetime = 30 
info['wind_fhc_L'] = (wind_capital_cost_L * capital_recovery_factor(wind_lifetime) + wind_fixed_OandM_L) / 8760
info['wind_fhc_M'] = (wind_capital_cost_M * capital_recovery_factor(wind_lifetime) + wind_fixed_OandM_M) / 8760
info['wind_fhc_H'] = (wind_capital_cost_H * capital_recovery_factor(wind_lifetime) + wind_fixed_OandM_H) / 8760
######################################## Offshore wind 
offwind_capital_cost_L = np.array([5002, 4621, 4337, 4107, 3910, 3737, 3581, 3437, 3304, 3179, 3061, 2949, 2888, 2831, 2778, 2728, 2681, 2636, 2594, 2553, 2515, 2478, 2443, 2410, 2377, 2346, 2316, 2287, 2259, 2232, 2206, 2181])
offwind_capital_cost_M = np.array([5183, 4848, 4598, 4395, 4221, 4068, 3929, 3802, 3684, 3573, 3468, 3368, 3314, 3265, 3218, 3174, 3133, 3094, 3057, 3022, 2988, 2956, 2925, 2896, 2867, 2840, 2814, 2789, 2764, 2740, 2718, 2695])
offwind_capital_cost_H = np.array([5469, 5250, 5086, 4950, 4834, 4730, 4635, 4547, 4466, 4388, 4315, 4245, 4211, 4179, 4150, 4123, 4097, 4072, 4049, 4027, 4005, 3985, 3966, 3947, 3929, 3912, 3896, 3880, 3864, 3849, 3835, 3821])
offwind_fixed_OandM_L = np.array([80, 75, 71, 69, 66, 64, 62, 61, 60, 58, 57, 56, 55, 54, 53, 53, 52, 51, 51, 50, 49, 49, 48, 48, 47, 47, 46, 46, 45, 45, 44, 44])
offwind_fixed_OandM_M = np.array([83, 79, 75, 73, 71, 69, 68, 66, 65, 64, 63, 62, 61, 60, 60, 59, 58, 58, 57, 57, 56, 56, 55, 55, 54, 54, 53, 53, 53, 52, 52, 51])
offwind_fixed_OandM_H = np.array([88, 85, 83, 81, 80, 79, 78, 77, 76, 76, 75, 74, 74, 73, 73, 72, 72, 72, 71, 71, 71, 70, 70, 70, 69, 69, 69, 69, 68, 68, 68, 68])
offwind_lifetime = 30 
info['offwind_fhc_L'] = (offwind_capital_cost_L * capital_recovery_factor(offwind_lifetime) + offwind_fixed_OandM_L) / 8760
info['offwind_fhc_M'] = (offwind_capital_cost_M * capital_recovery_factor(offwind_lifetime) + offwind_fixed_OandM_M) / 8760
info['offwind_fhc_H'] = (offwind_capital_cost_H * capital_recovery_factor(offwind_lifetime) + offwind_fixed_OandM_H) / 8760
######################################## Nuclear
nuclear_capital_cost = np.array([7388, 7334, 7279, 7257, 7198, 7044, 7044, 7007, 6972, 6934, 6893, 6846, 6807, 6755, 6699, 6653, 6606, 6556, 6508, 6463, 6420, 6373, 6322, 6277, 6234, 6191, 6152, 6107, 6059, 6010, 5962, 5856])
nuclear_fixed_OandM = 145
nuclear_var_OandM = 2
nuclear_fuel_cost = 8
nuclear_lifetime = 30 
info['nuclear_fhc'] = (nuclear_capital_cost * capital_recovery_factor(nuclear_lifetime) + nuclear_fixed_OandM) / 8760 + ( nuclear_var_OandM + nuclear_fuel_cost ) / 1000
######################################## Storage 
storage_capital_cost_L = np.array([290, 277, 253, 232, 211, 191, 170, 159, 147, 136, 125, 115, 113, 111, 108, 106, 104, 101, 99,  97,  95,  92,  90,  88,  86,  83,  81,  79,  77,  74,  72,  70 ])
storage_capital_cost_M = np.array([290, 277, 259, 242, 224, 207, 190, 181, 172, 164, 155, 147, 145, 142, 140, 138, 136, 133, 131, 129, 126, 124, 122, 120, 117, 115, 113, 111, 108, 106, 104, 102])
storage_capital_cost_H = np.array([290, 277, 267, 259, 252, 244, 236, 228, 219, 210, 202, 193, 193, 193, 193, 193, 193, 193, 193, 193, 193, 193, 193, 193, 193, 193, 193, 193, 193, 193, 193, 193])
storage_fixed_OandM_L = np.array([36, 34, 31, 29, 26, 24, 21, 20, 18, 17, 16, 14, 14, 14, 13, 13, 13, 12, 12, 12, 12, 11, 11, 11, 11, 10, 10, 10, 10, 9,  9,  9 ])
storage_fixed_OandM_M = np.array([36, 34, 32, 30, 28, 26, 24, 23, 22, 21, 20, 20, 19, 19, 19, 19, 18, 18, 18, 18, 17, 17, 17, 17, 16, 16, 16, 16, 15, 15, 15, 15])
storage_fixed_OandM_H = np.array([36, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25])
storage_lifetime = 15
info['storage_fhc_L'] = (storage_capital_cost_L * capital_recovery_factor(storage_lifetime) + storage_fixed_OandM_L) / 8760
info['storage_fhc_M'] = (storage_capital_cost_M * capital_recovery_factor(storage_lifetime) + storage_fixed_OandM_M) / 8760
info['storage_fhc_H'] = (storage_capital_cost_H * capital_recovery_factor(storage_lifetime) + storage_fixed_OandM_H) / 8760
info['storage_vhc'] = 1e-6
info['storage_rte'] = 0.85
######################################## Geothermal 
geothermal_capital_cost_L = np.array([19977,18378,16939,15519,14118,12736,11372, 10028, 8702,  7395,  6108,  4876,  4852,  4827,  4803,  4779,  4755,  4732,  4708,  4684,  4661,  4638,  4614,  4591,  4568,  4546,  4523,  4500,  4478,  4455,  4433,  4411 ])
geothermal_capital_cost_M = np.array([19977,19296,18686,18072,17460,16853,16248, 15647, 15050, 14456, 13865, 13312, 13245, 13179, 13113, 13048, 12983, 12918, 12853, 12789, 12725, 12661, 12598, 12535, 12472, 12410, 12348, 12286, 12225, 12164, 12103, 12042])
geothermal_capital_cost_H = np.array([19977,19878,19778,19679,19581,19483,19386, 19289, 19192, 19096, 19001, 18906, 18811, 18717, 18624, 18530, 18438, 18346, 18254, 18163, 18072, 17981, 17892, 17802, 17713, 17625, 17536, 17449, 17361, 17275, 17188, 17102])
geothermal_fixed_OandM_L = np.array([268, 257, 246, 235, 224, 213, 202, 191, 179, 168, 157, 146, 146, 146, 146, 146, 146, 146, 146, 146, 146, 146, 146, 146, 146, 146, 146, 146, 146, 146, 146, 146])
geothermal_fixed_OandM_M = np.array([268, 264, 260, 256, 252, 248, 244, 240, 236, 232, 228, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224])
geothermal_fixed_OandM_H = np.array([268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268, 268])
geothermal_lifetime = 30 
info['geothermal_fhc_L'] = (geothermal_capital_cost_L * capital_recovery_factor(geothermal_lifetime) + geothermal_fixed_OandM_L) / 8760
info['geothermal_fhc_M'] = (geothermal_capital_cost_M * capital_recovery_factor(geothermal_lifetime) + geothermal_fixed_OandM_M) / 8760
info['geothermal_fhc_H'] = (geothermal_capital_cost_H * capital_recovery_factor(geothermal_lifetime) + geothermal_fixed_OandM_H) / 8760
######################################## Biopower 
biopower_capital_cost = np.array([4346, 4333, 4319, 4306, 4278, 4275, 4275, 4253, 4232, 4209, 4185, 4156, 4133, 4101, 4068, 4040, 4012, 3981, 3953, 3925, 3900, 3871, 3840, 3814, 3787, 3761, 3738, 3711, 3682, 3652, 3624, 3560])
biopower_fixed_OandM = 150
biopower_var_OandM = 5
biopower_fuel_cost = 43
biopower_lifetime = 30 
info['biopower_fhc'] = (biopower_capital_cost * capital_recovery_factor(biopower_lifetime) + biopower_fixed_OandM) / 8760
info['biopower_vhc'] = (biopower_var_OandM + biopower_fuel_cost) / 1000

# with open('Time_transient_cost.pickle', 'wb') as handle:
#     # pickle.dump(info, handle, protocol=pickle.HIGHEST_PROTOCOL) 
#     pickle.dump(info, handle) 

# for idx in info.keys():
#     try:
#         print (idx, np.array(info[idx])[-1])
#     except:
#         print (idx, info[idx] )


# Test here 
loop_var = []
loop_var += [ [list(info['CCS_fhc_L']),        list(info['CCS_fhc_M']),        list(info['CCS_fhc_H'])] ]
loop_var += [ [list(info['solar_fhc_L']),      list(info['solar_fhc_M']),      list(info['solar_fhc_H'])] ]
loop_var += [ [list(info['wind_fhc_L']),       list(info['wind_fhc_M']),       list(info['wind_fhc_H'])] ]
loop_var += [ [list(info['offwind_fhc_L']),    list(info['offwind_fhc_M']),    list(info['offwind_fhc_H'])] ]
loop_var += [ [list(info['storage_fhc_L']),    list(info['storage_fhc_M']),    list(info['storage_fhc_H'])] ]
loop_var += [ [list(info['geothermal_fhc_L']), list(info['geothermal_fhc_M']), list(info['geothermal_fhc_H'])] ]


from itertools import product

ensem_idx = 0
loop_idx = len(loop_var)
count = 0
for items in product(*loop_var):
    ccs_fhc        = items[0]
    solar_fhc      = items[1]
    wind_fhc       = items[2]
    offwind_fhc    = items[3]
    storage_fhc    = items[4]
    geothermal_fhc = items[5]




    # for i in range(loop_idx):
    #     tech_list[loop_loc[i]]['fixed_cost'] = items[i]

    # if ensem_idx >= starting_point and ensem_idx < starting_point+100:
    #     case_name_output = f'{case_name_default}_Scenarios2050_{str(ensem_idx)}'
    #     pass_variables(single_year_index, case_dic, tech_list, co2_constraints_list, co2_constraints_percentage, case_name_output, info_idx)
    # ensem_idx += 1
