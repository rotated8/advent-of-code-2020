DEBUG = True

def parse_pass(line):
    rule, _, password = line.partition(': ')
    occurs, _, char = rule.partition(' ')
    min_occurs, _, max_occurs = occurs.partition('-')

    return (int(min_occurs), int(max_occurs), char, password)

def validate(min_occurs, max_occurs, char, password, version='2'):
    if version == 1:
        return True if min_occurs <= password.count(char) <= max_occurs else False

    letters = [password[min_occurs-1], password[max_occurs-1]]
    return True if letters.count(char) == 1 else False

if __name__ == '__main__':
    DEBUG = False

    with open('./input.txt') as inputfile:
        print(len([ True for line in inputfile if validate(*parse_pass(line), 2) ]))
