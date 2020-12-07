from pprint import pprint
from itertools import repeat, chain


def function(offset, step):
    FILE_LENGTH = 323
    ROW_LENGTH = 31
    count = 0
    matrix = []
    with open('day3_input', 'r') as f:
        for line in f:
            # matrix.append(line.strip())
            line = line.strip()
            max_repeat = int(FILE_LENGTH*offset/ROW_LENGTH + 1)
            matrix.append(chain(*repeat(line, max_repeat)))

    for i in range(0, len(matrix), step):
        # print(list(matrix[i])[int(i/step * offset)])
        if (list(matrix[i])[int(i/step * offset)]) == '#':
            count += 1
    return count


print(function(1,1))
print(function(3,1))
print(function(5,1))
print(function(7,1))
print(function(1,2))
