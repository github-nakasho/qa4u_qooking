#!/usr/bin/env python3

import collections as cl
import csv
import itertools as it
import numpy as np


def make_instance():
    # set the number of foods you use
    N = 5
    # set foods you should use
    fixed_foods = ['rice']
    # set csv file name
    filename = '../data/srep00196-s3.csv'
    # read csv 
    with open(filename) as f:
        reader = csv.reader(f)
        # extrace EastAsian recipe
        east_asian = [row for row in reader if row[0]=='EastAsian']
    # get information of combination
    comb = []
    for recipe in east_asian:
        recipe = recipe[1:]
        for i in it.combinations(recipe, 2):
            sort_i = tuple(sorted(list(i)))
            comb.append(sort_i)
    frequency = cl.Counter(comb)
    # make dictionary for mapping numbers to foods
    food_num_dict = {}
    num = 0
    for food1, food2 in frequency.keys():
        if food1 not in food_num_dict:
            food_num_dict[food1] = num
            num += 1
        if food2 not in food_num_dict:
            food_num_dict[food2] = num
            num += 1
    # make normalized frequency matrix (symmetry matrix)
    num_foods = len(food_num_dict)
    freq_matrix = np.zeros((num_foods, num_foods), dtype=int)
    for food1, food2 in frequency.keys():
        num1 = food_num_dict[food1]
        num2 = food_num_dict[food2]
        freq_matrix[num1][num2] = frequency[(food1, food2)]
    upper = np.triu(freq_matrix) + np.triu(freq_matrix).T
    lower = np.tril(freq_matrix) + np.tril(freq_matrix).T
    freq_matrix = upper + lower
    freq_matrix = (freq_matrix-freq_matrix.min()) / (freq_matrix.max()-freq_matrix.min())
    return {'N': N, 'fixed_foods': fixed_foods, 
            'food_num_dict': food_num_dict, 'num_foods': num_foods, 
            'freq_matrix': freq_matrix}
