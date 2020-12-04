with open('problem4_input.txt') as file:
    inputs = file.readlines()

inputs = [i.strip() for i in inputs]

passports = []
passport = ''

for line in inputs:
    if line == '':
        passports.append(passport)
        passport = ''

    else:
        passport = passport + ' ' + line
        passport = passport.strip()

passports.append(passport)


def is_valid_password(passport):
    if 'byr' not in passport:
        return False
    
    if 'iyr' not in passport:
        return False

    if 'eyr' not in passport:
        return False

    if 'hgt' not in passport:
        return False

    if 'hcl' not in passport:
        return False

    if 'ecl' not in passport:
        return False

    if 'pid' not in passport:
        return False

    return True

count = 0

for passport in passports:
    print(passport)
    fields = passport.split(' ')

    field_map = {}

    for field in fields:
        split_field = field.split(':')

        field_map[split_field[0]] = split_field[1]

    if is_valid_password(field_map):
        count += 1

print(count)


