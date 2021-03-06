import itertools
from itertools import cycle

f = open('day12_input', 'r').readlines()
data = [str.strip() for str in f]
cleaned_data = [(elem[0], int(elem[1:])) for elem in data]


def rotate(x, y, direction, val):
    if (val == 90 and direction == 'R') or ((val == 270 and direction == 'L')):
        return y, -x
    if val == 180:
        return -x, -y
    if (val == 270 and direction == 'R') or (val == 90 and direction == 'L'):
        return -y, x


actions = {
    'N': lambda x, y, wx, wy, val: (x, y, wx + val, wy),
    'S': lambda x, y, wx, wy, val: (x, y, wx - val, wy),
    'E': lambda x, y, wx, wy, val: (x, y, wx, wy - val),
    'W': lambda x, y, wx, wy, val: (x, y, wx, wy + val),
    'F': lambda x, y, wx, wy, val: (x + val * wx, y + val * wy, wx, wy),
    'R': lambda x, y, wx, wy, val: (x, y, *rotate(wx, wy, 'R', val)),
    'L': lambda x, y, wx, wy, val: (x, y, *rotate(wx, wy, 'L', val))
}

wx, wy = (1, -10)
x, y = 0, 0
for action, value in cleaned_data:
    print(action, value)
    x, y, wx, wy = actions[action](x, y, wx, wy, value)
    print(f"waypoint: {wx, wy} ship: {x, y}")
print(abs(x) + abs(y))
