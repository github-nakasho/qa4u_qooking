#!/usr/bin/env python3

    
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
    # visuazlize result
    print('***** Result for you *****')
    for i in range(instance_data['num_foods']):
        if solution.array('x', i) == 1:
            food = [k for k, v in instance_data['food_num_dict'].items() if v == i][0]
            print(food)
        
        