#!/usr/bin/env python3

import numpy as np
from pyqubo import Array, Constraint, LogEncInteger, Placeholder


def make_hamiltonian(instance_data):
    # set constant values
    N = instance_data['N']
    freq_matrix = instance_data['freq_matrix']
    num_foods = len(freq_matrix)
    x = Array.create('x', shape=(num_foods), vartype='BINARY')
    # fix x
    x = np.array(x)
    for food in instance_data['fixed_foods']:
        num = instance_data['food_num_dict'][food]
        x[num] = 1
    # set hyperparameters
    lamb1 = Placeholder('h1')
    # set the number of foods limit constraint
    sum_x = sum([x[i] for i in range(num_foods)])
    const = (N-sum_x) ** 2
    h1 = Constraint(const, label='h1')
    # set objective function
    obj = - np.dot(x, np.dot(freq_matrix, x))
    # compute total hamiltonian
    hamiltonian = obj + lamb1 * h1
    # compile
    model = hamiltonian.compile()
    return model
