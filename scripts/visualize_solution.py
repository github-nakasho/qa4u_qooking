#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt

    
def visualize_solution(solution, energy, broken, instance_data):
    # check broken
    print('***** Broken check *****')
    print(broken)
    include_fixed = solution.sample
    # add fixed variables
    for food in instance_data['fixed_foods']:
        num = instance_data['food_num_dict'][food]
        string = 'x[{}]'.format(num)
        include_fixed[string] = 1
    solution.sample = include_fixed
    # visuazlize result of ingredients combination
    print('***** Result for you *****')
    foods = []
    for i in range(instance_data['num_foods']):
        if solution.array('x', i) == 1:
            for k, v in instance_data['food_num_dict'].items():
                if i == v:
                    print(k)
                    foods.append(k)
    # visualize frequency of cooking method
    method_dict = instance_data['method_dict']
    total_keys = []
    for food in foods:
        keys = method_dict[food].keys()
        for key in keys:
            if key not in total_keys:
                total_keys.append(key)
    bottom = [0] * len(total_keys)
    for food in foods:
        ans_dict = {key: 0 for key in total_keys}
        for key in method_dict[food]:
            ans_dict[key] = method_dict[food][key]
        ans_list = ans_dict.items()
        ans_list = sorted(ans_list)
        x, y = zip(*ans_list)
        plt.bar(x, y, label=food, bottom=bottom)
        bottom = [bottom[i]+y[i] for i in range(len(bottom))]
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), ncol=4)
    plt.xticks(rotation=45)
    plt.title('Frequency of cooking method')
    ratio = math.ceil(len(foods)/4)
    plt.subplots_adjust(bottom=0.2+ratio*0.05)
    plt.savefig('figure.png')
    
        
        
        