#!/usr/bin/env python

# 1- load a dataset from a file
# 2- "organize" that file to access rows or columns
# 3- compute "summary statitics" about datasets
# 4- print those summary statitics

# 1- load the dataset
# 1a. accept arbritary filename as argument
# 1b. load filename

# Instead of importing the intire library, use the following
from argparse import ArgumentParser

parser = ArgumentParser(description = 'A CSV reader + stats maker')
parser.add_argument('csvfile', help = 'Path to input csv file')

parsed_args = parser.parse_args()
print(parsed_args.csvfile)

my_csv_file =  parsed_args.csvfile

import os
import os.path as op

# the following 2 if statements can help bring an error
# if op.isfile(my_csv_file):
#     print('good file!')
# else:
#     print('not file')

# if not op.isfile(my_csv_file):
#     raise ValueError("not a valid file")
assert os.path.isfile(my_csv_file), "this is not a real file"
print("woot the file exists")

# 1b. load the file
import pandas as pd

data = pd.read_csv(my_csv_file, sep='\s+|,', header=None, engine='python')

headers = data.iloc[0]

# Obtains first row to identify header is string or numeric
try:
    pd.to_numeric(headers)
except:
    data = pd.DataFrame(data.values[1:], columns=headers)

# Changes strings to numbers (self identifies for float or integer)
data = data.apply(pd.to_numeric)

print(data.head())
print(data.shape)
print(type(data))
print(data.dtypes)

# 2. "organize" that file, so we can access columns or rows
# 2a. access any row
print(data.iloc[3:5,:])
# 2b. access any column
print(data.iloc[:3, -3:])
# 2c. access any value
print(data.iloc[3,4])

# 3/4. compute some "summary statistics" about datasets
import numpy as np

print(np.mean(data))
print(np.std(data))
