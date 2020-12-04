import re

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


def is_valid_byr(passport):
    if 'byr' not in passport:
        return False
    else:
        byr = int(passport['byr'])

        return byr >= 1920 and byr <= 2002

def is_valid_iyr(passport):
    if 'iyr' not in passport:
        return False
    else:
        iyr = int(passport['iyr'])

        return iyr >= 2010 and iyr <= 2020

def is_valid_eyr(passport):
    if 'eyr' not in passport:
        return False
    else:
        eyr = int(passport['eyr'])

        return eyr >= 2020 and eyr <= 2030

def is_valid_hgt(passport):
    if 'hgt' not in passport:
        return False
    else:
        hgt = passport['hgt']

        system = hgt[-2:]
        num = int(hgt[:-2])

        if system == 'cm':
            return num >= 150 and num <= 193
        elif system == 'in':
            return num >= 59 and num <= 76
        else:
            return False

valid_ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def is_valid_ecl(passport):
    if 'ecl' not in passport:
        return False
    else:
        ecl = passport['ecl']

        return ecl in valid_ecls 
        
def is_valid_pid(passport):
    if 'pid' not in passport:
        return False
    else:
        pid = passport['pid']

        return len(pid) == 9

def is_valid_hcl(passport):
    if 'hcl' not in passport:
        return False
    else:
        hcl = passport['hcl']

        if hcl[0] != '#':
            return False
        
        return re.match(r"^[A-Fa-f0-9]+$", hcl[1:])

def is_valid_passport(passport):
    return is_valid_byr(passport) and is_valid_iyr(passport) and is_valid_eyr(passport) and is_valid_hgt(passport) and is_valid_hgt(passport) and is_valid_hcl(passport) and is_valid_ecl(passport) and is_valid_pid(passport)

count = 0

for passport in passports:
    fields = passport.split(' ')

    field_map = {}

    for field in fields:
        split_field = field.split(':')

        field_map[split_field[0]] = split_field[1]

    if is_valid_passport(field_map):
        count += 1

print(count)


