import itertools
from itertools import cycle

f = open('day12_input', 'r').readlines()
data = [str.strip() for str in f]
cleaned_data = [(elem[0], int(elem[1:])) for elem in data]


def rotate(rotate_dir, current_dir, val):
    directions = ['N', 'E', 'S', 'W']
    if rotate_dir == 'L':
        directions.reverse()
    current_dir = directions.index(current_dir)
    position = int(val / 90)
    never_ending_dir = cycle(directions)
    next_direction = next(itertools.islice(never_ending_dir, current_dir + position, None))
    return next_direction


actions = {
    'N': lambda x, y, dir, val: (x + val, y, dir),
    'S': lambda x, y, dir, val: (x - val, y, dir),
    'E': lambda x, y, dir, val: (x, y + val, dir),
    'W': lambda x, y, dir, val: (x, y - val, dir),
    'F': lambda x, y, dir, val: actions[dir](x, y, dir, val),
    'R': lambda x, y, dir, val: (x, y, rotate('R', dir, val)),
    'L': lambda x, y, dir, val: (x, y, rotate('L', dir, val))
}
direction = 'E'
x, y = 0, 0
for action, value in cleaned_data:
    x, y, direction = actions[action](x, y, direction, value)

print(cleaned_data)
print(direction, x, y)
print('Manhattan distance: ', abs(x) + abs(y))
