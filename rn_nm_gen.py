import random
import os
import argparse




# with open('./first_names.txt', 'r')

file = open(r'./first_names.txt')
names = file.readlines()

print(names)