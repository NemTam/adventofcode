from pprint import pprint

VALID_SET1 = {'eyr', 'iyr', 'pid', 'hcl', 'byr', 'hgt', 'ecl'}
VALID_SET2 = {'eyr', 'iyr', 'pid', 'hcl', 'byr', 'hgt', 'ecl', 'cid'}

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
    print(len(list))
    pprint(list)
    valid = 0
    invalid = 0
    for d in list:
        if set(d.keys()) == VALID_SET1 or set(d.keys()) == VALID_SET2:
            # print(set(d.keys()) | VALID_SET)
            valid += 1
        else:
            invalid+=1
            # print(d.get('pid'))
            # print(VALID_SET2 - set(d.keys()))
    return valid, invalid


print(function())
