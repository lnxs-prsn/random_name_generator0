import random
import os
import argparse




# with open('./first_names.txt', 'r')
try:
    ffile = open(r'./first_names.txt')
    fnames = ffile.readlines()

    lfile = open(r'./names.txt')
    lnames = lfile.readlines()
except :
    pass

print(type(fnames))

def random_names():
    random_fn = random.choice(fnames)
    random_ln = random.choice(lnames)
    return (f'{random_fn.rstrip()} {random_ln.strip()}')


def multiple_names(c):
    print(type(c))
    c = int(c)
    c = abs(c)
    while c >= 0:
        print(random_names())
        c = c - 1
        if c == 0:
            break



# print(random_names())
# print(multiple_names())

def main():

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()
    get_name_parser = subparser.add_parser('gn', help='get name')
    get_name_parser.set_defaults(func=lambda args: multiple_names(args.amount))
    name_amount = get_name_parser.add_argument('amount', type=int, help='give numerical value of the amount of random names you want to get printed')


    args = parser.parse_args()
    args.func(args)

main()