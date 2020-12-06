import operator

def valid_password(pass_line):
    parsed_pass = parse_pass(pass_line)
    return validate_pass(parsed_pass)

def parse_pass(pass_line):
    rule, _, password = pass_line.partition(': ')
    occurs, _, char = rule.partition(' ')
    min_occurs, _, max_occurs = occurs.partition('-')

    return {'min': int(min_occurs), 'max': int(max_occurs), 'char': char, 'pass': password}

def validate_pass_v1(options):
    count = options['pass'].count(options['char'])
    if options['min'] <= count and count <= options['max']:
        return True
    return False

def validate_pass(options):
    index1 = options['min'] - 1
    index2 = options['max'] - 1

    match1 = options['pass'][index1] == options['char']
    match2 = options['pass'][index2] == options['char']

    return operator.xor(match1, match2)

with open('./input.txt') as inputfile:
    valid = [line for line in inputfile if valid_password(line)]
    print(len(valid))
