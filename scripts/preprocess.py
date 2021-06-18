#!/usr/bin/env python3

import csv
import random


if __name__ == '__main__':
    # set cooking method
    method_list = ['saute', 'pan-fry', 'stir-fly', 'deep-fry', 'boil', 
                    'poach', 'simmer', 'grill', 'bake', 'toast', 
                    'microwave']
    # set csv file name
    filename = '../data/srep00196-s3.csv'
    # read csv 
    with open(filename) as f:
        header = next(csv.reader(f))
        reader = csv.reader(f)
        # extract recipes and add method randomly
        recipe = [row for row in reader]
        print(recipe)
    # initialize list for dummy data
    dummy = []
    for row in recipe:
        method = random.choice(method_list)
        row.append(method)
        dummy.append(row)
    # write to csv
    with open('../data/dummy.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(dummy)

    