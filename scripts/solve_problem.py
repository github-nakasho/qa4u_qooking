#!/usr/bin/env python3

import openjij as oj

    
def solve_problem(model, feed_dict):
    # convert to qubo
    qubo, offset = model.to_qubo(feed_dict=feed_dict)
    # solve with OpenJij (SA)
    sampler = oj.SASampler(num_reads=100, num_sweeps=100)
    response = sampler.sample_qubo(Q=qubo)
    # take mininum state
    dict_solution = response.first.sample
    energy = response.first.energy
    # decode soution
    solution = model.decode_sample(dict_solution, vartype='BINARY', feed_dict=feed_dict)
    # extract broken
    broken = solution.constraints(only_broken=True)
    return solution, energy, broken