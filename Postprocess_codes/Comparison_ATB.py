
import matplotlib.pyplot as plt 


ATB_2021 = {
    'solar': [15.42188211, 5.794755718, 7.581521169, 9.079343507], 
    'wind': [18.11895838, 7.569390621, 10.75863775, 12.95979032],
    'offwind': [57.15517459, 25.08663768, 30.61419606, 42.91331596],
    'nuclear': [84.51739145, 70.4239702],
    'biopower': [57.10371115, 49.8730133],
    'geothermal': [214.3692446, 57.24504862, 136.349483, 187.9210814],
    'storage': [7.744342599, 1.904751567, 2.990759329, 5.272872439],
    'gas': [12.77831841, 11.42601233],
    'gas_ccs': [31.98238555, 18.83942967, 22.48822899, 26.25118356]
    }



ATB_2022v3 = {
    'solar': [14.88831916, 5.551809411, 7.187622166, 8.64864706], 
    'wind': [18.35814177, 7.596988705, 10.80463455, 13.01498648],
    'offwind': [54.05833694, 30.13708694, 34.68951304, 44.87277988],
    'nuclear': [85.12831221, 72.10201684],
    'biopower': [57.86182168, 50.59432638],
    'geothermal': [207.8695053, 42.4479014, 117.0312707, 182.847243],
    'storage': [9.53358636, 2.825116991, 3.419607958, 6.39377599],
    'gas': [12.74528389, 11.52176886],
    'gas_ccs': [27.66914283, 17.17560297, 19.46289684, 21.87354532]
    }


color_colors = {'gas': 'black', 'gas_ccs': 'grey', 'biopower': 'lightslategrey', 
                'solar': 'wheat', 'wind': 'skyblue', 'offwind': 'darkblue', 
                'nuclear': 'tomato', 'geothermal': 'darkred', 
                'storage': 'lightpink', 'pgp': 'lightgreen'} 



start = 0 
for keys in ATB_2021.keys():
    cost1 = ATB_2021[keys]
    cost2 = ATB_2022v3[keys]
    len_cost = len(cost1)
    for i in range(len_cost):
        # plt.scatter(start + i, cost1[i], marker='o', facecolors='none', edgecolors=color_colors[keys])
        # plt.scatter(start + i, cost2[i], c=color_colors[keys], marker='^')
        plt.scatter(start + i, cost2[i]/cost1[i], c=color_colors[keys], marker='x')
    start = start + len_cost
plt.xlim(-1, 30)
# plt.ylim(0, 220)
plt.ylim(0, 1.6)
# plt.show()
plt.savefig('ATB_2021_2022v3.ps')
plt.clf() 