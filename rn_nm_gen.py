import random
import os
import argparse
import json


# checks if files exist and open if they exist.
if os.path.exists('./first_names.txt') and os.path.exists('./names.txt'):
    try:
        ffile = open(r'./first_names.txt')
        fnames = ffile.readlines()

        lfile = open(r'./names.txt')
        lnames = lfile.readlines()
    # raises error if there is problem when opening the file
    except OSError as e:
        print(e)
else:
    print('files are not available ')


# function returns first name and last name
def random_names():
    # picks random name from the list
    random_fn = random.choice(fnames)
    random_ln = random.choice(lnames)
    return (f'{random_fn.rstrip()} {random_ln.strip()}')

# this function limits amount of names returned to amount user set   
def multiple_names(c):
    print(type(c))
    c = int(c)
    c = abs(c)
    # loop print only the amount necessary   --> this comment is not good instead in the future try """ at the top of the function to explain what happens  """
    while c >= 0:
        print(random_names())
        c = c - 1
        if c == 0:
            break



# print(random_names())
# print(multiple_names())

def main():
    # sets up the parser so the above functions can receive necessary values 
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()
    get_name_parser = subparser.add_parser('gn', help='get name')
    get_name_parser.set_defaults(func=lambda args: multiple_names(args.amount))
    # AI recommends using the function directly from now on I will try to do it this will be left as reference
    name_amount = get_name_parser.add_argument('amount', type=int, help='give numerical value of the amount of random names you want to get printed')


    args = parser.parse_args()
    args.func(args)

main()
"""  
comments should explain why I did as I did 
for example 
    - why I used subparsers 
        - I used subparser as they have set_defaults which connects to function without extra hassle 
    - how lambda function connects to business logic
        - it passes the argument to function silently 
this is the program entry point
"""