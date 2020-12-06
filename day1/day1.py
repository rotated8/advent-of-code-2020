from itertools import combinations

DEBUG = True

def pt1(entries):
    DEBUG_STR = 'e1: {}, e2: {}, sum: {}, product: {}'

    for entry1, entry2 in combinations(entries, 2):
        if DEBUG:
            print(DEBUG_STR.format(entry1, entry2, entry1+entry2, entry1*entry2))

        if entry1+entry2 == 2020:
            return entry1*entry2

def pt2(entries):
    DEBUG_STR = 'e1: {}, e2: {}, e3: {}, sum: {}, product: {}'

    for e1, e2, e3 in combinations(entries, 3):
        if DEBUG:
            print(DEBUG_STR.format(e1, e2, e3, e1+e2+e3, e1*e2*e3))

        if e1+e2+e3 == 2020:
            return e1*e2*e3

if __name__ == '__main__':
    with open('./input.txt') as inputfile:
        DEBUG = False

        entries = [ int(line) for line in inputfile ]
        entries.sort()

        if DEBUG:
            print('Total entries:', len(entries))

        print('Pt 1 product:', pt1(entries))
        print('Pt 2 product:', pt2(entries))
