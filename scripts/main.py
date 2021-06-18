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
    lam1 = 10
    parameters = {'h1': lam1}
    # solve with OpenJij (SA)
    print('Solve problem...')
    solution, energy, broken = sp.solve_problem(model=model, feed_dict=parameters)
    print('Finish solving problem !')
    # visualize solution
    vs.visualize_solution(solution, energy, broken, instance_data)
