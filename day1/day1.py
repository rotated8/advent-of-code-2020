from itertools import combinations
from math import prod

DEBUG = True

def target_product(entries, items=2, target=2020):
    DEBUG_STR = 'entries: {}, sum: {}, product: {}'

    for combination in combinations(entries, items):
        if DEBUG:
            print(DEBUG_STR.format(combination, sum(combination), prod(combination)))

        if sum(combination) == target:
            return prod(combination)

if __name__ == '__main__':
    with open('./input.txt') as inputfile:
        DEBUG = False

        entries = [ int(line) for line in inputfile ]
        entries.sort()

        if DEBUG:
            print('Total entries:', len(entries))

        print('Pt 1 product:', target_product(entries))
        print('Pt 2 product:', target_product(entries, 3))
