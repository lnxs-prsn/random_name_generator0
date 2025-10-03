import random
import os
import argparse




# with open('./first_names.txt', 'r')

ffile = open(r'./first_names.txt')
fnames = ffile.readlines()

lfile = open(r'./names.txt')
lnames = lfile.readlines()
print(type(fnames))

def random_names():
    random_fn = random.choice(fnames)
    random_ln = random.choice(lnames)
    return (f'{random_fn.rstrip()} {random_ln.strip()}')


def multiple_names(c):
    c = int(c)
    while c > 0:
        print(random_names())
        c - 1
        if c == 0:
            break



# print(random_names())
print(multiple_names(4))



parser = argparse.ArgumentParser()
# name = parser.add_argument('random_name', type=str, help='get random name')

