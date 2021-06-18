#!/usr/bin/env python3

import collections as cl
import csv
import itertools as it
import numpy as np


def make_instance():
    # set the number of foods you use
    N = 7
    # set foods you should use
    fixed_foods = ['rice', 'fish']
    # set csv file name
    filename = '../data/dummy.csv'
    # read csv 
    with open(filename) as f:
        reader = csv.reader(f)
        whole = [row for row in reader]
        # delete header
        del whole[0]
        del whole[1]
        del whole[2]
        # extrace EastAsian recipe
        east_asian = [row for row in whole if row[0] == 'EastAsian']
    # initialize comination list and method dictionary
    comb = []
    method_dict = {}
    for recipe in east_asian:
        # get ingredients in recipe
        ingredients = recipe[1:-1]
        for i in it.combinations(ingredients, 2):
            sort_i = tuple(sorted(list(i)))
            # get combination
            comb.append(sort_i)
        # get method of recipe
        method = recipe[-1]
        for i in ingredients:
            if i not in method_dict:
                method_dict[i] = {}
            else:
                # add 1 to {ingredients: {method: num}}
                if method not in method_dict[i]:
                    method_dict[i][method] = 1
                else:
                    method_dict[i][method] += 1
    # compute frequencyt of combination (= compatibility)
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
            'freq_matrix': freq_matrix, 'method_dict': method_dict}
