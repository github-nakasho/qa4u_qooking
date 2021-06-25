#!/usr/bin/env python3

import make_hamiltonian as mh
import make_instance as mi
import solve_problem as sp
import visualize_solution as vs


if __name__ == '__main__':
    # set instance information
    print('Make instance ...')
    instance_data = mi.make_instance()
    print('Finish making instance !')
    # set costs & constraints
    print('Make Hamiltonian...')
    model = mh.make_hamiltonian(instance_data=instance_data)
    print('Finish making Hamiltonian !')
    # set hyperparameters
    nu1 = 1
    parameters = {'h1': nu1}
    # set update parameter
    eta = 0.1
    nu_list = []
    # iteration for finding optimal solution
    for _ in range(100):
        nu_list.append(parameters['h1'])
        # solve with OpenJij
        solution, energy, broken = sp.solve_problem(model=model, feed_dict=parameters)
        # update hyperparameters
        for i in broken.keys():
            parameters[i] -= eta * broken[i][1]
        # if broken is empty, get out of the loop
        if len(broken) == 0:
            break
    print('Finish solving problem !')
    # visualize solution
    vs.visualize_solution(solution, energy, broken, instance_data)
