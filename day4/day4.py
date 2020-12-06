import re

# Debugging was a late addition, as I added comments.
DEBUG = True

class Passport:
    FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    HAIR_PATTERN = re.compile('#[0-9a-f]{6}')

    def __init__(self):
        for key in Passport.FIELDS:
            setattr(self, key, None)

    def update(self, data):
        fields = data.split()
        for field in fields:
            field_key, field_value = field.split(sep=':', maxsplit=2)
            if field_key in Passport.FIELDS:
                setattr(self, field_key, field_value)

    def valid(self, strict=True):
        #import pdb; pdb.set_trace()
        if DEBUG:
            print('Passport:', vars(self))

        # Played with __slots__, but I like using `vars(self).values()` here.
        # Ensures all the fields are present, and prevents errors in the strict validators.
        if None in vars(self).values():
            if DEBUG:
                print('Rejected for missing value')

            return False

        # Allows you to get part 1 answers.
        if not strict:
            return True

        # Wanted to make a one-liner, and use `all()`. (Moved the import for clarity)
        #from itertools import repeat
        #return True if all(getattr(self, f'validate_{key}')() for self, key in zip(repeat(self), Passport.FIELDS)) else False
        # This works, but I don't like the zip. Also, can't print which field failed validation.
        #zipped = zip(repeat(self), Passport.FIELDS)
        #if not all(getattr(self, f'validate_{key}')() for self, key in zipped):
            #return False

        # This was my original solution, but a REALLY don't like using `eval()`.
        # I refactored it into the solution below, after creating the one-liner.
        #for key in Passport.FIELDS:
            #validator = 'self.validate_{}()'.format(key)
            #if not eval(validator):
                #print(key, 'did not validate')
                #return False

        # Could remove returning the key in the tuple if I didn't want it for debugging.
        for key, validator in [ (key, f'validate_{key}') for key in Passport.FIELDS ]:
            if not getattr(self, validator)():
                if DEBUG:
                    print(key, 'did not validate')

                return False

        return True

    def validate_byr(self):
        return True if int(self.byr) >= 1920 and int(self.byr) <= 2002 else False

    def validate_iyr(self):
        return True if int(self.iyr) >= 2010 and int(self.iyr) <= 2020 else False

    def validate_eyr(self):
        return True if int(self.eyr) >= 2020 and int(self.eyr) <= 2030 else False

    def validate_hgt(self):
        if self.hgt[-2:] == 'cm':
            return True if int(self.hgt[:-2]) >= 150 and int(self.hgt[:-2]) <= 193 else False
        elif self.hgt[-2:] == 'in':
            return True if int(self.hgt[:-2]) >= 59 and int(self.hgt[:-2]) <= 76 else False
        return False

    def validate_hcl(self):
        return True if Passport.HAIR_PATTERN.match(self.hcl) else False

    def validate_ecl(self):
        return True if self.ecl in Passport.EYE_COLORS else False

    def validate_pid(self):
        return True if len(self.pid) == 9 and int(self.pid) else False

if __name__ == '__main__':
    DEBUG = False
    curr_pass = Passport()
    valid_pass = 0

    with open('./input.txt') as inputfile:
        for line in inputfile:
            # The number of times this has bit me is TOO DAMN HIGH.
            line = line.strip()

            if line == '':
                # End of current passport. Validate, then unset current passport.
                if curr_pass.valid():
                    valid_pass += 1

                curr_pass = Passport()

            # Add this line of info to this passport. This is safe for blank lines.
            curr_pass.update(line)

    # Validate this last passport
    if curr_pass.valid():
        valid_pass += 1

    print('Valid passports: {}'.format(valid_pass))
