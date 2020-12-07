import re
from pprint import pprint

VALID_SET1 = {'eyr', 'iyr', 'pid', 'hcl', 'byr', 'hgt', 'ecl'}
VALID_SET2 = {'eyr', 'iyr', 'pid', 'hcl', 'byr', 'hgt', 'ecl', 'cid'}


def validate_color(c):
    return bool(re.match(r"^#[0-9a-f]{6}$", c))


def validate_pid(pid):
    return bool(re.match(r"^[0-9]{9}$", pid))


def validate_eye(c):
    return c in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def validate_height(h):
    if h:
        metric = h[-2:]
        if metric == 'cm':
            return 150 <= int(h.split(metric)[0]) <= 193
        if metric == 'in':
            return 59 <= int(h.split(metric)[0]) <= 76
    return False


def validate(d):
    return (1920 <= int(d.get('byr', -1)) <= 2002) and (2010 <= int(d.get('iyr', -1)) <= 2020) and \
           (2020 <= int(d.get('eyr', -1)) <= 2030) and validate_height(d.get('hgt', '')) \
           and validate_color(d.get('hcl')) and validate_eye(d.get('ecl')) and validate_pid(d.get('pid', '0')) \
           and (set(d) == VALID_SET1 or set(d) == VALID_SET2)


def function():
    with open('day4_input', 'r') as f:
        list = []
        subdict = {}
        empty = 0
        for line in f:
            if line == "\n":
                empty += 1
                list.append(subdict.copy())
                subdict.clear()
            else:
                import re
                res = re.split(':| | ', line.strip())
                dict = {res[i]: res[i + 1] for i in range(0, len(res), 2)}
                subdict.update(dict)
    pprint(list)
    valid = 0
    invalid = 0
    for d in list:
        if validate(d):
            valid += 1
        else:
            invalid += 1
    return valid, invalid


print(function())
